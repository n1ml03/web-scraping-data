import sqlalchemy as sa
import pandas as pd

dataset = pd.read_csv("data.csv")
engine_str = (
    "mysql+pymysql://{user}:{password}@{server}/{database}".format(
    user      =  "root",
    password  =  "root888",
    server    =  "localhost",
    database  =  "datasciencerecipes")
    )
engine = sa.create_engine(engine_str)
conn = engine.connect()

# check whether connection is Successful or not
if (conn):
    print("MySQL Connection is Successful ... ... ...")
else:
    print("MySQL Connection is not Successful ... ... ...")

dataset.to_sql(name="data", con=engine,
                schema="datasciencerecipes",
                if_exists = "replace", chunksize = 1000,
                index=False)
conn.close()