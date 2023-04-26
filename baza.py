import psycopg2 as psql
import pandas as pd


pdb = psql.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "Hfazliddin98"
)
cursor = pdb.cursor()
cursor.execute("SELECT version()")
print(cursor.fetchone())