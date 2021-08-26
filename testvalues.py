import os
import json

data = os.environ.get('MYSQLPY')
data = json.loads(data)
print( data['host'] + ' ' + data['user']  )