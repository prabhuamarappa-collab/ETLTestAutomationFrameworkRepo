import pandas as pd
import pytest

df = pd.read_csv("customer.csv")
#1 Null value check (customer_id, name, email, country)
def test_NullValueCheck():
    assert df['customer_id'].notnull().all(),"customer_id contains null values"
    assert df['name'].notnull().all(),"name contains null values"
    assert df['email'].notnull().all(), "email contains null values"
    assert df['country'].notnull().all(), "country contains null values"

#2 Duplicate check (customer_id)
def test_Duplicate_Check():
    duplicated_df= df[df['customer_id'].duplicated()]
    assert duplicated_df.empty,"Customer id is having duplicate values"

 #3 country not allowed from a china
def test_CountryNotAllowedCheck():
    country_not_allowed = df[df['country'] == 'China']
    assert country_not_allowed.empty, "Country is there with china name"




