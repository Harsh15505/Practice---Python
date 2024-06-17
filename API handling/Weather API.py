import requests
import Credentials

api_key = Credentials.api_key

def fetch_weather_data(user_input):
    
    try:

        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")  
        data.raise_for_status() 
        weather_data = data.json()
        if not weather_data:
            print("Cannot fetch data. Please try again.")
            return None
        return weather_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the weather data : {e}")
        return None


def main():
    print("------------------WELCOME TO WEATHER REPORT------------------")

    user_input = input("Please Enter your city:")
    weather_data = fetch_weather_data(user_input)
    
    if weather_data:
        
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
