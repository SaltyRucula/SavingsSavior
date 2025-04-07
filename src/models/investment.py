from enum import Enum
from .yaml_parseable import YamlParseable


class InvestmentClass(Enum):
    SAVINGS_ACCOUNT = 1
    CRYPTO = 2
    STOCK = 3
    ETF = 4
    BONDS = 5


class Investment(YamlParseable):
    def __init__(self, investment_type: str, symbol: str, investment_value: int):
        #try except, raising exceptions
        try:
            self.investment_type = InvestmentClass[investment_type]
        except KeyError:
            raise KeyError(f"value must be a ExpenseClass, got {type(investment_type).__name__}")

        self.symbol = symbol
        self.investment_value = investment_value

    @staticmethod
    def from_dict_entry(data: dict):
        return Investment(data.get('investment_type'), data.get('symbol'), data.get('investment_value'))
