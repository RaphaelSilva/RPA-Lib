from selenium.webdriver.remote.webelement import WebElement

class Stock():
    _name: str
    _short_name: str
    _info: str
    _theoric_price: float
    _variation: float
    _min: float
    _max: float
    _lote: int
    _last_trade_date: str
    _last_trade_hour: str

    def __init__(self,
                 name: str,
                 short_name: str,
                 info: str,
                 theoric_price: float,
                 variation: float,
                 min: float,
                 max: float,
                 lote: int,
                 last_trade_date: str,
                 last_trade_hour: str):
    self._name = name
    self._short_name = short_name
    self._info = info
    self._theoric_price = theoric_price
    self._variation = variation
    self._min = min
    self._max = max
    self._lote = lote
    self._last_trade_date = last_trade_date
    self._last_trade_hour = last_trade_hour

    @staticmethod
    def factory(WebElement el):
        print(el)


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def short_name(self) -> str:
        return self._short_name

    @short_name.setter
    def short_name(self, short_name: str) -> None:
        self._short_name = short_name

    @property
    def info(self) -> str:
        return self._info

    @info.setter
    def info(self, info: str) -> None:
        self._info = info

    @property
    def theoric_price(self) -> float:
        return self._theoric_price

    @theoric_price.setter
    def theoric_price(self, theoric_price: float) -> None:
        self._theoric_price = theoric_price

    @property
    def variation(self) -> float:
        return self._variation

    @variation.setter
    def variation(self, variation: float) -> None:
        self._variation = variation

    @property
    def min(self) -> float:
        return self._min

    @min.setter
    def min(self, min: float) -> None:
        self._min = min

    @property
    def max(self) -> float:
        return self._max

    @max.setter
    def max(self, max: float) -> None:
        self._max = max

    @property
    def lote(self) -> int:
        return self._lote

    @lote.setter
    def lote(self, lote: int) -> None:
        self._lote = lote

    @property
    def last_trade_date(self) -> str:
        return self._last_trade_date

    @last_trade_date.setter
    def last_trade_date(self, last_trade_date: str) -> None:
        self._last_trade_date = last_trade_date

    @property
    def last_trade_hour(self) -> str:
        return self._last_trade_hour

    @last_trade_hour.setter
    def last_trade_hour(self, last_trade_hour: str) -> None:
        self._last_trade_hour = last_trade_hour
