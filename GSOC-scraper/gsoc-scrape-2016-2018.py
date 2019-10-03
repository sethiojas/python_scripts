from bs4 import BeautifulSoup
import requests
from csv import writer
from tqdm import tqdm
from time import sleep
from os import system
LINK = "https://summerofcode.withgoogle.com/archive/" #link to gsoc archives

#base url of gsoc. It will be used to surf relative links which are gathered
base_url = "https://summerofcode.withgoogle.com"

response = requests.get(LINK)
page = BeautifulSoup(response.text, 'html.parser')

gsoc_list = page.findAll('section')[1]
gsoc = gsoc_list.findAll('md-card-content')

#discard the last element which has links to gsoc
#links from before 2016
gsoc = gsoc[:-1:]

#get links to GSOC webpages (year 2016-2018)
abs_link = []
for year in gsoc:
	#extract relative link to gsoc web pages for years 2018-2016.
	#add relative url to base url and append them to absolute link list
	#so that it can be visited.
	rel_link = year.findAll('a')[1]['href']
	abs_link.append(base_url + rel_link)

#visit each link of gsoc(year 2018, 2017, 2016) webpage
print("Visiting GSOC webapages for each year (2016-2018)")
for link in tqdm(abs_link):
	response = requests.get(link)
	page = BeautifulSoup(response.text, 'html.parser')

	link = link.split('/')
	#split gives
	#['https:', '', 'summerofcode.withgoogle.com', 'archive', '2018', 'organizations', '']

	#name of file would be the third last list element
	#seperated by hyphen from the second last list element
	#for eg : 2018-organisation.csv
	#		  2017-organisations.csv
	file_name = link[-3]+'-'+link[-2]

	#write headers of csv file
	with open(f"{file_name}.csv", 'w') as file:
		organisation_writer = writer(file)
		organisation_writer.writerow(["Name","Technologies"])

	#find and get absolute url to page of each organisation
	organisation = page.findAll('a', class_="organization-card__link")
	abs_org_link = []
	for org in organisation:
		rel_org_link = org['href']
		abs_org_link.append(base_url+rel_org_link)

	#visit url of each organisation to get their name and technologies they
	#work on
	file = open(f"{file_name}.csv", 'a')
	organisation_writer = writer(file)
	print("Visiting organisation pages for year")
	for org_link in tqdm(abs_org_link):
		response = requests.get(org_link)
		page = BeautifulSoup(response.text, 'html.parser')
		org_name = page.find('h3').get_text()
		techs = page.find('ul', class_='org__tag-container').findAll('li')
		technology = []

		for tech in techs:
			technology.append(tech.get_text())

		#write the name and technologies to csv file
		organisation_writer.writerow([org_name, technology])

		sleep(1)
	system('clear')
	file.close()