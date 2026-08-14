from src.config import load_config
from src.mysql_ingest import connect_mysql, fetch_orders_df, fetch_products_df, fetch_users_df
from src.recommendations import build_copurchase_pairs
from src.analytics import compute_category_revenue, compute_clv_by_user, compute_product_affinity_score
from src.export_powerbi import export_all
from src.neo4j_graph import connect_neo4j, upsert_graph

def main():
    cfg = load_config()
    mysql_conn = connect_mysql(cfg["mysql"])