(function () {
  const links = [
    { label: "APCS 題型", url: "https://apcs.csie.ntnu.edu.tw/index.php/questionstypes/websites/" },
    { label: "APCS 歷屆", url: "https://apcs.csie.ntnu.edu.tw/index.php/questionstypes/previousexam/" },
    { label: "LeetCode 題庫", url: "https://leetcode.com/problemset/" },
    { label: "Python 101", url: "https://hackmd.io/@arthurzllu/python101" }
  ];

  function addQuickLinks() {
    const headerInner = document.querySelector('.md-header .md-header__inner');
    if (!headerInner) return;
    if (headerInner.querySelector('.qa-links')) return; // 已加入

    const wrap = document.createElement('div');
    wrap.className = 'qa-links';

    links.forEach(l => {
      const a = document.createElement('a');
      a.href = l.url;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      const txt = document.createElement('span');
      txt.textContent = l.label;
      a.appendChild(txt);
      wrap.appendChild(a);
    });

    // 嘗試找搜尋框，將連結放在其「前面」
    const searchEl =
      headerInner.querySelector('[data-md-component="search"]') ||
      headerInner.querySelector('.md-search') ||
      null;

    if (searchEl && searchEl.parentNode === headerInner) {
      headerInner.insertBefore(wrap, searchEl);
    } else if (searchEl) {
      // 若 search 不在 headerInner 之下，則插入到其祖先前
      headerInner.insertBefore(wrap, headerInner.firstChild);
    } else {
      // 後備：找不到 search 時，仍加到右側
      headerInner.appendChild(wrap);
    }
  }

  document.addEventListener('DOMContentLoaded', addQuickLinks);
  // MkDocs Material SPA 導航事件
  document.addEventListener('navigation', addQuickLinks);
})();
