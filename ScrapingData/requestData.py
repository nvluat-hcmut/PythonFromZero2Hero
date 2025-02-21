import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

# Convert to object
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('.score'))

# file = open('./sample.html', 'w')
# file.write(str(soup))
# file.close()
# # print(soup.body.contents)
# # print(soup.find_all('div'))
# # print(soup.title)
# # print('\n')
# # print(soup.find(id = '32126637'))
# # print(soup.select('.score'))
links = soup.select('.titlelink')
votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace('points', ''))
        print(points)
        # hn.append(title)
        hn.append({'title': title, 'link': href})
    return hn
# print(votes)
# print(create_custom_hn(links, votes))
print(create_custom_hn(links, votes))


