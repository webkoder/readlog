import sys
from datetime import date, datetime, timedelta
from flask import request

def byCommand():
    if len(sys.argv) == 1:
        data = date.today()  - timedelta(days=1)
    else:
        data = datetime.strptime(sys.argv[1],'%Y-%m-%d')

    return data

def byRequest( ):
    if 'data' not in request.args:
        data = date.today()  - timedelta(days=1)
    else:
        data = datetime.strptime(request.args['data'],'%Y-%m-%d')

    return data