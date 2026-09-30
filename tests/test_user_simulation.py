# projects/personal-website/tests/test_user_simulation.py
import pytest

# Simulates the Reciprocal Rank Fusion calculation logic from rrf-simulator.js
def compute_rrf_scores(k: int, w_dense: float, w_sparse: float):
    documents = [
        {"id": "Doc-A", "denseRank": 1, "sparseRank": 14},
        {"id": "Doc-B", "denseRank": 8, "sparseRank": 1},
        {"id": "Doc-C", "denseRank": 3, "sparseRank": 4},
        {"id": "Doc-D", "denseRank": 12, "sparseRank": 9},
        {"id": "Doc-E", "denseRank": 2, "sparseRank": 11}
    ]
    results = []
    for doc in documents:
        score = w_dense * (1 / (k + doc["denseRank"])) + w_sparse * (1 / (k + doc["sparseRank"]))
        results.append({
            "id": doc["id"],
            "score": score
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def test_user_simulation_default_rrf():
    # User Scenario 1: Default standard settings (k=60, equal weights 1.0, 1.0)
    scores = compute_rrf_scores(k=60, w_dense=1.0, w_sparse=1.0)
    # Doc-C (rank 3 in dense, rank 4 in sparse) is consistently strong across both and should be top 2
    top_ids = [d["id"] for d in scores[:2]]
    assert "Doc-C" in top_ids
    assert scores[0]["score"] > scores[-1]["score"]

def test_user_simulation_heavy_dense_bias():
    # User Scenario 2: User prioritizes dense semantic search (w_dense=2.0, w_sparse=0.2)
    scores = compute_rrf_scores(k=60, w_dense=2.0, w_sparse=0.2)
    # Doc-A has denseRank=1; with heavy dense weight, Doc-A must win #1
    assert scores[0]["id"] == "Doc-A"

def test_user_simulation_heavy_sparse_bias():
    # User Scenario 3: User prioritizes exact BM25 keyword matching (w_dense=0.2, w_sparse=2.0)
    scores = compute_rrf_scores(k=60, w_dense=0.2, w_sparse=2.0)
    # Doc-B has sparseRank=1; with heavy sparse weight, Doc-B must win #1
    assert scores[0]["id"] == "Doc-B"
