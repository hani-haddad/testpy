import re 
import itertools
from operator import is_not
from functools import partial
from site_extract import SoupExtractor

class PhoneNumber(SoupExtractor):
    re_phone ="(\d{3}|\(\d{3}\))(\s|-|\.)+(\d{3}|\(\d{3}\))(\s|-|\.)+(\d{4}|\(\d{4}\))(\s*(ext|x|ext.)\s*(\d{2,5}))?"
    #search_tags=["h1","h2","h3","h4","h5","h6"]
    search_class_phones=["telnum"]
    search_phrases_phones=['tel','phone','call','contact','telephone']

    def __init__(self):
        pass

    def phone_extrator(self,soup):
        if phones :=self.find_in_contact_page(soup):
            return phones

        if phones :=self.find_in_class(soup):
            return phones

        elif phones :=self.find_by_phone_phrases(soup):
            return phones
        
        elif phones :=self.general_search(soup):
            return phones

    def clean_up_phone(self,phones):
        phones=list(filter(partial(is_not, None), phones))
        try:
          phones=[num.strip("\n") for num in phones ]
        except:pass
        result = [{}]
        for item in phones:
            try:
                key, val = item.split(":")
            except: key,val = None,item
            if key in result[-1]:
                result.append({})
            result[-1][key] = val
        return result

    def find_in_contact_page(self,soup):
        print(11) 
        try:
            contact_link = soup.find('a',text=re.compile('contact',re.I))['href']
            contact_page = self.request(contact_link)
            self.write_html("html", contact_page.text)
            contact_soup= self.get_soup("html")
            phones=contact_soup.find_all("",text=re.compile(self.re_phone,re.I))
            return [phone if phone not in phones or '@context' not in phone else  None for phone in phones]
        except: return None
        
    
    def find_in_class(self,soup,tag=""):
        print(22) 
        self.search_class_phones=list(itertools.chain.from_iterable([class_.split(" ") for class_ in self.search_class_phones]))
        if found_tags := soup.find_all(class_=self.search_class_phones,string=re.compile(self.re_phone,re.I)):
          [self.search_tags.append(tag.name) if tag.name not in self.search_tags else  None for tag in found_tags]
          return [name.text for name in found_tags] if(len(found_tags)>0)  else  None
    
    def find_by_phone_phrases(self,soup,tag=""):
        print(33) 
        for phrase in self.search_phrases_phones:
           contacts = soup.find_all(tag="",text=re.compile(phrase,re.I))
           for tag in contacts:
                if tag.name == 'script':
                    continue
                phones_match=soup.find_all(tag.name,text=re.compile(self.re_phone,re.I))
                phones=[phone if phone not in phones or '@context' not in phone else  None for phone in phones_match]
                for iterator in range(0,20):
                    tag=tag.next_element
                    if tag.name != 'script':
                        phones_match=soup.find_all(tag.name,text=re.compile(self.re_phone,re.I))
                        phones=[phone.text if phone not in phones or '@context' not in phone else  None for phone in phones_match]
        return phones

    def general_search(self,soup):
        print(44) 
        phones=soup.find_all(string=re.compile(self.re_phone,re.I))
        phones=[phone if phone not in phones or '@context' not in phone else  None for phone in phones]  
        return phones
        