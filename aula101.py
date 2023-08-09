# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# Raise faz surgir um erro como neste exemplo "raise ValueError('Deu erro')"  vai aparecer a mensagem
# que está na string, ao invés da mensagem que daria normalmente.
# Com raise, você cria suas próprias exceções, e erros.
def erro_divide_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('É impossível calcular a divisão do zero.')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float,int)):
        raise TypeError(
            f'{n} deve ser int ou float.'
           f'"{tipo_n.__name__} enviado"'
        )

def divide(n,d):
    
    deve_ser_int_ou_float(d)
    deve_ser_int_ou_float(n)
    erro_divide_por_zero(d)
    erro_divide_por_zero(n)

    return n / d
print(divide(8,'0'))