import os
import psycopg
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from elasticapm.contrib.flask import ElasticAPM
import logging

load_dotenv()

app = Flask(__name__)

app.config['ELASTIC_APM'] = {

  'SERVICE_NAME': 'app_flask',


  'SECRET_TOKEN': '',
  'DEBUG': True,

# # # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': 'http://192.168.56.10:8200',

# # # Set the service environment
  'ENVIRONMENT': 'Cohort turma 4',
  }

apm = ElasticAPM(app)

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
        apm.capture_message(app.logger.critical(err), level='error')
        response = {'message': 'Internal Server Error 2'}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = 0 )
