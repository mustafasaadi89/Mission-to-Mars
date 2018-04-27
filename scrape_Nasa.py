#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time

def scrape():
    #define where to look for chromedriver
    executable_path={"executable_path":'chromedriver.exe'}
    browser = Browser('chrome',**executable_path, headless=False)

    data = {}

    url= 'https://mars.nasa.gov/news/?page=1&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    
    browser.visit(url)
    time.sleep(2)

    html=browser.html

    text_soup = BeautifulSoup('html.parser')
    elem = text_soup.find(class_='grid_layout')
    title=elem.find('div',class_='content_title')
    text=elem.find('div',class_='article_teaser_body')

    time.sleep(2)

    data['title_text']=title
    data['article_text']=text

scrape()
print(data)



