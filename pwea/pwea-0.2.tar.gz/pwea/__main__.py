import requests
import argparse

from rich import print
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from pwea.key import KEY
from pwea.WeatherCard import WeatherCard


def get_weather(report_type='current', location='Warwick'):
    base_url = f'https://api.weatherapi.com/v1'
    weather_report = requests.get(f"{base_url}/{report_type}.json?key={KEY}"
                                  f"&q={location}&aqi=yes")
    return weather_report


def main():
    console = Console()

    parser = argparse.ArgumentParser(
        usage='pwea [location]',
        description="description: pwea is a simple tool used to retrieve"
        "current weather weather_reportrmation")

    parser.add_argument('location', nargs='+',
                        help="Input a city name, US/UK/Canadian postal code,"
                        "IP address, or Latitude / Longitude (in decimal"
                        "degree)")

    args = parser.parse_args()
    location = ' '.join(args.location)
    weather_report = get_weather('current', location).json()
    card = WeatherCard(weather_report)
    card.display_weather()


if __name__ == '__main__':
    main()
