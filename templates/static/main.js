function diffView(selector, isInline) {
    console.log(selector, isInline);
    const accordion = document.getElementById(selector);
    let hideEl, showEl;
    if (isInline) {
        hideEl = accordion.querySelector("table.diff-side-by-side");
        showEl = accordion.querySelector("table.diff-inline");
    } else {
        hideEl = accordion.querySelector("table.diff-inline");
        showEl = accordion.querySelector("table.diff-side-by-side");
    }
    hideEl.style.display = "none";
    showEl.style.display = "block";
}
