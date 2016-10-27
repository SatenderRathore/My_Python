import requests, json, sys

API = '31672a407d0c97b66562574015d184e5'

city = sys.argv[1]
print("Please wait.... while we get u ur weather report")
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API
res = requests.get(url)
data = json.loads(res.text)
print("Temperature = " + str(round((data['main']['temp'] - 273.15), 3)))
print("Weather = " + str(data['weather'][0]['description']))
print("Humidity = " + str(data['main']['humidity']))