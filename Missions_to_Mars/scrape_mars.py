# Import dependencies and setup
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # ======================= #
    # Scraping MARS news site #
    # ======================= #

    MarsNews_url = 'https://redplanetscience.com/'
    print("Scraping MARS News...")

    # visit the NASA MARS News
    browser.visit(MarsNews_url)
    time.sleep(1)

    news_html = browser.html
    news_soup = soup(news_html, "html.parser")

    # Retrieve the latest element that contains news title and news_paragraph
    news_title = news_soup.find('div', class_='content_title').text.strip()
    news_p = news_soup.find('div', class_='article_teaser_body').text.strip()
    print("Mars News Scraping Complete.")


    # ====================================== #
    # Scraping JPL Mars Space Featured Image #
    # ====================================== #

    # Visit the JPL Mars Space Images
    JPL_img_url = 'https://spaceimages-mars.com/'
    print("Scraping JPL Mars Space Images...")
    
    browser.visit(JPL_img_url)
    time.sleep(1)

    JPL_html = browser.html
    JPL_soup = soup(JPL_html, "html.parser")

    # Retrieve the link for image
    featured_image = JPL_soup.find('a', class_="fancybox-thumbs")
    # featured_image
    featured_img_url = JPL_img_url + featured_image['href']

    print("JPL Featured Space Image Scraping Complete.")

  
    # ==================== #
    #  Scraping Mars Facts
    # ==================== #

    # Visit the Mars facts
    facts_url = 'https://galaxyfacts-mars.com/'
    print("Scraping Mars Facts...")

    browser.visit(facts_url)
    time.sleep(1)

    facts_html = browser.html
    # fact_soup = soup(facts_html, "html.parser")

    # Retrieve the Mars facts, use pandas read as table and rename
    table = pd.read_html(facts_html)

    facts_df = table[1]
    facts_df.columns =['Description', 'Measurement']

    # convert the dataframe to a HTML table
    facts_df = facts_df.to_html(index=False, header=False, border=1)  

    print("Mars Facts Scraping Complete.")


    # ========================= #
    # Scarping Mars Hemispheres #
    # ========================= #
    
    # Visit the Mars hemisphere
    hemisphere_url = 'https://marshemispheres.com/'
    print("Scraping Mars Hemispheres...")

    browser.visit(hemisphere_url)
    time.sleep(1)

    hemisphere_html = browser.html
    hemisphere_soup = soup(hemisphere_html, "html.parser")
    divs = hemisphere_soup.find_all('div', class_='item')

    # Empty list as placeholder
    hemisphere_image_data = []

    for hemisphere in range(len(divs)):

        # --- use splinter's browser to click on each hemisphere's link in order to retrieve image data ---
        hem_link = browser.find_by_css("a.product-item h3")
        hem_link[hemisphere].click()
        time.sleep(1)
    
        # --- create a beautiful soup object with the image detail page's html ---
        img_detail_html = browser.html
        image_soup = soup(img_detail_html, 'html.parser')
    
        # --- create the base url for the fullsize image link ---
        # base_url = 'https://astrogeology.usgs.gov'
    
        # --- retrieve the full-res image url and save into a variable ---
        hem_url = image_soup.find('img', class_="wide-image")['src']
    
        # --- complete the featured image url by adding the base url ---
        img_url = hemisphere_url + hem_url

        # --- retrieve the image title using the title class and save into variable ---
        img_title = image_soup.find('h2').text
    
        # --- add the key value pairs to python dictionary and append to the list ---
        hemisphere_image_data.append({"title": img_title, "img_url": img_url})
    
        # --- go back to the main page ---
        browser.back()

    
    browser.quit()
    print("Mars Hemisphere Images Scraping Complete.")


    # =============== #
    # Store MARS data #
    # =============== #
    scraped_mars = {
        
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_img_url,
        "mars_fact_table": facts_df, 
        "hemisphere_info": hemisphere_image_data
        }

    return scraped_mars