import pandas as pd

REQUIRED_ORDERS_COLS = {"order_id", "user_id", "order_date", "product_id", "quantity", "unit_price"}
REQUIRED_USERS_COLS = {"user_id", "email", "full_name"}
REQUIRED_PRODUCTS_COLS = {"product_id", "sku", "name", "category", "price"}

class ValidationError(Exception):
    pass

def ensure_columns(df, required, name):
    missing = required - set(df.columns)
    if missing:
        raise ValidationError(f"{name} missing columns: {sorted(missing)}")

def validate_users_df(df):
    ensure_columns(df, REQUIRED_USERS_COLS, "users")
    if df["user_id"].isna().any():
        raise ValidationError("users.user_id contains nulls")
    if df["email"].isna().any():
        raise ValidationError("users.email contains nulls")
    if df["email"].duplicated().any():
        raise ValidationError("users.email contains duplicates")
    return True

def validate_products_df(df):
    ensure_columns(df, REQUIRED_PRODUCTS_COLS, "products")
    if (df["price"] <= 0).any():
        raise ValidationError("products.price must be positive")
    if df["sku"].duplicated().any():
        raise ValidationError("products.sku contains duplicates")
    return True

def validate_orders_df(df):
    ensure_columns(df, REQUIRED_ORDERS_COLS, "orders")
    if (df["quantity"] <= 0).any():
        raise ValidationError("orders.quantity must be positive")
    if (df["unit_price"] <= 0).any():
        raise ValidationError("orders.unit_price must be positive")
    if df["order_id"].isna().any():
        raise ValidationError("orders.order_id contains nulls")
    if df["product_id"].isna().any():
        raise ValidationError("orders.product_id contains nulls")
    return True

def validate_pipeline_inputs(users_df, products_df, orders_df):
    validate_users_df(users_df)
    validate_products_df(products_df)
    validate_orders_df(orders_df)
    return True