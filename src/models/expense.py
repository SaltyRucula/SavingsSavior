from enum import Enum
from .yaml_parseable import Parseable

#Enums
class ExpenseClass(Enum):
    LEISURE: 1
    HOUSE: 2
    FOOD: 3


class Expense(Parseable):
    def __init__(self, expense_class: ExpenseClass, expense_value: int):
        if not isinstance(expense_class, ExpenseClass):
            raise ValueError(f"value must be a ExpenseClass, got {type(expense_class).__name__}")

        self.expense_class = expense_class
        self.expense_value = expense_value

    @staticmethod
    def to_object(data: dict):
        return Expense(data.get('expense_class'), data.get('expense_value'))
