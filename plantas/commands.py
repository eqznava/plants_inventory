import click

from plantas.services import PlantServices
from plantas.species import Plants

@click.group()
def plants():
    """It is responsible for the plant management process"""
    pass


@plants.command()
@click.option('-q', '--quantity',
              type= int,
              prompt=True,
              help='The quantity of the same plant in the garden')
@click.option('-n', '--name',
              type= str,
              prompt=True,
              help='The common name')
@click.option('-s', '--sciname',
              type= str,
              prompt=True,
              help='The scientific name')
@click.option('-k', '--typeplant',
              type= str,
              prompt=True,
              help='The type of the plant')
@click.option('-i', '--irrigation',
              type= str,
              prompt=True,
              help='The irrigation of the plant')
@click.option('-s', '--season',
              type= str,
              prompt=True,
              help='The season of plant')
@click.pass_context
def create(ctx, quantity, name, sciname, typeplant, irrigation, season):
    """It is responsible for crete new plant"""
    plant =Plants(quantity, name, sciname, typeplant, irrigation, season)
    plant_service = PlantServices(ctx.obj['plants_table'])

    plant_service.create_plant(plant)

@plants.command()
@click.pass_context
def list(ctx):
    """Show the list of plants"""
    plant_service = PlantServices(ctx.obj['plants_table'])

    plants_list = plant_service.list_plants()

    click.echo('QUANTITY  |  NAME  |  SCIENTIFIC NAME  |  TYPE OF PLANTS  |  IRRIGATION  |  SEASON  |  ID')
    click.echo('-' * 140)

    for plant in plants_list:
        click.echo('{quantity} | {name} | {sciname} | {typeplant} | {irrigation} | {season} | {pui}'.format(
            quantity = plant['quantity'],
            name = plant['name'],
            sciname = plant['sciname'],
            typeplant = plant['typeplant'],
            irrigation = plant['irrigation'],
            season = plant['season'],
            pui = plant['pui']))


@plants.command()
@click.argument('plant_pui',
                type=str)
@click.pass_context
def update(ctx, plant_pui):
    """Update a plant information"""
    plant_service = PlantServices(ctx.obj['plants_table'])

    plants_list = plant_service.list_plants()

    plant = [plant for plant in plants_list if plant['pui'] == plant_pui]

    if plant:
        plant = _update_plant_flow(Plants(**plant[0]))
        plant_service.update_plant(plant)

        click.echo('The plant was updated correctly')
    else:
        click.echo('Client not found')


def _update_plant_flow(plant):
    click.echo('Leave empty if you don\'t want modify the value')

    plant.quantity = click.prompt('New quantity ', type=int, default=plant.quantity)
    plant.name = click.prompt('New name ', type=str, default=plant.name)
    plant.sciname = click.prompt('New sciname ', type=str, default=plant.sciname)
    plant.typeplant = click.prompt('New typeplant ', type=str, default=plant.typeplant)
    plant.irrigation = click.prompt('New irrigation ', type=str, default=plant.irrigation)
    plant.season = click.prompt('New season ', type=str, default=plant.season)

    return plant


@plants.command()
@click.argument('plant_pui',
                type=str)
@click.pass_context
def delete(ctx, plant_pui):
    """Remove the plant by its ID"""
    plant_service = PlantServices(ctx.obj['plants_table'])
    plants_list = plant_service.list_plants()

    plant = [plant for plant in plants_list if plant['pui'] == plant_pui]

    if plant:
        plant_to_deleted = _deleted_plant_flow(Plants(**plant[0]))

        if plant_to_deleted:
            plant_service.delete_plant(plant_to_deleted)
            click.echo('Plant removed successfully')
        else:
            click.echo('Process aborted')


def _deleted_plant_flow(plant):
    click.echo('Plant with ID: {pui} was found.'.format(pui = plant.pui))

    delete_confirmation = click.prompt('Delete [Y] / [N]', type= str)

    if delete_confirmation.upper() == 'Y':
        return plant

    return None

all = plants
