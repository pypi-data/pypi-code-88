from random import choice
import csv
import os


class Cities:
    def __init__(self):

        self.cities = self.get_all()

    def get_cities(self):
        path = os.path.join(os.path.dirname(__file__), "world_cities.csv")
        f = open(path, 'r', encoding='utf-8')
        reader = csv.DictReader(f)
        return reader

    def get_all(self):
        """
        return list of all cities
        :return:
        """
        return [city['name'].rstrip() for city in list(self.get_cities())]

    def get_single(self, country=None):
        """
        returns a string of a random city
        :param country: str, optional parameter choosing which country the city is from
        :return: str, city name
        """
        # Check if there a country preference was given
        if country is None:
            return choice(self.get_all())
        else:
            return choice(self.get_by_country(country))

    def get_random_cities(self, n):
        """
        returns a list of random cities in the given amount
        :param n: int, number of desired cities
        :return: list
        """
        cities = list()

        full_list = self.get_all()
        # Iterate through the given number
        for _ in range(n):
            city = choice(full_list)

            cities.append(city)
        return cities

    def get_by_country(self, name):
        """
        returns a list of cities based on a given country
        Note: There is only 'United Kingdom' not England
        :param name: str, country name
        :return: list
        """
        return [city['name'] for city in self.get_cities()
                if city['country'].lower() == name.lower()]

    def get_by_letter(self, letter):
        """
        returns a list of cities based on a given letter
        :param letter: chr
        :return: list
        """
        cities = list()

        for city in self.get_all():
            if city[0].lower() == letter.lower():
                cities.append(city)

        return cities
