from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
import requests as r
import re

def scrap(query, currency, os):
    # Constantes de webs con cargado dinamico
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=Service('D:\geckodriver\geckodriver.exe'), options=options)
    lista = []
    # Dolar Tarjeta
    page = r.get(f'https://dolarhoy.com/cotizacion-dolar-tarjeta')
    soup = bs(page.content, 'html.parser')
    dolar = soup.find("div", attrs={"class":"value"}).text
    
    # Obtiene listas de distintos proveedores
    page = r.get(f'https://www.eneba.com/store/all?os[]={os}&text={query}', cookies={'exchange':currency, 'region':'spain'})
    soup = bs(page.content, 'html.parser')
    eneba = [i.find("span", attrs={"class":"YLosEL"}).text+"_|_"+i.find("span", attrs={"class":"L5ErLT"}).text+"_|_"+"https://eneba.com"+i.find("a", attrs={"class":"oSVLlh"}).get('href') 
    for i in soup.find_all("div", attrs={"class":"pFaGHa"})]
    
    page = r.get(f"https://store.steampowered.com/search/?term={query.replace(' ','+')}")
    soup = bs(page.content, 'html.parser')
    steam = [i.find("span", attrs={"class":"title"}).text+'steam'+"_|_"+i.find("div", attrs={"class":"discount_final_price"}).text+"_|_"+i.get('href')
             for i in soup.find_all("a", attrs={"class":"search_result_row"})[:5] if i.find("div", attrs={"class":"discount_final_price"}) != None]

    driver.get('https://www.microsoft.com/es-ar/search/shop?q=fallout+76')
    driver.implicitly_wait(6)
    html = driver.page_source
    driver.quit()

    soup = bs(html, 'html.parser')
    
    mstore = soup.find_all("div", attrs={"class":"card"})
    mstore = [i for i in mstore if 'bg-blue' not in i.get('class', []) and len(i.find_all("p")) >= 1]
    mstore = [i.find("a", attrs={"data-bi-mto":"true"}).text+'mstore'+"_|_"+i.find("p", attrs={"class":"sr-only"}).text+"_|_"+i.find("a", attrs={"data-bi-mto":"true"}).get('href') 
            for i in mstore if i.find("p", attrs={"class":"sr-only"}).text.count("$") >= 1]

    results = eneba+steam+mstore
    # Procesa la lista de todos los proveedores juntos
    for i in results:
        i = i.split('_|_')
        name = i[0]
        price = i[1].replace("$","")
        url = i[2]
        # Steam Price Filter
        if 'steam' in name: 
            platform = 'steam'
            name=name[:-5].replace('\n','')
            price = float(price)*float(dolar[1:])
            price = f"{float(price):,.2f}"
        # Microsoft Store Price Filter
        elif 'mstore' in name:
            platform = 'mstore'
            name=name[:-6]
            match = re.search(r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?', price)
            if match: price = match.group(0)
            else: price = None
            price = re.sub(r'(?<=\d).(?=\d{3}(?:[.,]|$))', '', price)

        elif 'xbox' in name: platform = 'xbox'
        else: platform = 'pc'

        # Eneba Price filter
        if platform == "pc" or platform == "xbox":
            price = price.split(currency)[1].strip()
        
        # General Price Format
        price = re.sub(r'(?<=\d),(?=\d{3}(?:[.,]|$))', '', price)
        price = price.replace(',', '.')
        price = f"{float(price):,.2f}"
        lista.append({"name":name, "price":price.strip(), "platform":platform, "url":url})
    return lista