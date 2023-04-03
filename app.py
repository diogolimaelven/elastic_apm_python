import os
import psycopg
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import logging
from elasticapm.contrib.flask import ElasticAPM

# ENVs
load_dotenv()

# Start Flask
app = Flask(__name__)

# APM Config

@app.route("/")
def test_db():
    try:
        conn_db = psycopg.connect(host=os.environ['DATABASE_HOST'],
            dbname=os.environ['DATABASE_NAME'],
            user=os.environ['DATABASE_USER'],
            port=os.environ['DATABASE_PORT'],
            password=os.environ['DATABASE_PASS'],)
        test_db="e Banco conectado com sucesso"
        get_command_linux = os.popen('hostname')
        d_command = get_command_linux.read()
        d_result = d_command + test_db
        return render_template('index.html', d_output=d_result)
    except psycopg.Error as err:
        # APM
        
        response = {'message': 'Internal Server Error'}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = 1 )
