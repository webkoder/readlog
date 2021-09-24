"""
A sample Hello World server.
"""
import os

from flask.wrappers import Response
# from testbigquery import test
from mysqldata import MySQLData
from dataparam import defaultValue
from bigqueryservice import getUrls
from flask_cors import cross_origin
import time
from main import principal

from flask import Flask, render_template, jsonify

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def hello( ):
    # Front end

    return render_template('index.html')

@app.route('/resumo')
def resumo( ):
    # tela de resumo
    return render_template('resumo.html')

# Load scripts from bigquery
@app.route('/scripturls', defaults={'data': None})
@app.route('/scripturls/<data>')
@cross_origin()
def scripturls( data ):
    """Return a list of url from bigquery."""

    if data is None:
        data = defaultValue()
    bqurls = getUrls( data )
    if type( bqurls ) == str:
        return Response(bqurls, status=404)

    urls = []
    for row in bqurls:
        url = row[0].replace('https://api.nobeta.com.br/nobetaads&id=', '')
        url = url.replace('.inter', '')
        urls.append( url )

    return jsonify(urls)

# load data from mysql for checking
@app.route('/checksites/<data>')
@cross_origin()
def checksites( data ):
    # data = byRequest()
    db = MySQLData()
    blocos = db.getData( data )

    return jsonify( blocos )

# process an url
@app.route('/process/<data>/<id>')
@cross_origin()
def processUrl( data, id ):
    rows = principal( id, data )
    return jsonify( {'id':id, 'data': data, 'rows': rows } )

# load data from mysql for checking
@app.route('/summary')
@cross_origin()
def summary():
    db = MySQLData()
    datas = db.getSummary( )

    return jsonify( datas )

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
