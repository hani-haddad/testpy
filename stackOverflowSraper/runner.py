from stack_overflow_scraper import Scraper

if __name__ == '__main__':
    # Init scraper instance
    scraper1 = Scraper("python", "page1.html",)
    scraper2 = Scraper("java", "page2.html")

    # Start scraper
    scraper1.run(2, "C:/Users/shatha/Desktop/e")
    # scraper2.run("w")