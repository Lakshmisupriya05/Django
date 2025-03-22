import requests
api_key ="e33bc36a7451d777195795ce2fa335b1"
city = "KAKINADA"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    print(f"Temperature of the city is: {weather_data['main']['temp']}")
    print(f"Weather of the city is: {weather_data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data.")
