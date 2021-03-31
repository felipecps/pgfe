import math

from Services.ExerciciosPython.utils import isFloat, verificaSeNroTerminaComVirgulaOuPonto


def exercicio01():
    resposta = "Alo mundo"
    print(resposta)
    return {"resposta": resposta, "status": 200}


def exercicio02(param):
    resposta = "O valor informado não é um número"
    valor_original = param['valor1']

    if verificaSeNroTerminaComVirgulaOuPonto(valor_original):
        return {"resposta": resposta, "status": 200}
    valor = str(valor_original).replace(",", ".")
    if valor.isdigit() or isFloat(valor):
        resposta = "O número informado foi " + str(valor_original)
    return {"resposta": resposta, "status": 200}


def exercicio03(param):
    soma = "Soma impossível de ser realizada. Verifique se os valores informados são realmente números."
    nro1 = param['valor1']
    nro2 = param['valor2']

    if verificaSeNroTerminaComVirgulaOuPonto(nro1) or verificaSeNroTerminaComVirgulaOuPonto(nro2):
        return {"resposta": soma, "status": 400}

    if (nro1.isdigit() or isFloat(nro1)) and (nro2.isdigit() or isFloat(nro2)):
        soma = int(param['valor1']) + int(param['valor2'])
        return {"resposta": soma, "status": 200}

    return {"resposta": soma, "status": 400}


def exercicio04(param):
    nota1 = float(str(param['valor1']).replace(',', '.'))
    nota2 = float(str(param['valor2']).replace(',', '.'))
    nota3 = float(str(param['valor3']).replace(',', '.'))
    nota4 = float(str(param['valor4']).replace(',', '.'))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    media = round(media, 2)
    return {"resposta": media, "status": 200}


def exercicio05(param):
    try:
        metros = float(str(param['valor1']).replace(',', '.'))
        if isFloat(metros):
            centimentros = metros * 100
            return {"resposta": centimentros, "status": 200}
    except:
        centimetros = 'Não é um valor válido para conversão'
        return {"resposta": centimetros, "status": 400}


def exercicio06(param):
    try:
        raio_do_circulo = param['valor1'].replace(',', '.')
        area = math.pi * float(raio_do_circulo) * float(raio_do_circulo)
        return {"resposta": round(area, 2), "status": 200}
    except:
        return {"resposta": "O valor informado não é valido.", "status": 400}
