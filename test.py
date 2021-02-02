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