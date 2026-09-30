// assets/js/rrf-simulator.js — Interactive Reciprocal Rank Fusion (RRF) Playground
document.addEventListener("DOMContentLoaded", () => {
  const kSlider = document.getElementById("rrf-k-slider");
  const kVal = document.getElementById("rrf-k-val");
  const denseWeightSlider = document.getElementById("rrf-dense-slider");
  const denseWeightVal = document.getElementById("rrf-dense-val");
  const sparseWeightSlider = document.getElementById("rrf-sparse-slider");
  const sparseWeightVal = document.getElementById("rrf-sparse-val");
  const tableBody = document.getElementById("rrf-results-body");

  if (!tableBody) return;

  // Sample Documents representing candidate passages for:
  // "How does image extraction compare between OCR and ColPali in multimodal RAG?"
  const documents = [
    {
      id: "Doc-A",
      title: "ColPali: Efficient Document Retrieval with Vision Language Models & Patch Embeddings",
      denseRank: 1,  // High semantic alignment
      sparseRank: 14 // Low exact BM25 keyword overlap
    },
    {
      id: "Doc-B",
      title: "Benchmarking Tesseract OCR vs AWS Textract on Financial PDF Balance Sheets",
      denseRank: 8,  // Moderate semantic alignment
      sparseRank: 1  // Exact lexical keyword match on 'OCR' and 'extraction'
    },
    {
      id: "Doc-C",
      title: "Hybrid Search Fusion: Evaluating Reciprocal Rank Fusion on Multi-Page Documents",
      denseRank: 3,  // High semantic
      sparseRank: 4  // Strong lexical
    },
    {
      id: "Doc-D",
      title: "Naive Chunking Strategies: The 512-Token Window Trap in Unstructured Text",
      denseRank: 12,
      sparseRank: 9
    },
    {
      id: "Doc-E",
      title: "Multi-Vector Late Interaction: Accelerating PLAID Indexing for Visual Retrieval",
      denseRank: 2,
      sparseRank: 11
    }
  ];

  function recalculate() {
    const k = parseInt(kSlider ? kSlider.value : "60", 10);
    const wDense = parseFloat(denseWeightSlider ? denseWeightSlider.value : "1.0");
    const wSparse = parseFloat(sparseWeightSlider ? sparseWeightSlider.value : "1.0");

    if (kVal) kVal.innerText = k;
    if (denseWeightVal) denseWeightVal.innerText = wDense.toFixed(1);
    if (sparseWeightVal) sparseWeightVal.innerText = wSparse.toFixed(1);

    const scored = documents.map(doc => {
      const denseScore = wDense * (1 / (k + doc.denseRank));
      const sparseScore = wSparse * (1 / (k + doc.sparseRank));
      const totalRrf = denseScore + sparseScore;
      return {
        ...doc,
        denseScore,
        sparseScore,
        totalRrf
      };
    });

    // Sort descending by total RRF score
    scored.sort((a, b) => b.totalRrf - a.totalRrf);

    // Render HTML rows
    tableBody.innerHTML = scored.map((item, index) => {
      const rank = index + 1;
      const rankBadgeColor = rank === 1 ? "var(--accent-emerald)" : rank === 2 ? "var(--accent)" : "var(--text-muted)";
      return `
        <tr>
          <td><span class="rank-badge" style="background: rgba(255,255,255,0.06); color: ${rankBadgeColor}">#${rank}</span></td>
          <td><strong>${item.id}</strong></td>
          <td style="max-width: 320px;">${item.title}</td>
          <td><span style="font-family: var(--font-mono);">#${item.denseRank}</span></td>
          <td><span style="font-family: var(--font-mono);">#${item.sparseRank}</span></td>
          <td><strong style="font-family: var(--font-mono); color: var(--accent);">${item.totalRrf.toFixed(6)}</strong></td>
        </tr>
      `;
    }).join("");
  }

  if (kSlider) kSlider.addEventListener("input", recalculate);
  if (denseWeightSlider) denseWeightSlider.addEventListener("input", recalculate);
  if (sparseWeightSlider) sparseWeightSlider.addEventListener("input", recalculate);

  recalculate();
});
