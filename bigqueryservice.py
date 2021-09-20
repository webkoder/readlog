from bigqueryclient import getClient

def getUrls( data ):
    dataf = data.strftime('%Y%m%d')
    client = getClient()    
    query = """select 
        httpRequest.requestUrl as url
    from `nobeta.scriptnobeta.requests_""" + dataf + """` group by httpRequest.requestUrl;"""

    query_job = client.query(query)
    return query_job.result()
