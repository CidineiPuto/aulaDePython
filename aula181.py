# os.listdir para navegar em caminhos
# C:\Users\rafae\OneDrive\Imagens\Lipidios, trabalho
# caminho = r'C:\\Users\\rafae\\OneDrive\\Imagens\\Lipidios, trabalho'
import os

caminho = os.path.join('C:\\Users', 'rafae', 'OneDrive',
                       'Imagens', 'Lipidios, trabalho')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    print(f'A pasta acessada é {pasta}')
    print('#'*80)
    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)
        print()
