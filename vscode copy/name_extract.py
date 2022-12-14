import re
class FullName():
    def __init__(self):
        pass

    suffixes=['I\.?\s?','II\.?\s?','III\.?\s?','IV\.?\s?','V\.?\s?','Senior\.?\s?','Junior\.?\s?','Jr\.?\s?','Sr\.?\s?','Ph\.?\s?D\.?', 'APR\.?\s?','RPh\.?\s?','PE\.?\s?','MD\.?\s?','MA\.?\s?','DMD\.?\s?','CME\.?\s?']
    honer_suffixes=["Mr\.?\s?","master\.?\s?","mister\.?\s?","Mrs\.?\s?","Dr\.?\s?","Rev\.?\s?","Fr\.?\s?","miss","ms\.?\s?"]
    #search_header_tags=["h1","h2"]
    search_tags=["h1","h2","h3","h4","h5","h6"]
    search_class_names=['name_att']
    re_full_name="([a-zA-Z'?-?,?.?]*\s[a-zA-Z'?-?,?.?]*\s?[a-zA-Z'?-?,?.?]*\s?([a-zA-Z'?-?,?.?]*)?)"
    suffixes_string='|'.join(suffixes)
    honer_suffixes_string='|'.join(honer_suffixes)

    re_compund_name= rf'^({honer_suffixes_string})?{re_full_name}({suffixes_string}\.?\s?)?' 
    
    def name_extrator(self, soup):
        if name := self.find_title_tag(soup):
            return name
        elif name := self.find_header_tag(soup):
            return name
        elif name := self.find_by_class(soup):
            return name
        elif name := self.find_specialCase_tag(soup):
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
        return [name.text for name in name_tags] if(len(name_tags)>0)  else  None

    def find_by_class(self,soup,tag=""):
        print(3) 
        if found_tags := soup.find_all(tag,{'class':self.search_class_names,'string':}):
            for target_tag in found_tags:
                name_tags = target_tag.find_all(' ',string=re.compile(self.re_compund_name,re.I))
        # name_tags=soup.find_all(tag,self.search_class_names,string=re.compile(self.re_compund_name,re.I))
        [self.search_tags.append(tag.name) if tag.name not in self.search_tags else  None for tag in name_tags]
        return [name.text for name in name_tags] if(len(name_tags)>0)  else  None
        
    def find_specialCase_tag(soup):
        print(4)
        return
