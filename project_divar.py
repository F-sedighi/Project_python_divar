import requests
from bs4 import BeautifulSoup

response = requests.get('https://divar.ir/s/kurdistan-province/car/peugeot/405')
soup = BeautifulSoup(response.text, 'html.parser')
res1 = soup.find_all('h2', attrs = {'class': 'kt-post-card__title'})
#res2 = soup.find_all('div', attrs = {'class': 'kt-post-card__info'})
res2 = soup.find_all(attrs={'class':{'kt-post-card__description', 'kt-post-card__title', 'kt-post-card__bottom-description kt-text-truncate'}})

x=[string for iter in range(len(res2)) for string in res2[iter].stripped_strings]
