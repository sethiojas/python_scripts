#!/usr/bin/python3

#use ./news.py <search bar contents>
#Displays the first 5 results from google news in seperate tabs
#of browser.
#If no search keyword is entered then first 5 news from
#home page are displayed

import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
import webbrowser

BASE_URL = 'https://news.google.com'

if len(sys.argv) > 1:					#if search term is passed then generate query string
	append_url_temp = sys.argv[1:]						
	append_url_temp = '+'.join(append_url_temp)
	append_url = '/search?q=' + ''.join(append_url_temp)
	new_url = BASE_URL + append_url
else:									#if search term is not passed scrape base url
	new_url = BASE_URL

response = requests.get(new_url)
page = BeautifulSoup(response.text,'html.parser')


#showed first news two times (why?)
#news = page.findAll('div', {'class':['NiLAwe', 'y6IFtc', 'R7GTQ', 'keNKEd', 'j7vNaf', 'nID9nc']})


news = page.findAll('div', {'class':'NiLAwe'})

news_count = 0	#track news
for headline in news:
	news_link_temp_rel = headline.find('a')['href'] #scrape link: eg- ./redirection_to_news_on_other_site
	news_link_temp = news_link_temp_rel[1:]# to remove the period('.') from the start
	news_link = BASE_URL + news_link_temp # append relatve url to base url
	
	webbrowser.open(news_link)	#open link
	
	news_count += 1 #increase the news count
	if news_count >= 5:
		break #exit when 5 news are scraped
	
	sleep(2) #give some time to browser
