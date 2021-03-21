from Services.ExerciciosPython.EstruturaSequencial import exercicio01, exercicio02, exercicio03, exercicio04, \
    exercicio05, exercicio06


def distribuir_exercicios(params):
    nro = params['nro_do_exercicio']
    if nro == '1':
        return exercicio01()
    if nro == '2':
        return exercicio02(params)
    if nro == '3':
        return exercicio03(params)
    if nro == '4':
        return exercicio04()
    if nro == '5':
        return exercicio05(params)
    if nro == '6':
        return exercicio06(params)
