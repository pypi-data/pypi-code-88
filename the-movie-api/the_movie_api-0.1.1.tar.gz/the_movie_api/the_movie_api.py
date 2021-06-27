import os

import requests
from loguru import logger

from utils.regex_utils import extract_year_and_movie_name
from utils.search_utils import get_closest_matched_field_in_dicts



class TheMovieAPI:
    def __init__(self, api_key, session_id, api_version="3"):
        self.class_name = type(self).__name__
        logger.info(f'{self.class_name} initialised')
        self.base_url = f'https://api.themoviedb.org/{api_version}'
        self.params = {
            'api_key'   : api_key,
            'session_id': session_id
        }

    def get_account_details(self):
        api_url = self.base_url + '/account'
        response = requests.get(api_url,
                                params=self.params).json()
        return response

    def search_for_movie(self,
                         search_query,
                         language="en-US",
                         page=1,
                         include_adult="false"
                         ):
        """
        :param search_query: Only required param, name of the movie
        :param language:
        :param page:
        :param include_adult:
        :return:
        """
        if search_query is not None:
            logger.info('Searching for {}'.format(search_query))

            api_url = self.base_url + '/search/movie'

            query_params = {
                'api_key'      : self.params['api_key'],
                'language'     : language,
                'query'        : search_query,
                'page'         : page,
                'include_adult': include_adult
            }

            response = requests.get(api_url, query_params)
            if response.status_code == 200:
                logger.info('Successfully found results')
                response_data = response.json()
                return response_data
            else:
                logger.error("Problem getting results")
                response_data = response.json()
                logger.error(response_data)

    def add_movie_to_watchlist(self, movie_id):
        """

        :param movie_id:
        :return:
        """
        account_data = self.get_account_details()
        account_id = account_data['id']
        api_url = self.base_url + '/account/{account_id}/watchlist'.format(
            account_id=account_id)
        logger.info(api_url)
        logger.info(self.params)
        request_body = {
            "media_type": "movie",
            "media_id"  : movie_id,
            "watchlist" : True
        }

        response = requests.post(api_url, data=request_body, params=self.params)
        if response.status_code == 201:
            logger.info("Item successfully added")
        else:
            logger.error("Problem adding item")
            logger.error(response)
            logger.error(response.status_code)

    def add_movie_to_list(self, list_id, movie_id):
        """

        :param movie_id:
        :param list_id:
        :return:
        """
        api_url = self.base_url + '/list/{list_id}/add_item'.format(
            list_id=list_id)
        request_body = {
            "media_id": movie_id
        }
        response = requests.post(api_url, data=request_body, params=self.params)
        if response.status_code == 201:
            logger.info("Item successfully added")
        else:
            logger.error("Problem adding item")
            logger.error(response)
            logger.error(response.status_code)

    def get_all_list_details(self):
        """
         :return:
        """
        account_data = self.get_account_details()
        account_id = account_data['id']
        api_url = self.base_url + '/account/{account_id}/lists'.format(
            account_id=account_id)
        response = requests.get(api_url, params=self.params)
        return response.json()

    def get_list_id(self, list_name):
        """

        :param list_name:
        :return:
        """
        existing_lists = self.get_all_list_details()
        for user_list in existing_lists["results"]:
            if user_list["name"] == list_name:
                list_id = user_list["id"]
                return list_id
            else:
                list_id = self.create_list(list_name=list_name)
                return list_id

    def is_item_already_on_list(self, list_id, movie_id):
        """
        :param list_id:
        :param movie_id:
        :return:
        """
        api_url = self.base_url + "/list/{list_id}/item_status".format(
            list_id=list_id)
        params = self.params
        params['movie_id'] = movie_id
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            return response.json()['item_present']
        else:
            logger.error("Problem check item")

    def search_for_tv_show(self):
        """
        Not yet implemented, currently use the tvdbapi for all of these requests
        """
        raise NotImplementedError

    def delete_list(self, list_id):
        """
         :param list_id:
        :return:
        """
        logger.info(f"Removing {list_id}")
        api_url = self.base_url + f'/list/{list_id}'
        requests.delete(api_url, params=self.params)
        # Would like to do some validation here but TV DB responsds with 500 no matter the message,
        # But still deletes so fine .
        return True

    def create_list(self, list_name, description="", language="en"):
        """
        :param list_name:
        :param description:
        :param language:
        :return:
        """
        request_body = {
            "name"       : list_name,
            "description": description,
            "language"   : language
        }
        api_url = self.base_url + '/list'
        response = requests.post(api_url,
                                 data=request_body,
                                 params=self.params)
        if response.status_code == 201:
            list_id = response.json()['list_id']
            logger.success(f"Successfully created {list_name}")
            logger.success(response.json())
            return list_id
        else:
            logger.error(f"Problem creating {list_name}")
            logger.error(response.status_code)
            logger.error(response)

    def rate_movie(self, movie_id, rating=6.0):
        """
            /movie/{movie_id}/rating
        :param movie_id:
        :param rating:
        :return:
        """
        request_body = {
            "value": rating
        }

        api_url = self.base_url + f'/movie/{movie_id}/rating'

        response = requests.post(api_url, data=request_body, params=self.params)
        if response.status_code == 201:
            logger.info("Item successfully added")
        else:
            logger.error("Problem adding item")
            logger.error(response)
            logger.error(response.status_code)

    def get_list_details(self, list_id):
        """

        :param list_id:
        :return:
        """
        api_url = self.base_url + f"/list/{list_id}"
        response = requests.get(api_url, params=self.params)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            logger.error("Problem getting list")
            logger.error(response)
            logger.error(response.status_code)

    def filter_results(self, search_result_list, search_string, year_released):
        """

        :param search_result_list:
        :param search_string:
        :param year_released:
        :return:
        """
        # First filter out by year,
        filtered_results = [result for result in search_result_list
                            if result['release_date'][0:4] == year_released]
        if len(filtered_results) == 1:
            return filtered_results[0]
        elif len(filtered_results) > 1:
            best_matched_result = \
                get_closest_matched_field_in_dicts(filtered_results,
                                                               search_string,
                                                               key_field="title")
            return best_matched_result
        else:
            # only here if the first filter removes everything,
            # then likely the release year is wrong
            best_matched_result = \
                get_closest_matched_field_in_dicts(
                    search_result_list, search_string, key_field="title")
            return best_matched_result

    def search_for_all_movies(self, all_movie_names):
        """

        :return:
        """
        all_movie_data = []
        for movie_name in all_movie_names:
            clean_movie_name = os.path.splitext(movie_name)[0]
            clean_movie_name, year_released = extract_year_and_movie_name(
                clean_movie_name)
            if clean_movie_name is not None:
                all_results_data = self.search_for_movie(
                    search_query=clean_movie_name)
                if all_results_data['total_results'] >= 1:
                    if all_results_data['total_results'] > 1:
                        result = self.filter_results(
                            all_results_data['results'], clean_movie_name,
                            year_released)
                    else:
                        result = all_results_data['results'][0]

                    movie_data = {
                        "movie_id": result.get("id"),
                        "title"   : result.get("title")
                    }
                    all_movie_data.append(movie_data)
                else:
                    logger.warning("No results for {}".format(clean_movie_name))

        return all_movie_data

    def add_all_movies_to_list(self, movies_to_add, list_name="Watched"):

        list_id = self.get_list_id(list_name)
        self.delete_list(list_id)
        list_id = self.get_list_id(list_name)
        all_movie_data = self.search_for_all_movies(movies_to_add)
        for movie_data in all_movie_data:
            if self.is_item_already_on_list(list_id=list_id,
                                            movie_id=movie_data["movie_id"]):
                logger.error("Item already on list")
            else:
                self.add_movie_to_list(list_id, movie_data["movie_id"])

    def rate_all_movies_in_list(self, list_name="Watched"):
        list_id = self.get_list_id(list_name)
        list_details = self.get_list_details(list_id=list_id)
        for item in list_details['items']:
            self.rate_movie(item["id"])
