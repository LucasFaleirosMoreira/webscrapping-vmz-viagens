from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd 

#Para utilizar o código corretamente instale:
# pip install pandas openpyxl
# pip install selenium
# pip install requests beautifulsoup4
# Por conta do selenium você precisa colocar o .exe do seu google chrome na mesma pasta que o codigo. Eu não conseguir enviar o .exe do google pelo email pois
#o email detecta como se fosse virus e bloqueia o arquivo de ser enviado.

# Utilizei pandas openpyxl para conseguir converter uma lista de dados (dicionario) em uma tabela de formato .xlsx (para excel)
# Eu ia tentar utilizar beautifulsoup porém essa biblioteca só funciona para dados que não estão sendo distribuidos de forma dinamica na página, porém já que
# a pagina de cotação do UOL é algo dinamico tive q utilizar o selenium e fazer ele abrir o navegador por conta propria e "pegar o Javascript" para conseguir acessar os dados
# por isso o chrome.exe na pasta.



service = Service()
driver = webdriver.Chrome(service=service)

url = 'https://economia.uol.com.br/cotacoes/cambio/'
driver.get(url)

time.sleep(5)

html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')

dados = []


cotacao = bs.find('span','chart-info-val ng-binding').text
horarioAtual = bs.find('span', 'chart-upd-text col-sm-12 col-xs-4 ng-binding').text
data = horarioAtual.split()[2].strip()
hora = horarioAtual.split()[4].strip()
valor = cotacao.strip()

print(f"Valor de compra atual: {valor} \nData: {data} {hora}" )

dados.append ({
    'Data': data,
    'Hora': hora,
    'Valor de Compra': valor
})

tabela = pd.DataFrame(dados)

tabela.to_excel('dados.xlsx', index=False)

driver.quit()