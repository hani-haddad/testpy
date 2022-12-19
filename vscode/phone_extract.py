import re 
import itertools
from site_extract import SoupExtractor

class PhoneNumber(SoupExtractor):
    re_phone ="(\d{3}|\(\d{3}\))(\s|-|\.)+(\d{3}|\(\d{3}\))(\s|-|\.)+(\d{4}|\(\d{4}\))(\s*(ext|x|ext.)\s*(\d{2,5}))?"
    search_tags=["h1","h2","h3","h4","h5","h6"]
    search_class_phones=["telnum"]
    search_phrases_phones=['tel','phone','call','contact']



    def __init__(self):
        pass

    def phone_extrator(self,soup):
     phone=soup.find(string=re.compile(self.re_phone,re.I)).text   
     return phone.split(":")

    

    def find_by_class(self,soup,tag=""):
      print(3) 

      self.search_class_phones=list(itertools.chain.from_iterable([class_.split(" ") for class_ in self.search_class_phones]))
      if found_tags := soup.find_all(tag,{'class':self.search_class_phones},string=re.compile(self.re_phone,re.I)):
          [self.search_tags.append(tag.name) if tag.name not in self.search_tags else  None for tag in found_tags]
          return [name.text for name in found_tags] if(len(found_tags)>0)  else  None

    def find_in_contact_page(self,soup):
        try:
            contact_link = soup.find('a',text=re.compile('contact',re.I))['href']
            contact_page = self.request(contact_link)
            self.write_html(self.html_location, contact_page.text)
            contact_soup= self.get_soup(self.html_location)
            found_tags=contact_soup.find_all("",text=re.compile(self.re_phone,re.I))
            return [name.text for name in found_tags] if(len(found_tags)>0)  else  None
        except:
            return None
    
    def find_by_phone_phrases(self,soup,tag=""):
        contact = soup.find_all(tag="",text=re.compile('contact',re.I))
        phones=[]
        for index,i in enumerate(contact):

            if i.name == 'script':
                continue
            f=soup.find_all(i.name,text=re.compile(self.re_phone,re.I))
            phones.append(f) if(len(f)>0 and f not in phones)  else  None
            for t in range(0,5):
                i=i.next_element
                if i.name != 'script':
                  print(i.name)
                f=soup.find_all(i.name,text=re.compile(self.re_phone,re.I))
                n=[u if u not in phones and '@context' not in u else  None for u in f]
                t+1
        return

    def general_search(self,soup):
        phone=soup.find(string=re.compile(self.re_phone,re.I)).text   
        return phone.split(":")
        
        

