from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape():
	# start the splinter browser instance
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	browser = webdriver.Chrome(options=chrome_options)
	try:
		# To get Mars' news
		browser.get('https://mars.nasa.gov/news/')
		news_title = browser.find_element_by_css_selector("div.content_title > a").text
		news_p = browser.find_element_by_css_selector("div.article_teaser_body").text
		#news_p = browser.find_element_by_class_name('article_teaser_body').text
		#soup_news=BeautifulSoup(browser.html,'lxml')
		#news_title=soup_news.find('div', class_='content_title').get_text(strip=True)
		#news_p=soup_news.find('div', class_='article_teaser_body').get_text(strip=True)

		# To get Mars' images
		image_urls = []
		browser.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
		links = [i.get_attribute('href') for i in browser.find_elements_by_css_selector('div.SearchResultCard > a')]
		for link in links:
			browser.get(link)
			image_urls.append(browser.find_element_by_css_selector("img.BaseImage.object-scale-down").get_attribute('src'))
		# soup_img = BeautifulSoup(browser.html,'lxml')
		# url_links = soup_img.findAll('div',class_='SearchResultCard')
		# image_urls = []
		# for link in url_links:
		#     url = 'https://www.jpl.nasa.gov'+ link.find('a',href=True)['href']
		#     browser.get(url)
		#     soup_img_url = BeautifulSoup(browser.html,'lxml')
		#     image_urls.append(soup_img_url.find('img',class_='BaseImage object-scale-down')['src'])


		# To get facts about Mars
		browser.get('http://space-facts.com/mars/')
		facts = [i.text for i in browser.find_element_by_tag_name('tbody').find_elements_by_class_name('column-2')]
		attrib = ['Equatorial Diameter','Polar Diameter','Mass','Moons','Orbit Distance','Orbit Period','Surface Temperature','First Record','Recorded By']
		facts_dict = dict(zip(attrib,facts))
		# soup_facts=BeautifulSoup(browser.html,'lxml')
		# table_facts= soup_facts.find('table')
		# df_facts = pd.read_html(str(table_facts))
		# df_facts_json = json.loads(df_facts[0].to_json())


		# To get hemisphere_image
		browser.get('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
		hd_img_title = [i.text for i in browser.find_elements_by_css_selector('div.description > a.itemLink.product-item')]
		hd_img_links = [i.get_attribute('href') for i in browser.find_elements_by_css_selector('div.description > a.itemLink.product-item')]
		hd_img_urls=[]
		for url in hd_img_links:
			sleep(5)
			browser.get(url)
			hd_img_urls.append(browser.find_element_by_css_selector('img.wide-image').get_attribute('src'))
		# soup_hd_img=BeautifulSoup(browser.html,'lxml')
		# hd_img_title=[]
		# hd_img_links=[]
		# for url in soup_hd_img.select('div.description > a.itemLink.product-item'):
		#     hd_img_links.append('https://astrogeology.usgs.gov'+url['href'])
		#     hd_img_title.append(url.get_text(strip=True))
		# hd_img_urls=[]
		# for url in hd_img_links:
		#     browser.get(url)
		#     time.sleep(5)
		#     soup=BeautifulSoup(browser.html,'lxml')
		#     hd_img_urls.append('https://astrogeology.usgs.gov'+soup.find('img', class_='wide-image')['src'])
		#
		key = ['title','img_url']
		hemisphere_image_urls = []
		for i in range(len(hd_img_title)):
		    value = []
		    value.append(hd_img_title[i])
		    value.append(hd_img_urls[i])
		    hemisphere_image_urls.append(dict(zip(key,value)))

		#close the browser
		browser.close()


		# prepare the dictionary of the data
		key = ['news_title','news_p','feature_img_url','df_facts','hemisphere_image_urls']
		value = ['-']*5
		value[0] = news_title
		value[1] = news_p
		value[2] = image_urls
		value[3] = facts_dict
		value[4] = hemisphere_image_urls
		dict_mars = dict(zip(key,value))
		return dict_mars
	except:
		browser.close()
