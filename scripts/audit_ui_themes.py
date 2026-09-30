import json
import os
import sys
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:8085"
OUTPUT_DIR = "/Users/prajwal/praj_work/praj_personal/scratch/screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGES = [
    "/index.html",
    "/articles/index.html",
    "/articles/multimodal-rag-image-extraction.html",
    "/articles/rag-system-evaluation-and-metrics.html",
    "/articles/hybrid-retrieval-rrf-and-fusion.html",
    "/articles/agentic-rag-routing-and-crag.html",
    "/articles/multi-agent-systems-orchestration.html",
    "/articles/multi-agent-failure-modes-and-observability.html",
    "/articles/multi-agent-security-guardrails-and-hitl.html",
    "/articles/multi-agent-human-in-the-loop-dual-key.html",
]

VIEWPORTS = {
    "desktop": {"width": 1280, "height": 800},
    "mobile": {"width": 390, "height": 844, "is_mobile": True},
}

THEMES = ["light", "dark"]

def run_audit():
    findings = {
        "broken_images": [],
        "failed_requests": [],
        "console_errors": [],
        "visual_inspections": []
    }
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for page_path in PAGES:
            page_slug = page_path.strip("/").replace("/", "_").replace(".html", "")
            if not page_slug:
                page_slug = "home"
                
            for vp_name, vp_config in VIEWPORTS.items():
                for theme in THEMES:
                    context = browser.new_context(
                        viewport={"width": vp_config["width"], "height": vp_config["height"]},
                        is_mobile=vp_config.get("is_mobile", False),
                        has_touch=vp_config.get("is_mobile", False)
                    )
                    page = context.new_page()
                    
                    # Capture errors
                    page.on("console", lambda msg: findings["console_errors"].append(
                        {"page": page_path, "type": msg.type, "text": msg.text}
                    ) if msg.type in ["error", "warning"] else None)
                    page.on("pageerror", lambda err: findings["console_errors"].append(
                        {"page": page_path, "type": "uncaught", "text": str(err)}
                    ))
                    page.on("requestfailed", lambda req: findings["failed_requests"].append(
                        {"page": page_path, "url": req.url, "failure": req.failure}
                    ))
                    
                    # Set localStorage theme before load
                    page.add_init_script(f"""
                        try {{
                            localStorage.setItem('theme', '{theme}');
                        }} catch (e) {{}}
                    """)
                    
                    url = f"{BASE_URL}{page_path}"
                    res = page.goto(url, wait_until="networkidle")
                    
                    # Force data-theme explicitly just to be 100% sure
                    page.evaluate(f"document.documentElement.setAttribute('data-theme', '{theme}');")
                    page.wait_for_timeout(200)
                    # Scroll to trigger lazy loading
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                    page.wait_for_timeout(400)
                    page.evaluate("window.scrollTo(0, 0);")
                    page.wait_for_timeout(200)
                    
                    # Check for broken images
                    broken_imgs = page.evaluate("""() => {
                        const imgs = Array.from(document.querySelectorAll('img'));
                        return imgs.filter(img => !img.complete || img.naturalWidth === 0).map(img => ({
                            src: img.getAttribute('src'),
                            alt: img.getAttribute('alt') || '',
                            currentSrc: img.currentSrc
                        }));
                    }""")
                    
                    if broken_imgs:
                        for b in broken_imgs:
                            findings["broken_images"].append({
                                "page": page_path,
                                "theme": theme,
                                "viewport": vp_name,
                                "img": b
                            })
                    
                    # Inspect contrast and hardcoded styling
                    style_check = page.evaluate("""(theme) => {
                        const results = [];
                        // Check diagram wrappers
                        document.querySelectorAll('.article-diagram-wrapper').forEach((el, idx) => {
                            const cs = window.getComputedStyle(el);
                            results.push({
                                element: `.article-diagram-wrapper[${idx}]`,
                                bg: cs.backgroundColor,
                                border: cs.borderColor,
                                theme: theme
                            });
                        });
                        // Check diagram captions
                        document.querySelectorAll('.article-diagram-caption').forEach((el, idx) => {
                            const cs = window.getComputedStyle(el);
                            results.push({
                                element: `.article-diagram-caption[${idx}]`,
                                bg: cs.backgroundColor,
                                color: cs.color,
                                theme: theme
                            });
                        });
                        // Check TOC
                        document.querySelectorAll('.article-toc, .toc-wrapper, .table-of-contents').forEach((el, idx) => {
                            const cs = window.getComputedStyle(el);
                            results.push({
                                element: `TOC[${idx}]`,
                                bg: cs.backgroundColor,
                                border: cs.borderColor,
                                color: cs.color,
                                theme: theme
                            });
                        });
                        return results;
                    }""", theme)
                    
                    findings["visual_inspections"].extend(style_check)
                    
                    screenshot_name = f"{page_slug}_{theme}_{vp_name}.png"
                    screenshot_path = os.path.join(OUTPUT_DIR, screenshot_name)
                    page.screenshot(path=screenshot_path, full_page=True)
                    print(f"Captured: {screenshot_name}")
                    
                    context.close()
                    
        browser.close()
        
    report_path = os.path.join(OUTPUT_DIR, "audit_report.json")
    with open(report_path, "w") as f:
        json.dump(findings, f, indent=2)
    print(f"\nAudit completed. Report written to {report_path}")

if __name__ == "__main__":
    run_audit()
