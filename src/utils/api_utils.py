"""
Utils to support api calls
"""
import json
import logging
import os
from urlparse import urlparse, parse_qsl, urlunparse
from urllib import urlencode

import requests
from src.utils.logger_utils import CustomLogger

LOG = CustomLogger.getLogger(__name__)


class ApiUtils():

    def __init__(self, username=None, password=None, hostname=None, is_https=False):
        self.session = requests.session()
        self.session.headers['Content-Type'] = 'application/json'
        self.session.auth = (
            username, password) if username and password else ()
        self.session.verify = False
        self.session.allow_redirects = False
        self.session.cookies.clear_session_cookies()
        self.hostname = hostname.lstrip("https://").lstrip("http://")
        self.base_url = "https://" + self.hostname if is_https else "http://" + self.hostname

    def get(self, url, params_dict={}, headers={}, verify=True):
        """ Makes GET call to url

        Args:
            url (string): 
            params_dict (dict, optional): Defaults to {}.
            headers (dict, optional): Defaults to {}.
            verify (bool, optional): Defaults to True.

        Returns:
            [type]: [description]
        """
        LOG.info("Sending GET for %s with headers = %s and params = %s",
                 url, headers, params_dict)
        return self.session.get(url, params=params_dict, headers=headers, verify=verify)

    def post(self, url, data={}, headers={}, json={}, verify=True):
        """ Makes a POST call to url

        Args:
            url (string):
            data (dict, optional): [description]. Defaults to {}.
            headers (dict, optional): [description]. Defaults to {}.
            json (dict, optional): [description]. Defaults to {}.
            verify (bool, optional): [description]. Defaults to True.

        Returns:
            [type]: [description]
        """
        LOG.info("Sending Post for %s with headers = %s, params = %s and json = %s",
                 url, headers, data, json)
        return requests.post(url, data=data, json=json, headers=headers, verify=verify)

    def get_resp_json(self, response):
        """[summary]

        Args:
            response (): response body

        Returns:
            json:
        """
        LOG.info("Response code : %s" % response.status_code)
        if response.ok:
            try:
                response_json = json.loads(response.text)
                LOG.debug("response json = %s", json.dumps(
                    response_json, indent=2))
                return json.loads(response.text)
            except Exception as err:
                LOG.error("Empty Response: %s, %s" % (response.headers, err))
                return {}
        else:
            LOG.info(response.text)
            return response._content

    def build_url(self, *path, **query_params):
        """Builds a complete url from given path and query_params

        Returns:
            string: final url string
        """
        url_parts = list(urlparse(self.base_url))
        if path:
            final_path = "/".join([each.lstrip('/').rstrip('/')
                                   for each in path])
            url_parts[2] = final_path
        if query_params:
            query = dict(parse_qsl(url_parts[4]))
            query.update(query_params)
            url_parts[4] = urlencode(query_params)
        final_url = urlunparse(url_parts)

        return final_url
