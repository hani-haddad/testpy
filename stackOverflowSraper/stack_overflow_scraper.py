from soup_setup import download_htmls
from data_export import Exporter
from datetime import datetime


class Scraper(download_htmls, Exporter):

    def __init__(self, tag, html_location):
        # self.data_location = data_location
        self.html_location: str = html_location
        self.question_list: list = []
        self.tag: str = tag

    # call this an extract_page and don't use camle case to function names
    def extract_page(self, page_soup):

        page_summary = page_soup.find_all('div', class_="s-post-summary")

        for question in page_summary:
            Question = self.scrap_question(question)
            self.question_list.append(Question)

        return self.question_list

    @staticmethod
    def scrap_question(question):

        # never use nameless variables v,i,...
        scraped_skills = question.find('ul', class_="ml0 list-ls-none js-post-tag-list-wrapper d-inline").contents
        skills = []
        for skill in scraped_skills:
            skill = skill.text
            skills.append(skill)

        Question = {
            'title': question.find('a', class_="s-link").text,
            'link': "https://stackoverflow.com/" + question.find('a', class_="s-link")["href"],
            'votes': int(question.find('span', class_="s-post-summary--stats-item-number").text),
            'question_date': datetime.strptime(question.find('span', class_="relativetime")["title"][0:-1],
                                               "%Y-%m-%d %H:%M:%S").date().strftime('%Y-%m-%d'),
            'question_time': datetime.strptime(question.find('span', class_="relativetime")["title"][0:-1],
                                               "%Y-%m-%d %H:%M:%S").time().strftime('%H:%M:%S'),
            'skills': skills
        }
        return Question

    def run(self, pages_nums, data_location):
        """Start scraper"""

        # this is called setup scraper need to setup scraper and scrape and crowl the html and save it and then start the extractor
        #  the extractor should reed from file location to setup the soup and start extract the qustions for example
        #  extractor should send its final object to another class for writing to csv of json or DB or any other
        # Loop over page range
        for page in range(1, pages_nums+1):
            # Init next page's URL
            url = f'https://stackoverflow.com/questions/tagged/{self.tag}?tab=Active&page={page}&pagesize=50'

            page = self.request(url)
            file_path = self.open_file(self.html_location)
            self.write_html(file_path, page.text)
            soup = self.get_soup(file_path)

            # Parse the response
            questions = self.extract_page(soup)

            export = Exporter(data_location)
            data = Exporter.to_data_frame(questions)

            export.json_export(data)
            export.csv_export(data)
