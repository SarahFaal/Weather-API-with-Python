import datetime as dt
import requests
import os
from tabulate import tabulate

def Kelvin_to_Celsius(kelvin):
    return kelvin - 273.15



Iran_cities = [
    ["1.Tehran", "2.Mashhad", "3.Shahrud"],
    ["4.Isfahan", "5.Karaj", "6.Shiraz"],
    ["7.Tabriz", "8.Qom", "9.Ahvaz"],
    ["10.Rasht", "11.Hamedan", "12.Kerman"],
    ["13.Quchan", "14.Bojnourd", "15.Bandar Abbas"],
    ]


def main():

    flag = True
    CITY = "1"
    while len(CITY) != 0 and flag:
        print("\n(You can choose from the List or type yourself)\n")
        # for i in range(0, len(Iran_cities), 3):
        #     print(Iran_cities[i], "\t", Iran_cities[i+1], "\t",  Iran_cities[i+2], i)
        print(tabulate(Iran_cities))
        print()

        CITY = input("Enter the name(or number) of your city:")

        if CITY.isnumeric():
            number = int(CITY)
            if number == 1:
                CITY = "Tehran"
                flag = False
            elif number == 2:
                CITY = "Mashhad"
                flag = False
            elif number == 3:
                CITY = "Shahrud"
                flag = False
            elif number == 4:
                CITY = "Isfahan"
                flag = False
            elif number == 5:
                CITY = "Karaj"
                flag = False
            elif number == 6:
                CITY = "Shiraz"
                flag = False
            elif number == 7:
                CITY = "Tabriz"
                flag = False
            elif number == 8:
                CITY = "Qom"
                flag = False
            elif number == 9:
                CITY = "Ahvaz"
                flag = False
            elif number == 10:
                CITY = "Rasht"
                flag = False
            elif number == 11:
                CITY = "Hamadan"
                flag = False
            elif number == 12:
                CITY = "Kerman"
                flag = False
            elif number == 13:
                CITY = "Quchan"
                flag = False
            elif number == 14:
                CITY = "Bojnourd"
                flag = False
            elif number == 15:
                CITY = "Cambarao"
                flag = False
            else:
                flag = True
        else:
            flag = False   


    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open('api_key.txt', 'r').read()


    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius = Kelvin_to_Celsius(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = Kelvin_to_Celsius(feels_like_kelvin)

    wind_speed = response['wind']['speed']

    humidity = response['main']['humidity']

    descrioption = response['weather'][0]['description']

    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    os.system('cls')

    print(f"Temperature in {CITY}: {temp_celsius:.2f}°C\n")
    print(f"But it's actually feels like {feels_like_celsius:.2f}°C\n")
    print(f"Humidity in {CITY}: {humidity}%\n")
    print(f"Wind speed in {CITY}: {wind_speed}m/s\n")
    print(f"General weather in {CITY}: {descrioption}\n")
    print(f"Sun rises in {CITY} at {sunrise_time} local time\n")
    print(f"Sun sets in {CITY} at {sunset_time} local time\n")

    user_input = input("you want to continue?(Y/N):)")

    return user_input == "Y" or user_input == "y"   



print("\n<< Welcome to the weather app >>")

while True:
    again = main()
    os.system('cls')
    # print(again)
    if not again:
        break


print("\n\n\nGoodBye, See you next time! :D\n\n\n")


