import pandas as pd
from sqlalchemy import create_engine, false
import pymysql
import oracledb

#mysql conn
mysql_conn = create_engine("mysql+pymysql://root:Root%401234@localhost:3306/etlqalabs")
df = pd.read_sql("select * from employees_raw",mysql_conn)
print(df)

#oracle conn
oracle_conn = create_engine("oracle+oracledb://C##HR:hr123@localhost:1521/xe")

