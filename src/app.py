"""
A sample Hello World server.
"""
import os
import testbigquery
import testmysql
from dataparam import byRequest

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello( ):
    """Return a friendly HTTP greeting."""
    # message = "Está rodando!"

    """Get Cloud Run environment variables."""
    # service = os.environ.get('K_SERVICE', 'Unknown service')
    # revision = os.environ.get('K_REVISION', 'Unknown revision')

    data = byRequest( )

    bq = testbigquery.test()
    print( bq )

    sites = testmysql.test()
    print( sites )

    return 'data ' + str(data) + ' ' + ' bq  ' + bq + ' site ' +  sites

    # return render_template('index.html',
    #     message=message,
    #     sites=sites,
    #     Service=service,
    #     Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
