import pandas as pd

def compute_category_revenue(orders_df, products_df):
    df = orders_df.merge(products_df, on="product_id", how="left")
    df["line_revenue"] = df["quantity"] * df["unit_price"]
    return df.groupby("category", as_index=False) ["line_revenue"].sum().sort_values("line_revenue", ascending=False)

def compute_clv_by_user(orders_df):
    df = orders_df.copy()
    df["line_revenue"] = df["quantity"] * df["unit_price"]