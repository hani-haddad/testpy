import re 

class Address:
    re_postel_code ='\s\d{5}'
    re_region = '[A-Z]{2}' #,\s[A-Z]{2}
    re_locality='[A-Z]\w+,'
    re_adr_name= rf'^({re_locality}\s?{re_region}({re_postel_code}\s?' 
    ['street','street_1','state_1','zip_1']
    
    search_phrases_address=["addr","home"]

    def find_class(self,soup):
      search_class_address=[]
      for element in soup.find_all(class_=True):
          #print(element["class"])
          search_class_address.extend(element["class"]) 
      for phrase in self.search_phrases_address:
        r = re.compile(phrase)
        search_class_address = list(filter(r.search, self.search_class_address)) # Read Note below
      return self.search_class_address


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