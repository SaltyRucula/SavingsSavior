from file_reader import *
from api.fetch_asset_info import fetch_asset_info

import click  #mention the argparser alternative?


@click.group()
def cli():
    """Main CLI group for investment and expense management."""
    pass


@click.command()
def update_investment_state():
    """Updates the state of investments from your investments yaml"""
    investments = create_investment_objects()

    #good point to talk about for loops
    for investment in investments:
        asset_info = fetch_asset_info(investment.symbol)

    click.echo("Investment state updated.")


@click.command()
def calculate_expenses():
    """Calculates expenses from your expenses yaml"""
    expenses = create_expenses_objects()
    click.echo("Expenses calculated.")


cli.add_command(update_investment_state)
cli.add_command(calculate_expenses)

if __name__ == '__main__':
    cli()
