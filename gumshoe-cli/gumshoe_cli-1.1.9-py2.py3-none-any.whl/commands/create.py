import sys
import click
from gumshoe.classes import habits
from gumshoe.models import models

@click.command()
@click.argument("name", nargs=-1,required=True)
@click.option("-q", "--quota", type=int, default=1, help="Use this option to increase your quota of times you need to complete a habit, default is 1")
@click.argument("period", nargs=1, required=True)
def cli(name, quota ,period):
    """The create command creates new habits and will expect the following arguments and options:\n
       name, name of the task(habit) - required\n
       period, expecting one of the following , daily, weekly, monthly - required
    """
    name = ' '.join(name)
    if period != "daily" and period != "weekly" and period != "monthly":
        click.echo("Period - daily, weekly, or monthly, please try again")
        sys.exit()

    db = models.HabitModel()
    new_habit = habits.Habit(name, quota, period)
    habit = db.check_habit_exists(new_habit)
    if len(habit) == 0:
        if db.create_habit(new_habit):
            click.echo("New habit has been created!")
        else:
            click.echo("Seems there has been a system error, please check the log file.")
    else:
        click.echo("This habit already exists.")