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
  database=config["database"],
  query={"ssl_ca": "BaltimoreCyberTrustRoot.crt.pem"},
)
engine = create_engine(sqlUrl)
with engine.begin() as connection:
  print("Connection established")

  # Drop previous table of same name if one exists
  connection.execute("DROP TABLE IF EXISTS inventory;") 
  connection.execute("DROP TABLE IF EXISTS users;") 
  print("Finished dropping table (if existed).")

  # Create and insert data into table
  pd_table = pd.DataFrame([("pinapple", 20),("banana", 150),("orange", 154)], columns=['name','quantity'])
  pd_table.to_sql("inventory", connection, index=False)

  # query all tables
  sql = "SHOW tables;"
  query = pd.read_sql(sql, connection)
  print(query)

  # read SQL to dataframe
  sql = "SELECT * from inventory;"
  pd_read = pd.read_sql(sql, connection)
  print(pd_read)
  print("Finished show table.")

  #Change dataframe
  df = pd.DataFrame([("apple", 230),("guava", 151)], columns=['name','quantity'])
  pd_modified = pd_read.append(df)

  #Upload to database
  pd_modified.to_sql("inventory", connection, if_exists='replace', index=False)
  print("Uploaded to database.")

  # query all tables
  sql = "SHOW tables;"
  query = pd.read_sql(sql, connection)
  print(query)

  # read SQL to dataframe
  sql = "SELECT * from inventory;"
  pd_read_modified = pd.read_sql(sql, connection)
  print(pd_read_modified)
  print("Finished show modified table.")

# Cleanup
connection.close()
print("Done.")