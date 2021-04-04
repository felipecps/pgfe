from Services.ExerciciosPython.EstruturaSequencial import exercicio01, exercicio02, exercicio03, exercicio04, \
    exercicio05, exercicio06, exercicio07, exercicio08


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
