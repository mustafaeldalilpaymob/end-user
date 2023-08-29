from src.utils.utils import load_env_vars

from src.data_cleaning.cleaning_phone_numbers import *

from src.database.db_utils import *


######################## Testing Connection and Trx Data Retrival ###########################
# load all envs variables
env_vars = load_env_vars()

#make connection
conn = redshift_db_connector(env_vars['USERNAME'], env_vars['PASSWORD'], env_vars['TRX_DB_NAME'], env_vars['REDSHIFT_HOST'], env_vars['REDSHIFT_PORT'])


query_file_name = 'src/database/get_trx_data_for_online_users.sql'
operation = 'r'

initial_df = run_query(query_file_name, operation, conn)
print(initial_df.head(2))