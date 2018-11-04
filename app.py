from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import numpy as np 
import pandas as pd 
import time
import json


app = Flask(__name__, static_url_path='')

myDictObj = { "type":"Feature", "properties":{"title": "Medical Emergency","marker-color": "#ff0000" \
,"marker-symbol": "danger","line": "red"} \
, "geometry":{"type":"Point","coordinates":[-77.04404229438322,38.85341638599062]} }

myDictObj2 = { "type":"Feature", "properties":{"title": "Medical Center","iconSize":[60,60],"description": "recommended location for a medical center", "marker-color": "#0000ff" \
,"marker-symbol": "hospital","line": "blue"} \
, "geometry":{"type":"Point","coordinates":[-77.04404229438322,38.85341638599062]} }

@app.route('/')
def root():
	return app.send_static_file('index.html')


@app.route('/submit', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		k = int(request.form['text'])
		f = request.files['file']
		f.save(secure_filename(f.filename))
		df = pd.read_csv(f.filename)

		rows = df.shape[0]
		groupsize = int(rows/k)
		currentAvgLat=0
		currentAvgLon=0
		current=0
		centersLeft=k

		g=0
		update2 = open("static/medcenters.txt","w")
		update = open("static/stations2.geojson","w")
		update.write('{\n  "type": "FeatureCollection",\n  "crs": {\n    "type": "name",\n    "properties": {\n     "name": "urn:ogc:def:crs:OGC:1.3:CRS84"')
		update.write('\n    }\n   },\n   "features": [\n    ')
		a1=0
		a2=0
		for a, b, c in zip(df.lat,df.lng,df.addr):
			myDictObj["geometry"]["coordinates"]=[b,a]
			myDictObj["properties"]["description"]=c

			currentAvgLon+=b
			currentAvgLat+=a
			current+=1
			if current == groupsize or (g==df.shape[0]-1 and centersLeft>0):
				myDictObj2["geometry"]["coordinates"]=[float(float(currentAvgLon)/float(groupsize)),float(float(currentAvgLat)/float(groupsize))]
				update2.write(str(float(float(currentAvgLon)/float(groupsize))) + " " + str(float(float(currentAvgLat)/float(groupsize))) +"\n")
				current=0
				currentAvgLat=0
				centersLeft-=1
				currentAvgLon=0
				update.write(str(json.dumps(myDictObj2, sort_keys=False, indent=3)) + (",\n" if g<df.shape[0] else "\n  ]\n}"))		

			a1+=a
			a2+=b
			g+=1
			update.write(str(json.dumps(myDictObj, sort_keys=False, indent=3)) + (",\n" if g<df.shape[0] else "\n  ]\n}"))		
		update.close()
		update2.close()
		
		return render_template('map.html',avglat=(a1/g),avglon=(a2/g))
	

if __name__ == '__main__':
	app.run(debug=True)


