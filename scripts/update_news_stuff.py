#!/usr/bin/env python3

import datetime as dt
import requests
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ARTICLES_JSON = "../news-articles.json"
WHATHAPPEN_HTML = "../what-is-happening.html"
RSS_FILE = "../rss.xml"

COMMUNITY_CORRECTIONS_DIR = "../community-corrections/"


def create_articles_html(article_data):
    with open(WHATHAPPEN_HTML, "r") as outf:
        soup = BeautifulSoup(outf, 'html.parser')

        articles_html_sxn = soup.select("article#oads-text-articles")
        articles_html_sxn.clear()

        articles_header = soup.new_tag("h3")
        articles_header.string = "Articles"
        articles_html_sxn.append(articles_header)

        articles_list = soup.new_tag("ul")
        articles_list['id'] = "articles"

        for article_obj in article_data['textArticles']:
            article_list_item = soup.new_tag("li")
            article_list_item['class'] = "oads-article"

            if article_obj['communityCorrections'] is None:
                title_link = soup.new_tag("a")
                title_link['target'] = "_blank"
                title_link.string = article_obj['title']
                title_link['href'] = article_obj['url']

                remaining_metadata_str = " by " + article_obj['author'] + " for " + article_obj['outlet'] + " on " + article_obj['pubDate']

                article_list_item.append(title_link)
                article_list_item.append(remaining_metadata_str)

            else:
                article_summary = soup.new_tag("summary")
                summary_str = "\"" + article_obj['title'] + "\" by " + article_obj['author'] + " for " + article_obj['outlet'] + " on " + article_obj['pubDate']
                article_summary.string = summary_str

                corrections_note = soup.new_tag("b")
                corrections_note.string = "Community Corrections"

                article_link = soup.new_tag("a")
                article_link['target'] = "_blank"
                article_link.string = "Read the article"
                article_link['href'] = article_obj['url']

                article_details = soup.new_tag("details")
                article_details.append(article_summary)
                article_details.append(corrections_note)
                
                corrections_file = COMMUNITY_CORRECTIONS_DIR + article_obj['communityCorrections'] + ".html"
                with open(corrections_file, 'r') as f:
                    corrections_soup = BeautifulSoup(f, 'html.parser')
                    article_details.append(corrections_soup)

                article_details.append(article_link)

                article_list_item.append(article_details)

            articles_list.append(article_list_item)

        articles_html_sxn.append(articles_list)

    with open(WHATHAPPEN_HTML, "w") as html_outf:
        html_outf.write(soup.prettify())        



def add_articles_to_rss(rss_channel, article_data):

    for article_obj in article_data['textArticles']:

        article_title = article_obj['title']
        author = article_obj['author']
        outlet = article_obj['outlet']
        pub_date = article_obj['pubDate']
        url = article_obj['url']

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
            elif "CNN" in outlet:
                source_rss = "http://rss.cnn.com/rss/edition.rss"

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




def generate_rss(article_data):
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


    add_articles_to_rss(rss_channel, article_data)
    #add_videos_to_rss(rss_channel)

    tree = ET.ElementTree(rss_doc)
    tree.write(RSS_FILE, xml_declaration=True, encoding="UTF-8")



with open(ARTICLES_JSON, "r") as inf:
    article_data = json.load(inf)
    create_articles_html(article_data)
    generate_rss(article_data)

