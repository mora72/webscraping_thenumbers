# -*- encoding: utf-8 -*-

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pickle


def builddict(anoid):
    # Grab content from URL
    url = f'https://www.the-numbers.com/movies/year/{anoid}'
    driver.get(url)
    driver.implicitly_wait(10)  # in seconds

    element = driver.find_element_by_xpath("//div[@id='page_filling_chart']//center//table")
    html_content = element.get_attribute('outerHTML')

    # Parse HTML (Parsear o conteúdo HTML) - BeaultifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Data Structure Conversion (Estruturar conteúdo em um Data Frame) - Pandas
    df_full = pd.read_html(str(table))[0]
    df = df_full[['ReleaseDate', 'Movie', 'Genre', 'ReleaseType', 'Revenueto Date']]
    df.columns = ['Data_Lanc', 'Filme', 'Genero', 'Tipo', 'Receita']
    # Convert to Dict
    return df.to_dict('records')  # records é uma das formas de converter o df para um dicionário


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

lista_anos = (2020, 2019)
dictresult = {}
for ano in lista_anos:
    dictresult[f'{ano}'] = builddict(ano)
    print(ano, len(dictresult[f'{ano}']))
driver.quit()

# Salva Dicionário em arquivo
file = open('moviesdict', 'wb')
pickle.dump(dictresult, file)
file.close()
