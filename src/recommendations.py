import pandas as pd

def build_copurchase_pairs(orders_df):
    pairs = {}
    for order_id, grp in orders_df.groupby('order_id'):
        product_ids = sorted(set(grp['product_id'].tolist()))
        for i in range(len(product_ids)):
            for j in range(i + 1, len(product_ids)):
                a, b = product_ids[i], product_ids[j]
                pairs[(a, b)] = pairs.get((a, b), 0) + 1