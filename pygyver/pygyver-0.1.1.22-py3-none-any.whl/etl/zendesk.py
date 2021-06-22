#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: Mon June 17 16:27:12 2019
Updated on: Wed Feb 17 21:50:00 2021

@authors: kzaoui, dankruse1
"""

import os
import time
import re
import json
from time import sleep
import logging
import requests


class ZendeskDownloader:
    """
    Class to download data from a Zendesk API endpoint specified by params.
    """

    def __init__(self, start_time=None, uri=None, sideload=None, per_page=None, limit=None, base_url="https://madecom.zendesk.com/"):
        """
        Construct all the necessary attributes for the ZendeskDownloader instance
        
        Args:
          uri (str): API endpoint.
          start_time (str, optional): Start time of the request
          limit (int, optional): Per request limit of results returned, optional paramater for some endpoints.
          sideload (str, optional): Additional parameters seperated by &.
          per_page (int, optional): Size of page to fetch from the API.
          base_url (str, optional): Base url of the api call.
          
        Examples:
          downloader = ZendeskDowloader(
            uri="api/v2/incremental/tickets",
            start_time="2018-12-31 22:45:32",
            sideload="include=comment&include=metric_sets",
            per_page=200,
            pagination=True
          )
        """
        self.user = "analytics@made.com/token"
        self.base_url = base_url
        self.start_time = start_time
        self.sideload = sideload
        self.uri = uri
        self.per_page = per_page
        self.limit = limit
        self.endpoint = None
        self.access_token = None
        self.next_page = None
        self.retry = 0
        self.max_retry = 3
        self.params_list = []
        self.endpoint_params = ''
        self.finished=False
        self.set_start_time()
        self.set_auth_token()
        self.set_auth()
        self.set_uri()
        self.set_start_time_param()
        self.set_per_page_param()
        self.set_limit_param()
        self.set_sideload_param()
        self.set_endpoint_params()
        
    def set_start_time(self):
        """Convert `self.start_time` to epoch timestamp.

        Raises:
          ValueError: If `self.start_time` does not follow the format "%Y-%m-%d %H:%M:%S"
        """
        pattern = "%Y-%m-%d %H:%M:%S"
        if self.start_time is not None:
            try:
                logging.info("Start date: %s", self.start_time)
                self.start_time = int(time.mktime(
                    time.strptime(self.start_time, pattern)))
            except ValueError:
                raise ValueError("""Incorrect date format, must be '%Y-%m-%d %H:%M:%S',
                eg. '2018-12-31 22:45:32'""")

    def set_auth_token(self):
        """Load access token file to `self.access_token`
        
        Raises:
          KeyError: if env var ZENDESK_ACCESS_TOKEN_PATH does not exist
        """
        try:
            with open(os.environ["ZENDESK_ACCESS_TOKEN_PATH"]) as zendesk_file:
                data = json.load(zendesk_file)
                self.access_token = data["access_token"]
        except KeyError:
            raise KeyError("ZENDESK_ACCESS_TOKEN_PATH env variable needed")

    def set_auth(self):
        """Set `self.auth` as required to access API based on `self.user` and `self.access_token` values
        """
        self.auth = (self.user, self.access_token)

    def set_uri(self):
        """Format the `self.uri` value for use in the endpoint 
  
        Raises:
          KeyError: if `self.uri` is None
        """
        if self.uri is not None:
          self.uri= "{}.json".format(self.uri)
        else:
          raise KeyError("URI param required")
            
    def set_start_time_param(self):
        """Format and append start_time param to params_list if `self.start_time` is not None
        """
        if self.start_time:
          param ="start_time={}".format(self.start_time)
          self.params_list.append(param)
            
    def set_per_page_param(self):
        """Format and append per_page param to params_list if `self.per_page` is not None
        """
        if self.per_page:
          param = "per_page={}".format(self.per_page)
          self.params_list.append(param)

    def set_limit_param(self):
      """Append limit param to params_list if `self.limit` is not None
      """
      if self.limit:
          param = "limit={}".format(self.limit)
          self.params_list.append(param)
        
    def set_sideload_param(self):
        """Format and append sideload param to params_list if `self.sideload` is not None
        """
        if self.sideload:
          param = self.sideload
          self.params_list.append(param)
        
    def set_endpoint_params(self):
        """Set `self.endpoint_params`
        
        Iterate through `self.params_list` generating a string of params integrating '?' and '&' where required
        """
        for i, k in enumerate(sorted(self.params_list)):
          if i == 0:
            self.endpoint_params = self.endpoint_params + "?{}".format(k)
          else:
            self.endpoint_params = self.endpoint_params + "&{}".format(k)
  
    def set_endpoint(self):
        """Set `self.endpoint`. 
        
        The first call sets the endpoint based on values from the provided uri and params.
        Subsequent calls set the endpoint based on the returned next page value from the previous call (next_page/after_url).
        """
        self.retry = 1
        if not self.endpoint:
            self.endpoint = self.base_url + self.uri + self.endpoint_params
            logging.info("Endpoint generated - {}".format(self.endpoint))
        else:
            next_endpoint = self.data.get("next_page", self.data.get("after_url"))
            if next_endpoint:
              self.endpoint = next_endpoint
            else:
              self.finished = True

    def api_call(self):
        """ Make the API request and handle retry based response codes.
        
        After each request update `self.endpoint` with the next_page endpoint provided in the response.
        If the rate limit is reached (429) process sleeps for period defined in the response.

        Raises:
          ValueError: If there is an error response and max retires has been exhausted  
        """
        response = requests.get(url=self.endpoint, auth=self.auth)
        if response.status_code == 200:
            self.data = json.loads(response.content)
        elif response.status_code == 429:  # timed-out
            sleep_time = int(response.headers['retry-after'])
            logging.warning('Too many requests (429). Waiting %s secs to retry…', sleep_time)
            sleep(sleep_time)
            self.api_call()
        else:
            while self.retry < self.max_retry:
                logging.info("Error {}. Attempt {}/{} failed, retrying after 1 second...".format(response.status_code, self.retry, self.max_retry))
                sleep(1)
                self.retry = self.retry + 1
                self.api_call()
            logging.info("Reached max_retry, raising error")
            raise ValueError("HTTP Error {}".format(response.status_code))
            
    def download(self):
        """ Download API responses based on provided URI and params
        Returns
          obj: Object of API response data
        """
        self.set_endpoint()
        if not self.finished:
            self.api_call()
            responses = self.data
        else:
            logging.info("No further call to be made. Closing loop.")
            responses = []
        return responses
