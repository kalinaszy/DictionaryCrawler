import requests
from bs4 import BeautifulSoup

#  page = requests.get("https://sensiblechinese.com/common-chinese-characters/")
#  page = requests.get("http://www.mementoslangues.fr/Chinois/Sinogrammes/Table3000CaracteresChinois.pdf")
#  page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("http://hanzidb.org/character-list/by-frequency")
page
print(page.status_code)

class Word:
    def __init__(self, character, definition):
        self.character = character
        self.definition = definition
    def __str__(self):
        return self.character + self.definition
    def __repr__(self):
        return self.character + self.definition

def get_content(url):
    page = requests.get(url)                              
    return BeautifulSoup(page.content, 'html.parser') 

def find_words(soup):
    words_list = []
    table_tr = soup.find_all("tr")
    for item in table_tr[1:]:
        a = item.find("a")
        character = a.get_text()
        definition = item.find("span", class_="smmr").get_text()
        word = Word(character=character, definition=definition)
        words_list.append(word)
    return words_list

def main():
    url = "http://hanzidb.org/character-list/by-frequency?page={}"
    for i in range(10):
        soup = get_content(url.format(i))
        print(find_words(soup))

main()










#print(soup.prettify())



#print(list(soup.children))

#print(soup.title)
# print(soup.find_all('a'))
# tr d a href znak
# example = soup.find(text="Most common Chinese characters - ordered by frequency")
# print(example)
#
#
# import requests
# from bs4 import BeautifulSoup
#
# url_pagination= "http://hanzidb.org/character-list/by-frequency"
# r = requests.get(url_pagination)
# soup = BeautifulSoup(r.content, "html.parser")
#
# page_url = "http://hanzidb.org/character-list/by-frequency?page={}"
# last_page = soup.find('ul', class_='pagination').find('li', class_='next').a['href'].split('=')[1]
# #last_page = soup.select_one('ul.pagination li.next a')['href'].split('=')[1] # with css selectors
# dept_page_url = [page_url.format(i) for i in range(1, int(last_page)+1)]
#
# print(dept_page_url)
#
#
#
