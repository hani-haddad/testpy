import re 

class Email:
    re_email ="([\d\w\.]+@[\d\w\.\-]+(\.\w{1,2})?\.[a-zA-Z][^\.]{1,2})"
    #search_tags=["h1","h2","h3","h4","h5","h6"]
    search_phrases_email=['tel','phone','call','contact','contacts','contact us']

    def __init__(self):
        pass

    def email_extrator(self,soup):
        if phones :=self.find_in_a_tag(soup):
            return phones

        elif phones :=self.find_by_email_phrases(soup):
            return phones
        
        elif phones :=self.general_search(soup):
            return phones
    
    def clean_up_email(self,email):
        return email
    
    def find_in_a_tag(self,soup):
        emails=soup.find_all('a',href=re.compile('^mailto:'+self.re_email))
        emails=[email.text if '@context' not in email else  None for email in emails]
        return emails

    def find_by_email_phrases(self,soup,tag=""):
        print(33) 
        for phrase in self.search_phrases_email:
           contacts = soup.find_all(tag="",text=re.compile(phrase,re.I))
           for tag in contacts:
                if tag.name == 'script':
                    continue
                emails_match_tag=soup.find_all(tag.name,text=re.compile(self.re_email,re.I))
                emails1=[email if email not in emails1 or '@context' not in email else  None for email in emails_match_tag]
                for iterator in range(0,5):
                    tag=tag.next_element
                    emails_match_after_tag=soup.find_all(tag.name,text=re.compile(self.re_email,re.I))
                    emails2=[email.text if email not in emails2 or '@context' not in email else  None for email in emails_match_after_tag]
                emails=emails1+emails2        
        return emails
    
    def general_search(self,soup):
        print(44) 
        emails=soup.find_all(string=re.compile(self.re_email,re.I))
        emails=[email if email not in emails or '@context' not in email else  None for email in emails]  
        return emails

