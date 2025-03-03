# Note: Run 'pip install requests' to use the requests module
import requests

def fetch_astronauts() -> dict:
    """Fetch the list of astronauts currently in space."""
    url = 'http://api.open-notify.org/astros.json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

def main():
    """Display the names of people currently in space."""
    data = fetch_astronauts()

    if not data or 'people' not in data:
        print("No astronaut data available.")
        return

    print("\nThe people currently in space are:")
    for person in data['people']:
        print(f"- {person['name']} (on {person['craft']})")

if __name__ == "__main__":
    main()
