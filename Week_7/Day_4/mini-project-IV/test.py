from pandas.core import base
import requests as r
import pandas as pd
import json
base_url = 'http://127.0.0.1:5000/'

json_data = {'Gender': 'Male',
 'Married': 'Yes',
 'Dependents': '1',
 'Education': 'Graduate',
 'Self_Employed': 'Yes',
 'ApplicantIncome': 3466,
 'CoapplicantIncome': 1210.0,
 'LoanAmount': 130.0,
 'Loan_Amount_Term': 360.0,
 'Credit_History': 1.0,
 'Property_Area': 'Rural'}


# test = pd.read_csv("test.csv", index_col=0)
# test = test.to_json(orient='records')
# test = json.loads(test)

#Get Response
#response = r.get(base_url + 'helloworld')

response = r.post(base_url + "predict", json = json_data)

if response.status_code == 200:
    print("...")
    print("Test 1: Success")
    print("...")
    print(response.json())
else:
    print("request failed")

