import click
import sys
import shutil
from gumshoe.classes import habits
from gumshoe.classes import activity
from gumshoe.models import models
import logging

COMPLETE = u"\u25A0"  # 713, black square - 25A0, 25AA, 25AF
NOT_COMPLETE = u"\u25A1"  # 2717, white square - 25A1, 25AB, 25AE
PARTIAL_COMPLETE = u"\u25A0"  # t2713, green(click.style) square - 25A0, 25AA, 25AF

logger = logging.getLogger("gumshoe")

@click.command()
@click.option("-n", "--name", help="Use this option to specify the name of the habit you wish to show", default="")
@click.option("-m", "--more", help="Use this option with the -n option to show more details", is_flag=True)
@click.option("-p", "--period", help="Use this option to show all habits in a specific period, example daily, weekly or monthly", default="")
def cli(name,more,period):
    """The show commands allows you to see your progress on a specify habit as well as view all habits you have created. You can also view your current streak and longest streaks on a given habit"""
    from terminaltables import SingleTable
    from textwrap import wrap
    db = models.HabitModel()
    db2 = models.ActivityModel()
    #get terminal width
    terminal_width, terminal_height = shutil.get_terminal_size()
    #check if terminal will be big enough to display data, else give error
    nr_of_dates = terminal_width // 10 - 6
    if nr_of_dates < 1:
        logger.debug("list: Actual terminal width = {0}.".format(shutil.get_terminal_size()[0]))
        logger.debug("list: Observed terminal width = {0}.".format(terminal_width))
        click.echo("Your terminal window is too small. Please make it wider and try again")
        raise SystemExit(1)
    #if name is specified run this section
    if name != "":
        habit = db.check_habit_exists(habits.Habit(name, "", ""))
        activity_title = ""
        if len(habit) != 0:
            activities = db2.get_activities(habit[0])
            entries = activity.Activity()
            if habit[3] == "daily":
                group = entries.get_daily_activies(habit[2], activities,nr_of_dates)
                activity_title = "Daily Activities"
            elif habit[3] == "weekly":
                group = entries.get_weekly_activites(habit[2],activities,nr_of_dates)
                activity_title = "Weekly Activities"
            elif habit[3] == "monthly":
                group = entries.get_monthly_activites(habit[2],activities,nr_of_dates)
                activity_title = "Monthly Activities"
        else:
            click.echo("This habit doe not exsit, please use the show -p all command to see all available habits.")
            sys.exit()
        #if more option is specified run this options
        less = not more
        if less:
            table_title = ["Name", "Target", "Current Streak", "Longest Streak", "Period"]
            table_title.append(activity_title)
            table_rows = [table_title]
            progress = ""
            for x in group["activities"]:
                if x == "yes":
                    column_text = click.style(COMPLETE, fg="green")
                elif x == "part":
                    column_text = click.style(PARTIAL_COMPLETE)
                elif x == "no":
                    column_text = click.style(NOT_COMPLETE)
                progress += column_text + " "

            row = [str(habit[1]), habit[2], group["current_streak"], group["longest_streak"], habit[3], progress]
            table_rows.append(row)
        else:
            table_title = ["Name", "Target", "Streak", "Period"]
            row = [str(habit[1]), habit[2], group["current_streak"], habit[3]]
            for key, value in group.items():
                if key != "current_streak" and key != "longest_streak" and key != "activities":
                    table_title.append(key)
                    row.append(value)
                table_rows = [table_title]
                table_rows.append(row)
    #else if period is specified run this section
    elif period != "":
        if period != "all" and period != "daily" and period != "weekly" and period != "monthly":
            click.echo("Period - daily, weekly, or monthly, please try again")
            sys.exit()
        else:
            table_info = db.show_habit(period)
            if len(table_info) == 0:
                click.echo("There are no defined habits within this period")
                sys.exit()

            table_title = ["Name", "Target", "Period"]
            table_rows = [table_title]

            for data in table_info:
                habit = data
                row = [habit[1], str(habit[2]), str(habit[3])]
                table_rows.append(row)

    else:
        click.echo("Please make sure you specify a habit name or a periodicity, use --help for more information.")
        sys.exit()

    table = SingleTable(table_rows)

    max_col_width = table.column_max_width(0)
    max_col_width = max_col_width if max_col_width > 0 else 20

    for r in table_rows:
        r[0] = '\n'.join(wrap(r[0], max_col_width))
    #print out info to screen
    click.echo(table.table)