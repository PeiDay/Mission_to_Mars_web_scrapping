# Mission to Mars
![mission_to_mars](https://github.com/PeiDay/Web-Scraping-Challenge/blob/main/image/mission_to_mars.png)

## Background
We are building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps taken:

### 1. Scraping
### 2. MongoDB and Flask Application

## Scraping
Initial scraping of the following websites was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter:

* NASA Mars News - the [Mars News Site](https://redplanetscience.com/) and collect the latest **News Title** and **Paragraph Text**.

* JPL Mars Space Images Featured Image - the Featured Space Image site [here](https://spaceimages-mars.com)

* Mars Facts - the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing **facts** about the planet including Diameter, Mass, etc.

* Mars Hemispheres - the astrogeology site [here](https://marshemispheres.com/) to obtain **high resolution images** for each of Mar's hemispheres.

## MongoDB and Flask Application
MongoDB with Flask templating was used to create a new HTML page that displays all of the information that was scraped from the URLs above. The following tasks were completed:

* The Jupyter notebook was converted into a Python script called 'scrape_mars.py' with a function called scrape that executes all of the scraping code from above and returns one Python dictionary containing all of the scraped data called `scraped_mars`.

* A **root route /** was created, that opens a cover page with a button to begin the initial scraping (index.html).

* A route called **/scrape** was created, that imports the `scrape_mars.py` script and calls the `.scrape()` function. This returns a Python dictionary that is stored in Mongo. 

* After scraping is complete, the **/scrape route** redirects to the **/mission** route to display the results.

* The **/mission** route queries the Mongo database and passes the Mars data into an HTML template for display (mission.html).

## Images of Mission to Mars

* Home page ('/) 
Bootstrap CSS(`cover.css`) was used to style an initial landing page with a single button to begin scraping data by calling the **/scrape route**.

![index_cover](https://github.com/PeiDay/Web-Scraping-Challenge/blob/main/image/index_cover.png)

* Results page ('/mission')
The **/scrape route** redirects to a **/mission route** that renders a second html template, created to display the scraped results using Bootstrap and custom CSS(`style.css`). This page also has a 'New Data' button that calls the **/scrape route** again to refresh the data.

![info_mission_1](https://github.com/PeiDay/Web-Scraping-Challenge/blob/main/image/info_mission_1.png)
![info_mission_2](https://github.com/PeiDay/Web-Scraping-Challenge/blob/main/image/info_mission_2.png)

