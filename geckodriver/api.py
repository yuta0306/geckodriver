import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import os
import sys
from typing import Any, AnyStr, List, Tuple, Text, Iterable, Optional, Union, ClassVar, Final
from dataclasses import dataclass


@dataclass
class GeckoDriver:
    _BASE_URL: Final[Text] = 'https://api.coingecko.com/api/v3/'

    def __post_init__(self):
        self.request_timeout: int = 120
        self._session: requests.Session = requests.Session()
        self._retries: Retry = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self._session.mount('http://', HTTPAdapter(max_retries=self.retries))

    

    @property
    def BASE_URL(self):
        return self._BASE_URL

    @property
    def session(self):
        return self._session

    @property
    def retries(self):
        return self._retries
