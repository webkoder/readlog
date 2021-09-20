"""
A sample Hello World server.
"""
import os
# from testbigquery import test
from testmysql import test as mysqltest
from dataparam import byRequest
from bigqueryservice import getUrls
from flask_cors import cross_origin

from flask import Flask, render_template, jsonify

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello( ):
    """Home page"""

    return render_template('index.html')

@app.route('/scripturls')
@cross_origin()
def scripturls( ):
    """Return a list of url from bigquery."""

    data = byRequest()
    bqurls = getUrls( data )
    urls = []
    for row in bqurls:
        urls.append( row[0].replace('https://api.nobeta.com.br/nobetaads&id=', '') )

    return jsonify(urls)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
