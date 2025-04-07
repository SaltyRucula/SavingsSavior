import yaml
import csv
from models.expense import Expense
from models.investment import Investment

BASE_YAML_PATH = "yaml/"


def create_investment_objects() -> list[Investment]:
    yaml_data = read_yaml(BASE_YAML_PATH + "investments.yaml")

    investments = []
    for investment in yaml_data.get("investment"):
        investments.append(Investment.from_dict_entry(investment))

    return investments


def create_expenses_objects() -> list[Expense]:
    yaml_data = read_yaml(BASE_YAML_PATH + "expenses.yaml")

    expenses = []
    for expense in yaml_data.get("expenses"):
        expenses.append(Expense.from_dict_entry(expense))

    return expenses


def read_yaml(yaml_path: str) -> dict:
    with open(yaml_path, "r") as file:
        return yaml.safe_load(file)

#if we want the csv approach
def read_csv(csv_path: str) -> list:
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

#create_expenses_objects()
create_investment_objects()
