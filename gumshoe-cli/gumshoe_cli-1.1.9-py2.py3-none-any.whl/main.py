from gumshoe.models import models
from gumshoe.classes import gumshoecli

db = models.Database()
db.setup()

cli = gumshoecli.GumShoeCli(help='Welcome to GumShoe the habit tracking command line tool.')

if __name__ == "__main__":
    cli()