"""2.Visualize the daily temperature changes over time in a city and give your conclusion

 Input: days = list(range(1, 32)) 

# Daily temperature data (replace with your own data) 

temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]"""

import matplotlib.pyplot as plt

# Days and temperature data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', linestyle='-', color='teal')

# Add title and labels
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')
plt.grid(True)

# Show the plot
plt.show()

# Conclusion based on the data
max_temp = max(temperature)
min_temp = min(temperature)
avg_temp = sum(temperature) / len(temperature)

conclusion = (
    f"Maximum Temperature: {max_temp}°F\n"
    f"Minimum Temperature: {min_temp}°F\n"
    f"Average Temperature: {avg_temp:.2f}°F\n"
    f"The temperature fluctuated throughout the month, with a noticeable increase towards the end of the month."
)
print(conclusion)
