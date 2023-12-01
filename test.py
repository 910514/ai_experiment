import matplotlib.pyplot as plt

# Sample data
x = ['2023-11-26 12:00:00', '2023-11-26 18:00:00', '2023-11-26 18:00:00', '2023-11-27 06:00:00', '2023-11-27 06:00:00', '2023-11-27 18:00:00', '2023-11-27 18:00:00', '2023-11-28 06:00:00', '2023-11-28 06:00:00', '2023-11-28 18:00:00', '2023-11-28 18:00:00', '2023-11-29 06:00:00', '2023-11-29 06:00:00', '2023-11-29 18:00:00', '2023-11-29 18:00:00', '2023-11-30 06:00:00', '2023-11-30 06:00:00', '2023-11-30 18:00:00', '2023-11-30 18:00:00', '2023-12-01 06:00:00', '2023-12-01 06:00:00', '2023-12-01 18:00:00', '2023-12-01 18:00:00', '2023-12-02 06:00:00', '2023-12-02 06:00:00', '2023-12-02 18:00:00', '2023-12-02 18:00:00', '2023-12-03 06:00:00']
y = [20.0, 19.0, 20.0, 18.0, 20.0, 19.0, 23.0, 20.0, 20.0, 17.0, 18.0, 16.0, 19.0, 17.0]
formatted_x = [f'{start} ->\n{end}' for start, end in zip(x[::2], x[1::2])]

# Create a plot with labels and title
plt.plot(formatted_x, y, label='average temperature')
plt.xlabel('Time Range')
plt.ylabel('Temperature')
plt.title('Tamsui Weather Forecast')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Add grid lines and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
