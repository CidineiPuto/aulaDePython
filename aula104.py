import importlib # Serve para recarregar um módulo importado

import aula104_m 

print(aula104_m.variavel)

for i in range (10):
    importlib.reload(aula104_m) # a cada repetição o módulo irá reniciar
    print(i)
    

# Módulo é singleton : Só pode existir ELE em outro módulo, não podendo ter outra instância

print('Fim')

