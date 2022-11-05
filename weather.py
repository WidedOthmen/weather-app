import requests
API_KEY = 'Type your API Key'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)


if response.status_code == 200 :
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15 , 2)
    print("the weather today is ",weather , "and the temperature is", temp , "celsius")
    
else :
    print("An error occurred!") 