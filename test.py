from sqlalchemy import create_engine, engine
import numpy as np
import pandas as pd

# Obtain connection string information from the portal
from config import config

# Construct connection string
sqlUrl = engine.url.URL(
  drivername="mysql",
  username=config["user"],
  password=config["password"],
  host=config["host"],
  query={"ssl_ca": "BaltimoreCyberTrustRoot.crt.pem"},
)
engine = create_engine(sqlUrl)

#Begin Connection
with engine.begin() as connection:  
  print("Connection established")

  #Create Database
  connection.execute("CREATE DATABASE test2;")
  connection.execute("USE test2;")
  print("Created Database")

  # Create and insert data into table
  pd_table = pd.DataFrame([("pinapple", 20),("banana", 150),("orange", 154)], columns=['name','quantity'])
  pd_table.to_sql("inventory", connection, index=False)

  # query all tables
  sql = "SHOW tables;"
  query = pd.read_sql(sql, connection)
  print(query)
  print("Created and uploaded table")
  
  # read SQL to dataframe
  sql = "SELECT * from inventory;"
  pd_read = pd.read_sql(sql, connection)
  print(pd_read)
  print("Finished show table.")