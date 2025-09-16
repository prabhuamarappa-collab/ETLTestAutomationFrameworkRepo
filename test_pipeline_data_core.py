import pytest
import pandas as pd
import numpy as np
from numpy import nan

@pytest.fixture()
def df():
    df = pd.read_excel("Product.xlsx")
    return df

#1Check if Column Exist (ProducKey)
def test_col_exists(df):
    name = 'ProductKey'
    assert name in df.columns,'column does not exist'

#2Check for nulls
def test_null_check(df):
    #assert np.where(df['ProductKey'].isnull())
    assert df['ProductKey'].notnull().all(),"found null values in ProductKey column"

#3Check values are unique
def test_unique_check(df):
    assert df['ProductKey'].is_unique,'found duplicates'
    #assert pd.Series(df['ProductKey']).is_unique

#4Check Datatype
def test_Productkey_dtype_int(df):
    assert (df['ProductKey'].dtype == int or df['ProductKey'].dtype == np.int64)

#5Check datatype
def test_Productkey_dtype_srt(df):
    assert (df['EnglishProductName'].dtype == str or df['EnglishProductName'].dtype =='O')

#6Check value in range
def test_range_val(df):
    assert df['SafetyStockLevel'].between(0,1000).all()

#7Check list of values in dataframe column
def test_range_val_str(df):
    assert set(df['Color'].unique()) == {nan, 'Black', 'Silver', 'Red', 'White', 'Blue', 'Multi', 'Yellow', 'Grey', 'Silver/Black'}
