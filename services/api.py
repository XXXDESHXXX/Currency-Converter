import requests
from abc import ABC, abstractmethod

from config import Config


class AbstractCurrencyAPI(ABC):

    @abstractmethod
    def get_currencies(self):
        pass

    @abstractmethod
    def get_currency(self, currency_code):
        pass


class FreeCurrencyAPI(AbstractCurrencyAPI):
    base_url = Config.FREE_CURRENCY_API_BASE_URL
    api_key = Config.FREE_CURRENCY_API_KEY

    def get_currencies(self) -> dict[str, float]:
        url = f"{self.base_url}/latest?apikey=fca_live_Ngra2Kah62tBClH5yrhsOQhvWPIzs5IPfG4kdBAt"
        response = requests.get(url)
        result = response.json()
        return result["data"]

    def get_currency(self, currency_code: str) -> float:
        data = self.get_currencies()
        return data[currency_code]
