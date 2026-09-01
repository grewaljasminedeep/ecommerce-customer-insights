from src.neo4j_graph import connect_neo4j
from src.graph_queries import GraphQueries

def run_graph(cfg, users_df, products_df, orders_df):
    driver = connect_neo4j(cfg["neo4j"])
    with driver.session() as session:
        for q in GraphQueries.create_constraints():
            session.run(q)
        for _, row in users_df.iterrows():
            session.run(GraphQueries.upsert_user(), id=int(row["user_id"]), email=row["email"], full_name=row["full_name"])
        for _, row in products_df.iterrows():
            session.run(GraphQueries.upsert_product(), id=int(row["product_id"]), sku=row["sku"], name=row["name"], category=row["category"], price=float(row["price"]))
        for _, row in orders_df.iterrows():
            session.run(GraphQueries.upsert_purchase(), user_id=int(row["user_id"]), product_id=int(row["product_id"]), order_id=int(row["order_id"]), quantity=int(row["quantity"]), unit_price=float(row["unit_price"]))
    driver.close()