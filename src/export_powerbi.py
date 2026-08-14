import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def export_df(df, path): 
    ensure_dir(os.path.dirname(path)) 
    df.to_csv(path, index=False)

def export_all(export_dir, category_df, clv_df, affinity_df):