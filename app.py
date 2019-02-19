import scrape_mars
import pymongo

from flask import Flask, render_template, jsonify, redirect

## get scrape info and add it to mongo
dict_mars_info = scrape_mars.scrape()
print(dict_mars_info)
#jsonify(dict_mars_info)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client["marsDB"]
### Insert one if not exist before webpage starts
dict_mars_info = scrape_mars.scrape()
collection = db["mars_info"]
#collection.insert_one(dict_mars_info)
collection.update({}, dict_mars_info, upsert=True)



app = Flask(__name__)



@app.route('/')
def index():
    # Store the entire team collection in a list
    # mars_info = "getting mars infor"
    mars_info = db["mars_info"].find_one()
    fact_table = mars_info["mars_fact_html"]
 
    #print(mars_info)
    # Return the template with the teams list passed in
    if (mars_info):
        return render_template('index.html', mars_info=mars_info, fact_table=fact_table )
    else:
        redirect("/getData", code=302)


@app.route("/getData")
def insert_mars_info():
    #calling scrape function to get data in dictionary
    dict_mars_info = scrape_mars.scrape()
    #print(dict_mars_info)

    collection = db["mars_info"]
    #collection.insert_one(dict_mars_info)
    collection.update({}, dict_mars_info, upsert=True)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)    