import requests


class getHtml:
    results = []

    def Request(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        page = requests.get(url)
        print(' | Status code: %s' % page.status_code)

        return page

    def to_html(self, html):
        with open('page.html', 'w') as html_file:
            html_file.write(html)

    def from_html(self):
        html = ''

        with open('page.html', 'r') as html_file:
            for line in html_file.read():
                html += line

        return html