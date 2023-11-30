import requests
import json
from datetime import datetime
import numpy as np

json_file_path = 'response_1700983905482.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    data_json = json.load(file)
target_location_name = "淡水區"
locations = data_json['records']['locations']   # Access the 'locations' list
data = []
# Filter locations based on the target location name
danshui_data = [location for location in locations if location["location"][3]["locationName"] == target_location_name]

for location in danshui_data:
    location_data = {'Location': location['location'][3]['locationName'], 'Elements': []}

    for element in location['location'][3].get('weatherElement', []):
        element_data = {'Element': element['elementName'], 'TimeEntries': []}

        for time_entry in element.get('time', []):
            time_entry_data = {
                'StartTime': time_entry['startTime'],
                'EndTime': time_entry['endTime'],
                'Value': f"{time_entry['elementValue'][0]['value']} {time_entry['elementValue'][0]['measures']}"
            }

            element_data['TimeEntries'].append(time_entry_data)

        location_data['Elements'].append(element_data)

    data.append(location_data)


data_np = np.array(data)
'''
for location_data in data:
    print(f"Location: {location_data['Location']}")
    for element_data in location_data['Elements']:
        print(f"Element: {element_data['Element']}")
        for time_entry_data in element_data['TimeEntries']:
            print(f"Start Time: {time_entry_data['StartTime']}")
            print(f"End Time: {time_entry_data['EndTime']}")
            print(f"Value: {time_entry_data['Value']}")
            print()
'''
#print(data_np)

# Initialize an empty list to store precipitation probability values
precipitation_probability = []

# Iterate through each location in the data
for location_data in data_np:
    # Iterate through each element in the location
    for element_data in location_data['Elements']: 
        # Check if the element is 'PoP12h' (12-hour precipitation probability)
        if element_data['Element'] == 'PoP12h':
            # Iterate through each time entry in the element
            for time_entry in element_data['TimeEntries']:
                # Extract the 'Value' and convert it to a numeric value
                value_str = time_entry['Value'].split()[0]
                value = float(value_str) if value_str.isdigit() else np.nan

                # Append the value to the list
                precipitation_probability.append(value)

# Now 'precipitation_probability' contains the 12-hour precipitation probability values
print(precipitation_probability)

average_temp = []

# Iterate through each location in the data
for location_data in data_np:
    # Iterate through each element in the location
    for element_data in location_data['Elements']:
        # Check if the element is 'PoP12h' (12-hour precipitation probability)
        if element_data['Element'] == 'T':
            # Iterate through each time entry in the element
            for time_entry in element_data['TimeEntries']:
                # Extract the 'Value' and convert it to a numeric value
                value_str = time_entry['Value'].split()[0]
                value = float(value_str) if value_str.isdigit() else np.nan

                # Append the value to the list
                average_temp.append(value)

# Now 'precipitation_probability' contains the 12-hour precipitation probability values
print(average_temp)

wx_values = []

# Specify the target location and element
target_location_name = "瑞芳區"
target_element_name = "Wx"

# Iterate through each location in your data
for location_entry in data_json["records"]["locations"]:
    if location_entry["location"][0]["locationName"] == target_location_name:
        # Iterate through each weather element
        for weather_element in location_entry["location"][0]["weatherElement"]:
            if weather_element["elementName"] == target_element_name:
                # Iterate through each time entry for the specified element
                for time_entry in weather_element["time"]:
                    value_str = time_entry["elementValue"][0]["value"]
                    wx_values.append(value_str)

print(wx_values)

timestamps = []

# Iterate through each location in your data
for location_entry in data_json["records"]["locations"]:
    if location_entry["location"][0]["locationName"] == target_location_name:
        # Iterate through each weather element
        for weather_element in location_entry["location"][0]["weatherElement"]:
            if weather_element["elementName"] == target_element_name:
                # Iterate through each time entry for the specified element
                for time_entry in weather_element["time"]:
                    timestamp = time_entry["startTime"]  # Extract the start time as the timestamp
                    timestamps.append(timestamp)

print(timestamps)