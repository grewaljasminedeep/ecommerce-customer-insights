import pandas as pd

def build_copurchase_pairs(orders_df):
    pairs = {}
    for order_id, grp in orders_df.groupby('order_id'):
        product_ids = sorted(set(grp['product_id'].tolist()))
        for i in range(len(product_ids)):
            for j in range(i + 1, len(product_ids)):
                a, b = product_ids[i], product_ids[j]
                pairs[(a, b)] = pairs.get((a, b), 0) + 1
    rows = [{"product_id_a": a, "product_id_b": b, "copurchase_count": c} for (a, b), c in pairs.items()]
    return pd.DataFrame(rows)

def top_recommendations_for_product(pairs_df, product_id, limit=5, min_count=1):
    if pairs_df.empty:
        return pd.DataFrame(columns=["recommended_product_id", "co_purchase_count"])
    mask_a = pairs_df['product_id_a'] == product_id
    mask_b = pairs_df['product_id_b'] == product_id
    subset = pairs_df[mask_a | mask_b].copy()
    if subset.empty: