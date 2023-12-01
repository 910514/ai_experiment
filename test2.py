import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Paired date-time ranges
date_pairs = [
    ('2023-11-26 12:00:00', '2023-11-26 18:00:00'),
    ('2023-11-27 06:00:00', '2023-11-27 18:00:00'),
    ('2023-11-28 06:00:00', '2023-11-28 18:00:00'),
    ('2023-11-29 06:00:00', '2023-11-29 18:00:00'),
    ('2023-11-30 06:00:00', '2023-11-30 18:00:00'),
    ('2023-12-01 06:00:00', '2023-12-01 18:00:00'),
    ('2023-12-02 06:00:00', '2023-12-02 18:00:00')
]

# Corresponding temperature values (replace with your actual data)
temperature_values = [20.0, 19.0, 20.0, 18.0, 20.0, 19.0, 23.0, 20.0, 20.0, 17.0, 18.0, 16.0, 19.0, 17.0]

# Convert date-time strings to datetime objects
date_pairs = [(datetime.strptime(start, '%Y-%m-%d %H:%M:%S'), datetime.strptime(end, '%Y-%m-%d %H:%M:%S')) for start, end in date_pairs]

# Flatten the list of datetime objects
date_times = [time for pair in date_pairs for time in pair]

# Create a plot
plt.plot(date_times, temperature_values, marker='o', linestyle='-')

# Customize the plot
plt.xlabel('Date-Time Range')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Plot for Date-Time Ranges')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))  # Format x-axis labels as dates

# Show the plot
plt.tight_layout()
plt.show()
