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