class GraphQueries:
    @staticmethod
    def create_constraints():
        return [
            "CREATE CONSTRAINT user_id_unique IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE",
            "CREATE CONSTRAINT product_id_unique IF NOT EXISTS FOR (p:Product) REQUIRE p.id IS UNIQUE",
        ]

    @staticmethod
    def upsert_users():
        return "MERGE (u:User {id: $id}) SET u.email = $email, u.full_name = $full_name"

    @staticmethod
    def upsert_product():
        return """
        MERGE (p:Product {id: $id})
        SET p.sku = $sku, p.name = $name, p.category = $category, p.price = $price
        """

    @staticmethod
    def upsert_purchase():
        return """
        MATCH (u:User {id: $user_id})
        MATCH (p:Product {id: $product_id})
        MERGE (u)-[:PURCHASED {order_id: $order_id}]->(p)
        SET _.quantity = $quantity, _.unit_price = $unit_price
        """

    @staticmethod
    def recommend_by_copurchase():
        return """
        MATCH (u:User)-[:PURCHASED]->(p1:Product {id: $product_id})
        MATCH (u)-[:PURCHASED]->(p2:Product)
        WHERE p2.id <> $product_id
        RETURN p2.id AS product_id, p2.name AS product_name, count(*) AS co_purchase_count
        ORDER BY co_purchase_count DESC, product_name ASC
        LIMIT $limit
        """

    @staticmethod
    def top_affinity_pairs():
        return """
        MATCH (p1:Product)<-[:PURCHASED]-(u:User)-[:PURCHASED]->(p2:Product)
        WHERE p1.id < p2.id
        RETURN p1.id AS product_id_a, p2.id AS product_id_b, count(*) AS co_purchase_count
        ORDER BY co_purchase_count DESC
        LIMIT $limit
        """