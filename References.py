# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 22:19:39 2014

@author: Nikhil
"""

from bs4 import BeautifulSoup
import re

def class_not_br(tag):
    print tag.name
    return tag.name!='br'

def GetReferencesFromHTML(html):
    soup = BeautifulSoup(html)
#    print soup.getText()
    lis = soup.find_all('li')
    references = []
    for li in lis:
        li_string = str(li)
        soup2 = BeautifulSoup(li_string)
        lis2 = soup2.find(text = True)
        references.append(str(lis2).strip())
    return references
    
def GetTitleFromRef(ref):
    quoted = re.compile('"[^"]*"')
    quotes = quoted.findall(ref)
    if (len(quotes)==1):
        return quotes[0][1:-1]
    else:
        return None

def test():
    with open('test_html') as f:
        html = ""    
        for line in f:
            html += line
        refs = GetReferencesFromHTML(html)
        #print refs
        for ref in refs:
            print GetTitleFromRef(ref)