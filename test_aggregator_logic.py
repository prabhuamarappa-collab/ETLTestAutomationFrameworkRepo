import pandas as pd
import pymysql
from sqlalchemy import create_engine
import pytest

mysql_engine = create_engine("mysql+pymysql://root:Root%401234@localhost:3306/etlqalabs2")

def test_sales_data_aggregation_logic():
    df = pd.read_csv("Sales.csv")
    df['total_sales_amount'] = df["Price"] * df["Quantity"]
    expected_df = df.groupby('CustomerID')['total_sales_amount'].sum().round(2).reset_index()
    actual_df = pd.read_sql("select * from total_sales_per_customer",mysql_engine)
    print(expected_df)
    print(actual_df)

    assert expected_df.equals(actual_df),"ETL Process is not correctly transforming aggregation-please check"
    print("My Test case is passed")


