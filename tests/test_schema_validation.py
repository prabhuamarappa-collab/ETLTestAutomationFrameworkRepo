import numpy as np
from math import isnan

import pandas as pd
from numpy.f2py.crackfortran import sourcecodeform
from sqlalchemy import create_engine, false
import pymysql
import oracledb
import pytest
from sqlalchemy.testing import fails
import allure
#blocker critical normal minor trivial

#Test related to structure
#TC1 --Rowcount
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_RowCount(src_df,tgt_df):
    myRow = len(src_df)
    oracRow = len(tgt_df)
    assert myRow == oracRow,'Row count mismatch'

@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_ColumnCount(src_df,tgt_df):
    srccolcount = len(src_df.columns)
    assert srccolcount == 11,'Source column count is not 11'
    tgtcolcount = len(tgt_df.columns)
    assert tgtcolcount == 18, 'target column count is not 18'

#TC4 --primary key uniqueness
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def testUniquePK(src_df,tgt_df):
    pk = "empid"
    nulls = tgt_df[pk].isnull().sum()
    dups = tgt_df['empid'].duplicated().sum()
    assert nulls==0,f"Nulls found in{pk}:{nulls}"
    assert dups==0,f"Duplicates found in{pk}:{dups}"

#TC5 --Data type check dob
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def testDatatypeCheck(src_df,tgt_df):
    dt =tgt_df['dob'].dtype
    assert dt == "datetime64[ns]",f"data type of dob is {dt}"

#TC6 --Data type check doj
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def testDatatypeCheckdoj(src_df,tgt_df):
    dj =tgt_df['doj'].dtype
    assert dj == "datetime64[ns]",f"data type of doj is {dj}"

@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
@allure.severity(allure.severity_level.BLOCKER)
def testFKvalidation(src_df,src_dept,tgt_df):
    invalid = src_df.loc[~src_df['dept'].isin(src_dept['dept_code'])]
    assert invalid.empty,f"orphan employees found with invalid dept_codes:{invalid['dept_code'].unique().tolist()}"