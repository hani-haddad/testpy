from bs4 import BeautifulSoup
import getHtml
import pandas as pd
import csv
import os.path
from datetime import datetime

class stackOverflowSraper(getHtml):
    questionlist = []

    def scrapQuestions(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        scraped_questions = soup.find_all('div', class_="s-post-summary")

        for question in scraped_questions:
            v = question.find('ul', class_="ml0 list-ls-none js-post-tag-list-wrapper d-inline").contents
            skills = []
            for i in v:
                i = i.text
                skills.append(i)

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
            self.questionlist.append(Question)
            self.to_csv(Question)
        df = pd.DataFrame(self.questionlist)
        # df.to_csv('file_name.csv')
        return df.to_json('Questions_Details.json', orient='records', lines=True)

    def to_csv(self, Question):
        '''Write item to CSV file'''

        # Check if "Questions Details.csv" file exists
        questions_exists = os.path.isfile('Questions_Details.csv')

        # Append data to CSV file
        with open('Questions_Details.csv', 'a') as csv_file:
            # Init dictionary writer
            writer = csv.DictWriter(csv_file, fieldnames=Question)

            # Write entry to CSV file
            writer.writerow(Question)

    def run(self, tag):
        '''Start scraper'''

        # Loop over page range
        for page in range(1, 4):
            # Init next page's URL
            Url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=Active&page={page}&pagesize=50'
            obj = stackOverflowSraper()
            page = obj.Request(Url)
            obj.to_html(page.text)
            response = obj.from_html()

            # Parse the response
            obj.scrapQuestions(response)


if __name__ == '__main__':
    # Init scraper instance
    scraper = stackOverflowSraper()

    # Start scraper
    scraper.run("python")
