import mysql.connector
from mysql.connector import errorcode
import numpy as np
import pandas as pd

# Obtain connection string information from the portal
from config import config
# mysql -h retailing-test1.mysql.database.azure.com -u retailing880@retailing-test1 -p
# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Drop previous table of same name if one exists
  cursor.execute("DROP TABLE IF EXISTS inventory;") 
  print("Finished dropping table (if existed).")

  # Create table
  cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

  # Insert some data into table
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
  print("Inserted",cursor.rowcount,"row(s) of data.")

  # query all tables
  sql = "SHOW tables;"
  query = pd.read_sql(sql,conn)
  print(query)
  # read SQL to dataframe
  sql = "SELECT * from inventory;"
  pd_table = pd.read_sql(sql,conn)
  print(pd_table)
  print(type(pd_table))
  print("Finished show table.")

  #Change dataframe
  df = pd.DataFrame([4,"pinapple",20], columns=['id','name','quantity'])
  pd_table = pd_table.append(df)
  print(pd_table)
  print("Modified table.")

  #Upload to database
  print("uploaded to database.")
  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")