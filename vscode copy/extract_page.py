from site_extract import SoupExtractor
from name_extract import FullName


class PageExtractor(SoupExtractor,FullName):
    name = ''
    def __init__(self):
        pass

    def extract_info(self):
        data={
                'names':[]
            }
         
        soups =self.profile_soup_generator()  
        for soup in soups:
            if name :=self.name_extrator(soup):
                self.name = self.clean_up_name(name)
                data['names'].append({'name':self.name})
        return {self.name:data}
