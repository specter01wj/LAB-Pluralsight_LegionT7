import requests

API_KEY = "d73af82268fa4a64a3c200007231402"  # Store API key as a constant
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather_json(city: str) -> dict:
    """Fetch weather data from WeatherAPI for a given city."""
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}

def get_current_temperature(weather_json: dict) -> float:
    """Extracts the current temperature in Fahrenheit from the weather data."""
    return weather_json.get("current", {}).get("temp_f", "Unknown")

def get_current_description(weather_json: dict) -> str:
    """Extracts the weather description from the weather data."""
    return weather_json.get("current", {}).get("condition", {}).get("text", "No data")

def main():
    """Main function to fetch and display weather details for a city."""
    city = "Rockville"
    weather_json = get_weather_json(city)

    if not weather_json:
        print("Failed to retrieve weather data.")
        return

    temp = get_current_temperature(weather_json)
    description = get_current_description(weather_json)

    print(f"Today's weather in {city} is {description} and {temp}°F.")

if __name__ == "__main__":
    main()
