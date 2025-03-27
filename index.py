import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulated Weather Data (Normally fetched from OpenWeatherMap API)
dates = ["Mar 26 00:00", "Mar 26 03:00", "Mar 26 06:00", "Mar 26 09:00", "Mar 26 12:00", "Mar 26 15:00", "Mar 26 18:00", "Mar 26 21:00"]
temperatures = [12, 14, 16, 18, 20, 19, 17, 15]  # Temperature in °C
humidities = [80, 75, 70, 65, 60, 63, 68, 72]   # Humidity in %

# Create a DataFrame for better visualization
df = pd.DataFrame({"Date & Time": dates, "Temperature (°C)": temperatures, "Humidity (%)": humidities})

# Plot the data
plt.figure(figsize=(10, 5))
sns.lineplot(x="Date & Time", y="Temperature (°C)", data=df, label="Temperature", marker="o", color="red")
sns.lineplot(x="Date & Time", y="Humidity (%)", data=df, label="Humidity", marker="s", color="blue")

# Formatting
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Value")
plt.title("Weather Forecast (Simulated Data)")
plt.legend()
plt.grid(True)
plt.show()
