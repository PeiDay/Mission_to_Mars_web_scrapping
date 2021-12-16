
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)
scraped_mars = mongo.db.scraped_mars

# Route to render index.html template for initial scraping
@app.route('/')
def home():

    # Find one record of data from the mongo database
    scraped_mars = mongo.db.scraped_mars.find_one()
    # Return template and data
    return render_template("index.html", mars_info=scraped_mars)


# Route that will trigger the scrape function
@app.route('/scrape')
def scrape():

    scraped_mars = mongo.db.scraped_mars
    # Run the scrape function
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    scraped_mars.update({}, mars_data, upsert=True)
    # Redirect back to home page
    return redirect("/mission", code=302)


# Route to render data.html template using data from Mongo
@app.route('/mission')
def mission():

    # Find one record of data from the mongo database
    mars_data = mongo.db.scraped_mars.find_one()

    # Return template and data
    return render_template('mission.html', mars_info=mars_data, code=302)


if __name__ == "__main__":
    app.run(debug=True)