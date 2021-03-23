import math


def exercicio01():
    resposta = "Alo mundo"
    print(resposta)
    return {"resposta": resposta, "status": 200}


def exercicio02(param):
    valor = param['valor1']
    resposta = "O número informado foi " + valor
    return {"resposta": resposta, "status": 200}


def exercicio03(param):
    nro1 = int(param['valor1'])
    nro2 = int(param['valor2'])
    soma = nro1 + nro2
    return {"resposta": soma, "status": 200}


def exercicio04(param):
    nota1 = param['valor1']
    nota2 = param['valor2']
    nota3 = param['valor3']
    nota4 = param['valor4']
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return {"resposta": media, "status": 200}


def exercicio05(param):
    centimentros = param['valor1']
    metros = centimentros / 100
    return {"resposta": metros, "status": 200}


def exercicio06(param):
    raio_do_circulo = param['valor1']
    area = math.pi * raio_do_circulo * raio_do_circulo
    return {"resposta": area, "status": 200}
