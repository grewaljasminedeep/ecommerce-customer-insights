from src.mysql_ingest import connect_mysql, fetch_orders_df, fetch_products_df, fetch_users_df
from src.validation import validate_pipeline_inputs

def run_ingest(cfg):
    conn = connect_mysql(cfg["mysql"])
    users_df = fetch_users_df(conn)
    products_df = fetch_products_df(conn)
    orders_df = fetch_orders_df(conn)
    validate_pipeline_inputs(users_df, products_df, orders_df)
    conn.close()
    return users_df, products_df, orders_df