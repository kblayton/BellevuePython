""" 1. Create a python application that asks the user for the zip code or city - GOOD
    2. Use the zip code or name in order to obtain weather forecast data from openweather - GOOD
    3. Display the weather forecast in a readable format to the user - GOOD
    4. Use comments - can make the necessary comments once this is working 
    5. Use functions including a main function - ##HAVING PROBLEMS HERE##
    6. Validate whether the suer entered valid data. If valid data isn't presented, notify the user - ##HAVING PROBLEMS HERE##
    7. Use the requests library in order to request data from the site
    8. Use try blocks when establishing connection to webservice. You must print a message to the user indicating whether or not the connection was successful - ##PROBLEMS
    """

import requests

def userInput():
    return input("Please enter your city or zip code: ")

def getUrl(url):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={url}&units=&APPID=2cbbdc039c8b366bd8f6e28fb6d14fb1')    
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def main():
    lookup = userInput()
    print(getUrl(lookup))

if __name__ == '__main__':
    main()

answer = 'yes'
while answer == 'yes':
    userInput()

    print("Would you like to get the weather again? (yes or no): ")
    answer = input()
    if answer == 'no':
        print("Have a great day!")
