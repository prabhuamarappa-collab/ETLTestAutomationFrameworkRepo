import pandas as pd
import pytest
import openpyxl
from sqlalchemy import create_engine

mysql_engine = create_engine("mysql+pymysql://root:Root%401234@localhost:3306/etlqalabs2")

def test_aggregated_summary_level():
    #1 extract data from file
    df_src = pd.read_excel("D:/Downloads/transaction_data.xlsx")

    #2 transform data to aggregated level
    df_aggregated = df_src.groupby('CustomerID')['TotalAmount'].sum().reset_index()

    #3 extract data from target mysql table
    df_tgt = pd.read_sql("select * from customer_aggregated_data",mysql_engine)

    #4 compare src & tgt data & flag if any error
    assert df_aggregated.equals(df_tgt),"my test failed"
