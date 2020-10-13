from bs4 import BeautifulSoup
from urllib import request

url = "https://www.bbc.co.uk/weather/2641170"

rawWeatherData = request.urlopen(url).read().decode('utf8', errors='ignore')

weatherData = BeautifulSoup(rawWeatherData, 'html.parser')

location = [item['data-location-name'] for item in weatherData.findAll("html", attrs={"data-location-name" : True})][0]
weatherToday = weatherData.findAll("div", {"class": "wr-day__weather-type-description-container"})[0].get_text()
highTemp = weatherData.findAll("span", {"class": "wr-value--temperature--c"})[0].get_text()
lowTemp = weatherData.findAll("span", {"class": "wr-value--temperature--c"})[1].get_text()

print(f"Python here with the latest weather report for {location}, your weather today is: {weatherToday.lower()}; with a high of {highTemp} and a low of {lowTemp} have a great day")
