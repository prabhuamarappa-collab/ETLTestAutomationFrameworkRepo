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
logger = logging.getLogger(__name__)
import allure

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testAge(src_df,tgt_df):
    src_df['dob'] = pd.to_datetime(src_df['dob'], format="%d-%m-%Y", errors="coerce")
    today = pd.Timestamp.today()
    src_age = today.year - src_df['dob'].dt.year
    before_birthday = ((today.month < src_df['dob'].dt.month)|(today.month == src_df['dob'].dt.month)&(today.day< src_df['dob'].dt.day))
    src_age = src_age - before_birthday.astype(int)
    mismatches = src_age != tgt_df['age']
    failing = mismatches[mismatches].index
    if not failing.empty:
        logger.error(f"Age mismatch for rows : {failing.tolist()}")
    assert failing.empty, f"Age mismatch for rows : {failing.tolist()}"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testExperience(src_df,tgt_df):
    src_df['doj'] = pd.to_datetime(src_df['doj'], format="%d-%m-%Y")
    src_doj = src_df['doj'].dt.year
    today = pd.Timestamp.today()
    before_anniversary = ((today.month < src_df['doj'].dt.month)|(today.month == src_df['doj'].dt.month)&(today.day<src_df['doj'].dt.day))
    src_exp = today.year- src_doj - before_anniversary.astype(int)
    mismatches = src_exp != tgt_df['experience_years']
    failing = mismatches[mismatches].index
    assert failing.empty,f"Experience mismatch for rows :{failing.tolist()}"

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
@pytest.mark.regression
def testLoadDate(src_df,tgt_df):
    expected_date = pd.Timestamp("2025-09-12").date()
    mismatches = tgt_df['load_date'].dt.date != expected_date
    failing = mismatches[mismatches].index
    assert failing.empty,f"load_date mismatch rows:{failing.tolist()}"

@allure.severity(allure.severity_level.MINOR)
@pytest.mark.functional
@pytest.mark.regression
def test_phone_numbers(src_df,src_dept,tgt_df):
    tgt_df['phone'] = tgt_df['phone'].astype(str).str.strip().str.upper()
    phone = (tgt_df['phone'].astype(str).str.match(r"^\d{10}$")) | (tgt_df['phone'] == 'UNKNOWN')
    failing = tgt_df.loc[~phone].index.tolist()
    assert not  failing, f"Invalid phone numbers at rows: {failing}"

@allure.severity(allure.severity_level.MINOR)
@pytest.mark.functional
@pytest.mark.regression
def test_email(src_df,src_dept,tgt_df):
    email_ok = (
        (tgt_df['email'].str.contains("@") & tgt_df['email'].str.contains("abc"))
        | (tgt_df['email'] == "UNKNOWN")
    )
    failing = tgt_df.index[~email_ok].tolist()
    assert not failing, f"Invalid emails at rows: {failing}"


