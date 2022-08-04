import requests, json

api_key = "c5c91ed829af194d6978fa05f69a7764"
base_url ="http://api.openweathermap.org/data/2.5/weather?"
city_names = ["Singapore", "Shanghai"]

weather_description_table = {'clear sky': 'We have a clear sky', 'few clouds': 'There are only a few clouds',
'scattered clouds': 'There are scattered clouds', 'broken clouds': 'It is too cloudy. Maybe there is a rain?',
'shower rain': 'There is light rain', 'rain': 'It is a rainny day.', 'thunderstorm': 'It is stormy.',
'snow': 'There is snow today','mist': 'Today is foggy.'}


complete_url_sg = base_url + "appid=" + api_key + "&q=" + city_names[0]
complete_url_sh = base_url + "appid=" + api_key + "&q=" + city_names[1]



try:
    response = requests.get(complete_url_sg)
except:
    print("Sorry, please try a again after connect me to the internet")
else:
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = round(y["temp"] - 273.15, 1)
        # current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        try:
            weather_description = weather_description_table[weather_description]
        except:
            weather_description = "There is " + weather_description
    
        # print following values
        # print(" Temperature (in kelvin unit) = " +
        #                 str(current_temperature) +
        #     "\n atmospheric pressure (in hPa unit) = " +
        #                 str(current_pressure) +
        #     "\n humidity (in percentage) = " +
        #                 str(current_humidity) +
        #     "\n description = " +
        #                 str(weather_description))
        print(str(weather_description) + ". The temperature is " 
        + str(current_temperature) + " Celsius. The humidity is "+ str(current_humidity) 
        +" percent.")
    else:
        print(" sorry, the city was not found")