#!/usr/bin/env python3

import datetime as dt
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

INFILE = "./what-is-happening.html"
OUTFILE = "./rss.xml"

rss_items = []

rss_doc = ET.Element('rss', {'version': '2.0'})
rss_channel = ET.SubElement(rss_doc, 'channel')

channel_title = ET.SubElement(rss_channel, 'title')
channel_title.text = "Border Aid News Updates"

channel_link = ET.SubElement(rss_channel, "link")
channel_link.text = "https://borderaidsandiego.org"

channel_description = ET.SubElement(rss_channel, "description")
channel_description.text = "Journalistic media curated by border aid volunteers, examining the situation on the ground at San Diego open air detention sites"

channel_build_date = ET.SubElement(rss_channel, 'lastBuildDate')
channel_build_date.text = dt.datetime.now().strftime('%a %d %b %Y, %I:%M%p')

with open(INFILE) as inf:
    soup = BeautifulSoup(inf, 'html.parser')

    article_items = soup.select('#articles li')

    article_links = soup.select("#articles li a")
    
    for a in article_links:
        link = a.attrs['href']
        article_title = a.text

    for i in range(len(article_items)):
        item = article_items.__getitem__(i).text
        
        link_item = article_links.__getitem__(i)
        url = link_item.attrs['href']

        if "Community Corrections" in item:
            item = item.split("Community Corrections")[0].strip()
            article_title = item.split(' by ')[0].strip()

        else:
            article_title = link_item.text.strip()
        
        item = item.replace(article_title, '')
        author = item.split(' for ')[0].replace(' by ', '').strip()
        outlet = item.split(' for ')[1].split(' on ')[0].strip()
        pub_date = item.split(' on ')[1].strip()

        #month_day_year = pub_date.split(' ')
        #month = dt.datetime.strptime(month_day_year[0][:3], '%b').month
        #day = int(month_day_year[1])
        #year = int(month_day_year[2])

        # attempt to retrieve article preview data from pub page
        article_description = "No summary available"
        try:
            article_html = requests.get(url, timeout=3).content
            article_soup = BeautifulSoup(article_html, 'html.parser')

            meta_items = article_soup.find_all('meta', {"property": "og:description"})
            
            for m in meta_items:
                article_description = m.attrs['content']

        except:
            article_description = "No summary available"

        

        # build new RSS Item
        rss_item = ET.SubElement(rss_channel, 'item')

        rss_title = ET.SubElement(rss_item, 'title')
        rss_title.text = article_title

        rss_link = ET.SubElement(rss_item, 'link')
        rss_link.text = url

        rss_description = ET.SubElement(rss_item, 'description')
        rss_description.text = article_description

        rss_author = ET.SubElement(rss_item, 'author')
        rss_author.text = author

        rss_source = ET.SubElement(rss_item, 'source')
        rss_source.text = outlet
        
        rss_pubDate = ET.SubElement(rss_item, 'pubDate')
        rss_pubDate.text = pub_date

        



tree = ET.ElementTree(rss_doc)
tree.write(OUTFILE, xml_declaration=True, encoding="UTF-8")