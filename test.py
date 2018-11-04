import json
print('serialization')
myDictObj = { "type":"Feature", "properties":{"name": "Reagan","marker-color": "#0000ff" \
,"marker-symbol": "defibrillator","line": "blue"} \
, "geometry":{"type":"Point","coordinates":[-77.04404229438322,38.85341638599062]} }
##convert object to json
serilaized= json.dumps(myDictObj, sort_keys=True, indent=3)
print(str(serilaized))
## now we are gonna convert json to object
deserialization=json.loads(serilaized)
print(deserialization)

print(sum(range(101)))

"""
i=0
while i < 32:
	print("hello, this is " + str(i) +  " times")
	i+=4

def method(arr,ind):
	if ind>=len(arr)-2:
		if ind>= len(arr)-1:
			return False
		if arr[ind]*5==arr[ind+1]:
			return True
		else:
			return False
	return method(arr,ind+1)

print(method([1,1,3,5,25],30))
"""