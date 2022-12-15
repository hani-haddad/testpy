from site_extract import soup_extractor
from name_extract import full_name


class page_extractor(soup_extractor,full_name):
    
    def __init__(self):
        pass

    def extract_info(self):
        data={
                'names':[]
            }
         
        soups =self.profile_soup_generator()  
        for soup in soups:
            if name :=self.name_extrator(soup):
                data['names'].append({'name':self.clean_up_name(name)})
        return data
