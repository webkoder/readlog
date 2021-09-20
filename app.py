"""
A sample Hello World server.
"""
import os
# from testbigquery import test
from mysqldata import MySQLData
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
        url = row[0].replace('https://api.nobeta.com.br/nobetaads&id=', '')
        url = url.replace('.inter', '')
        urls.append( url )

    return jsonify(urls)

@app.route('/checksites/<data>')
@cross_origin()
def checksites( data ):
    # data = byRequest()
    db = MySQLData()
    blocos = db.getData( data )

    return jsonify( blocos )

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
