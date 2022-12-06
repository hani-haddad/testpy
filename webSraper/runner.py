from stack_overflow_scraper import Scraper
from wikipedia_ListofWaltDisneyfilms_scraping import Extractor

if __name__ == '__main__':
    # Init scraper instance
    stack_overflow_scraper1 = Scraper("python", "page1.html",)
    stack_overflow_scraper1= Scraper("java", "page2.html")

    wikipedia_scraper = Extractor("hh.html")
    

    # Start extracting data for multiple websites 
    stack_overflow_scraper1.run(2, "C:/Users/shatha/Desktop/questions_details_python")
    wikipedia_scraper.get_info("C:/Users/shatha/Desktop/WaltDisneyfilms_details")
    

