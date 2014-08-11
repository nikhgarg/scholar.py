# -*- coding: utf-8 -*-
"""
Created on Mon Jul 07 20:23:40 2014

@author: Nikhil
"""

import scholar2

query = scholar2.SearchScholarQuery()
query.set_phrase("what will 5g be")
query.set_author("andrews")

print query.get_url()

querier = scholar2.ScholarQuerier()
querier.send_query(query)

print querier.articles

scholar2.txt(querier)

article = querier.articles.pop()
print article
querier2 = scholar2.ScholarQuerier()
querier2.parse(querier2._get_http_response(article.__getitem__('url_citations')))

scholar2.txt(querier2)


print "finished"

#take a phrase/specific article
#(TODO) find sources cited by this article, recursively do that
#recursively (up to 10 citations per article, 100 total) find articles that cite these articles
