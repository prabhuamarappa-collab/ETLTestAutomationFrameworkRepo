import pandas as pd
import pytest
from sqlalchemy import create_engine
import oracledb

engine = create_engine("oracle+oracledb://system:newpassword@localhost:1521/XE")

def test_data_type_validation():
    df = pd.read_sql("select * from city",engine)
    print("actual data :", df)
    actual_datatype = df.dtypes.to_dict()
    print("datatype of actual :",actual_datatype)
    expected_datatype = {"id":"int64","name":"object"}
    print("datatype of expected :", expected_datatype)

    assert actual_datatype == expected_datatype,"actual datatype does not match expected"