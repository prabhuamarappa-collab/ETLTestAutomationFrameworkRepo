import pandas as pd
import pytest

#4 Test cases

#1 test if there are any duplicate records/rows in the target system
def test_checkDuplicates():
    target_df = pd.read_csv("target.csv")
    count = target_df.duplicated().sum()
    assert count == 0,"Duplicated found please verify the target"

#2 test if target is not blank
def test_DataCompleteness():
    target_df = pd.read_csv("target.csv")
    assert not target_df.empty,"Target file is empty, please verify the ETL Process"

#3 test if deptno is a mandatory column, check for null values any
def test_deptNoForNullValueCheck():
    target_df = pd.read_csv("target.csv")
    isDeptNoNull = target_df['deptno'].isnull().any()
    assert isDeptNoNull==False, "depno is having null value - please check"

#4 test if eno is always a primary key
def test_enoForUniqueValueCheck():
    target_df = pd.read_csv("target.csv")
    totalCount = target_df['eno'].count()
    deptNoUniqueValueCount = len(target_df['eno'].unique())
    assert totalCount == deptNoUniqueValueCount, "eno column values are not unique - please check"