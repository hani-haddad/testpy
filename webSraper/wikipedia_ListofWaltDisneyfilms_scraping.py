from site_setup import download_htmls
from data_export import Exporter
from bs4 import NavigableString, Tag


class Extractor(download_htmls, Exporter):
    main_url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films#Released"
    

    def __init__(self,html_location):
        self.html_location: str = html_location

    def get_movies_details(self, movie_soup):
        self.remove_reference_tags(movie_soup)
        table = movie_soup.find("table", {'class': 'infobox vevent'})
        rows = table.find("tbody").find_all('tr')
        movie = {}
        for index, row in enumerate(rows):
            if index == 0:
                movie['title'] = row.find("th").text
            elif index == 1:
                continue
            else:
                th = row.find('th').get_text(" ", strip=True)
                td = self.get_values(row)
                movie[th] = td
        return movie

    def movies_site_iterator(self, main_soup, movie_name):
        tables = main_soup.find_all("table", class_="wikitable sortable")
        movies = []
        for index, table in enumerate(tables):
            if index == 1:
                break
            rows = table.find("tbody").find_all('tr')
            for row in rows:
                if row.a:
                    page_link = "https://en.wikipedia.org" + row.a["href"]
                    print(page_link)
                    movie_soup = self.request_soup(str(page_link))
                    try:
                        movies.append(self.get_movies_details(movie_soup),self.text_between_2tags("h2","h2"))
                    except Exception as e:
                        print(e)
                        print("strange case profile")
                else:
                    continue
        return movies

    # save_data("ListofWaltDisneyfilms", movies)
    # print(soups)

    @staticmethod
    def get_values(row):
        if row.td.find("br"):
            values = [text for text in row.td.stripped_strings]
            return values
        elif row.td.find("ul"):
            if row.td.find("b"):
                nested_values = []
                nested_names = []
                for div in row.td.find_all("div", class_='plainlist'):
                    values = [li.text.replace("\xa0", " ") for li in div.ul.find_all('li')]
                    nested_values.append(values)
                for b in row.td.find_all("b"):
                    nested_names.append(b.text)

                nested_elements = {nested_names[i]: nested_values[i] for i in range(len(nested_values))}
                return nested_elements

            else:
                for ul in row.td.find_all('ul'):
                    values = [li.get_text(" ", strip=True).replace("\xa0", " ") for li in ul.find_all('li')]
                return values

        else:
            return row.find('td').get_text(" ", strip=True).replace("\xa0", " ")

    @staticmethod
    def remove_reference_tags(soup):
        for tag in soup.find_all("sup"):
            tag.decompose()

    def request_soup(self, url):
        page = self.request(url)
        file_path = self.open_file(self.html_location)
        self.write_html(file_path, page.text)
        soup = self.get_soup(file_path)
        return soup

    def get_info(self, data_location):
        # Parse the response
        
        movies = self.movies_info_generator(self.request_soup(self.main_url), "Snow White and the Seven Dwarfs")

        export = Exporter(data_location)
        data = Exporter.to_data_frame(movies)

        export.json_export(data)
        export.csv_export(data)

    def text_between_2tags(start_tag,end_tag,moviesoup):
        movieDetails = moviesoup.find("div", class_="vector-body")
        movieDescription = {}
        for header in movieDetails.find_all(start_tag):
            movieDetail = header.get_text().strip()
            nextNode = header
            movieDetailText = []
            nested_data=[]

            while True:
                nextNode = nextNode.nextSibling
                # This writes out the last of the H2 tags and its following contents
                if not nextNode:
                    movieDescription[movieDetail] = "\n".join(movieDetailText)
                    break
                # This adds non-H2 tags to the text to attach to the text of the H2
                elif isinstance(nextNode, NavigableString):
                    if nextNode.strip():
                        movieDetailText.append(nextNode.strip())
                        pass
                # This detects the next H2 and writes the compiled text to the previous H2
                elif isinstance(nextNode, Tag):
                    if nextNode.name == end_tag:
                        break
                    elif nextNode.name == "div" or nextNode.name == "style":
                        continue
                    elif nextNode.name == "h3" :
                        res= self.text_tags(nextNode)
                        nested_data.append(res)
                        movieDescription[movieDetail]= nested_data
        
                    movieDetailText.append(nextNode.get_text())
                    nested_data.append(nextNode.get_text())
                    movieDescription[movieDetail] = "\n".join(movieDetailText)
                
        return movieDescription

    def text_tags(tag):
        movieDescription = {}
        for header in tag.find_next_siblings():
            movieDetail = tag.get_text().strip()
            movieDescription[movieDetail] =""
            nextNode= header.previous_sibling
            movieDetailText = []
            while True:
                nextNode = nextNode.nextSibling
                
                # This writes out the last of the H2 tags and its following contents
                if not nextNode:
                    movieDescription[movieDetail] = "\n".join(movieDetailText)
                    break
                # This adds non-H2 tags to the text to attach to the text of the H2
                elif isinstance(nextNode, NavigableString):
                    if nextNode.strip():
                        movieDetailText.append(nextNode.strip())
                        pass
                # This detects the next H2 and writes the compiled text to the previous H2
                elif isinstance(nextNode, Tag):
                    if nextNode.name == "h2" or nextNode.name == "h3" or nextNode.name == "h4" or nextNode.name == "h5":
                        return movieDescription
                    if nextNode.name == "p":
                        movieDetailText.append(nextNode.get_text())
                        movieDescription[movieDetail] = "\n".join(movieDetailText)
                    elif nextNode.name == "div" or nextNode.name == "style":
                        continue
                    movieDetailText.append(nextNode.get_text())

        return movieDescription
