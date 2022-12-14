from bs4 import BeautifulSoup
import requests

class soup_extractor:
    Url='https://lawyers.lawyerlegion.com/california/administrative-law'

    def __init__(self):
        pass
        
    @staticmethod
    def request(url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)
        return page
    
    def get_soup(self):
            page = self.request(self.Url)
            soup = BeautifulSoup(page, 'html.parser')
            return soup

    def profile_soup_generator(self):
        main_soup= self.get_soup()
        sections = main_soup.find_all("section",class_="listing")
        pages_soup=[]
        for index ,section in  enumerate(sections):
            #if index == 1:
            # break
            page_link = section.a["href"]
            soup= self.get_soup(page_link)
            pages_soup.append(soup)
        return pages_soup