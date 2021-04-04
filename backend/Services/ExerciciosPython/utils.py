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

def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')
