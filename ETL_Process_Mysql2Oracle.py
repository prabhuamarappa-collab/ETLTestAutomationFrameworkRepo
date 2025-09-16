import pandas as pd
from sqlalchemy import create_engine
import pymysql
import oracledb

#mysql configuartions
username = "root"
password = 'Root%401234'
host = "localhost"
port = 3306
database = "etlqalabs"

#Oracle configuartions
Ousername = "C##HR"
Opassword = 'hr123'
Ohost = "localhost"
Oport = 1521
Odatabase = "XE"


#Extract data from mysql
def extract():
    try:
        mysql_conn = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        tabe_name = 'customers'
        df = pd.read_sql(f"select * from {tabe_name}", mysql_conn)
        print("data from mysql:")
        print(df)
        return df, tabe_name
    except Exception as e:
        print("Data Extract error:" + str(e))

#Load data to Oracle
def load(df,tbl):
    try:
        oracle_conn = create_engine(f"oracle+oracledb://{Ousername}:{Opassword}@{Ohost}:{Oport}/{Odatabase}")
        df.to_sql(f'{tbl}', oracle_conn, if_exists="replace", index=False)

        print("Data Successfully Copied from Mysql to Oracle")
    except Exception as e:
        print("Data Load error :" + str(e))




