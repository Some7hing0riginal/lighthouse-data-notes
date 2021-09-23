import psycopg2
import config as cfg
import pandas as pd

postgres_pwd = cfg.postgres['password'] # This is the password you entered when you set up PGSQL

con = psycopg2.connect(database='drinks', user='postgres', password=postgres_pwd,
                       host='127.0.0.1', port='5432')  # This should work if you left everything as default

cur = con.cursor()

#cur.execute(open('drinks.sql', 'r').read())  # Uncomment this the first time you run the db

# Before doing anything else, let's create a function out
# of the things we're doing above
def execute_query(query_string, return_pandas=True):
    if return_pandas:
        response = pd.read_sql_query(query_string, con)
    else:
        cur.execute(query_string)
        response = cur.fetchall()
    return response