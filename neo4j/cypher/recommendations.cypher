MATCH (u:User)-[:PURCHASED]->(p1:Product {id: $productId})
MATCH (u)-[:PURCHASED]->(p2:Product)
WHERE p2.id <> $productId
RETURN p2.name AS RecommendedProduct, count(*) AS CoPurchaseCount
ORDER BY CoPurchaseCount DESC
LIMIT 5;