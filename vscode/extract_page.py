from name_extract import FullName


class PageExtractor(FullName):
    name = ''
    def __init__(self):
        pass

    def extract_info(self,soup):
        data={}  

        if name :=self.name_extrator(soup):
            self.name = self.clean_up_name(name)
            data['names']=self.name
            return {self.name:data}
