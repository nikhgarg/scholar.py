# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 18:22:33 2014

@author: Nikhil
"""

class Article:
    title = ""
    identification = 0
    link = ""
    references = []
    citedBy = []
    
    def __str__( self ):
        buf = "ID = %d\ntitle = %s\nlink = %s\nreferences = %s\ncitedBy = %s\n\n" % (self.identification, self.title, self.link 
        , str(self.references), str(self.citedBy))
        return buf

def parseIdentificationFromLink(link):
    index = link.find("&arnumber=")
    if index < 0:
        raise Exception('First result is not article')
    query = link[index:]
    endIndex = query[1:].find("&")+1
    if endIndex < 0:
        endIndex = len(query)
    return int(query[len("&arnumber="):endIndex])
    