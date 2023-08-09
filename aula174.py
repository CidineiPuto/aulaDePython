# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

# datetime comparação__________________________________________________________

# fmt = '%d/%m/%Y %H:%M:%S'
# data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
# data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=3)
# print(data_fim + delta)

# delta = data_fim - data_inicio
# print(delta)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)


# CTRL ESPAÇO - Atalho, mostra os parametros dentro de algo

# dateutil_____________________________________________________________________

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = timedelta(days=10, hours=3)
print(data_fim - delta)
print(data_fim + relativedelta(days=10, minutes=12))
print(delta)
# delta2 = relativedelta(data_fim, data_inicio)
# print(f'A diferença do inicio ao fim é de "{delta2.days}" dias.')
