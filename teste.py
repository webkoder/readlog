
from datetime import date,timedelta

data = date.today() - timedelta(days=1)
dataf = data.strftime('%Y%m%d')

query = """select timestamp,
    httpRequest.requestUrl as url,
    httpRequest.userAgent as useragent,
    httpRequest.referer as referer,
    httpRequest.latency as latency,
    jsonpayload_type_loadbalancerlogentry.statusdetails as details,
    insertId, httpRequest.responseSize as size, httpRequest.status as status
 from `nobeta.scriptnobeta.requests_"""+dataf+"""` limit 50;"""

print(query)


