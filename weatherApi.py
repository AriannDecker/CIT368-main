import requests
from secret import API_KEY
import valid
import logger

def get_weather(zipcode):
    try:
        logger.log(f"Getting weather for {zipcode}")
        base_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={zipcode},US&appid={API_KEY}&units=imperial"
        
        res = requests.get(base_url)
        
        if res.status_code != 200:
            if res.status_code == 404:
                logger.log("Error: 404")
                return { "cod": "404" }
            logger.log("Error: " + str(res.status_code))
            return None

        json = res.json()

        for i in json["list"]:
            if not valid.weather(i):
                logger.log("Invalid weather data")
                return None

        return json
    except:
        logger.log("Unexpected error getting weather")
        return None