import requests
import json
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-071'
api_key = 'your_api_key'  # Replace 'your_api_key' with your actual API key

headers = {
    'Authorization': f'{api_key}',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data_json = response.json()
    locations = data_json['records']['locations']
    print("Get location info in json!")
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the response content for more details on the error

with open('weather_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(locations, json_file, ensure_ascii=False, indent=4)
        
print("Weather API updated successfully.")