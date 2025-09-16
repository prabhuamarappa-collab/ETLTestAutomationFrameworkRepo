import pandas as pd
from sqlalchemy import create_engine
import pymysql
import oracledb
import numpy as np
import pytest
from ETL_Process_Mysql2Oracle import extract, load

@pytest.fixture(scope='session',autouse=True)
def df():
    df, tbl = extract()
    yield df
    #will be executed after last test
    load(df,tbl)

#1Check if Column Exist (ProducKey)
def test_col_exists(df):
    name = 'cid'
    assert name in df.columns,'column does not exist'

#2Check for nulls
def test_null_check(df):
    #assert np.where(df['ProductKey'].isnull())
    assert df['cid'].notnull().all(),"found null values in CID column"

#3Check values are unique
def test_unique_check(df):
    assert df['cid'].is_unique,'found duplicates'
    #assert pd.Series(df['ProductKey']).is_unique

#4Check Datatype
def test_Productkey_dtype_int(df):
    assert (df['cid'].dtype == int or df['CID'].dtype == np.int64)

#5Check datatype
def test_Productkey_dtype_srt(df):
    assert (df['cname'].dtype == str or df['cname'].dtype =='O')

#6Check value in range
def test_range_val(df):
    assert df['cid'].between(1,5).all()

#7Check list of values in dataframe column
def test_range_val_str(df):
    assert set(df['cname'].unique()) == { 'prabhu', 'guru', 'shivu', 'shreyas', 'manta'}
