from bigqueryclient import getClient
from google import api_core

def getUrls( data ):
    if( type( data ) == str ):
        dataf = data.replace('-', '')
    else:
        dataf = data.strftime('%Y%m%d')

    client = getClient()    
    query = """select 
        httpRequest.requestUrl as url
    from `nobeta.scriptnobeta.requests_""" + dataf + """` group by httpRequest.requestUrl;"""

    query_job = client.query(query)
    res = None
    try:
        res = query_job.result()
    except api_core.exceptions.NotFound as notfound:
        return dataf + ' não existe'

    return res
