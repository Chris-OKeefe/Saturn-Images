#!/usr/bin/env python

#Script to extract titles and captions from Buzzfeed page with images of Saturn. 
#I want to extract them and put them in a README doc.
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("17 Incredible Pictures Of Moons And Planets Taken By The Cassini Space Probe.html"))

#Define results sets for titles and captions.
title = soup.find_all('h2', 'subbuzz_name')
caption = soup.find_all('p', 'article_caption_w_attr')

with open('README.md', 'w') as file: 
    #Write Title
    file.write('###Cassini images, titles and captions \n')
    #Additional info.
    file.write('From Buzzfeed article, https://www.buzzfeed.com/tomchivers/this-is-better-than-your-instagrammed-sunsets?utm_term=.niJm3vJW6o#.wdBQEN0p5V \n\n')
    #Write photo title and credits caption.
    for m, n in zip(title, caption): #should loop over one each
        file.write('## %s \n' % m.get_text().encode('utf-8')) 
        file.write('%s \n\n' % n.get_text().encode('utf-8')) 
