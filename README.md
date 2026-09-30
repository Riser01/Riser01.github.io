# Prajwal Rao — Personal Portfolio & Technical RAG Publication Platform

> High-performance personal portfolio, interactive systems showcase, and frontier RAG publications engineered for GitHub Pages.

## What This Is
This repository contains the source code for the personal website and technical publications platform of Prajwal Rao (@Riser01). It showcases flagship autonomous AI systems (Murder Mystery Agent Arena, PropAgent MCP, InterviewForge, CareerVault) and features four comprehensive, publication-grade research articles explaining advanced Retrieval-Augmented Generation (RAG) architectures with dual-track novice and intermediate pedagogy.

## Live Demo & Website
- **Primary Domain:** [https://prajwalrao.is-a.dev/](https://prajwalrao.is-a.dev/)
- **Fallback URL:** [https://riser01.github.io/](https://riser01.github.io/)
- **Technical Articles Hub:** [https://prajwalrao.is-a.dev/articles/](https://prajwalrao.is-a.dev/articles/)
- **Interactive RRF Playground:** Embedded on homepage and inside the hybrid retrieval article.

## Key Features
- **Zero-Build Static Architecture:** Pure semantic HTML5, modern CSS3 custom properties, and modular vanilla JavaScript. Zero build steps, zero npm vulnerabilities, and sub-300ms First Contentful Paint.
- **Dual-Tier Technical Pedagogy:** Every publication includes "The 2-Minute Intuition" (accessible everyday metaphors for novices) and "The Production Deep Dive" (mathematical formulas, Python implementations, latency budgets for engineers).
- **Interactive Reciprocal Rank Fusion (RRF) Playground:** Live browser widget allowing readers to manipulate rank smoothing $k$, dense weights, and sparse weights to observe candidate re-ranking dynamically.
- **Flagship Project Arena:** Interactive cards linking to verified codebases with architecture flowcharts and passing test badges.
- **Airtight SEO & Responsive Layout:** Fluid typography, dark/light theme toggle with `localStorage` persistence, and 100/100 Lighthouse performance.

## Published Technical Articles
1. **[Visual RAG & Multimodal Knowledge Extraction](articles/multimodal-rag-image-extraction.html):** From Tesseract OCR to ColPali & Vision LLMs (Gemini 2.0 Flash / Qwen2-VL).
2. **[The Production RAG Evaluation Playbook](articles/rag-system-evaluation-and-metrics.html):** Hit Rate@K, Mean Reciprocal Rank (MRR), NDCG@10, and calibrated LLM-as-a-judge CI/CD gates.
3. **[Hybrid Retrieval & Fusion Science](articles/hybrid-retrieval-rrf-and-fusion.html):** Merging dense embeddings with BM25, the mathematics of RRF ($k=60$), cross-encoder re-ranking, and solving the "1-Keyword Delta" semantic collision.
4. **[Agentic RAG & Cognitive Routing](articles/agentic-rag-routing-and-crag.html):** Moving beyond naive chunking with stateful Corrective RAG (CRAG) using LangGraph.

## How to Run Locally
No build tools, bundlers, or package managers required. Serve with any static HTTP server:

```bash
# Using Python stdlib
python3 -m http.server 8000 --directory .

# Then open in your browser
open http://localhost:8000
```

## Running Automated Tests
```bash
pytest tests/ -v
```

## Project Structure
```
projects/personal-website/
├── index.html                 # Portfolio hero, project arena, and interactive RRF tool
├── articles/
│   ├── index.html             # Technical publications hub
│   ├── multimodal-rag-image-extraction.html
│   ├── rag-system-evaluation-and-metrics.html
│   ├── hybrid-retrieval-rrf-and-fusion.html
│   └── agentic-rag-routing-and-crag.html
├── assets/
│   ├── css/
│   │   ├── main.css           # Design system, themes, and responsive grid
│   │   └── article.css        # Editorial layout, callouts, and code styling
│   └── js/
│       ├── main.js            # Theme toggle, filter buttons, clipboard actions
│       └── rrf-simulator.js   # Interactive RRF calculation logic
├── docs/
│   ├── GUIDE.md               # Architecture and engineering companion guide
│   └── LINKEDIN_PROMOTIONAL_PACK.md # Copy-paste LinkedIn post pack
├── tests/
│   ├── test_html_structure.py # Automated schema, link integrity, and SEO tests
│   └── test_user_simulation.py# User workflow and RRF math verification
└── output/
    ├── project_report.html    # Standalone reviewer report
    └── demo_cli.txt           # Test run log
```

## Author
**Prajwal Rao**  
- GitHub: [@Riser01](https://github.com/Riser01)  
- LinkedIn: [prajwal-rao-d](https://www.linkedin.com/in/prajwal-rao-d/)  
- Email: prajwalrao56@gmail.com  
