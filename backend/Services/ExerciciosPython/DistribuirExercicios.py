from Services.ExerciciosPython.EstruturaSequencial import exercicio01, exercicio02, exercicio03, exercicio04, \
    exercicio05, exercicio06, exercicio07, exercicio08, exercicio09, exercicio10, exercicio11, exercicio12, exercicio13, \
    exercicio14, exercicio15, exercicio16, exercicio17, exercicio18


def distribuir_exercicios(params):
    nro = params['nro_do_exercicio']
    if nro == '1':
        return exercicio01()
    if nro == '2':
        return exercicio02(params)
    if nro == '3':
        return exercicio03(params)
    if nro == '4':
        return exercicio04(params)
    if nro == '5':
        return exercicio05(params)
    if nro == '6':
        return exercicio06(params)
    if nro == '7':
        return exercicio07(params)
    if nro == '8':
        return exercicio08(params)
    if nro == '9':
        return exercicio09(params)
    if nro == '10':
        return exercicio10(params)
    if nro == '11':
        return exercicio11(params)
    if nro == '12':
        return exercicio12(params)
    if nro == '13':
        return exercicio13(params)
    if nro == '14':
        return exercicio14(params)
    if nro == '15':
        return exercicio15(params)
    if nro == '16':
        return exercicio16(params)
    if nro == '17':
        return exercicio17(params)
    if nro == '18':
        return exercicio18(params)
