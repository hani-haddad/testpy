import re
class full_name():
    suffixes=[' I ',' II ',' III ',' IV ',' V ',' Senior ',' Junior ','Jr',' Sr ',' PhD ',' APR ',' RPh ',' PE ',' MD ',' MA ',' DMD ',' CME ']
    honerfixse=["Mr.","master","mister","Mrs.","Dr.","Rev.","Fr."]
    #search_header_tags=["h1","h2"]
    search_tags=["h1","h2"]
    search_class_names=[]
    re_name_mid="full_name"
    suffixes_string='|'.join(suffixes)
    re_compund_name= rf'({suffixes_string}){re_name_mid}' 
    

    def name_extrator(self,soup):
     if name :=self.find_title_tag(soup):
        return name

     elif name :=self.find_header_tag(soup):
        return name

     elif name :=self.find_by_class(soup):
        return name
    
     elif name :=self.find_specialCase_tag(soup):
        return name

     soup.find_all(self.search_header_tags,string=re.complie(self.re_compund_name,re.I))

    def clean_up_name(name):
        return

    def find_title_tag(self,soup):
        name_regex = re.compile(self.re_compund_name,re.I)
        title=soup.find("title",string=name_regex).text
        title_list=re.split(',|_|-|!', title)[0]
        res= [name_regex.sub('', x).strip() for x in title_list]
        return res if(len(res)>0) else  None 

    def find_header_tag(self,soup):
          name_tags=soup.find_all(self.search_tags,string=re.compile(self.re_compund_name,re.I))
          [self.search_class_names.append(tag["class"]) if tag["class"] not in self.search_class_names else  None for tag in name_tags]
          return [name.text for name in name_tags] if(len(name_tags)>0)  else  None

    def find_by_class(self,soup,tag=""):
          name_tags=soup.find_all(tag,self.search_class_names,string=re.compile(self.re_compund_name,re.I))
          [self.search_tags.append(tag.name) if tag.name not in self.search_tags else  None for tag in name_tags]
          return [name.text for name in name_tags] if(len(name_tags)>0)  else  None
        
    def find_specialCase_tag(soup):
        return
