import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.airbnb.co.id/s/Yogyakarta--Indonesia/homes?place_id=ChIJxWtbvYdXei4RcU9o09Q_ciE&refinement_paths%5B%5D=%2Fhomes')

soup = BeautifulSoup(page.content, 'html.parser')

villas = soup.find_all("div", "_1048zci")

for villa in villas :
    name = villa.find("div",  "_bzh5lkq").text
    price = villa.find("span", "_1p7iugi").text
    description = villa.find_all("div", "_kqh46o")
    room = description[0].text
    facilty = description[0]

    print(name)
    print(facilty.text)
    print(facilty, "\n")