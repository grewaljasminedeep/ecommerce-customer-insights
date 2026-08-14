from src.config import load_config
from src.mysql_ingest import connect_mysql, fetch_orders_df, fetch_products_df, fetch_users_df
from src.recommendations import build_copurchase_pairs
from src.analytics import compute_category_revenue, compute_clv_by_user, compute_product_affinity_score
from src.export_powerbi import export_all
from src.neo4j_graph import connect_neo4j, upsert_graph

def main():
    cfg = load_config()
    mysql_conn = connect_mysql(cfg["mysql"])
    users_df = fetch_users_df(mysql_conn)
    products_df = fetch_products_df(mysql_conn)
    orders_df = fetch_orders_df(mysql_conn)
    pairs_df = build_copurchase_pairs(orders_df)
    category_df = compute_category_revenue(orders_df, products_df)
    clv_df = compute_clv_by_user(orders_df)
    affinity_df = compute_product_affinity_score(pairs_df)
    export_all(cfg["pipeline"] ["export_dir"], category_df, clv_df, affinity_df)
    neo4j_driver = connect_neo4j(cfg["neo4j"])
    upsert_graph(neo4j_driver, users_df, products_df, orders_df)
    neo4j_driver.close()
    mysql_conn.close()

if __name__ == "__main__": main()