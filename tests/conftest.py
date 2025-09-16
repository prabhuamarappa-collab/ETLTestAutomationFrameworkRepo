import numpy as np
from math import isnan

import pandas as pd
from numpy.f2py.crackfortran import sourcecodeform
from sqlalchemy import create_engine, false
import pymysql
import oracledb
import pytest
from sqlalchemy.testing import fails

#mysql conn
@pytest.fixture(scope='session')
def mysql_conn():
    mysql_conn = create_engine("mysql+pymysql://root:Root%401234@localhost:3306/etlqalabs")
    return mysql_conn

@pytest.fixture(scope='session')
def oracle_conn():
    oracle_conn = create_engine("oracle+oracledb://C##HR:hr123@localhost:1521/xe")
    return oracle_conn

@pytest.fixture(scope='session')
def src_df(mysql_conn):
    src_df = pd.read_sql("select * from employees_raw", mysql_conn)
    return src_df

@pytest.fixture(scope='session')
def src_dept(mysql_conn):
    src_dept = pd.read_sql("select * from departments", mysql_conn)
    return src_dept

@pytest.fixture(scope='session')
def tgt_df(oracle_conn):
    tgt_df = pd.read_sql("select * from employees_dw", oracle_conn)
    return tgt_df