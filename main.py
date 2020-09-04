# newsBot scrapes BBC news articles, then tweets the top 5 stories with links every three hours

import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('http://www.bbc.co.uk/news')
doc = BeautifulSoup(response.text, 'html.parser')

count = 0
stories_list = []
stories = doc.find_all('div', { 'class': 'gs-c-promo' })

for story in stories:
    count += 1
    headline = story.find('h3')
    time_pub = story.find('span', {'class': 'gs-u-vh'})
    link = story.find('a')
    story_dict = {
        'headline': headline.text,
        'time': time_pub.text,
        'link': 'https://www.bbc.co.uk' + link['href']
    }
    stories_list.append(story_dict)
    if count == 5:
        break

df = pd.DataFrame(stories_list)
df.to_csv('./bbc.csv', index=False)