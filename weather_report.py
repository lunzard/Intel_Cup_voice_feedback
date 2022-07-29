import requests, json

api_key = "c5c91ed829af194d6978fa05f69a7764"
base_url ="http://api.openweathermap.org/data/2.5/weather?"
city_names = ["Singapore", "Shanghai"]

complete_url_sg = base_url + "appid=" + api_key + "&q=" + city_names[0]
complete_url_sh = base_url + "appid=" + api_key + "&q=" + city_names[1]

response = requests.get(complete_url_sg)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
else:
    print(" City Not Found ")