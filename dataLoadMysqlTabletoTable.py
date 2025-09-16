import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine = create_engine("mysql+pymysql://root:Root%401234@localhost:3306/etlqalabs")

df = pd.read_sql("select * from source_data",engine)

df['Date_of_joining'] = pd.to_datetime(df['Date_of_joining'])

today = pd.to_datetime("today")
df['Experience'] = (today-df['Date_of_joining']).dt.days // 365

df_target = df.rename(columns={
    "empid" : "trg_emp",
    "emp_name" : "trg_emp_name",
    "emo_salary":"trg_emp_salary"
})

df_target = df_target[ ["trg_emp","trg_emp_name","trg_emp_salary","Experience"]]

df_target.to_sql("target_data",con=engine,if_exists="append",index=False)

print("Data successfully loaded into target_data table!")


