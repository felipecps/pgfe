import datetime
import os
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS

# from Services.SendEmail.sendEmail import send_email
from Services.ExerciciosPython.DistribuirExercicios import distribuir_exercicios
from Services.SendEmail.sendEmail import send_email

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/envia_email', methods=['POST'])
def envia_email():
    body = request.args.get('text', '')
    subject = request.args.get('subject', '')
    if subject == '':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        subject = "Lembrete enviado às: " + str(current_time)

    checked_emails = request.args.get('checked', '').split(',')
    for receiver in checked_emails:
        send_email(body, subject, receiver)
    return 'ok'


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/hora_atual')
def hora_atual():
    return 'Hora atual: ' + str(datetime.datetime.now().time())


@app.route('/resolve_exercicios', methods=['POST'])
def resolve_exercicios():
    exercicio = request.args.get('exercicio', '')
    resposta = distribuir_exercicios(exercicio)
    if resposta['status'] == 200:
        return jsonify(resposta)
    else:
        return 'erro'


try:
    computerName = os.environ['COMPUTERNAME']
    if __name__ == "__main__" and computerName == 'DESKTOP-EDKQLLT':
        app.run()
except KeyError:
    pass
