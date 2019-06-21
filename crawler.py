import hashlib
import os
from random import randint

import PIL
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


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
    list_of_all_characters = []
    for i in range(1, 10):
        soup = get_content(url.format(i))
        words_list = find_words(soup)
        for i in range(len(words_list)):
            word = str(words_list[i])
            char = word[0]
            rest_def = word[1:]
            if not rest_def: continue
            random_answer = str(words_list[randint(1, len(words_list)-1)])
            random_answer2 = str(words_list[randint(1, len(words_list)-1)])
            guessed_wrong1 = random_answer[1:]
            guessed_wrong2 = random_answer2[1:]
            list_of_all_characters.append((char, rest_def, guessed_wrong1, guessed_wrong2))
    print(list_of_all_characters)
    return list_of_all_characters

my_list = main()

def get_file_name(rest_def):
    return hashlib.sha224(rest_def.encode()).hexdigest()+".jpg"

outputs = {} #  naplenic go w petli, kluczem getfilename, w srodku ospathimage
# pozniej dump json zapisac w json na dysku
# pozniej a aplikacji komenda load images i paramtrem bd json (to bd django commands managmene)


for character in my_list:
    img = Image.new("RGB", size=(50,50))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.otf", 40)
    draw.text((0, 0), character[0], (255,255,255), font=font)
    img.save(os.path.join("images", get_file_name(character[1])))


