from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
import requests as r

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
        url = i[1]
        i = i[0]
        if 'steam' in i: platform = 'steam'; i=i[:-5]
        elif 'epic' in i: platform = 'epic'; i=i[:-4]
        elif 'mstore' in i: platform = 'mstore'; i=i[:-6]
        elif 'xbox' in i: platform = 'xbox'
        else: platform = 'pc'
       
        name = ' '.join(i.split(' '))
        if currency in i: price = i.split(currency)
        elif '$' in i: price = i.split('$')
        elif platform == 'epic': price = i.split('|')[1].split(' ')[0]
        if platform == 'mstore': price = i.split('_|_')[-1]
        else: price = price[len(price)-1]

        if len(price) > 2:
            if platform == "mstore":
                if price.count("$") > 1: price = price.split("ahora")[1]
                else: 
                    char = price[price.index(',')+2]
                    price = price.split(char)[0]+char
                price = price.replace(',','[_]').replace('.',',').replace('[_]','.')
            else: price = price.split('.')[0]+'.'+price.split('.')[1][:2]

            if platform == 'steam':
                price = str(float(price)*float(dolar[1:]))
                price = price.split('.')[0]+'.'+price.split('.')[1][:2]
                price = "{:,.2f}".format(float(price))
            lista.append({"name":name, "price":price.strip(), "platform":platform, "url":url})
    return lista