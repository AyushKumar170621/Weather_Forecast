import requests
import os
from dotenv import load_dotenv

load_dotenv()
mykey = os.getenv('APIKEY')
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
URL = "https://api.openweathermap.org/data/2.5/weather"
#printing whether of respective city provided by user
def get_weather(city):
    PARAMS = {'q':city,'appid':mykey}
    # sending get request and saving the response as response object
    r = requests.get(url = URL , params=PARAMS)
    # extracting data in json format
    data = r.json()
    print("City :",data['name'])
    print("Temprature :",data['main']['temp'])
    print("Min Temprature :",data['main']['temp_min'])
    print("Max Temprature :",data['main']['temp_max'])
    print("Feels Like :",data['main']['feels_like'])
    print("Pressure :",data['main']['pressure'])
    print("Humidity :",data['main']['humidity'])
    print("Clouds :",data['weather'][0]['main'])
    print("Visibility :",data['visibility'])
    print("Description:",data['weather'][0]['description'])
    print("Wind Speed :",data['wind']['speed'])
    print("Wind Degree:",data['wind']['deg'])

ipcity=input("Enter city name :")
get_weather(ipcity)