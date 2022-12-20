from extract_page import PageExtractor
from data_export import Exporter
from site_extract import SoupExtractor

if __name__ == '__main__':
    # Init scraper instance
    info_scraper = PageExtractor()
    soup_extractor=SoupExtractor("C:/Users/shatha/Desktop/souphtml")
    
    soups = soup_extractor.profile_soup_generator() 
    id_to_att_list = []
    o = {}
    for soup in soups:
            if o := info_scraper.extract_info(soup):
                id_to_att_list.append(o)


    export=Exporter("C:/Users/shatha/Desktop/info")
    export.json_export(id_to_att_list)

