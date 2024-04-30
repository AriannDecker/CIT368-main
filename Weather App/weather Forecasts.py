# Ariann Decker
# WeatherApp
# Build an app that will report weather forecasts given a location
# 29 December 2024
import os
import requests
import datetime as dt


# Call Weather API
base_url = "https://api.openweathermap.org/data/2.5/forecast?"
geo_url = "http://api.openweathermap.org/geo/1.0/zip?"
api_key = "6dcf727098be830db27d377532c508f2"


 # Get zipcode from user
zipcode = input("What is your zip code: " + "\n")


# Call Geo API to change zip into lat and lon coordinates
g_url = f"{geo_url}appid={api_key}&zip={zipcode},us"

r = requests.get(g_url)

if r.status_code == 200:
   # print(r.status_code)    //Print the status code to verify it is 200
   data = r.json()

# Extract the latitude and longitude
   lat = data['lat']
   lon = data['lon']

   # print(f"Latitude: {lat}, Longitude: {lon}") \\ Test to verify lat and lon are correct

else:
   print(f"Error: {r.status_code}" + "\n" + "Please try again")

# Use lat and lon to get weather forecast
url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=imperial"

res = requests.get(url)

if res.status_code == 200:
   data = res.json()
   
      #3 day forecast
   for i in range(3):
         # Date
         date_str = data['list'][i]['dt_txt']
         date = dt.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
         date = date.strftime('%m/%d/%Y')
   
   # Fetching weather display
         # Temperature
         Temp = data['list'][i]['main']['temp']
      
          # Humidity
         humidity = data['list'][i]['main']['humidity']
        
           # Description
         description = data['list'][i]['weather'][0]['description']

           # Precipitation
         precipitation = data['list'][i]['pop']

          # min and max temps
         min_temp = data['list'][i]['main']['temp_min']
         max_temp = data['list'][i]['main']['temp_max']


   # Print the 3 day forecast
         print(f"Date: {date}")
         print(f"Temperature: {Temp} F")
         print(f"Min: {min_temp}F " + f"Max: {max_temp}F")
         print(f"Humidity: {humidity}%")
         print(f"Precipitation: {precipitation}%")
         print(f"Description: {description}")
         print("")

else:
   print(f"Error: {res.status_code}")

 
