from extract_page import page_extractor
from data_export import Exporter

if __name__ == '__main__':
    # Init scraper instance
    info_scraper = page_extractor()
    data =info_scraper.extract_info()

    export=Exporter("C:/Users/shatha/Desktop/info")
    data=export.to_data_frame(data)
    export.json_export(data)




