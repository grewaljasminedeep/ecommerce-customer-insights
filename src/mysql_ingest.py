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