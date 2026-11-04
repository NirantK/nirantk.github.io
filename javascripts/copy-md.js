(function () {
  const RAW_BASE =
    "https://raw.githubusercontent.com/NirantK/nirantk.github.io/main/docs/";
  const ORIGINAL_LABEL = "Copy as Markdown";

  function setLabel(btn, text) {
    const label = btn.querySelector(".copy-md-label");
    if (label) label.textContent = text;
  }

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      const ok = await navigator.clipboard
        .writeText(text)
        .then(() => true, () => false);
      if (ok) return true;
    }
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.top = "0";
    ta.style.left = "0";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    const ok = document.execCommand("copy");
    document.body.removeChild(ta);
    return ok;
  }

  async function handleClick(e) {
    const btn = e.currentTarget;
    const src = btn.getAttribute("data-md-src");
    if (!src) return;

    setLabel(btn, "Fetching…");
    btn.disabled = true;

    const url = RAW_BASE + src;
    const res = await fetch(url, { cache: "no-cache" });
    if (!res.ok) {
      setLabel(btn, "Failed — try again");
      btn.disabled = false;
      setTimeout(() => setLabel(btn, ORIGINAL_LABEL), 2000);
      return;
    }
    const text = await res.text();
    const copied = await copyText(text);
    setLabel(btn, copied ? "Copied ✓" : "Press ⌘C to copy");
    setTimeout(() => {
      setLabel(btn, ORIGINAL_LABEL);
      btn.disabled = false;
    }, copied ? 1800 : 3000);
  }

  function inject() {
    const meta = document.querySelector('meta[name="md-src-uri"]');
    if (!meta) return;
    const src = meta.getAttribute("content");
    if (!src) return;

    const article = document.querySelector("article.md-content__inner");
    if (!article) return;
    if (article.querySelector(".md-button--copy-md")) return;

    const wrap = document.createElement("div");
    wrap.className = "copy-md-wrap";

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "md-button md-button--copy-md";
    btn.setAttribute("data-md-src", src);
    btn.setAttribute("aria-label", "Copy page as Markdown");

    const label = document.createElement("span");
    label.className = "copy-md-label";
    label.textContent = ORIGINAL_LABEL;

    btn.appendChild(label);
    wrap.appendChild(btn);
    article.insertBefore(wrap, article.firstChild);

    btn.addEventListener("click", handleClick);
  }

  if (typeof document$ !== "undefined" && document$ && document$.subscribe) {
    document$.subscribe(inject);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inject);
  } else {
    inject();
  }
})();
