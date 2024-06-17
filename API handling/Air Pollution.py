import requests
import Credentials

def geocoder(user_input):
    
    data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&appid={Credentials.api_key}")
    location_data = data.json()
    coordinates = [location_data[0]['lat'], location_data[0]['lon']]
    return coordinates


def fetch_air_pollution_data(coordinates):

    data = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={coordinates[0]}&lon={coordinates[1]}&appid={Credentials.api_key}")
    air_pollution_data = data.json()
    return air_pollution_data

def main():
    print("------------------WELCOME TO AIR POLLUTION REPORT------------------")
    location = input("Enter your location: ")
    print('---------------------------------------------------------------')
    coordinates = geocoder(location)
    air_pollution_data = fetch_air_pollution_data(coordinates)
    
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
