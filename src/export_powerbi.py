import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def export_df(df, path): 
    ensure_dir(os.path.dirname(path)) 
    df.to_csv(path, index=False)

def export_all(export_dir, category_df, clv_df, affinity_df):
    ensure_dir(export_dir)
    export_df(category_df, os.path.join(export_dir, "category_revenue.csv"))
    export_df(clv_df, os.path.join(export_dir, "customer_clv.csv"))
    export_df(affinity_df, os.path.join(export_dir, "product_affinity.csv"))