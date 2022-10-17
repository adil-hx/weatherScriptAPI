import requests
import os
from datetime import datetime

user_api = "214267fce1b044ab00f043a929accbb0"
location = input("Enter city name, followed with the Country Code:")


complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link_key_1 = "https://api.openweathermap.org/data/2.5/weather?q="+location+location+"&appid="+user_api
api_link = requests.get(api_link_key_1)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
# date_time = int(date_time.strftime("%d %b %Y | %I:%M:%S %p"))
# time = api_data['timezone']
# if time < 0:
#     time+-date_time
# else:
#     time-=date_time

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
#print ("Time zone             :",datetime.fromtimestamp(time).strftime('%Y%m%d'))