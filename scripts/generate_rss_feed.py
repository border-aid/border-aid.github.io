#!/usr/bin/env python3

import datetime as dt
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

INFILE = "../what-is-happening.html"
OUTFILE = "../rss.xml"



def add_articles_to_rss(rss_channel):
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

        
            
            try:
                # this could be automated with BS4 searching for <link type="application/rss+xml" href="..."> items on the site home, but BS4 isn't finding the links for some reason
                outlet_home_html = requests.get(urlparse(url).netloc, timeout=3).content
                outlet_soup = BeautifulSoup(outlet_home_html, 'html.parser')

                rss_link_items = outlet_soup.find_all('link')

                #rss_link = rss_link_items.pop()

                for r in rss_link_items:
                    print(r)
                    if r.attrs['type'] == "application/rss+xml":
                        source_rss = r.attrs['href']
            except:
                # check if publisher fits list of known RSS feeds so we can include the RSS URL in our new item
                source_rss = ""
            
                if "San Diego Union-Tribune" in outlet:
                    source_rss = "https://www.sandiegouniontribune.com/index.rss"
                elif "Left Coast Right Watch" in outlet:
                    source_rss = "https://leftcoastrightwatch.org/index.xml"
                elif "CalMatters" in outlet:
                    source_rss = "https://calmatters.org/feed/"
                elif "KPBS" in outlet:
                    source_rss = "https://www.kpbs.org/index.rss"
                elif "San Diego Magazine" in outlet:
                    source_rss = "https://sandiegomagazine.com/feed/"
                elif "ABC 10 News" in outlet:
                    source_rss = "https://www.10news.com/index.rss"
                elif "Telemundo 20" in outlet:
                    source_rss = "https://www.telemundo20.com/?rss=y"
                elif "LA Times" in outlet:
                    source_rss = "https://www.latimes.com/index.rss"
                elif "Border Report" in outlet:
                    source_rss = "https://www.borderreport.com/feed/"
                elif "Scripps News" in outlet:
                    source_rss = "https://scrippsnews.com/feedrss/rss/100/"
                elif "France 24" in outlet:
                    source_rss = "https://www.france24.com/en/rss"
                elif "Capital & Main" in outlet:
                    source_rss = "https://capitalandmain.com/feed"
                elif "NBC 7 San Diego" in outlet:
                    source_rss = "https://www.nbcsandiego.com/?rss=y"
                elif "Hispanic LA" in outlet:
                    source_rss = "https://hispanicla.com/feed"


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

            rss_source = ET.SubElement(rss_item, 'source', {'url' : source_rss})
            rss_source.text = outlet
        
            rss_pubDate = ET.SubElement(rss_item, 'pubDate')
            rss_pubDate.text = pub_date



def add_videos_to_rss(rss_channel):
    with open(INFILE) as inf:
        soup = BeautifulSoup(inf, 'html.parser')

        video_items = soup.select('#youtube-gallery .grid-item')
    
        for v in video_items:
            
            vid_title = v.h4.text
            print(vid_title)
            vid_embed = v.iframe
            link = vid_embed.attrs['src']
            print(vid_embed)

            pub_details = v.contents[2].text

            pub_date = pub_details.split(" by ")[0].replace("Published ", "").strip()
            print(pub_date)
            #link = a.attrs['href']
            #article_title = a.text



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


add_articles_to_rss(rss_channel)
#add_videos_to_rss(rss_channel)

tree = ET.ElementTree(rss_doc)
tree.write(OUTFILE, xml_declaration=True, encoding="UTF-8")