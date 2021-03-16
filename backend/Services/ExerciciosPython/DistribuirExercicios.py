from Services.ExerciciosPython.EstruturaSequencial import exercicio01, exercicio02


def distribuir_exercicios(params):
    nro = params['nro_do_exercicio']
    if nro == '1':
        return exercicio01()
    if nro == '2':
        return exercicio02(params)