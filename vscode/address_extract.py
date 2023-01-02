import re
import itertools 
import os
from serpapi import GoogleSearch

class Address:
    re_postel_code ='\s\d{5}'
    re_region = ',?\s([A-Z][A-Z]|[A-Z]\w+(\s[A-Z]\w+)?)'
    re_locality='[A-Z]\w+(\s[A-Z]\w+)?,'
    re_streetAddress='(^\d{3,4})?[a-z]*\s?([A-Z]\w+)?(\s[A-Z]\w+)?\s?#?(\d{3,4})?'
    ['street','street_1','state_1','zip_1']
    re_adr_name= rf'({re_streetAddress})?,?\s({re_locality})?\s?({re_region})?,?\s({re_postel_code})?\s?' 
    search_tags=[]
    search_phrases_address=["addr","home"]

    def address_extrator(self,soup):
     if address :=self.find_by_class_name(soup):
        return address
    
     elif address :=self.find_in_script_tag(soup):
        return address
      
     elif address :=self.google_map_search(soup):
        return address

    def clean_up_address(self,address):
      return address

    def find_class(self,soup):
      search_class_address=[]
      for element in soup.find_all(class_=True):
          #print(element["class"])
          search_class_address.extend(element["class"]) 
      for phrase in self.search_phrases_address:
        r = re.compile(phrase)
        search_class_address = list(filter(r.search, self.search_class_address)) 
      return search_class_address

    def find_by_class_name(self,soup,tag=""):
      print(3)
      self.search_class_names=list(itertools.chain.from_iterable([class_.split(" ") for class_ in self.find_class(soup)]))
      if found_tags := soup.find_all(class_=self.search_class_names):
       for target_tag in found_tags:
         name_tags = target_tag.find_all(tag,string=re.compile(self.re_adr_name,re.I))
       [self.search_tags.append(tag.name) if tag.name not in self.search_tags else  None for tag in found_tags]
       names=[name.text for name in name_tags] if(len(name_tags)>0)  else  None
       return names[0]

    def find_in_script_tag(soup):
      scripts=soup.find_all("script")
      for script in scripts:
        if '@context' in script.text :
          #print(re.findall('Address',script.text,re.I))
            try: 
             script_data=eval(script.text) 
            except: continue 
            if type(script_data)== list:
             for i in script_data:
              mydict1=dict(i)
              for x, y in mydict1.items():
                if re.compile("address", re.IGNORECASE).search(x):
                      print(x,"=>",y)
                if type(y)==dict:
                  for x1, y1 in y.items():
                    if re.compile("address", re.IGNORECASE).search(x1):
                      print(x1,"=>",y1)
            else:
                for x, y in script_data.items():
                 if re.compile("address", re.IGNORECASE).search(x):
                      print(x,"=>",y)
                 if type(y)==dict:
                  for x1, y1 in y.items():
                    if re.compile("address", re.IGNORECASE).search(x1):
                      print(x1,"=>",y1)
        elif re.compile("(var\s)(street|state|zip|postal_code)", re.IGNORECASE).search(script.text):
            print(script)

    def find_in_address_tag (self,soup):
        try:
          if re.compile(self.re_adr_name, re.IGNORECASE).match(soup.find('address').text):
           address=soup.find('address').text 
          return address
        except: pass

    
    def google_map_search(self):
        params = {
            "engine": "google_maps",
            "q": "S J Harris Law",
            "type": "search",
          
            "api_key": '1d97aabdc07c5ca86da7698cb7f5b750ed1c0ffa7dae05a044c5f8f350e203ab'
        }
        client = GoogleSearch(params)
        data = client.get_dict()

        print(data)

        for x, y in data.items():
          if re.compile("address", re.IGNORECASE).search(str(y)):
            for x1, y1 in data[x].items():
              print(x1,": ",y1)