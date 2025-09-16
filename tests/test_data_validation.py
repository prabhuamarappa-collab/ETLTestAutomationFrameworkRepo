import numpy as np
from math import isnan

import pandas as pd
from numpy.f2py.crackfortran import sourcecodeform
from sqlalchemy import create_engine, false
import pymysql
import oracledb
import pytest
from sqlalchemy.testing import fails
import logging
import allure

#Tests comparing src & tgt data values
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testFullnameSplit(src_df,tgt_df):
    src = src_df['fullname'].str.strip()
    sfirstname = src.str.split(r"[ .@]").str[0]
    slastname = src.str.split(r"[ .@]").str[-1]
    tfirstname = tgt_df['firstname']
    tlastname = tgt_df['lastname']
    assert sfirstname.all() == tfirstname.all(),"firstname is not matching between src & tgt"
    assert slastname.all() == tlastname.all(),"lastname is not matching between src & tgt"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.integration
@pytest.mark.regression
def testdept_codeAndName(src_df,src_dept,tgt_df):
    merged_df = pd.merge(src_df, src_dept, left_on='dept', right_on='dept_code', how='left')
    target_aligned = tgt_df.loc[merged_df.index]
    mismatch_code = merged_df['dept_code'] != target_aligned['dept_code']
    failing1 = mismatch_code[mismatch_code].index
    mismatch_name = merged_df['dept_name'] != target_aligned['dept_name']
    failing2 = mismatch_name[mismatch_name].index
    assert failing1.empty, f"dep_code mismatch for rows:{failing1.tolist()}"
    assert failing2.empty, f"dep_name mismatch for rows:{failing2.tolist()}"

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.integration
@pytest.mark.regression
def testManagerIDName(src_df,src_dept,tgt_df):
    merged_mgr_df = pd.merge(src_df, src_df, left_on='manager_id', right_on='empid', how='left')
    target_align = tgt_df.loc[merged_mgr_df.index]
    mismatch_mgrid = merged_mgr_df['manager_id_x'] != target_align['manager_id']
    mismatch_mgrname = merged_mgr_df['fullname_y'] != target_align['manager_name']
    failing_id = mismatch_mgrid[mismatch_mgrid].index
    failing_name = mismatch_mgrname[mismatch_mgrname].index
    assert failing_id.empty, f"managerid mismatch for rows:{failing_id.tolist()}"
    assert failing_name.empty, f"managername mismatch for rows:{failing_name.tolist()}"

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def testSalaryMinMax(src_df,src_dept,tgt_df):
    src_min, src_max = src_df['salary'].min(), src_df['salary'].max()
    tgt_min, tgt_max = tgt_df['salary'].min(), tgt_df['salary'].max()
    assert src_min == tgt_min,f"min salary mismatch src={src_min} and tgt={tgt_min}"
    assert src_max == tgt_max,f"min salary mismatch src={src_max} and tgt={tgt_max}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testmandatory_column(src_df,src_dept,tgt_df):
    mandatory_cols = ["empid", "firstname", "lastname"]
    nulls = tgt_df[mandatory_cols].isnull()
    failing = nulls[nulls.any(axis=1)].index.tolist()
    assert not failing,f"null/empty mandatory columns rows:{failing}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def test_Nullabilty(src_df,tgt_df):
    mandatory_col = [col for col in tgt_df if col != 'manager_name']
    nullcheck = tgt_df[mandatory_col].isnull().sum()
    failing = nullcheck[nullcheck > 0]
    if not failing.empty:
        logger = logging.error(f"Nulls found:{failing.to_dict()}")
    assert failing.empty,f"Nulls found:{failing.to_dict()}"