import os

import yaml
import csv
import glob
from models.expense import Expense
from models.investment import Investment

BASE_YAML_PATH = "yaml/"
BASE_CSV_PATH = "csv/"


def create_investment_objects() -> list[Investment]:
    csv_files = glob.glob(os.path.join(BASE_CSV_PATH, "*.csv"))

    investments = []
    for file in csv_files:
        symbol = os.path.splitext(os.path.basename(file))[0]
        with open(file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            investments.append(Investment.to_object(reader, symbol=symbol))

    return investments


def create_expenses_objects() -> list[Expense]:
    yaml_data = read_yaml(BASE_YAML_PATH + "expenses.yaml")

    expenses = []
    for expense in yaml_data.get("expenses"):
        expenses.append(Expense.to_object(expense))

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
