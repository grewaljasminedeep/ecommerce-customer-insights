from neo4j import GraphDatabase

def connect_neo4j(cfg):
    return GraphDatabase.driver(cfg["uri"], auth=(cfg["user"], cfg["password"]))

def upsert_graph(driver, users_df, products_df, orders_df):
    with driver.session() as session:
        for _, row in users_df.iterrows():
            session.run(
                "MERGE (u:User {id: $id}) SET u.email = $email, u,full_name = $full_name",
                id=int(row["id"]),
                email=row["email"],
                full_name=row["full_name"]
            )
        for _, row in products_df.iterrows():
            session.run(
                "MERGE (p:Product {id: $id}) SET p.sku = $sku, p.name = $name", p.category = $category", p.price = $price",
                id=int(row["product_id"]),
                sku=row["sku"],
                name=row["name"],