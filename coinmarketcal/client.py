# Author: mfuellbier
# This file is part of python-coinmarketcal.
#
# python-coinmarketcal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-coinmarketcal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-coinmarketcal.  If not, see <http://www.gnu.org/licenses/>.

import logging
import json
import requests
import datetime

logger = logging.getLogger('python-coinmarketcal')


class Coinmarketcal:

    def __init__(self, secret):
        self.headers = {'x-api-key':secret, 'Accept-Encoding': "deflate, gzip", 'Accept': "application/json"}

    def get_coins(self):
        url = "https://developers.coinmarketcal.com/v1/coins"
        try:
            events =requests.get(url, headers=self.headers)
            result = json.loads(events.text)
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        return result

    def get_categories(self):
        url = "https://developers.coinmarketcal.com/v1/categories"
        try:
            events =requests.get(url, headers=self.headers)
            result = json.loads(events.text)
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        return result

    def get_events(self, page=None, max=None,
                  dateRangeStart=None, dateRangeEnd=None,
                  coins=None, categories=None, sortBy=None, showOnly=None):
        payload = {
            "page": page,
            "max": max,
            "dateRangeStart": dateRangeStart,
            "dateRangeEnd": dateRangeEnd,
            "coins": coins,
            "categories": categories,
            "sortBy": sortBy,
            "showOnly": showOnly}

        url = "https://developers.coinmarketcal.com/v1/events"
        try:
            events =requests.get(url, params=payload, headers=self.headers)
            result = json.loads(events.text)
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        return result
