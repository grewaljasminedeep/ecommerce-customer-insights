from neo4j import GraphDatabase

def connect_neo4j(cfg):
    return GraphDatabase.driver(cfg["uri"], auth=(cfg["user"], cfg["password"]))

def upsert_graph(driver, users_df, products_df, orders_df):
    with driver.session() as session:
        for _, row in users_df.iterrows():
            session.run(
                "MERGE (u:User {id: $id}) SET u.email = $email, u,full_name = $full_name",