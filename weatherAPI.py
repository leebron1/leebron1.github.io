import requests #pip install

baseurl = "http://api.openweathermap.org/data/2.5/forecast?"  #baseurl, how to get access to our api, given
api_key = "63758d7bb2d8505bae31ab99c28cd142"                  #api key to unlock the api access, given

user_input = input("Enter City: ")                            #asks user for their city as a string

def Kelvin_Farenhiet(kelvin):                                 #converts given kelvin data and converts it to farenheit
        F = (kelvin-273.15)*(9/5)+32
        return int(F)

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&unites=imperial&appid={api_key}")  #requests data from an api, KEY COMPONENT

if response.json()['cod'] == '404' :        #if an the city typed in does not exsist it will return no city found, ERROR catcher
    print("No city Found")
else:
    weather = response.json()['weather'][0]['main']                   # tracks down the specifc data we want within the json text
    temp = response.json()['main']['temp']                            # tracks down the specifc data we want within the json text

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {Kelvin_Farenhiet(temp)} degrees")


