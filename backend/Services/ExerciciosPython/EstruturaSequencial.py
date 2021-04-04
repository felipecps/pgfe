import math

from Services.ExerciciosPython.utils import isFloat, verificaSeNroTerminaComVirgulaOuPonto, formatNumber


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
    try:
        soma = float(param['valor1'].replace(',', '.')) + float(param['valor2'].replace(',', '.'))
        resposta = "A soma dos dois números é: " + str(formatNumber(soma))
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {"resposta": "Soma impossível de ser realizada. Verifique se os valores informados são realmente números.", "status": 400}


def exercicio04(param):
    try:
        nota1 = float(str(param['valor1']).replace(',', '.'))
        nota2 = float(str(param['valor2']).replace(',', '.'))
        nota3 = float(str(param['valor3']).replace(',', '.'))
        nota4 = float(str(param['valor4']).replace(',', '.'))
        media = (nota1 + nota2 + nota3 + nota4) / 4
        media = round(media, 2)
        resposta = "A média das notas dos 4 bimestres é: " + str(media)
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {"resposta": "O valor informado não é valido.", "status": 400}


def exercicio05(param):
    try:
        valor_em_metros = param['valor1'].replace(',', '.')
        if verificaSeNroTerminaComVirgulaOuPonto(valor_em_metros):
            raise Exception
        centimentros = float(valor_em_metros) * 100
        resposta = "" + valor_em_metros + " metro(s) são " + str(formatNumber(centimentros)) + " centimetros"
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {"resposta": "O valor informado não é valido.", "status": 400}


def exercicio06(param):
    try:
        raio_do_circulo = param['valor1'].replace(',', '.')
        if verificaSeNroTerminaComVirgulaOuPonto(raio_do_circulo):
            raise Exception
        area = math.pi * float(raio_do_circulo) * float(raio_do_circulo)
        resposta = "A área do circulo é: " + str(round(area, 2)) + "m²"
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {"resposta": "O valor informado não é valido.", "status": 400}


def exercicio07(param):
    try:
        lado_quadrado = param['valor1'].replace(',', '.')
        if verificaSeNroTerminaComVirgulaOuPonto(lado_quadrado):
            raise Exception
        area_quadrado = math.pow(float(lado_quadrado), 2)
        area = round(area_quadrado, 2)
        resposta = "O dobro da áre do quadrado de lado " + lado_quadrado + " metros é: " + str(2 * area) + " m²"
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {"resposta": "O valor informado não é valido.", "status": 400}
