from bs4 import BeautifulSoup as bs
import requests as r

def scrap(query, currency, os):
    lista = []
    # Dolar Tarjeta
    page = r.get(f'https://dolarhoy.com/cotizacion-dolar-tarjeta')
    soup = bs(page.content, 'html.parser')
    dolar = soup.find("div", attrs={"class":"value"}).text
    # Pages
    page = r.get(f'https://www.eneba.com/store/all?os[]={os}&text={query}', cookies={'exchange':currency, 'region':'spain'})
    soup = bs(page.content, 'html.parser')
    eneba = [i.text+"_|_https://eneba.com"+i.find("a", attrs={"class":"oSVLlh"}).get('href') for i in soup.find_all("div", attrs={"class":"pFaGHa"})]
    
    page = r.get(f"https://store.steampowered.com/search/?term={query.replace(' ','+')}")
    soup = bs(page.content, 'html.parser')
    steam = [i.text+'steam'+"_|_"+i.get('href') for i in soup.find_all("a", attrs={"class":"search_result_row"})[:5]]

    results = eneba+steam
    for i in results:
        url = i.split("_|_")[1]; i = i.split('_|_')[0]
        if 'steam' in i: platform = 'steam'; i=i[:-5]
        if 'epic' in i: platform = 'epic'; i=i[:-4]
        elif 'xbox' in i: platform = 'xbox'
        else: platform = 'pc'
        name = ' '.join(i.split(' ')[:5])
        if currency in i: price = i.split(currency)
        if '$' in i: price = i.split('$')
        if platform == 'epic': price = i.split('|')[1].split(' ')[0]
        price = price[len(price)-1]
        if len(price) > 2: 
            price = price.split('.')[0]+'.'+price.split('.')[1][:2]
            if platform == 'steam': 
                price = str(float(price)*float(dolar[1:])+(float(price)*float(dolar[1:]))*0.65)
                price = price.split('.')[0]+'.'+price.split('.')[1][:2]
                price = "{:,.2f}".format(float(price))
            lista.append({"name":name, "price":price.strip(), "platform":platform, "url":url})
    return lista