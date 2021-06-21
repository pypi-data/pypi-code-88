import click

from quickstats.components import ExtendedModel
    
@click.group(name='inspect_ws')
def inspect_ws():
    pass

def inspect_ws_nuisance_parameter_names