from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
from splinter.exceptions import ElementDoesNotExist
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    #browser = init_browser()
    #Mars News
    url_mars_news = "https://mars.nasa.gov/news/"
    browser.visit(url_mars_news)
    time.sleep(5)

    response_news = browser.html
    soup_news = bs(response_news, 'html.parser')

    #get news_title and news_p
    news_result = soup_news.find('div', class_='content_title')
    news_title = news_result.find_all('a')[0].text.strip()
    news_p = soup_news.find('div', class_='rollover_description_inner').text.strip()


    #Featured image mars
    url_featured_img = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response_featured_img = requests.get(url_featured_img)
    soup_mars_featured_img = bs(response_featured_img.text, 'html.parser')
    browser.visit(url_featured_img)
    browser.click_link_by_id('full_image')
    fancybox = soup_mars_featured_img.find('a',class_='button fancybox')
    mars_featured_url = fancybox['data-fancybox-href']
    featured_image_url = "https://www.jpl.nasa.gov" + mars_featured_url



    #Get mars weather information
    url_mars_twitter = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_mars_twitter)
    response_mars_twitter = requests.get(url_mars_twitter)
    soup_twitter = bs(response_mars_twitter.text, 'html.parser')
    tweet = soup_twitter.find('div', class_='js-tweet-text-container').text.strip()
    mars_weather = tweet.split('pic')[0]
    #print(mars_weather)


    #Get mars fact table
    url_mars_facts = 'https://space-facts.com/mars/'
    browser.visit(url_mars_facts)
    mars_facts_table = pd.read_html(url_mars_facts)
    mars_facts_df = mars_facts_table[0]
    mars_facts_df.columns = ['Description', 'Values']
    mars_facts_df.set_index('Description', inplace=True)
    mars_facts_df.to_html('mars_facts_table.html')
    mars_facts = mars_facts_df.to_html()

    #Get Mars hemispheres titles
    url_mars_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_mars_facts)
    response_mars_hemi = requests.get(url_mars_hemi)
    soup_mars_hemi = bs(response_mars_hemi.text, 'html.parser')

    #Get Mars hemispheres titles
    #title = soup_mars_hemi.find('h2',class_='title')
    cereberus_title = soup_mars_hemi.find_all('h3')[0].text
    schiaparelli_title = soup_mars_hemi.find_all('h3')[1].text
    syrtis_title = soup_mars_hemi.find_all('h3')[2].text
    valles_title = soup_mars_hemi.find_all('h3')[3].text

    #Cerebrus Image URL
    url_cereberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    response_cereberus = requests.get(url_cereberus)
    soup_cereberus = bs(response_cereberus.text, 'html.parser')
    cerebrus = soup_cereberus.find_all('img',class_='wide-image')[0]
    cerebrus_img = cerebrus['src']
    cerebrus_img_url = 'https://astrogeology.usgs.gov' + cerebrus_img

    #Schiaparelli Image URL
    url_schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    response_schiaparelli = requests.get(url_schiaparelli)
    soup_schiaparelli = bs(response_schiaparelli.text, 'html.parser')
    schiaparelli = soup_schiaparelli.find_all('img',class_='wide-image')[0]
    schiaparelli_img = schiaparelli['src']
    schiaparelli_img_url = 'https://astrogeology.usgs.gov' + schiaparelli_img

    #Syrtis Image URL
    url_syrtis = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    response_syrtis = requests.get(url_syrtis)
    soup_syrtis = bs(response_syrtis.text, 'html.parser')
    syrtis = soup_syrtis.find_all('img',class_='wide-image')[0]
    syrtis_img = syrtis['src']
    syrtis_img_url = 'https://astrogeology.usgs.gov' + syrtis_img

    #Valles Image URL
    url_valles = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    response_valles = requests.get(url_valles)
    soup_valles = bs(response_valles.text, 'html.parser')
    valles = soup_valles.find_all('img',class_='wide-image')[0]
    valles_img = valles['src']
    valles_img_url = 'https://astrogeology.usgs.gov' + valles_img


    hemisphere_image_urls = [
        {"title": cereberus_title, "img_url": cerebrus_img_url},
        {"title": schiaparelli_title, "img_url": schiaparelli_img_url},
        {"title": syrtis_title, "img_url": syrtis_img_url},
        {"title": valles_title, "img_url": valles_img_url},
    ]

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "mars_weather": mars_weather,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls,
        "cereberus_title": cereberus_title,
        "cerebrus_img_url": cerebrus_img_url,
        "schiaparelli_title": schiaparelli_title,
        "schiaparelli_img_url": schiaparelli_img_url,
        "syrtis_title": syrtis_title,
        "syrtis_img_url": syrtis_img_url,
        "valles_title": valles_title,
        "valles_img_url": valles_img_url
    }
    browser.quit()
    return mars_data