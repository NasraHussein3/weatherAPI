#I installed requests through pip before i could use the api

import requests
import json


# First function sets up the API url and gets the weather info from the API
def getWeatherInfo(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Use Celsius for temperature
    }

    response = requests.get(base_url, params=params)

    # This part checks if the api request is working by giving us 200 as a status code
    if response.status_code == 200:
        return response.json()
    else:
        return None


#This is the second function that will display the weather data

def displayWeatherInfo(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("Weather data not found!")


# Lastly, this function using my API Key and asks the user the Question
def main():
    api_key = "377c5076b804646983a12615ce5d11f2"
    while True:
        city_name = input("Enter a city name (or 'exit' to quit): ")

        if city_name.lower() == 'exit':
            break

        weather_data = getWeatherInfo(city_name, api_key)

        displayWeatherInfo(weather_data)


        with open("weather_info.txt", "a") as file:
            if weather_data:
                city = weather_data["name"]
                temperature = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"]
                file.write(f"Weather in {city.capitalize()}:\n")
                file.write(f"Temperature: {temperature}°C\n")
                file.write(f"Description: {description.capitalize()}\n")
            else:
                file.write(f"Weather data for {city_name} not found!\n")


if __name__ == "__main__":
    main()
