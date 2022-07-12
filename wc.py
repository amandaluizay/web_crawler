import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):
    # lista vazia para armazenar conteúdo do site
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    # trasnforma o conteudo das div e classes em txt
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text.text

        # transforma tudo em letra minuscula e separa por linha
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


# remove simbolos da lista
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%&*()_+/|\~^;:.,{}[]'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


# dicionario que possui cada palavra
def create_dictionary(clean_list):
    word_count = {}
    # conta quantas vezes  as palavras aparecem
    for word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("% s : %s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start('https://www.codingame.com/playgrounds/52499/programacao-python-intermediario---prof--marco-vaz/exercitando')
