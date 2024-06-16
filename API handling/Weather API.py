import requests

def fetch_weather_data(user_input):
    api_key = "9a503fe041f05b990d94b48c306dcff1"
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")

    weather_data = data.json()
    return weather_data


def main():
    print("------------------WELCOME TO WEATHER REPORT------------------")

    user_input = input("Please Enter your city:")
    weather_data = fetch_weather_data(user_input)
    
    print('---------------------------------------------------------------')
    print(f"\n\n*** WEATHER REPORT OF {user_input} ***")
    print("-"*70)

    print(f"Weather = {weather_data['weather'][0]['main']} with {weather_data['weather'][0]['description']}")
    print(f"Temperatue = {weather_data['main']['temp']} °C and it Feels Like = {weather_data['main']['feels_like']} °C")
    print(f"Max Temperature of the day = {weather_data['main']['temp_max']} °C")
    print(f"Humidity = {weather_data['main']['humidity']} %")
    print(f"Pressure = {weather_data['main']['pressure']} hPa")
    print("-"*70)
  

if __name__ == "__main__":
    main()
