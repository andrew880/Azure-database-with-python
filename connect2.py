import mysql.connector
from mysql.connector import errorcode
from sqlalchemy import create_engine, engine
import numpy as np
import pandas as pd

# Obtain connection string information from the portal
from config import config
# mysql -h retailing-test1.mysql.database.azure.com -u retailing880@retailing-test1 -p
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
  df1 = pd.DataFrame({'name' : ['User 4', 'User 5']})
  df1.to_sql('users', con=connection, if_exists='append')
  
  # Drop previous table of same name if one exists
  connection.execute("DROP TABLE IF EXISTS inventory;") 
  connection.execute("DROP TABLE IF EXISTS inventoryw;") 
  print("Finished dropping table (if existed).")

  # Create table
  connection.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

  # Insert some data into table
  connection.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted1 1 row of data.")
  connection.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
  print("Inserted1 1 row of data.")
  connection.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
  print("Inserted1 1 row of data.")

  # query all tables
  sql = "SHOW tables;"
  query = pd.read_sql(sql, connection)
  print(query)
  # read SQL to dataframe
  sql = "SELECT * from inventory;"
  pd_table = pd.read_sql(sql, connection)
  print(pd_table)
  print("Finished show table.")

  #Change dataframe
  df = pd.DataFrame([(4, "pinapple", 20)], columns=['id','name','quantity'])
  print(df)
  pd_table = pd_table.append(df)
  # print(pd_table)
  # print("Modified table.")

  #Upload to database
  pd_table.to_sql("inventory", connection, if_exists='replace', index=False)
  pd_table.to_sql("inventory", connection, if_exists='append', index=False)
  print("Uploaded to database.")

  # query all tables
  sql = "SHOW tables;"
  query = pd.read_sql(sql, connection)
  print(query)

  # read SQL to dataframe
  sql = "SELECT * from inventory;"
  pd_table = pd.read_sql(sql, connection)
  print(pd_table)
  print("Finished show modified table.")

# Cleanup
connection.close()
print("Done.")