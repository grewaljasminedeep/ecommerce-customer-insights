import pandas as pd
import pytest
from src.validation import validate_users_df, validate_products_df, validate_orders_df, ValidationError

def test_validate_users_ok():
    df = pd.DataFrame([{
        "user_id": 1,
        "email": "a@b.com",
        "full_name": "A"
    }])
    assert validate_users_df(df) is True

def test_validate_products_reject_negative_price():
    df = pd.DataFrame([{
        "product_id": 1,
        "sku": "S1",
        "name": "P",
        "category": "C",
        "price": -1}])
    with pytest.raises(ValidationError):
        validate_products_df(df)

def test_validate_orders_reject_zero_quantity():
    df = pd.DataFrame([{
        "order_id": 1,
        "user_id": 1,
        "order_date": "2023-01-01",
        "product_id": 1,
        "quantity": 0,
        "unit_price": 10}])
    with pytest.raises(ValidationError):
        validate_orders_df(df)