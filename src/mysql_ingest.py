import mysql.connector
import pandas as pd

def connect_mysql(cfg):
    return mysql.connector.connect(
        host=cfg["host"],
        port=cfg["port"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"]
    )

def fetch_orders_df(conn):
    query = """
    SELECT o.order_id, o.user_id, o.order_date, oi.product_id, oi.quantity, oi.price
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'COMPLETED'
    """
    return pd.read_sql(query, conn)

def fetch_products_df(conn):
    return pd.read_sql("SELECT product_id, sku, name, category, price FROM products", conn)

def fetch_users_df(conn):
    return pd.read_sql("SELECT user_id, email, full_name FROM users", conn)