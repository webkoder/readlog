import os
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

def getClient():
    load_dotenv()
    project_id = 'nobeta'
    credentials = None
    if( os.getenv('ENV') == 'local' ):
        path = os.path.dirname(os.path.realpath(__file__)) + os.sep
        credentials = service_account.Credentials.from_service_account_file( path + 'nobetabigquery.json' )
        
    return bigquery.Client(credentials= credentials,project=project_id)