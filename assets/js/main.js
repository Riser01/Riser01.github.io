// assets/js/main.js — Interactive Client Logic
document.addEventListener("DOMContentLoaded", () => {
  // 1. Theme Management (Dark / Light)
  const themeToggleBtn = document.getElementById("theme-toggle");
  const storedTheme = localStorage.getItem("theme") || "dark";
  document.documentElement.setAttribute("data-theme", storedTheme);
  updateThemeButton(storedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", () => {
      const currentTheme = document.documentElement.getAttribute("data-theme") || "dark";
      const newTheme = currentTheme === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme);
      updateThemeButton(newTheme);
    });
  }

  function updateThemeButton(theme) {
    if (!themeToggleBtn) return;
    themeToggleBtn.innerHTML = theme === "dark" 
      ? "☀️ <span>Light</span>" 
      : "🌙 <span>Dark</span>";
  }

  // 2. Project Filtering
  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const filter = btn.getAttribute("data-filter");
      projectCards.forEach(card => {
        if (filter === "all" || card.getAttribute("data-category") === filter) {
          card.style.display = "flex";
        } else {
          card.style.display = "none";
        }
      });
    });
  });

  // 3. Code Copy Buttons
  document.querySelectorAll(".copy-btn").forEach(btn => {
    btn.addEventListener("click", async () => {
      const wrapper = btn.closest(".code-wrapper");
      if (!wrapper) return;
      const code = wrapper.querySelector("code");
      if (!code) return;

      try {
        await navigator.clipboard.writeText(code.innerText);
        const originalText = btn.innerText;
        btn.innerText = "Copied!";
        btn.style.color = "var(--accent-emerald)";
        setTimeout(() => {
          btn.innerText = originalText;
          btn.style.color = "";
        }, 2000);
      } catch (err) {
        console.error("Failed to copy code: ", err);
      }
    });
  });

  // 4. Smooth scroll TOC highlighting
  const tocLinks = document.querySelectorAll(".toc-list a");
  const headings = Array.from(tocLinks).map(link => {
    const id = link.getAttribute("href").substring(1);
    return document.getElementById(id);
  }).filter(Boolean);

  if (headings.length > 0) {
    window.addEventListener("scroll", () => {
      const scrollPos = window.scrollY + 120;
      let activeId = "";

      for (const h of headings) {
        if (h.offsetTop <= scrollPos) {
          activeId = h.getAttribute("id");
        }
      }

      tocLinks.forEach(link => {
        if (link.getAttribute("href") === `#${activeId}`) {
          link.style.color = "var(--accent)";
          link.style.fontWeight = "600";
        } else {
          link.style.color = "";
          link.style.fontWeight = "";
        }
      });
    }, { passive: true });
  }
});
