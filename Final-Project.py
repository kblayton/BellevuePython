import json, requests

def main():
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = '2cbbdc039c8b366bd8f6e28fb6d14fb1'

print("")
city_zip = input()

url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print()

response = requests.get(url)
unformatted_data = response.json()

#print(unformatted_data)

temp = unformatted_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformatted_data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")