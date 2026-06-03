#!/usr/bin/env python3
"""Export an ipynb to a Chinese-friendly printable PDF.

This avoids the common LaTeX/nbconvert CJK font problem by:
1. converting ipynb cells to Markdown with standard-library JSON parsing;
2. using pandoc to produce standalone HTML with explicit CJK font CSS;
3. using Chrome headless to print the HTML to PDF.
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


CSS = r"""
@page {
  size: A4;
  margin: 16mm 14mm;
}

html, body {
  font-family: "PingFang TC", "Heiti TC", "Songti TC", "Arial Unicode MS",
    "Noto Sans CJK TC", "Noto Sans CJK SC", sans-serif;
  font-size: 11.5pt;
  line-height: 1.55;
  color: #111;
}

h1, h2, h3 {
  break-after: avoid;
  page-break-after: avoid;
  line-height: 1.25;
}

h1 {
  font-size: 22pt;
  margin: 0 0 12pt;
}

h2 {
  font-size: 16pt;
  margin-top: 18pt;
  border-bottom: 1px solid #ddd;
  padding-bottom: 3pt;
}

h3 {
  font-size: 13pt;
  margin-top: 14pt;
}

p, li {
  orphans: 2;
  widows: 2;
}

pre, code {
  font-family: "SFMono-Regular", "Menlo", "Consolas", "Noto Sans Mono CJK TC",
    monospace;
}

pre {
  font-size: 9.2pt;
  line-height: 1.35;
  background: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px 10px;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  break-inside: avoid;
  page-break-inside: avoid;
}

table {
  border-collapse: collapse;
  width: 100%;
  break-inside: avoid;
}

th, td {
  border: 1px solid #ccc;
  padding: 4px 6px;
}

blockquote {
  border-left: 4px solid #ccc;
  margin-left: 0;
  padding-left: 10px;
  color: #444;
}
"""


def find_chrome() -> str:
    for name in ("google-chrome", "chromium", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    for path in DEFAULT_CHROME_PATHS:
        if Path(path).exists():
            return path
    raise SystemExit("Chrome/Chromium not found. Install Chrome or pass --chrome.")


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def output_text(output: dict) -> str:
    if "text" in output:
        text = output["text"]
        return "".join(text) if isinstance(text, list) else str(text)
    data = output.get("data", {})
    if "text/plain" in data:
        text = data["text/plain"]
        return "".join(text) if isinstance(text, list) else str(text)
    if output.get("ename") or output.get("evalue"):
        return f"{output.get('ename', '')}: {output.get('evalue', '')}".strip()
    return ""


def ipynb_to_markdown(ipynb_path: Path) -> str:
    nb = json.loads(ipynb_path.read_text(encoding="utf-8"))
    parts: list[str] = []
    for cell in nb.get("cells", []):
        cell_type = cell.get("cell_type")
        source = cell_source(cell).rstrip()
        if cell_type == "markdown":
            if source:
                parts.append(source)
        elif cell_type == "code":
            if source:
                parts.append("```python\n" + source + "\n```")
            outputs = []
            for output in cell.get("outputs", []):
                text = output_text(output).rstrip()
                if text:
                    outputs.append(text)
            if outputs:
                escaped = "\n\n".join(outputs)
                parts.append("```text\n" + escaped + "\n```")
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def run(cmd: list[str]) -> None:
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError as exc:
        raise SystemExit(f"Command not found: {cmd[0]}") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"Command failed ({exc.returncode}): {' '.join(cmd)}") from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ipynb", type=Path, help="IPYNB file to export")
    parser.add_argument("-o", "--output", type=Path, help="PDF output path")
    parser.add_argument("--keep-html", action="store_true", help="Keep generated HTML")
    parser.add_argument("--chrome", help="Chrome/Chromium executable path")
    args = parser.parse_args()

    ipynb = args.ipynb.resolve()
    if not ipynb.exists():
        raise SystemExit(f"File not found: {ipynb}")
    output = (args.output or ipynb.with_suffix(".pdf")).resolve()
    html_output = output.with_suffix(".html")
    chrome = args.chrome or find_chrome()

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        md_path = tmpdir / "source.md"
        css_path = tmpdir / "print.css"
        temp_html = tmpdir / "source.html"
        md_path.write_text(ipynb_to_markdown(ipynb), encoding="utf-8")
        css_path.write_text(CSS, encoding="utf-8")

        run(
            [
                "pandoc",
                str(md_path),
                "--from",
                "markdown+tex_math_dollars",
                "--to",
                "html5",
                "--standalone",
                "--metadata",
                f"title={html.escape(ipynb.stem)}",
                "--css",
                str(css_path),
                "--output",
                str(temp_html),
            ]
        )

        if args.keep_html:
            html_output.write_text(temp_html.read_text(encoding="utf-8"), encoding="utf-8")

        run(
            [
                chrome,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                "--no-pdf-header-footer",
                "--print-to-pdf-no-header",
                f"--print-to-pdf={output}",
                temp_html.as_uri(),
            ]
        )

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
