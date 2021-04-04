def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def verificaSeNroTerminaComVirgulaOuPonto(nro):
    if str(nro).endswith(',') or str(nro).endswith('.'):
        return True
    return False


def verificaSeValorEhIntOuFloat(valor):
    if valor.isdigit() or isFloat(valor):
        return True
    return False


def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num