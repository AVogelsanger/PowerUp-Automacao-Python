# instalar o pyautogui - pip install pyautogui
# instalar o pandas, numpy e openpyxl- pip install pandas numpy openpyxl
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('Enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('Enter')

time.sleep(2)
pyautogui.click(pyautogui.position(x=565, y=391))
pyautogui.write('alexandre@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345Brazil')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.click(pyautogui.position(x=1198, y=136))

# Importar base de dados de produtos para cadastrar.
tabela = pd.read_csv('produtos.csv')
#print(tabela)

# cadastrar um produto
# Clicar no campo código do produto

for linha in tabela.index:
    pyautogui.click(pyautogui.position(x=583, y=277))

    # escrever o código
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    # Marca do produto
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    # Marca do Tipo
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    # Marca do Categoria
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    # Marca do Preço unitário
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # Marca do Custo do produto
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    # Marca do OBS
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, "obs"])
    if obs != 'nan':
        pyautogui.write(obs)

    # Btn enviar
    pyautogui.press('tab')
    pyautogui.press('enter')
    # scrool pra subir no início da tela
    pyautogui.scroll(5000)





