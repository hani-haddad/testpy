from bs4 import BeautifulSoup
import requests

class SoupExtractor:
    Url='https://lawyers.lawyerlegion.com/california/administrative-law'

    def __init__(self):
        pass
        
    @staticmethod
    def request(url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)
        return page
    
    @staticmethod
    def get_soup(page):
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup

    def profile_soup_generator(self):
        main_page = self.request(self.Url)
        main_soup= self.get_soup(main_page)
        #if
        sections = main_soup.find_all("section",class_="listing")
        pages_soup=[]
        for index ,section in  enumerate(sections):

            page_link = section.a["href"]
            page=self.request(page_link)
            soup= self.get_soup(page)
            pages_soup.append(soup)
            if index == 1:
             break
        return pages_soup
