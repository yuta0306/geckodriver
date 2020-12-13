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

    request_timeout: int = 120
    session: requests.Session = requests.Session()
    retries: Retry = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])

    def __post_init__(self):
        self.session.mount('http://', HTTPAdapter(max_retries=self.retries))

    

    @property
    def BASE_URL(self):
        return self._BASE_URL