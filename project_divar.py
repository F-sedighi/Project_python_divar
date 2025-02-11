import requests
from bs4 import BeautifulSoup

response = requests.get('https://divar.ir/s/kurdistan-province/car/peugeot/405')
soup = BeautifulSoup(response.text, 'html.parser')
res1 = soup.find_all('h2', attrs = {'class': 'kt-post-card__title'})
res2 = soup.find_all(attrs={'class':{'kt-post-card__description', 'kt-post-card__title', 'kt-post-card__bottom-description kt-text-truncate'}})
[print(str2.get_text()) for str2 in res2]


#[print(str1.get_text(), str2.get_text()) for str1,str2 in zip(res1,res2)]
