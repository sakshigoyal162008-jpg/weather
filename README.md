# 🌤️ Weather App

## ✨ Features

- 🌡️ Current temperature
- 💦 Humidity
- 🌀 Weather condition
- 😃 Feels-like temperature
- 🌍 Atmospheric pressure
- 💨 Wind speed
- 🌄 Sunrise and sunset
- 👀 Visibility
- 🗓️ 5-day weather forecast
- 💾 Saves weather reports to a text file
- ⚠️ Handles invalid cities and connection errors
- 🔐 API key protected using `.env`

## 🛠️ Technologies Used

- Python
- Requests
- OpenWeatherMap API
- python-dotenv

## ▶️ How to Run

1. Install the required packages:

```bash  
pip install requests python-dotenv
 
```

2. Create a `.env` file:

 ```text
  OPENWEATHER_API_KEY=Your_api_key

  ```

3. Run the application:

 ```bash
 python Weather_app.py

 ```

4. Enter the city name and get the weather report.