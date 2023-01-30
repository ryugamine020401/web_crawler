# 爬巴哈姆特

import requests
from bs4 import BeautifulSoup
import time
url = 'https://forum.gamer.com.tw/B.php?bsn=36730'
headers = {'user-agent': 'Mozilla/5.0'}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# res = soup.find_all("div", class_ = "title")
res2 = soup.select("div.b-list__tile p")

# for i in res2:
#     print(i.text, f'https://forum.gamer.com.tw/{i["href"]}')
# res = soup.find_all("div", id ="BH-pagebtn")
# print(res)
# print(res[0].getText)

res = soup.find_all("a", class_ = "next")
print(res)





