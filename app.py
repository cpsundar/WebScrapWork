import scrape_mars
import pymongo

from flask import Flask, render_template, jsonify

## get scrape info and add it to mongo
dict_mars_info = scrape_mars.scrape()
print(dict_mars_info)
#jsonify(dict_mars_info)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client["marsDB"]

collection = db["mars_info"]
#collection.insert_one({"name":"create a new document"})
collection.insert_one(dict_mars_info)




app = Flask(__name__)



@app.route('/')
def index():
    # Store the entire team collection in a list
    mars_info = "getting mars infor"    

    # Return the template with the teams list passed in
    return render_template('index.html', mars_info=mars_info)


@app.route("/scrape")
def insert_mars_info():
    #calling scrape function to get data in dictionary
    dict_mars_info = scrape_mars.scrape()
    print(dict_mars_info)

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.marsDB

    collection = db.mars_info

    collection.insert_one(dict_mars_info)

if __name__ == '__main__':
    app.run(debug=True)    