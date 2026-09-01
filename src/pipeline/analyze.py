from src.recommendations import build_copurchase_pairs
from src.analytics import compute_category_revenue, compute_clv_by_user, compute_product_affinity_score

def run_analyze(products_df, orders_df):
    pairs_df = build_copurchase_pairs(orders_df)
    category_df = compute_category_revenue(orders_df, products_df)
    clv_df = compute_clv_by_user(orders_df)
    affinity_df = compute_product_affinity_score(pairs_df)
    return category_df, clv_df, affinity_df