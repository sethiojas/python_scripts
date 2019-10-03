from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import writer

BASE_URL = 'http://books.toscrape.com/'
url = BASE_URL

flag = 0 #to keep track if first page is scraped or not

#write Headers to csv file
with open("books.csv", 'w') as book_file:
	book_write = writer(book_file)
	book_write.writerow(['Name', 'Price', 'Availability','Rating (out of Five)'])

#scrape for book data
while True:
	
	print(f"Scraping.... {url}") #show url which is being scraped
	response = requests.get(url)
	html_pg = BeautifulSoup(response.text, 'html.parser')

	books = html_pg.find_all(class_= 'product_pod')

	for book in books:
		#name
		h3_header = book.find('h3')
		book_name = h3_header.findNext()['title'] #name of book
		
		#price
		book_price_temp = book.find(class_='price_color').get_text()
		book_price = book_price_temp[1:]	#remove unwanted character from start of price string

		#availability
		book_avail_temp = book.find(class_='instock availability').get_text()
		book_avail = book_avail_temp.strip() #remove unwanted newlines and white spaces
		
		#rating
		book_rating_temp = book.find('p',class_='star-rating')['class']
		book_rating = book_rating_temp[1]	# select second class from p tag where first class is star-rating
		
		#save book data
		with open("books.csv", 'a') as book_file:
			book_write = writer(book_file)
			book_write.writerow([book_name, book_price, book_avail, book_rating])

	next_pg_temp = html_pg.find('li', class_='next') #find url of next page
	
	if not next_pg_temp: #if no next page is there then end loop
		break
	
	next_pg = next_pg_temp.find('a')['href'] # relative url
	
	if flag == 1:
		url = BASE_URL + 'catalogue/' + next_pg
	else:
		url = BASE_URL + next_pg
		flag = 1 #next url on 1st page by default includes 'catalogue/',rest of the pages don't

	sleep(1) #crawl delay
print("Done")
