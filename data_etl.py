import numpy as np

import pandas as pd
import sqlite3 # Pour lire du SQL Lite
import pyodbc # Pour lire les tables SQL d'un Serveur

def read_data(path:str):
    data = None
    if '.csv' in path:
        data = pd.read_csv(path)
    elif '.xlsx' in path:
        data = pd.read_excel(path)
    elif '.json' in path:
        data = pd.read_excel(path)
    return data

def read_sql_table(path, query, con_type="sqlite3"): # Load SQL Table
    # Read sqlite query results into a pandas DataFrame
    con = create_connexion(path, con_type)
    data = pd.read_sql_table(query, con)
    con.close()
    return data

def read_no_sql_table(path, query, con_type="mongodb"): # Load No-SQL Table
    pass

def create_sql_data(path:str, data:pd.DataFrame, table_name:str, con_type="sqlite3"):
    con = create_connexion(path, con_type)
    # Write the new DataFrame to a new SQLite table
    data.to_sql(table_name, con, if_exists="replace")
    con.close()

def create_connexion(path, con_type="sqlite3"):
    if con_type == "sqlite3":
        return sqlite3.connect(path)
    return # D'autres cas à traiter