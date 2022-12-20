from name_extract import FullName
from phone_extract import PhoneNumber

class PageExtractor(FullName,PhoneNumber):
    name = ''
    def __init__(self):
        pass

    def extract_info(self,soup):
        data={}  

        if name :=self.name_extrator(soup):
            self.name = self.clean_up_name(name)
            data['names']=self.name
            
            
        if phone :=self.phone_extrator(soup):
            self.phone = self.clean_up_phone(phone)
            data['phones']=self.phone
            
        return {self.name:data}
