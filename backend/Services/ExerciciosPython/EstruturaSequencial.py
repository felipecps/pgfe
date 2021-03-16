def exercicio01():
    resposta = "Alo mundo"
    print(resposta)
    return {"resposta": resposta, "status": 200}


def exercicio02(param):
    valor = param['valor1']
    resposta = "O número informado foi " + valor
    return {"resposta": resposta, "status": 200}
