from name_extract import FullName
from phone_extract import PhoneNumber
from email_extract import Email
from address_extract import Address

class PageExtractor(FullName,PhoneNumber,Email,Address):
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

        if email :=self.email_extrator(soup):
            self.email = self.clean_up_email(email)
            data['emails']=self.email
        
        if address :=self.address_extrator(soup):
            self.address = self.clean_up_address(address)
            data['addresses']=self.address
   
        return {self.name:data}
