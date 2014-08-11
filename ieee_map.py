# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 23:30:19 2014

@author: Nikhil
"""

from selenium_test import GetHTMLSearchIEEEByName
from selenium_test import GetHTMLFromLink
from selenium_test import GetSearchLinkFromArticleName
from Article import Article
from Article import parseIdentificationFromLink
from database import AppendDatabaseFromMap
from database import LoadMapFromDatabase
from References import GetReferencesFromHTML
from References import GetTitleFromRef

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


global_identification_value = 0
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS()


def GetIdentificationNumber():
    global global_identification_value
    ret = global_identification_value
    global_identification_value += 1
    return ret

"""
returns list of Articles that can be recursively searched for references
this method can be recursively called with members of the array it returns
"""
def GetReferenceList(seedArticle, databaseFile = None, graphFile = None):
    global global_identification_value
    seedArticle.link = seedArticle.link.replace('articleDetails', 'abstractReferences')
    html =  GetHTMLFromLink(driver, seedArticle.link)
    references = GetReferencesFromHTML(html)
    articleList = []
    
    for ref in references:
        try :
            article = Article()
            article.title = GetTitleFromRef(ref)
            html = GetHTMLSearchIEEEByName(webdriver.Firefox(), article.title)
            article.link = GetSearchLinkFromArticleName(html, article.title)
            article.identification = parseIdentificationFromLink(article.link)
            
            
            articleList.append(article)
#            if (databaseFile is not None and graphFile is not None):
#                AppendDatabaseFromMap([article], databaseFile, graphFile)
            print article.identification
            print article.title
            print "\n"
        except :
            continue

    return articleList

def StartFromSeed(seedLink, seedTitle):  
    SeedArticle = Article()
    SeedArticle.link = seedLink
    SeedArticle.title = seedTitle
    SeedArticle.identification = parseIdentificationFromLink(SeedArticle.link)
    
    databasefile = "database.csv"
    graphfile = "graph.csv"
    
    SeedArticle.references = GetReferenceList(SeedArticle, databaseFile = databasefile, graphFile = graphfile)
    mapToInsert = {}
    mapToInsert[SeedArticle.identification] = SeedArticle
    for art in SeedArticle.references:
        mapToInsert[art.identification] = art
        
    AppendDatabaseFromMap(mapToInsert, databasefile, graphfile)

    print 'done'
    
def StartFromDatabaseAndGraph(databaseFileOrig, graphFileOrig, databaseFileNew, graphFileNew):
    articlesDict = LoadMapFromDatabase(databaseFileOrig, graphFileOrig)        #load into a dictonary <id: Article>
    articlesDictAdded = {}
    #for each Article in which len(references) == 0 
        #Get references as above, update article, add refrences to the map
    for idNum in articlesDict:
        try:
            article = articlesDict[idNum]
            if len(article.references) == 0:     
                article.references = GetReferenceList(article)
                try:
                    for art in article.references:
                        if not articlesDict.has_key(art.identification):
                            articlesDictAdded[art.identification] = art
                except Exception, e:
                    print "\tarticle failed : " + str(art)
                    print e
                print str(idNum) + ' succeeded: refs' + str(len(article.references))
            else:
                print str(idNum) + ' skipping: already has references'
        except Exception, e:
            print str(idNum) + ' failed'
            print e
            
    articlesDict.update(articlesDictAdded)
    AppendDatabaseFromMap(articlesDict, databaseFileNew, graphFileNew)   
    print 'done'


