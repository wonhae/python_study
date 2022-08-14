


import sqlite3
import pandas as pd
con = sqlite3.connect("/Users/guest1/documents/python_study/test.db")

def rrr() :

    return pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", con)
