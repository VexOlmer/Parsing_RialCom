from bs4 import BeautifulSoup
import requests

url = 'https://www.rialcom.ru/internet_tariffs/'
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

all_tr = soup.find_all('tr', class_='small text-center')

print(all_tr)