# Technical Architecture Guide: Personal Portfolio & RAG Platform

## Layer 1: The Big Picture (2 Minutes)
This platform serves two primary purposes:
1. Establish a high-authority personal engineering showcase for Prajwal Rao (@Riser01), highlighting production multi-agent systems and ML pipelines.
2. Provide a canonical, high-pedagogy publication platform for advanced AI systems research, specifically focusing on Retrieval-Augmented Generation (RAG).

The design philosophy favors **zero-maintenance resilience**: zero framework bloat, zero serverless runtime cold starts, zero client-side hydration delays, and instant deployment to GitHub Pages.

## Layer 2: How It Works — Step by Step
1. **Request Lifecycle:** When a user visits `https://riser01.github.io/`, GitHub Pages serves static semantic HTML. The browser parses CSS variables from `assets/css/main.css`, achieving First Contentful Paint in <300ms.
2. **Interactive Elements:**
   - Dark/Light Theme: `assets/js/main.js` reads `localStorage.getItem("theme")`, updating `data-theme` attribute on `<html>` without page flash.
   - Filter Grid: Pure DOM attribute queries (`data-category`) toggle project cards with CSS flex transitions.
   - Interactive RRF Calculator: `assets/js/rrf-simulator.js` recalculates multi-vector and lexical scores on every slider input event, updating table rows dynamically.
3. **Article Structure:**
   - Articles follow a dual-track pedagogical format (`.callout-novice` vs `.callout-deepdive`) ensuring high value for both beginners and senior engineers.

## Layer 3: Architecture & Design Decisions
### Why Pure Static HTML/CSS/JS over Next.js/Astro?
- **Zero Supply Chain Breakage:** Modern JS frameworks frequently suffer from package deprecation, security advisories in transitive dependencies, and breaking build-time changes. Pure HTML/CSS/JS is evergreen.
- **Maximized GitHub Pages Compatibility:** No GitHub Actions workflow build dependencies or custom Docker containers needed.
- **Portability:** The entire website can be previewed locally using `python3 -m http.server` without running `npm install`.

## Layer 4: Mathematical Formulations
### Reciprocal Rank Fusion (RRF)
$$RRF(d) = \sum_{m \in M} w_m \cdot \frac{1}{k + r_m(d)}$$
Where $k=60$ acts as a ranking dampener preventing top-rank outliers from monopolizing the merged list.

### Late Interaction MaxSim (ColPali / ColBERT)
$$\text{Score}(Q, D) = \sum_{i \in Q} \max_{j \in D} \left( \mathbf{E}(q_i) \cdot \mathbf{E}(d_j) \right)$$

### Normalized Discounted Cumulative Gain (NDCG@K)
$$\text{DCG}@K = \sum_{i=1}^{K} \frac{2^{\text{rel}_i} - 1}{\log_2(i + 1)}, \quad \text{NDCG}@K = \frac{\text{DCG}@K}{\text{IDCG}@K}$$

## Layer 5: Extending This Platform
- **Adding a New Article:**
  1. Duplicate an existing article HTML file into `articles/<slug>.html`.
  2. Add an entry to `articles/index.html` and the featured grid in `index.html`.
  3. Run `pytest tests/ -v` to ensure link integrity and SEO compliance.
