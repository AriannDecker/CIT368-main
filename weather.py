# Ariann Decker
# WeatherApp
# Build an app that will report weather forecasts given a location
# 29 December 2023
##UPDATE : 30 April 2024 Updated with security principles

import os
import requests
from datetime import datetime as dt
import valid
import weatherApi


def main():
    zipcode = None
    weather = None

    # Get User ZipCode
    while True:
        zipcode = input("What is your zip code: " + "\n")
        
        if not valid.zipcode(zipcode):
            print("Invalid Zipcode")
            continue
        
        weather = weatherApi.get_weather(zipcode)
        
        if not weather:
            print("could not get weather")
            continue
        
        if weather["cod"] == "404":
            print("Could not find city")
            continue
        
        break

    forecast = get_three_day_forecast(weather)
    
    print_weather(forecast)

def print_weather(forecast):
    print(f"Three Day Forecast for {forecast['city']}:")
    
    for i in forecast["three_day_forecast"]:
        date = dt.fromtimestamp(i["dt"])
        temp = i["main"]["temp"]
        description = i["weather"][0]["description"]
        
        print(f"\tDate: {date.strftime('%m/%d/%Y')}")
        print(f"\tTemperature: {temp} F")
        print(f"\tDescription: {description}")
        print()

def get_three_day_forecast(weather):
    forecast = {
        "city": weather["city"]["name"],
        "three_day_forecast": []
    }
    
    current_day = None
    count = 0
    
    for i in weather["list"]:
        if count == 3:
            break
        
        date = dt.fromtimestamp(i["dt"])
        
        if current_day and current_day.day == date.day:
            continue
        
        current_day = date
        
        forecast['three_day_forecast'].append(i)
        count += 1
    
    return forecast

def get_zip(zipcode):
    g_url = f"{geo_url}appid={api_key}&zip={zipcode},us"
    r = requests.get(g_url)
    if r.status_code == 200:
        data = r.json()
        lat = data['lat']
        lon = data['lon']
        return data['lat'], data['lon']
    else:
        print(f"Error: {r.status_code}" + "\n" + "Please try again")

    url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    res = requests.get(url)
    data = res.json()

    if r.status_code == 200:
        return data
    else:
        print(f"Error: {r.status_code}" + "\n" + "Please try again")

def get_weather(data):
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

        print(f"Date: {date}\n")
        print(f"Temperature: {Temp} F\n")
        print(f"Min: {min_temp}F " + f"Max: {max_temp}F\n")
        print(f"Humidity: {humidity}%\n")
        print(f"Precipitation: {precipitation}%\n")
        print(f"Description: {description}\n")

if __name__ == "__main__":
    main()