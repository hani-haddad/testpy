from extract_page import PageExtractor
from data_export import Exporter

if __name__ == '__main__':
    # Init scraper instance
    id_to_att_list = []
    o = {}
    info_scraper = PageExtractor()
    if o := info_scraper.extract_info():
        id_to_att_list.append(o)
    

    export=Exporter("C:/Users/shatha/Desktop/info")
    data=export.to_data_frame(id_to_att_list)
    export.json_export(id_to_att_list)




