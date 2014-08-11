# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 21:24:48 2014

@author: Nikhil
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import re


def GetHTMLFromLink(driver, link):
   
    # go to the google home page
    driver.get(link)
    
    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element(by = By.ID, value = "abstractReferences")
    html =  inputElement.get_attribute("innerHTML")
    driver.close()

    return html

    #print inputElement.get_attribute("outerHTML")
    
#    inputClasses = driver.find_elements(By.CLASS_NAME, "docs")
#    
#    
#    
#    parser = HTMLParser()
#    
#    for elem in inputClasses:
#        html =  elem.get_attribute("innerHTML")
#        print html
#        parsed_html = BeautifulSoup(html)
#        print len(parsed_html.contents)
#        print parsed_html.contents.pop()
#        print parsed_html.body.find('div', attrs={'class':'container'}).text
#        
#        parser.feed(html)
    
def GetHTMLSearchIEEEByName(driver, name):
    #TODO
    #insert some sort of checking for wrong results
    if name is None:
        return None
    link = "http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText="
    link = link+name
    driver.get(link)
    inputElement = driver.find_element(by = By.CLASS_NAME, value = "Results")
    html = inputElement.get_attribute("innerHTML")
    driver.close()
    return html

def GetSearchLinkFromArticleName(html, name):
    soup = BeautifulSoup(html)
    results = soup.find_all("div", "detail")
    #print results
    if (len(results)>0):
        #print results[0]
        soup2 = BeautifulSoup(str(results[0]))
        links = soup2.find_all("a", limit=1)
        quoted = re.compile('"[^"]*"')
        quotes = quoted.findall(str(links[0]))
        return "http://ieeexplore.ieee.org/"+str(quotes[0].replace('amp;',''))[1:-1]

def test():
    driver = webdriver.PhantomJS()
    #driver = webdriver.Firefox()
    html = GetHTMLSearchIEEEByName(driver, "4-the Generation Wireless Infrastructures: Scenarios and Research Challenges")
    print html


