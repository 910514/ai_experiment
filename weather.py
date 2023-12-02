import requests
import json
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

json_file_path = 'weather_data.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    data_json = json.load(file)
target_location_name = "淡水區"
# Create a dictionary to store location information
# Create a dictionary to store location information
data = {}

# Iterate through the data to find the target location
for dataset_entry in data_json:
    if dataset_entry["locationsName"] == "新北市":
        for location_entry in dataset_entry["location"]:
            if location_entry["locationName"] == target_location_name:
                # Extract information for the desired location
                data[target_location_name] = {
                    "geocode": location_entry["geocode"],
                    "lat": location_entry["lat"],
                    "lon": location_entry["lon"],
                    "weatherElements": []
                }

                # Iterate through weather elements
                for weather_element in location_entry["weatherElement"]:
                    element_info = {
                        "elementName": weather_element["elementName"],
                        "description": weather_element["description"],
                        "time": []
                    }

                    # Iterate through time entries for the weather element
                    for time_entry in weather_element["time"]:
                        time_info = {
                            "startTime": time_entry["startTime"],
                            "endTime": time_entry["endTime"],
                            "value": time_entry["elementValue"][0]["value"],
                            "measures": time_entry["elementValue"][0]["measures"]
                        }
                        element_info["time"].append(time_info)

                    # Add weather element information to the location
                    data[target_location_name]["weatherElements"].append(element_info)
#降雨機率
pop12h_values = [float(entry['value']) if entry['value'].isdigit() else np.nan for entry in data['淡水區']['weatherElements'][0]['time']]
#print(f"The PoP12h values are: {pop12h_values}")
#平均溫度
average_temp = [float(entry['value']) if entry['value'].isdigit() else np.nan for entry in data['淡水區']['weatherElements'][1]['time']]
#print(f"The average_temp are: {average_temp}")
#最大體感
MaxAT = [float(entry['value']) if entry['value'].isdigit() else np.nan for entry in data['淡水區']['weatherElements'][5]['time']]
#print(f"The MaxAT values are: {MaxAT}")
#天氣現象
Wx = [int(entry['value']) if entry['value'].isdigit() else entry['value'] for entry in data['淡水區']['weatherElements'][6]['time']]
#print(f"The Wx values are: {Wx}")
#時間戳
timestamps = [timestamp for entry in data['淡水區']['weatherElements'][0]['time'] for timestamp in (entry['startTime'], entry['endTime'])]
#print(timestamps)

#print precipitation_probability plot
x_precipitation_probability = timestamps
y_precipitation_probability = pop12h_values

formatted_x = [f'{start} ->\n{end}' for start, end in zip(x_precipitation_probability[::2], x_precipitation_probability[1::2])]
# Plot 1: Precipitation Probability
plt.figure()
plt.rcParams["figure.figsize"] = (20,6)
plt.plot(formatted_x, y_precipitation_probability, label='Precipitation Probability')
plt.xlabel('Time Range')
plt.ylabel('Precipitation Probability')
plt.title('Tamsui Weather Forecast')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('pop12h.png', dpi=100)

# Plot 2: Average Temperature
y_temp = average_temp
plt.figure()
plt.rcParams["figure.figsize"] = (30,10)
plt.plot(formatted_x, y_temp, label='Average Temperature')
plt.xlabel('Time Range')
plt.ylabel('Temperature')
plt.title('Tamsui Weather Forecast')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('average_temp.png', dpi=100)

# Plot 3: MaxAT
y_MaxAT = MaxAT
plt.figure()
plt.rcParams["figure.figsize"] = (20,10)
plt.plot(formatted_x, y_MaxAT, label='MaxAT')
plt.xlabel('Time Range')
plt.ylabel('Temperature')
plt.title('Tamsui Weather Forecast')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('maxAT.png', dpi=100)

print("Success plotting graph!")