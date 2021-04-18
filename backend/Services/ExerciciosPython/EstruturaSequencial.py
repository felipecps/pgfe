import math

from Services.ExerciciosPython.utils import isFloat, verificaSeNroTerminaComVirgulaOuPonto, formatNumber, \
    real_br_money_mask, le_parametro_float


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
        return {
            "resposta": "Soma impossível de ser realizada. Verifique se os valores informados são realmente números.",
            "status": 400}


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
        resposta = "O dobro da área do quadrado de lado " + lado_quadrado + " metros é: " + str(2 * area) + " m²"
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {"resposta": "O valor informado não é valido.", "status": 400}


def exercicio08(param):
    try:
        salario = float(param['valor1'].replace(',', '.')) * float(param['valor2'].replace(',', '.'))
        resposta = "O seu salário mensal é de R$" + str(real_br_money_mask(round(salario, 2))) + "."
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Calculo impossível de ser realizado. Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio09(param):
    # C = 5 * ((F-32) / 9).
    try:
        temperaturaFH = le_parametro_float(param)
        temperaturaCelsius = 5 * ((temperaturaFH - 32) / 9)
        celsius = "A temperatura de " + str(temperaturaFH) + " ºF convertida para graus Celsius é de " + str(
            (round(temperaturaCelsius, 2))) + " ºC."
        return {"resposta": celsius, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Conversão impossível de ser realizada. Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio10(param):
    # (C × 9/5) + 32 = 33,8 °F
    try:
        temperaturaCelsius = le_parametro_float(param)
        temperaturaFH = round(((temperaturaCelsius * (9 / 5)) + 32), 2)
        if (temperaturaFH == -0.0):
            temperaturaFH = 0.0

        fare = "A temperatura de " + str(temperaturaCelsius) + " ºC convertida para Fahrenheit é de " + str(
            temperaturaFH) + " ºF."
        return {"resposta": fare, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Conversão impossível de ser realizada. Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio11(param):
    try:
        int1 = int(param['valor1'].replace(',', '.'))
        int2 = int(param['valor2'].replace(',', '.'))
        real = float(param['valor3'].replace(',', '.'))

        if isinstance(int1, int) and isinstance(int2, int) and isinstance(real, float):
            calc1 = 2 * int1 * (int2 / 2)
            calc2 = 3 * int1 + (real)
            calc3 = math.pow(real, 3)

            resposta = "calculo 1: " + str(calc1) + "\n calculo 2: " + str(calc2) + "\n calculo 3: " + str(calc3)
            return {"resposta": resposta,
                    "calc1": str(calc1),
                    "calc2": str(calc2),
                    "calc3": str(calc3),
                    "status": 200}
        else:
            return {
                "resposta": "Verifique se os valores informados são números inteiros e real.",
                "status": 400}


    except Exception as error:
        print(error)
        return {
            "resposta": "Calculos impossível de serem realizados. Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio12(param):
    # (72.7*altura) - 58
    try:
        altura = le_parametro_float(param)
        pesoIdeal = (72.7 * altura) - 58
        peso = "O peso ideal para uma pessoa com altura de " + str(round(altura, 2)) + " m é de " + str(
            round(pesoIdeal, 2)) + "Kg."
        return {"resposta": peso, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Cálculo impossível de ser realizado. Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio13(param):
    try:
        h = le_parametro_float(param)
        pesoIdealH = (72.7 * h) - 58
        pesoIdealM = (62.1 * h) - 44.7
        pesoH = "O peso ideal para um homem com altura de " + str(round(h, 2)) + " m é de " + str(
            round(pesoIdealH, 2)) + " Kg."
        pesoM = "O peso ideal para uma mulher com altura de " + str(round(h, 2)) + " m é de " + str(
            round(pesoIdealM, 2)) + " Kg."
        return {"resposta": "",
                "pesoH": pesoH,
                "pesoM": pesoM,
                "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Cálculo impossível de ser realizado. "
                        "Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio14(param):
    resposta = "Não houve excesso no peso de peixe pescado e portanto não há multa a pagar."
    try:
        peso = le_parametro_float(param)
        excesso = -50 + peso
        if (excesso > 0):
            multa = 4 * excesso
            resposta = "O excesso foi de " + str(
                round(excesso, 2)) + " Kg e a multa a pagar é de R$ " + real_br_money_mask(multa)
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Calculo impossível de ser realizado. Verifique se o valor informado é valido.",
            "status": 400}


def exercicio15(param):
    try:
        salario_hora = float(param['valor1'].replace(',', '.'))
        nro_de_horas_mes = int(param['valor2'].replace(',', '.'))
        IR = 0.11
        INSS = 0.08
        sindicato = 0.05

        salario_bruto = round(salario_hora * nro_de_horas_mes, 2)
        pag_inss = round(salario_bruto * INSS, 2)
        pag_sindicato = round(salario_bruto * sindicato, 2)
        pag_IR = round(salario_bruto * IR, 2)

        salario_liquido = salario_bruto - pag_IR - pag_inss - pag_sindicato

        resposta = "O salário liquido é de R$ " + real_br_money_mask(salario_liquido) + ". INSS = R$ " + real_br_money_mask(
            pag_inss) + ". Sindicato = R$  " + real_br_money_mask(pag_sindicato) + ". IR = R$ " + real_br_money_mask(
            pag_IR) + "."

        return {"resposta": resposta,
                "salario_bruto": salario_bruto,
                "ir": pag_IR,
                "inss": pag_inss,
                "sindicato": pag_sindicato,
                "salario_liquido": salario_liquido,
                "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Calculo impossível de ser realizado. Verifique se o valor informado é realmente número.",
            "status": 400}


def exercicio16(param):
    try:
        tamanho_da_area_a_ser_pintada = float(param['valor1'].replace(',', '.'))
        tamanho_lata = 18
        preco_lata = 80
        area_por_lata = tamanho_lata * 3

        total_de_latas = math.ceil(tamanho_da_area_a_ser_pintada / area_por_lata)
        preco_da_compra = total_de_latas * preco_lata

        resposta = "Precisa(m) ser comprada(s) " + str(total_de_latas) + " lata(s) de tinta. O preço da compra é de R$ " + real_br_money_mask(
            preco_da_compra)
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Calculo impossível de ser realizado. Verifique se os valores informados são realmente números.",
            "status": 400}


def exercicio17(param):
    try:
        tamanho_da_area_a_ser_pintada = float(param['valor1'].replace(',', '.')) * 1.1
        tamanho_lata_1 = 18
        area_por_lata_1 = tamanho_lata_1 * 6  # 108 m²
        preco_lata_1 = 80

        tamanho_lata_2 = 3.6
        area_por_lata_2 = tamanho_lata_2 * 6  # 21,6 m²
        preco_lata_2 = 25

        total_de_latas_1 = math.ceil(tamanho_da_area_a_ser_pintada / area_por_lata_1)
        preco_da_compra_1 = total_de_latas_1 * preco_lata_1

        total_de_latas_2 = math.ceil(tamanho_da_area_a_ser_pintada / area_por_lata_2)
        preco_da_compra_2 = total_de_latas_2 * preco_lata_2

        nro_latas1 = tamanho_da_area_a_ser_pintada % area_por_lata_1
        area_restante = tamanho_da_area_a_ser_pintada - (nro_latas1 * area_por_lata_1)
        nro_latas2 = math.ceil(area_restante / area_por_lata_2)
    except:
        None


def exercicio18(param):
    try:
        tamanho_do_arquivo_mb = float(param['valor1'].replace(',', '.'))
        velocidade_do_link_mbps = float(param['valor2'].replace(',', '.'))
        tempo_de_download = tamanho_do_arquivo_mb / velocidade_do_link_mbps
        resposta = "O tempo para download do arquivo é de " + str(tempo_de_download) + "segundos"
        return {"resposta": resposta, "status": 200}
    except Exception as error:
        print(error)
        return {
            "resposta": "Calculo impossível de ser realizado. Verifique se os valores informados são realmente números.",
            "status": 400}
