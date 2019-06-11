import requests
from bs4 import BeautifulSoup

#  page = requests.get("https://sensiblechinese.com/common-chinese-characters/")
#  page = requests.get("http://www.mementoslangues.fr/Chinois/Sinogrammes/Table3000CaracteresChinois.pdf")
#  page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("http://hanzidb.org/character-list/by-frequency")
page

print(page.status_code)

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

print(list(soup.children))

print(soup.title)
# print(soup.find_all('a'))
# tr d a href znak
example = soup.find(text="Most common Chinese characters - ordered by frequency")
print(example)



