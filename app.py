
from flask import Flask, render_template
from flask import request
import os
import ilta_db
import json



app = Flask(__name__)

@app.route('/')
def index():
    
  return 'Web App Ilta with Python Flask!'

#Tämä kirjoittaa datan kantaan, kunhan kaikki asiat ovat jsonissa oikein.
#Jotain virheentarkistuksia pitää lisätä tähän
@app.route('/raw', methods= ['POST'] )
def raw():
  container=ilta_db.connect()
  data = request.json
  ilta_db.create_item(container, data)
  return "TEST: %s" % data

@app.route('/insert')
def insert():
  sensor=request.args.get('sensor')
  direction_in=request.args.get('direction_in')
  direction_out=request.args.get('direction_out')
  item_id=request.args.get('id')
  item={'id': item_id,
        'partitionKey': "sensmax-1", 
        'sensor': sensor,
        'direction_in': direction_in,
        'direction_out': direction_out}
  container=ilta_db.connect()
  ilta_db.create_item(container,item)
  return sensor

@app.route('/read')
def read():
  container=ilta_db.connect()
  data=ilta_db.read_items(container)
  return str(data)

@app.route('/test')
def test():
  return render_template('index.html')
 

if __name__ == "__main__":
  app.run()
