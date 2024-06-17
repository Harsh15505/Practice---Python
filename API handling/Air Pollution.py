import requests
import Credentials

api_key = Credentials.api_key

def geocoder(user_input):
    
    try:
        data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&appid={api_key}")
        data.raise_for_status()
        location_data = data.json()
        if not location_data:
            print("Location not found. Please try again.")
            return None
        coordinates = [location_data[0]['lat'], location_data[0]['lon']]
        return coordinates

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the location data : {e}")
        return None


def fetch_air_pollution_data(coordinates):
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={coordinates[0]}&lon={coordinates[1]}&appid={api_key}")
        data.raise_for_status()
        air_pollution_data = data.json()
        return air_pollution_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the air pollution data : {e}")
        return None

def main():
    print("------------------WELCOME TO AIR POLLUTION REPORT------------------")
    location = input("Enter your location: ")
    print('---------------------------------------------------------------')
    coordinates = geocoder(location)
    if coordinates:
        air_pollution_data = fetch_air_pollution_data(coordinates)
       
        if air_pollution_data:    
            
            aqi = air_pollution_data['list'][0]['main']['aqi']
            print(f"*** AIR POLLUTION REPORT OF {location} ***")
            match aqi:
                case 1:
                    print("AQI: Good. Air quality is satisfactory, and air pollution poses little or no risk.")
                
                case 2:
                    print("AQI: Fair. Air quality is acceptable. However, there may be a risk of health effects.")
                
                case 3:
                    print("AQI: Moderate. There may be a risk of health effects for some people, particularly those who are unusually sensitive to air pollution.")
                
                case 4:
                    print("AQI: Unhealthy for sensitive groups. People with lung disease, older adults, children, and individuals with heart or lung disease can be at greater risk from exposure to air pollution.")
                
                case 5:
                    print("AQI: Unhealthy. Everyone may begin to experience health effects, especially children and individuals with underlying health conditions.")
            
            print("-"*70)
            print("\n\n**NOTE** \n AQI is abbreviation for 'Air Quality Index'")

        print("-"*70)



if __name__ == '__main__':
    main()
