import re
import itertools
class FullName():
    def __init__(self):
        pass

    suffixes=['I','II','III','IV','V','Senior','Junior','Jr','Sr','PhD','Ph.D.','Ph. D.','Ph. D ', 'APR','RPh','PE','MD','MA','DMD','CME']
    honer_suffixes=["Mr","master","mister","Mrs","Dr","Rev","Fr","miss","ms"]

    search_tags=["h1","h2","h3","h4","h5","h6"]
    search_class_names=['atty-name']
    re_full_name="([a-zA-Z'?-?,?.?]*\s[a-zA-Z'?-?,?.?]*\s?[a-zA-Z'?-?,?.?]*\s?([a-zA-Z'?-?,?.?]*)?)"
    suffixes_string='|'.join(suffixes)
    honer_suffixes_string='|'.join(honer_suffixes)

    re_compund_name= rf'^({honer_suffixes_string}\.?\s?|\s?\.?)?{re_full_name}({suffixes_string}\.?\s?|\s?\.?)?' 
    
    def name_extrator(self,soup):
     if name :=self.find_title_tag(soup):
        return name

     elif name :=self.find_header_tag(soup):
        return name

     elif name :=self.find_by_class(soup):
        return name
    
     elif name :=self.find_specialCase_tag(soup):
        return name

    def clean_up_name(self,name):
        return name

    def find_title_tag(self,soup):
         print(1)
         name_regex = re.compile(self.re_compund_name,re.I)
         title=soup.find("title",string=name_regex).text
         title_list=re.split(',|_|-|!', title)
         #res= [name_regex.search(x).group(0) for x in title_list] #return only matched strings 
         return title_list[0]

    def find_header_tag(self,soup):
         print(2)
         name_tags=soup.find_all(self.search_tags,string=re.compile(self.re_compund_name,re.I))
         [self.search_class_names.append(tag["class"]) if tag["class"] not in self.search_class_names else  None for tag in name_tags]
         names=[name.text for name in name_tags] if(len(name_tags)>0)  else  None
         return names[0]

    def find_by_class(self,soup,tag=""):
         print(3)
         self.search_class_names=list(itertools.chain.from_iterable([class_.split(" ") for class_ in self.search_class_names]))
         if found_tags := soup.find_all(class_=self.search_class_names):
          for target_tag in found_tags:
            name_tags = target_tag.find_all(tag,string=re.compile(self.re_compund_name,re.I))
            #name_tags=soup.find_all(tag,self.search_class_names,string=re.compile(self.re_compund_name,re.I))
          [self.search_tags.append(tag.name) if tag.name not in self.search_tags else  None for tag in found_tags]
          names=[name.text for name in name_tags] if(len(name_tags)>0)  else  None
          return names[0]
        
    def find_specialCase_tag(self,soup):
        print(4)
        return
