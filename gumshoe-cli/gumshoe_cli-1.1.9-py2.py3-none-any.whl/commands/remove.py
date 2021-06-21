import click
from gumshoe.classes import habits
from gumshoe.models import models

@click.command()
@click.argument("name", nargs=-1, required=True)
def cli(name):
    """The remove command removes a habits and all its associated activities. Please specify the name of the habit you
    wish to remove. You can use the gumshoe show command to list all habits to get the habits name."""

    name = ' '.join(name)
    db = models.HabitModel()
    db2 = models.Database()
    new_habit = habits.Habit(name, "", "")
    habit = db.check_habit_exists(new_habit)

    confirmation = click.confirm('Do you really want to remove '+name)

    if confirmation == True:
        if name == "testdb":
            click.echo(db2.remove_test_db())
        else:
            if len(habit) == 0:
                click.echo("This habit doe not exists, use the show command "
                           "to list all habits.")
            else:
                if db.remove_habit(habit[0]):
                    click.echo("Habit removed successfully!")
                else:
                    click.echo("Seems there has been a system error, please check the log file.")
    else:
        click.echo("Habit removed cancelled!")