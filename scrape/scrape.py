import requests
from bs4 import BeautifulSoup

response_p1 = requests.get('https://news.ycombinator.com/news')
response_p2 = requests.get('https://news.ycombinator.com/news?p2')
soup1 = BeautifulSoup(response_p1.text, 'html.parser')
soup2 = BeautifulSoup(response_p2.text, 'html.parser')


topik1 = soup1.select('.subtext')
topik2 = soup2.select('.subtext')
links1 = soup1.select('.titleline > a')
links2 = soup2.select('.titleline > a')

all_links = links1 + links2
all_text = topik1 +topik2

def sort_topik_by_score(list_of_topik):
    return sorted(list_of_topik, key=lambda k:k['score'], reverse=True)


def create_custom_hackernews(all_links, score_list):
    hn = []
    for index, item in enumerate(all_links):
        title = item.getText()
        href = item.get('href', None)
        score = score_list[index].select('.score')
        if len(score):
            score = int(score[0].getText().replace(' points', ''))
            if score > 100:
                hn.append({'title': title, 'link': href, 'score': score})
    return sort_topik_by_score(hn)


print(create_custom_hackernews(all_links, all_text))
