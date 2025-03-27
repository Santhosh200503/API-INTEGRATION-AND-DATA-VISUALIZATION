# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: santhosh Kumar B

*INTERN ID*: CT04WG10

*DOMAIN*: PYTHON PROGRAMMINNG

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

##This project fetches real-time weather data from the OpenWeatherMap API and visualizes temperature and humidity trends using Python. The script utilizes the requests library to make API calls, retrieves weather forecasts, and processes the data for visualization using Matplotlib and Seaborn. It helps users analyze weather conditions over a specific period by displaying trends in temperature and humidity through a graphical representation.

The script starts by importing the necessary Python libraries: requests for fetching data, Matplotlib and Seaborn for visualization, and pandas for handling structured data. The OpenWeatherMap API provides weather forecasts in JSON format, which the script processes to extract temperature, humidity, and timestamps.

A request is sent to OpenWeatherMap using an API key, and the response is converted into JSON format. The script then checks for potential errors such as invalid API keys, incorrect city names, or request limits exceeding the free-tier quota. If successful, the JSON response is parsed to extract relevant weather parameters.

The extracted data consists of timestamps, temperatures in Celsius, and humidity percentages. These values are stored in lists and plotted using Seaborn’s lineplot function, making it easy to observe temperature and humidity fluctuations over time. The x-axis represents time intervals, while the y-axis represents weather values, with two separate line plots for temperature (red) and humidity (blue).

To ensure clarity, the script rotates x-axis labels for better readability and adds grid lines. The plt.legend() function is used to differentiate between temperature and humidity lines. Error handling is integrated into the script to manage cases where API requests fail or return unexpected responses. If the API does not return the expected data structure, the script prints an error message and exits gracefully.

Users can modify the script by changing the city name or API key to retrieve weather data for different locations. The project can be extended by incorporating additional weather parameters such as wind speed, pressure, or precipitation. Other enhancements could include integrating the script into a web application using Flask or Streamlit or storing historical weather data in a database for long-term analysis.

To run the script, users need to install dependencies using pip install requests matplotlib seaborn pandas, replace "your_api_key" with their actual API key, and execute the Python file. The script will fetch live data and display a graph of temperature and humidity variations over time.

This project is useful for anyone interested in data visualization, weather analysis, or API integration. It demonstrates how to retrieve real-world data and present it in an understandable format using Python. The visualization makes it easy to identify trends and compare different weather conditions over a selected period. Future improvements could involve adding interactive charts using Plotly or creating an automated weather dashboard.

##OUTPUT
