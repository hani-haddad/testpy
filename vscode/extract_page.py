from site_extract import soup_extractor
from name_extract import full_name

class page_extractor(soup_extractor,full_name):
    def __init__(self):
        soups =self.profile_soup_generator()

    def extract_info(self):
        data={
                'names':[]
            }
        for soup in self.soups:
            if name :=self.extract_name(soup):
                data['names']={'name':self.clean_up_name(name)}
            return data 
    
    def extract_name(profile_soup):
        
        return
