import click

from plantas import commands as plants_commands

PLANT_TABLE = '.plants.csv'
@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['plants_table'] = PLANT_TABLE


cli.add_command(plants_commands.all)
