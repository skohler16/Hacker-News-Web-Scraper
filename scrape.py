import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def create_custom_hn(links , subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.scores')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            print()
            hn.append({'title': title, 'link': href})
    return hn

print(create_custom_hn(links, subtext))