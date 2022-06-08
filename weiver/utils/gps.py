import requests
import json


if __name__ == "__main__":
    send_url = "http://ipinfo.io/loc"
    geo_req = requests.get(send_url)
    # geo_json = json.loads(geo_req.text)
    print(geo_req.text.strip().split(","))
    # lat, lon = geo_req.text.strip().split(",")
    # lat, lon = float(lat), float(lon)
    q = geo_req.text.strip()
    print(q)
    # lang = "ru"
    # units = "metric"
    # weather_api_key = "89e4f26519d59e85d509cbda179031c4"
    # # weather_url = f"https://api.openweathermap.org/data/2.5/weather\?lat\={lat}\&lon\={lon}\&appid\={weather_api_key}\&lang\={lang}\&units\={units}"
    # weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}"


    weather_api_key = "a8dab6f673ea4667b44221602220806"
    weather_url = f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={q}&aqi=no"
    weather = requests.get(weather_url)
    print(weather.status_code)
    print(weather.text)
    print(type(weather.text))
    weather_dict = json.loads(weather.text)
    print(type(weather_dict))
    print(weather_dict)
