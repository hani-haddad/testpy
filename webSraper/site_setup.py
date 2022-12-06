# call the function download htmls
import requests
from bs4 import BeautifulSoup


class download_htmls:

    def __init__(self) -> None:
        pass

    @staticmethod
    def request(url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)

        return page

    @staticmethod
    def open_file(path: str):
        with open(path, 'w') as File:
            return path

    # call it write html file to location and you need another function to setup location

    @staticmethod
    def write_html(path:str, html):
        with open(path, 'w+', encoding='utf-8') as html_file:
            html_file.write(html)

    # you can call this get_soup and send the file path to it no need to
    #  read by line and send the file path to the soup you can move the file location

    @staticmethod
    def get_soup(html_filePath: str):
        with open(html_filePath, 'r', encoding='utf-8') as html_file:
            html = html_file.read()
            soup = BeautifulSoup(html, 'html.parser')
            return soup
            
