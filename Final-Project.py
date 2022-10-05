""" 1. Create a python application that asks the user for the zip code or city - GOOD
    2. Use the zip code or name in order to obtain weather forecast data from openweather - GOOD
    3. Display the weather forecast in a readable format to the user - GOOD
    4. Use comments - can make the necessary comments once this is working 
    5. Use functions including a main function - ##HAVING PROBLEMS HERE##
    6. Validate whether the suer entered valid data. If valid data isn't presented, notify the user - ##HAVING PROBLEMS HERE##
    7. Use the requests library in order to request data from the site
    8. Use try blocks when establishing connection to webservice. You must print a message to the user indicating whether or not the connection was successful - ##PROBLEMS
    """

import json, requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = '2cbbdc039c8b366bd8f6e28fb6d14fb1'

def main():
    city_zip = input("Please enter your city or zip code: ") # getting user input for city or zip
    url = f"{base_url}?q={city_zip}&units=imperial&APPID={appid}" #Building URL
    response = requests.get(url)
    connection = response.status_code
    unformatted_data = response.json()
    temp = main(unformatted_data)["main"]["temp"]
    print(f"The current temp is: {temp}")
    temp_max = unformatted_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")

#Validating if we were able to make a succesful connection
#try:    
#    if connection == 200:
#        print("The connection to OpenWeather was successful!")
#except ConnectionError or KeyError:
#        print("The connection was not successful. Please try again later")

answer = 'yes'
while answer == 'yes':
    main()

    print("Would you like to get the weather again? (yes or no): ")
    answer = input()
    if answer == 'no':
        print("Have a great day!")