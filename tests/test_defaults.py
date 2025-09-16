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

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testTotalCompensation(src_df,tgt_df):
    src_tc = src_df['salary'].fillna(30000) + src_df['bonus'].fillna(0)
    tgt_tc = tgt_df['total_compensation']
    mismatches = src_tc != tgt_tc
    failing = mismatches[mismatches].index
    assert failing.empty,f"TotalCompensation mismatch for rows:{failing.tolist()}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testDefaultSalary(src_df,tgt_df):
    src_sal = src_df['salary'].fillna(30000)
    tgt_sal = tgt_df['salary']
    mismatches = src_sal != tgt_sal
    failing = mismatches[mismatches].index
    assert failing.empty, f"Salary /default mismatch rows:{failing.tolist()}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testDefaultbonus(src_df,tgt_df):
    src_bon = src_df['bonus'].fillna(0)
    tgt_bon = tgt_df['bonus']
    mismatches = src_bon != tgt_bon
    failing = mismatches[mismatches].index
    assert failing.empty, f"binus /default mismatch rows:{failing.tolist()}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testphonedefault(src_df,tgt_df):
    src_df['phone'] = np.where(src_df['phone'].isnull() | (src_df['phone'] == '') | (src_df['phone'] == 'INVALID'),
                               'UNKNOWN', src_df['phone'])
    tgt_phone = tgt_df['phone']
    mismatches = src_df['phone']  != tgt_phone
    failing = mismatches[mismatches].index
    assert failing.empty, f"phone /default mismatch rows:{failing.tolist()}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testemaildefault(src_df,tgt_df):
    src_df['email'] = np.where(src_df['email'].isnull() | (src_df['email'] == '') | (src_df['email'] == 'INVALID'),
                               'UNKNOWN', src_df['email'])
    tgt_email = tgt_df['email']
    mismatches = src_df['email']  != tgt_email
    failing = mismatches[mismatches].index
    assert failing.empty, f"email /default mismatch rows:{failing.tolist()}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testDefaultGender(src_df,tgt_df):
    src_gen = src_df['gender'].fillna('U')
    tgt_gen = tgt_df['gender']
    mismatches = src_gen != tgt_gen
    failing = mismatches[mismatches].index
    assert failing.empty,f"Gender /default mismatch rows:{failing.tolist()}"