# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

# from pytz import timezone

# datetime____________________________________________________________________
data_str = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'
data_str = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

data1 = datetime(2024, 7, 20, 3, 30, 33)
data = datetime.strptime(data_str, data_str_fmt)

# timezone_____________________________________________________________________

# data = datetime.now(timezone('America/Los_Angeles'))
# print(data)

# data = datetime(2024, 7, 20, 3, 30, 33, tzinfo=timezone('Asia/Tokyo'))
# print(data)

# time stemp___________________________________________________________________

# data = datetime.now()
# print(data.timestamp())  # isso está na base de dados
# print(datetime.fromtimestamp(1682459385))
