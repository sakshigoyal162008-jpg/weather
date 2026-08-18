#weather app
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
current_time=datetime.now()
print("📅 Date: ",current_time.strftime("%d-%m-%y"))
print("⏱️ Time: ",current_time.strftime("%I:%M:%S %p"))
def current_weather(city,API_KEY):
     print("="*50)
     print("         💭 CURRENT WEATHER REPORT 💭")
     print("="*50)
     url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
     response=requests.get(url,timeout=10)
     data=response.json()
     return data
def display_current_weather(data):
     if str(data["cod"])=="200":
               weather=data["weather"][0]["main"]
               if weather=="Clear":
                emoji="☀️"
               elif weather=="Rain":
                emoji="🌧️"
               elif weather=="Clouds":
                emoji="💭"
               elif weather=="Snow":
                emoji="❄️"
               elif weather=="Thunderstorm":
                emoji="⛈️"
               else:
                emoji="🌍"
     
               print(f"🏙️ city: {data['name']}")
               print(f"▶️ Temperature: {data['main']['temp']:.2f}°C")
               print(f"💦 Humidity: {data['main']['humidity']}%")
               print(f" 🌀 weather: {data['weather'][0]['main']}")
               print(f"😃 Feels like: {data['main']['feels_like']:.2f}°C")
               print(f"🌡️ weather_description: {emoji} {data['weather'][0]['description']}")
               print(f"🌍 Pressure: {data['main']['pressure']}hPa")
               print(f"💨 Wind speed: {data['wind']['speed']}m/s")
               print(f"😃 Min temperature: {data['main']['temp_min']}°C")
               print(f"😐 Max temperature: {data['main']['temp_max']}°C")
               print(f"🌍 country: {data['sys']['country']}")
               sunrise=datetime.fromtimestamp(data['sys']['sunrise'])
               sunset=datetime.fromtimestamp(data['sys']['sunset'])  
               print(f"🌄 Sunrise: {sunrise.strftime('%I:%M:%S %p')}")
               print(f"🌇 Sunset: {sunset.strftime('%I:%M:%S %p')}")
               visibility=data['visibility']/1000
               print(f"👀 Visibility: {visibility}Km")
               print("-"*23)
def save_current_weather(data):
        weather = data["weather"][0]["main"]

        if weather == "Clear":
          emoji = "☀️"
        elif weather == "Rain":
           emoji = "🌧️"
        elif weather == "Clouds":
          emoji = "💭"
        elif weather == "Snow":
          emoji = "❄️"
        elif weather == "Thunderstorm":
           emoji = "⛈️"
        else:
           emoji = "🌍"
        with open("weather.txt",'w',encoding="utf-8") as file:
          file.write("="*40 + "\n")
          file.write("\n      CURRENT WEATHER REPORT \n")
          file.write("="*40 + "\n")
          file.write(f"📅 Date: {current_time.strftime('%d-%m-%y')}\n")
          file.write(f"⏱️ Time: {current_time.strftime('%I:%M:%S %p')}\n")
          file.write(f"©️ City: {data['name']}\n")
          file.write(f"▶️  Temperature: {data['main']['temp']:.2f}°C\n")
          file.write(f"💦 Humidity: {data['main']['humidity']}%\n")
          file.write(f" 🌀 weather: {data['weather'][0]['main']}\n")
          file.write(f"😃 Feels like: {data['main']['feels_like']:.2f}°C\n")
          file.write(f"🌡️ weather_description: {emoji}{data['weather'][0]['description']}\n")
          file.write(f"🌍 Pressure: {data['main']['pressure']}hPa\n")
          file.write(f"💨 Wind speed: {data['wind']['speed']}m/s\n")
          file.write(f"😃 Min temperature: {data['main']['temp_min']}°C\n")
          file.write(f"😐 Max temeprature: {data['main']['temp_max']}°C\n")
          file.write(f"🌍 country: {data['sys']['country']}\n")
          sunrise=datetime.fromtimestamp(data['sys']['sunrise'])
          sunset=datetime.fromtimestamp(data['sys']['sunset'])
          file.write(f"🌄 Sunrise: {sunrise.strftime('%I:%M:%S %p')}\n")
          file.write(f"🌇 Sunset: {sunset.strftime('%I:%M:%S %p')}\n")
          visibility=data['visibility']/1000
          file.write(f"👀 Visibility: {visibility}Km\n")
          file.write("="*40)
def get_forecast(city,API_KEY):
    forecast_url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    forecast_response=requests.get(forecast_url,timeout=10)
    forecast_data=forecast_response.json()
    # print(forecast_response.status_code)
    return forecast_data
def display_forecast_data(data):
    if str(data['cod'])!='200':
        print("❌ Forecast Data is not available. Please try again.")
        return
    forecast_days = []
    print("----------💭💭 5-DAY FORECAST DATA 💭💭----------")
    print(f"Report day: {current_time.strftime('%d-%m-%y')}\n")
    print(f"Report time: {current_time.strftime('%I:%M:%S %p')}")
    for item in data["list"][::8]:
         weather = item["weather"][0]["main"]
         if weather == "Clear":
              emoji = "☀️"
         elif weather == "Rain":
              emoji = "🌧️"
         elif weather == "Clouds":
              emoji = "💭"
         elif weather == "Snow":
              emoji = "❄️"
         elif weather == "Thunderstorm": 
              emoji = "⛈️"
         else:
              emoji = "🌍"
         date = datetime.strptime(item["dt_txt"].split(" ")[0],"%Y-%m-%d").strftime("%d-%m-%Y") 
         if date not in forecast_days:
          forecast_days.append(date)
          day_number = len(forecast_days)
          print(f"\n📅 Day {day_number}: {date}")
          print(f"🌡️ Temperature: {item['main']['temp']:.2f}°C")
          print(f"💦 Humidity: {item['main']['humidity']}%")
          print(f"😃 Feels Like: {item['main']['feels_like']:.2f}°C")
          print(f"🌍 Description: {emoji} {item['weather'][0]['description'].title()}")
          print(f"💨 Wind Speed: {item['wind']['speed']:.2f}m/s")
          print("-" * 34)
          if len(forecast_days) == 5:
              break
def save_forecast_data(data):
     if str(data['cod'])!='200':
        return
     with open('weather.txt','a', encoding='utf-8') as file:
          file.write("\n\n")
          file.write("=" * 40 + "\n")
          file.write("           🗓️ 5-DAY FORECAST\n")
          file.write("=" * 40 + "\n")
          file.write(f"Report day: {current_time.strftime('%d-%m-%y')}\n")
          file.write(f"Report time: {current_time.strftime('%I:%M:%S %p')}\n")
          forecast_days = []
          for item in data["list"][::8]:
               weather = item["weather"][0]["main"]
               if weather == "Clear":
                       emoji = "☀️"
               elif weather == "Rain":
                        emoji = "🌧️"
               elif weather == "Clouds":
                        emoji = "💭"
               elif weather == "Snow":
                        emoji = "❄️"
               elif weather == "Thunderstorm": 
                        emoji = "⛈️"
               else:
                        emoji = "🌍"
               date = datetime.strptime(item["dt_txt"].split(" ")[0],"%Y-%m-%d").strftime("%d-%m-%Y") 
 
               if date not in forecast_days:
                forecast_days.append(date)
                day_number = len(forecast_days)
                file.write(f"\n Day {day_number}: {date}\n")
                file.write(f"🌡️ Temperature: {item['main']['temp']:.2f}°C\n")
                file.write(f"💦 Humidity: {item['main']['humidity']}%\n")
                file.write(f"😃 Feels like: {item['main']['feels_like']:.2f}°C\n")
                file.write(f"🌍 Description: {emoji} {item['weather'][0]['description'].title()}\n")
                file.write(f"💨 Wind Speed: {item['wind']['speed']:.2f}m/s\n")
              #.title() is a python string method that is used to convert the first letter of each word into upper case.
                file.write("-"*34)
                if len(forecast_days)==5:
                  break
          file.write("\n\n\n")
          
while True:
  city = input("Enter your city(or type 'exit' to quit ): ").strip().lower()
  #strip() removes extra spaces
  if not city:
      print("City can't be empty. Please try again.")
      continue
  if city.lower()=="exit":
      print("Thank you for using the Weather app !🙏")
      break
  else:
      API_KEY=os.getenv("OPENWEATHER_API_KEY")
      if not API_KEY:
        print("❌ API key not found. Please check your .env file.")
        break
      
      try:
         data=current_weather(city,API_KEY)
         if str(data["cod"])=="200":
             display_current_weather(data)
             save_current_weather(data)
             print("✅ report saved successfully.\n\n")
             forecast_data=get_forecast(city,API_KEY)
             display_forecast_data(forecast_data)
             save_forecast_data(forecast_data)
         else:
           print("❌ city not found.Please enter a valid city name")   
      except requests.exceptions.Timeout:
          print("❌ Request timed out.Please try again")
      except requests.exceptions.ConnectionError:
          print("❌ Internet Connection Problem⁉")
      except requests.exceptions.RequestException:
          print("❌ Something went wrong while connecting to the API ")
      except Exception as e:
               print("request failed!!")
               print(e)
           
               
   