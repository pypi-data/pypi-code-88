import click
from gumshoe.classes import habits
from gumshoe.models import models

@click.command()
@click.argument("name", nargs=-1, required=True)
@click.option("--quota", "-q", type=int, default=1, help="Amount of quota your wish to complete.")
def cli(name,quota):
    """The complete command adds a completion time and date for a specified habit. Specify the name of the habit you wish to updated."""

    name = ' '.join(name)
    db = models.HabitModel()
    db2 = models.ActivityModel()

    habit = db.check_habit_exists(habits.Habit(name, "", ""))
    if len(habit) == 0:
        habit_name = click.style("{0}".format(name), fg='red')
        click.echo("This habit '{0}' doe not exists, please use the create function to create it or use the show function "
               "to list all habits".format(habit_name))
    else:
        for x in range(quota):
            if not db2.complete_activity(habit[0]):
                click.echo("Seems there has been a system error, please check the log file.")

    habit_name = click.style("{0}".format(name), fg='green')
    complete_times = click.style("{0}".format(quota), fg='green')
    click.echo("Habit {0} completed {1} times".format(habit_name,complete_times))