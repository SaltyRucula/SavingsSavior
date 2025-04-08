from enum import Enum
from .yaml_parseable import Parseable


class Investment(Parseable):
    def __init__(self, symbol: str, investment_values: list[int], investment_dates: list[int]):
        self.symbol = symbol
        self.investment_dates = investment_dates
        self.investment_value = investment_values

    @staticmethod
    def to_object(data, **kwargs) -> 'Investment':
        investment_dates = []
        investment_values = []

        symbol = kwargs.get('symbol', None)

        for row in data:
            investment_dates.append(row['date'])
            investment_values.append(int(row['investment_value']))

        return Investment(symbol, investment_dates, investment_values)
