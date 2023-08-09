# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
# '' é o padrão do sistema operacional
# pt_BR = ''

print(calendar.calendar(2022))
print(locale.getlocale())

"""
Para ver todas as locales disponíveis no mac e no IOS apenas digitar
"locale -a " todos
"locale -a | grep 'pt'" mostra todos os que são português
"locale -a | grep 'pt_BR'" todos que são do português BRASIL
"""
