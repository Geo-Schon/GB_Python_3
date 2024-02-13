"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
"""

import requests
from bs4 import BeautifulSoup
from collections import Counter

url = 'https://ru.wikipedia.org/wiki/Бофорт,_Джон,_1-й_граф_Сомерсет'
resp = requests.get(url)


def get_description(soup):
    result = []
    dataset = soup.findAll('div', class_='mw-body-content')
    for data in dataset:
        for p in data.findAll('p'):
            result.append(p.text)
    return ' '.join(result)


draft_wiki_text = BeautifulSoup(resp.text, 'lxml')
wiki_text = get_description(draft_wiki_text)

split_wiki_text = wiki_text.split()
Counters_found = Counter(split_wiki_text)

most_occur = Counters_found.most_common(10)
print(most_occur)