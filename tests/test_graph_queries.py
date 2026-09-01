from src.graph_queries import GraphQueries

def test_recommend_query_contains_limit():
    q = GraphQueries.recommend_by_copurchase()
    assert "LIMIT $limit" in q