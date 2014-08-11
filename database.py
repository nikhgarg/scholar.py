# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 18:29:46 2014

@author: Nikhil
"""

"""
databaseFile with just article properties
 - articlenumber title, authors
graphFile file with network
articlenumber, reference1, reference2, ...

"""


import csv
from Article import Article

def LoadMapFromDatabase(databaseFileName, graphFileName):
    articleMap = {}
    #load database row by row, creating Article objects into the map
    with open(databaseFileName, 'r') as database:
        databasereader = csv.reader(database, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in databasereader:
            if row is None or len(row)<3 or len(row[0])==0:
                continue
            article = Article()
            article.identification = int(row[0])
            article.title = row[1]
            article.link = row[2]
            articleMap[article.identification] = article

    #load references
    with open(graphFileName, 'r') as graph:
        graphreader = csv.reader(graph, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in graphreader:
            if len(row) < 2:
                continue
            articleMap[int(row[0])].references = []
            for x in row[1:]:
                if len(x)>0 and int(x) in articleMap.keys():
                    articleMap[int(row[0])].references.append(articleMap[int(x)])
    #return map
    return articleMap
    
def testLoad(db, graph):
    aMap = LoadMapFromDatabase(db, graph)
    for ide in aMap:
        print aMap[ide]
    
    
#testLoad('database.csv', 'graph.csv')
###
#Add new articles to the database
###

def AppendDatabaseFromMap(articleMap, databaseFileName, graphFileName):
    with open(databaseFileName, 'a') as database:
        with open(graphFileName, 'a') as graph:
            databasewriter = csv.writer(database, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            graphwriter = csv.writer(graph, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            
            for key in articleMap:            
                article = articleMap[key]                
                databasewriter.writerow([article.identification, article.title, article.link])
                try:
                    if (article.references is not None):
                        refs = [ref.identification for ref in article.references]
                except Exception, e:
                    print article
                    print e
                graphwriter.writerow([article.identification] + refs)
            #open up file (clobber it)
            #write dictionary into the file
    return True;

###
# Add/Update articles to database - may or may not be new
###
def UpdateDatabaseFromMap(articleList, databaseFile, graphFile):
    #load database, merge it into article list
    #print the articlelist
    return True;

    