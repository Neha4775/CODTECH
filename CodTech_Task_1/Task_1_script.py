import requests
import matplotlib

# Use matplotlib backend
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Weather API URL (Hyderabad example)
url = "https://api.open-meteo.com/v1/forecast?latitude=17.3850&longitude=78.4867&hourly=temperature_2m"

# Get data from API
response = requests.get(url)
data = response.json()

# Extract first 10 temperature values
temperature = data["hourly"]["temperature_2m"][:10]
hours = list(range(1, 11))

# Create graph
plt.plot(hours, temperature)
plt.xlabel("Hours")
plt.ylabel("Temperature (°C)")
plt.title("Weather API Data Visualization using Matplotlib")
plt.show()