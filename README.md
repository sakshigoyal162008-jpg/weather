# 🌤️ Weather App

A Python-based Weather App that fetches real-time weather information and a 5-day forecast using the OpenWeatherMap API.

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


## 📸 Project Output

The application displays:

- Current weather information
- Temperature and feels-like temperature
- Humidity and pressure
- Wind speed
- Sunrise and sunset
- Visibility
- 5-day weather forecast

## 🔐 Security

The OpenWeatherMap API key is stored securely in a `.env` file and is excluded from GitHub using `.gitignore`.

## 👩‍💻 Author

**Sakshi Goyal**

BCA Student | Python & Web Development Learner