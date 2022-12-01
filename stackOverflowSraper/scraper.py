from bs4 import BeautifulSoup
import download_htmls
import pandas as pd
import exporter
from datetime import datetime

class scraper(download_htmls,exporter):
    questionlist = []

#call this an extract_page and dont use camle case to function names
    def extract_page(self, Page_soup):

        page_summarylist= Page_soup.find_all('div', class_="s-post-summary")
        Question=self.scrap_question(page_summarylist)
        # create another function to extract questions
        
        self.questionlist.append(Question)

        return self.questionlist 

    def scrap_question(question):
 
        #never use nameless variables v,i,...
        scraped_skills= question.find('ul', class_="ml0 list-ls-none js-post-tag-list-wrapper d-inline").contents
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

    def run(self, tag):
        '''Start scraper'''

    # this is called setup scraper need to setup scraper and scrape and crowl the html and save it and then start the extractor
    #  the extractor should reed from file location to setup the soup and start extract the qustions for example 
    #  extractor should send its final object to another class for writing to csv of json or DB or any other 
        # Loop over page range
        for page in range(1, 4):
            # Init next page's URL
            Url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=Active&page={page}&pagesize=50'
            obj = scraper()
            page = obj.Request(Url)
            file_path=obj.open_file("page.html")
            obj.write_html(file_path,page.text)
            soup = obj.get_soup(file_path)

            # Parse the response
            questions = obj.extract_page(soup)
            
            export = exporter()
            export.data= questions
            export.json_export()
            export.csv_export()

            



