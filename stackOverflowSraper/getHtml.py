import requests

# call the function download htmls
class getHtml:
    results = []

    def Request(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)

        return page

#call it write html file to location and you need another function to setup location
    def to_html(self, html):
        with open('page.html', 'w') as html_file:
            html_file.write(html)

# you can call this get_soup and send the file path to it no need to
#  read by line and send the file path to the soup you can move the file location 
    def from_html(self):
        html = ''

        with open('page.html', 'r') as html_file:
            for line in html_file.read():
                html += line

        return html