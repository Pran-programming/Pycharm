import requests
import time

def getWeather():
    city = input("")
    apikey = "dda1f46a20919096f27ebb02dff4b399"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    mintemp = int(json_data['main']['temp_min'] - 273.15)
    maxtemp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 21600))

    print(condition+"\n"+str(temp)+"°C")
    print("\n"+"Max Temp: "+str(maxtemp)+"\n"+"Min Temp: "+str(mintemp)+"\n"+"Max Temp: "+str(maxtemp)+"\n"+"Pressure: "+str(pressure)+"\n"+"Humidity: "+str(humidity)+"\n"+"Wind Speed: "+str(wind)+"\n"+"Sunrise: "+str(sunrise)+"\n"+"Sunset: "+str(sunset))

getWeather()