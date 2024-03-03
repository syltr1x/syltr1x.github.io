import requests as r
from bs4 import BeautifulSoup as bs

page = r.get(f"https://store.epicgames.com/es-ES/browse?q=gta v&sortBy=releaseDate&sortDir=DESC&count=40")
soup = bs(page.content, 'html.parser')
open('page.html', 'w', encoding='utf8').write(page.text)
epic = [i for i in soup.find_all("a", attrs={"class":"css-g3jcms"})]
print("----------------------------")
print(epic)
print("----------------------------")