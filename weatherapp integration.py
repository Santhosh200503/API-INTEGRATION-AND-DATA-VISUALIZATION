import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
CITY = "London"
API_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
def fetch_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

# Process data
def process_weather_data(data):
    forecast_list = data['list']
    df = pd.DataFrame([{ 
        'date': item['dt_txt'], 
        'temperature': item['main']['temp'], 
        'humidity': item['main']['humidity'], 
        'pressure': item['main']['pressure']
    } for item in forecast_list])
    df['date'] = pd.to_datetime(df['date'])
    return df

# Visualize data
def visualize_weather_data(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df['date'], y=df['temperature'], marker='o', label='Temperature (°C)')
    sns.lineplot(x=df['date'], y=df['humidity'], marker='s', label='Humidity (%)')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'Weather Forecast for {CITY}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Main function
def main():
    data = fetch_weather_data()
    if data:
        df = process_weather_data(data)
        visualize_weather_data(df)

if __name__ == "__main__":
    main()
