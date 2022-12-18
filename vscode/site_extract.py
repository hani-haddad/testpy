from bs4 import BeautifulSoup
import exceptiongroup
import requests

class SoupExtractor:
    Url='https://lawyers.lawyerlegion.com/california/administrative-law'

    def __init__(self, html_location):
        self.html_location: str = html_location
        
    @staticmethod
    def request(url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)
        page.raise_for_status()
        return page

    @staticmethod
    def write_html(path:str, html):
        with open(path, 'w+', encoding='utf-8') as html_file:
            html_file.write(html)

    @staticmethod
    def get_soup(html_filePath: str):
        with open(html_filePath, 'r', encoding='utf-8') as html_file:
            html = html_file.read()
            soup = BeautifulSoup(html, 'html.parser')
            return soup
    
    def profile_soup_generator(self):
        try:
          main_page = self.request(self.Url)
          self.write_html(self.html_location, main_page.text)
          main_soup= self.get_soup(self.html_location)
          sections = main_soup.find_all("section",class_="listing")
        except Exception as err:
          print(err)
        
        pages_soup=[]
        try:
            for index ,section in  enumerate(sections):
                page_link = section.a["href"]
                page=self.request(page_link)
                self.write_html(self.html_location, page.text)
                soup= self.get_soup(self.html_location)
                pages_soup.append(soup)
                if index == 1:
                  break
        except Exception as err:
            print(err)
        return pages_soup
