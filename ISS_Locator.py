
import json
import turtle
import urllib.request
import time

def makeRequest(url):
	return urllib.request.urlopen(url)

def getJSONData(response):
	return json.loads(response.read())

def printAstroData(result):
	num_on_iss = result['number']
	people_on_iss = result['people']
	print("\nThere are currently " + str(num_on_iss) + " occupants on the ISS.")
	print("\nCurrent Occupants: ")
	for person in people_on_iss:
		print(person['name'])

def printISSLocationData(result):
	location = result['iss_position']
	lat = location['latitude']
	lon = location['longitude']
	print("\nCurrent location of the ISS: Lat: " + lat + ", Lon: " + lon)
	displayISS(lat, lon)

def displayISS(lat, lon):
	# Initialize the screen and assets
	screen = turtle.Screen()
	screen.title("International Space Station Locator")
	screen.setup(720, 360)
	screen.setworldcoordinates(-180, -90, 180, 90)
	screen.bgpic('map.gif')
	screen.register_shape('iss2.gif')


	# Displays current ISS Position
	iss = turtle.Turtle()
	iss.shape('iss2.gif')
	iss.setheading(90)
	iss.penup()
	iss.goto(float(lon), float(lat))

def drawPingedPassOverData(lat, lon):
	# Sets location to ping for following request.
	style = ('Helvetica Neue', 16)
	location = turtle.Turtle()
	location.penup()
	location.color('yellow')
	location.goto(float(lon), float(lat))
	location.dot(10)
	location.hideturtle()

	# New Request - Finds timestamp when ISS passes over new location
	url = 'http://api.open-notify.org/iss-pass.json' + '?lat=' + str(lat) + '&lon=' + str(lon)
	response = makeRequest(url)
	result = getJSONData(response)
	pass_over = result['response'][1]['risetime']

	location.write(time.ctime(pass_over), font=style)

def main():
	# Gets the information of who is on the ISS
	response = makeRequest('http://api.open-notify.org/astros.json')
	result = getJSONData(response)
	printAstroData(result)

	# Gets the current location of the ISS 
	response = makeRequest('http://api.open-notify.org/iss-now.json')
	result = getJSONData(response)
	printISSLocationData(result)

	# Los Angeles
	lat = 34.052235
	lon = -118.243683

	# Insert get lat and lon coordinates method
	drawPingedPassOverData(lat, lon)

	turtle.done()


if __name__ == "__main__":
	main()


