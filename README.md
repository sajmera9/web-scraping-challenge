# Web Scraping Challenge - Mission to Mars

### Background - Web Scraping Challenge

In this challenge, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. In the Jupyter notebook, `mission_to_mars.ipynb`, I completed initial scraping using BeautifulSoup, Pandas, and Requests/Selenium. 

### Step 1 - Scraping

Furthermore, I scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text using BeautifulSoup. I scraped the featured image from [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) using Selenium and BeautifulSoup. I scraped the latest tweet and latest Mars weather report from the [Mars Weather Twitter](https://twitter.com/marswxreport?lang=en) using BeautifulSoup and Requests. Additionally, I scraped a table containing facts about the Diameter, Mass etc. from the [Mars Facts webpage](https://space-facts.com/mars/). Lastly, I scraped high resolution Mars' Hemispheres images from the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).


## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
