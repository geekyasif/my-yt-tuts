from tkinter import *
import requests
import json
from tkinter.messagebox import *


# lets create function to get info
def get_weather_info():
    api_key = "4b21bddcd184e584a2ad6d956ec1be5e"
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    res = requests.get(url)
    json_data = json.loads(res.text)
    print(json_data)
    print(json_data["main"]["temp"])


    weather = json_data["weather"][0]["description"]
    temperature = json_data["main"]["temp"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]
    city_name = json_data["name"]
    country_name = json_data["sys"]["country"]

    showinfo(f'{city.title()} Weather', f'City Name : {city_name} \n Country : {country_name} \n Weather: {weather} \n Temprature : {temperature} \n Humidity ; {humidity} : '
                                        f'{humidity} \n Wind Speed : {wind_speed}')

root = Tk()
root.title("Weather App")

app_label = Label(root, text="Weather App", font=("Times", 20, "bold"))
app_label.grid(row=0, column=0, columnspan=2)

city_label = Label(root, text="Enter city name : ")
city_label.grid(row=1, column=0, columnspan=2)

city_entry = Entry(root, width=30)
city_entry.grid(row=1, column=1, pady=10)

btn = Button(root, text="Get Weather Info", bd=1, command=get_weather_info)
btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()