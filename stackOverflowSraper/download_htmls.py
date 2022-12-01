import requests
from bs4 import BeautifulSoup

# call the function download htmls
class download_htmls:
    results = []

    def Request(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)

        return page

    def open_file(self,path):
      with open(path , 'w') as File:
        return path


#call it write html file to location and you need another function to setup location
    def write_html(self,File,html):
      with open(File , 'w+') as File:
            File.write(html)

# you can call this get_soup and send the file path to it no need to
#  read by line and send the file path to the soup you can move the file location 
    def get_soup(self,File):
      with open(File , 'r') as File:
        html= File.read()
        soup = BeautifulSoup(html,'html.parser')  
        return soup

obj= download_htmls
y=obj.Request("kkk","https://stackoverflow.com/questions/tagged/python?tab=Active")
file_path=obj.open_file("kkk","p.html")

obj.write_html("kkk",file_path,y.text)
soup = obj.get_soup("kkk",file_path)
print(soup)


