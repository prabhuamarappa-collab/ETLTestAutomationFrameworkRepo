import pandas as pd
from sqlalchemy import create_engine, false
import pymysql
import oracledb

#oracle conn
oracle_conn = create_engine("oracle+oracledb://C##HR:hr123@localhost:1521/xe")

df = pd.read_sql("select * from employees_dw",oracle_conn)

mysql_conn = create_engine("mysql+pymysql://root:Root%401234@localhost:3306/etlqalabs")

df2 = df.to_sql("employees_dw_Oracle_target",mysql_conn,if_exists="append",index=false())

print("data loaded to mysql table")

