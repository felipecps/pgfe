import datetime
import os
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
#from PIL import Image # Importando o módulo Pillow para abrir a imagem no script
#import pytesseract # Módulo para a utilização da tecnologia OCR

# from Services.SendEmail.sendEmail import send_email
from Services.ExerciciosPython.DistribuirExercicios import distribuir_exercicios
#from Services.OCR.ocr_utils import extair_texto
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

@app.route('/ocr', methods=['POST'])
def ocr():

    params = {}
    # http://pythonclub.com.br/extraindo-texto-de-imagens-com-python.html
    file = request.files["file"]
    print(file)
    file_bytes = file.read()
    f = open(os.getcwd() + "\Services\OCR\sample.png", "wb")
    f.write(file_bytes)
    f.close()

    resposta = extair_texto(os.getcwd() + "\Services\OCR\sample.png")
    try:
        os.remove(os.getcwd() + "\Services\OCR\sample.png")
    except Exception as error:
        print("OCR falhou para remover o arquivo")

    return {
        "resposta": resposta,
        "status": 200}


@app.route('/hora_atual')
def hora_atual():
    return 'Hora atual: ' + str(datetime.datetime.now().time())


@app.route('/resolve_exercicios', methods=['POST'])
def resolve_exercicios():
    params = {}
    nro_do_exercicio = request.args.get('exercicio', '')
    valor1 = request.args.get('valor1', False)
    valor2 = request.args.get('valor2', False)
    valor3 = request.args.get('valor3', False)
    valor4 = request.args.get('valor4', False)

    params.update({'nro_do_exercicio': nro_do_exercicio})
    params.update({'valor1': valor1})
    params.update({'valor2': valor2})
    params.update({'valor3': valor3})
    params.update({'valor4': valor4})

    resposta = distribuir_exercicios(params)
    if resposta['status'] == 200 or resposta['status'] == 400:
        return jsonify(resposta)
    else:
        return 'erro'


try:

    computerName = os.environ['COMPUTERNAME']
    if __name__ == "__main__" and computerName == 'DESKTOP-EDKQLLT':
        app.run()
except KeyError:
    pass
