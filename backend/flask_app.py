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
    # Status atual.
    # estou tentando fazer o exemplo 2. quero fazer o programa enviar do front end para o backend o valor digitado sem a
    # necessidade de apertar um botao

    params = {}
    nro_do_exercicio = request.args.get('exercicio', '')
    valor1 = request.args.get('valor1', False)

    params.update({'nro_do_exercicio': nro_do_exercicio})
    params.update({'valor1': valor1})

    resposta = distribuir_exercicios(params)
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
