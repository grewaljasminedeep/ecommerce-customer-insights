USE ecommerce_db;

INSERT INTO users (email, full_name) VALUES
('alice@example.com', 'Alice Chen'),
('bob@example.com', 'Bob Patel'),
('carla@example.com', 'Carla Gomez');

INSERT INTO products (sku, name, category, price) VALUES
('SKU-1001', 'Wireless Mouse', 'Accessories', 29.99),
('SKU-1002', 'Mechanical Keyboard', 'Accessories', 89.99),
('SKU-2001', 'USB-C Hub', 'Accessories', 49.99),
('SKU-3001', 'Office Chair', 'Furniture', 199.99);

INSERT INTO orders (user_id, status) VALUES
(1, 'COMPLETED'),
(2, 'COMPLETED'),
(3, 'COMPLETED');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 29.99),
(1, 2, 1, 89.99),
(2, 1, 1, 29.99),
(2, 3, 1, 49.99),
(3, 2, 1, 89.99),
(3, 3, 1, 49.99);