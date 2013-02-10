'''
Created on Feb 10, 2013

@author: Dinghua
'''
import urllib2, re
from bs4 import BeautifulSoup as bs

for i in range(1,1221):
    response = urllib2.urlopen('http://www.imdb.com/chart/top')
    html = response.read()
    soup=bs(html)