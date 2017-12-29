import re
import requests
from bs4 import BeautifulSoup

def get_loc(addr):
    url = "https://geoiptool.com/en/"
    params = {"ip":addr}
    html = requests.get(url, params=params).text
    soup = BeautifulSoup(html, 'html.parser')

    return html

#    country = soup.select('.data-item')[3].select('span')[1].text
#    lat = float(soup.select('.data-item')[8].select('span')[1].text)
#    lng = float(soup.select('.data-item')[9].select('span')[1].text)
#    return [country, lat, lng]


print(get_loc("210.125.84.116"))
