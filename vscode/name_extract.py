import re
class full_name():
    suffixes=[' I ',' II ',' III ',' IV ',' V ',' Senior ',' Junior ','Jr',' Sr ',' PhD ',' APR ',' RPh ',' PE ',' MD ',' MA ',' DMD ',' CME ']
    honerfixse=["Mr.","master","mister","Mrs.","Dr.","Rev.","Fr."]
    search_header_tags=["h1","h2"]
    re_name_mid="full_name"
    suffixes_string='|'.join(suffixes)
    re_compund_name= rf'({suffixes_string}){re_name_mid}' 
    def name_extrator(soup):
     
     soup.find_all(search_header_tags,string=re.complie(re_compund_name,re.I))

    def clean_up_name(name):
        return

    def find_title_tag(soup):
        title=soup.find_all("title",string=re.complie(re_compund_name,re.I)).text
        res = re.split(', |_|-|!', data)
        return

    def find_header_tag(soup):
        return

    def find_specialCase_tag(soup):
        return

