
import json
import turtle
import urllib.request
import time

#Gets the information of who is on the ISS
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)

result = json.loads(response.read())
num_on_iss = result['number']
people_on_iss = result['people']

print("\nThere are currently " + str(num_on_iss) + " occupants on the ISS.")
print("\nCurrent Occupants: ")
for person in people_on_iss:
	print(person['name'])


# Gets the current location of the ISS 
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']

print("\nCurrent location of the ISS: Lat: " + lat + ", Lon: " + lon)


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


# New York, City
lat = 34.052235
lon = -118.243683	


# Sets location to ping for following request.
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(float(lon), float(lat))
location.dot(10)
location.hideturtle()


# New Request - Finds timestamp when ISS passes over new location
url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())


# Gets time ISS passes over given Lat and Lon params
pass_over = result['response'][1]['risetime']
style = ('Helvetica Neue', 16)
location.write(time.ctime(pass_over), font=style)


turtle.done()

