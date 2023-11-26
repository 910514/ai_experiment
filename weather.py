import requests
import json

#url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-071?Authorization=my_apikey'
#data = requests.get(url)   # Get the JSON content as text
#data_json = data.json()    # Convert it to JSON format
json_file_path = 'response_1700983905482.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    data_json = json.load(file)
target_location_name = "淡水區"
locations = data_json['records']['locations']   # Access the 'locations' list
# Filter locations based on the target location name
danshui_data = [location for location in data_json["records"]["locations"] if location["location"][3]["locationName"] == target_location_name]
'''
for location in locations:
    for entry in location['location']:
        location_name = entry['locationName']  # Access 'locationName' for each entry in 'location'
        print(location_name)
'''

for location in locations:
    #print(location['location'])  # Print the 'location' list to inspect its structure
    location_name = location['location'][3]['locationName']  # Access 'locationName' within the 'location' list
    print(location_name)

'''
with open('weather_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(locations, json_file, ensure_ascii=False, indent=4)
'''
for location in danshui_data:
    print(f"Location: {location['location'][3]['locationName']}")
    for element in location['location'][3].get('weatherElement', []):
        print(f"Element: {element['elementName']}")
        for time_entry in element.get('time', []):
            print(f"Start Time: {time_entry['startTime']}")
            print(f"End Time: {time_entry['endTime']}")
            print(f"Value: {time_entry['elementValue'][0]['value']} {time_entry['elementValue'][0]['measures']}")
    