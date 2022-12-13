from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re

#["Mr.","master","mister","Mrs.","Dr.","Rev.","Fr."]

def is_suffixe(name):
  suffixes=[' I ',' II ',' III ',' IV ',' V ',' Senior ',' Junior ','Jr',' Sr ',' PhD ',' APR ',' RPh ',' PE ',' MD ',' MA ',' DMD ',' CME ']
  for suffix in suffixes:
    if suffix in name:
      return suffix

def is_compound_lname(name):
    words = ['vere','von','van','de','del','della','di','da','pietro','vanden','du','st.','st','la','ter']
    word = word.tolower()
    for word in words:
     if word in name:
      return word
    

name="Jonathan L. Kramer"
y=is_suffixe(name)
name=name.strip(y)
print(name)
def full_name_spliting(name):
  middle = re.compile('(?P<MIDDLE_NAME>[A-Z]\.\s+)', re.IGNORECASE)
  m = middle.search(name.strip())

  last = re.compile('(?P<LAST_NAME>[^\s+]+$)', re.IGNORECASE)
  m1 = last.search(name.strip())

  first = re.compile('(?P<FIRST_NAME>[A-Za-z]*\'?[A-Za-z]*\.?[A-Za-z]*\_?[A-Za-z]*\s+)', re.IGNORECASE)
  m2 = first.search(name.strip())   

  if(m != None):
    middle_name= m.group('MIDDLE_NAME')
    first = re.compile('(?P<FIRST_NAME>(?!.*A-Z\.\s+)\s+[A-Za-z]*\'?[A-Za-z]*\.?[A-Za-z]*\_?[A-Za-z]*\s+)', re.IGNORECASE)
    #first = re.compile('(?P<FIRST_NAME>[\w-]+\s', re.IGNORECASE) # if without prefixes 
    m2 = first.search(name.strip())
    first_name = m2.group('FIRST_NAME')
    print(6)
    print("f = "+first_name)

  else:
    middle = re.compile('(?P<MIDDLE_NAME>\s+.+\s+)', re.IGNORECASE)
    m = middle.search(name.strip())
    if (m != None):
      middle_name= m.group('MIDDLE_NAME')
      print("m = "+middle_name.strip(" "))
    else:
      middle_name=None

  

  if(m1 != None):
    last_name = m1.group('LAST_NAME')  
    print(1)
    print(last_name)

  if m2 != None:
    first_name = m2.group('FIRST_NAME')
    print(2)
    print(first_name)
  
  return [first_name,middle_name,last_name]
 

r=full_name_spliting(name)
if(y != None):
 r[0]=r[0]+" "+y
 print(r[0])
 print(r)