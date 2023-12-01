import matplotlib.pyplot as plt

# Sample data for the table
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"],
]

# Create a figure and axis
fig, ax = plt.subplots()

# Hide the axes
ax.axis("off")

# Create the table
table = ax.table(cellText=data, loc="center", cellLoc="center", colLabels=None)

# Customize the appearance of the table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)  # Adjust the table size

# Show the plot
plt.show()
