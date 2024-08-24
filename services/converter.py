from services.api import AbstractCurrencyAPI


class CurrencyConverter:
    def __init__(
            self,
            currency_api: AbstractCurrencyAPI,
            from_currency: str,
            to_currency: str,
            amount: int | float | str
    ):
        self.__currency_api = currency_api
        self.__from_currency = from_currency
        self.__to_currency = to_currency
        self.__amount = self._get_converted_amount(amount)
        self.__currencies = currency_api.get_currencies()

    @staticmethod
    def _get_converted_amount(amount: int | float | str) -> float:
        if isinstance(amount, str) or isinstance(amount, int):
            amount = float(amount)
        return amount

    def convert(self) -> float:
        from_currency_value = self.__currencies[self.__from_currency]
        to_currency_value = self.__currencies[self.__to_currency]
        return (to_currency_value / from_currency_value) * self.__amount
