# utils.py

from dotenv import load_dotenv
import os

def load_env_vars():
    """Load enviroment variables

    Returns:
        dictionary: key-value pairs of all enviroment variables
    """
    load_dotenv()
    return {
        "REDSHIFT_HOST": os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT": os.getenv('REDSHIFT_PORT'),
        'TRX_DB_NAME': os.getenv('TRX_DB_NAME'),
        "USERNAME": os.getenv('USERNAME'), 
        "PASSWORD": os.getenv('PASSWORD')
    }

