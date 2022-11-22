# import requests

from bs4 import BeautifulSoup
# req = requests.get('https://www.floridabar.org/directories/find-mbr/profile/?num=171560')

with open(r'htmls/testhtml.html', "r") as f:
    page = f.read()
soup = BeautifulSoup(page , 'html.parser')


#hani

def name_extraxt(soup):
    print(soup.findAll('title'))
    titleTag = soup.findAll('title')[0]
    return titleTag.text.split('–')[1].strip()



    ##jgkjhgkjh
