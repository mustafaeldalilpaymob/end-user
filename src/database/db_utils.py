
import redshift_connector
import sqlalchemy as sa
from sqlalchemy.engine.url import URL
import pandas as pd

def redshift_db_connector(user_name, password, database_name, redshift_host, redshift_port):
  """Connects to a given db with the given credentials

  Args:
      user_name (str): username through which connection should be established
      password (str): pass word for the username given
      database_name (str): db name to establish the connection
      redshift_host (str): host of connection
      redshift_port (str): port of connection

  Returns:
      conn: redshift connector
  """
  # REDSHIFT_HOST=redshift_host
  # REDSHIFT_PORT= redshift_port
  # DATABASE_NAME=database_name
  # REDSHIFT_USER=user_name
  # PASSOWORD=password

  conn = redshift_connector.connect(
        host=redshift_host,
        database=database_name,
        port=redshift_port,
        user=user_name,
        password=password
    )
  return conn



def run_query(query_file_name, operation, connection):
  """Runs a given query to acheive the given operation based on the given db connection

  Args:
      query_file_name (str): .sql file that contains the SQL query to run
      operation (str): read or write operations denoted by [r, w]
      connection (redshift connector): connection to the db against which the query will be executed

  Returns:
      df: resulting data after query execution
  """
  with open(query_file_name, operation) as file: 
    sql_script = file.read() 

  query = pd.read_sql_query(sql_script, conn)
  df = pd.DataFrame(query)

  return df