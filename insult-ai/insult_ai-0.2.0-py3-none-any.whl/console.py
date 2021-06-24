import click
import json 
from . import __version__
from detoxify import Detoxify
import pandas as pd 

@click.command()
@click.option('--message', default="", help='A message to send to insult-ai.')
@click.version_option(version=__version__)
def insult_me(message : str ):
    """Insult-ai Python project."""
    
    #load model
    model = Detoxify('original')
    
    #predict toxicity
    results = model.predict(message)
    
    #echo results
    click.echo(pd.Series(results).sort_values(ascending=False))
