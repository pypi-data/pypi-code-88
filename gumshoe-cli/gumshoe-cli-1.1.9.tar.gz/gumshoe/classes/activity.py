import sys
from datetime import datetime, timedelta
from functools import reduce
from dateutil import relativedelta


class Activity:

    def __init__(self, name="", quota="", period="", units=""):
        self.name = name
        self.quota = quota
        self.period = period
        self.units = units

    def __repr__(self):
        return "Activity('{}', '{}', {})".format(self.name, self.quota, self.period, self.units)

    def get_daily_activies(self,habit_quota,dates,nr_of_dates):
        days = {}
        activities_per_day = {}
        current_streak = 0
        longest_streak = 0
        activities = []
        streak_list = []

        for d in range(0, nr_of_dates):
            today = datetime.today()
            date_mod = today - timedelta(days=d)
            days[date_mod.strftime("%m-%d")] = []

        for date in reversed(dates):
            d = datetime.strptime(date[2], '%Y-%m-%d %H:%S')
            if d.month > 9:
                s = ""
            else:
                s = "0"
            if d.day > 9:
                f = ""
            else:
                f = "0"
            if s + str(d.month) + "-" + f + str(d.day) in days:
                get_list = days[s + str(d.month) + "-" + f + str(d.day)]
                get_list.append(date)
            else:
                days[s + str(d.month) + "-" + f + str(d.day)] = [date]

        for key, value in days.items():
            if reduce(lambda x, y: x + 1, value, 0) > 0:
                activities_per_day[key] = str(reduce(lambda x, y: x + 1, value, 0))
            else:
                activities_per_day[key] = 0

        for key, value in activities_per_day.items():
            streak_list.append(value)
            if int(value) >= int(habit_quota):
                activities.append("yes")
            elif int(value) > 0:
                activities.append("part")
            else:
                activities.append("no")

        for x in reversed(streak_list):
            if int(x) >= int(habit_quota):
                current_streak += 1
            else:
                if longest_streak == 0:
                    longest_streak = current_streak
                elif current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 0

            if current_streak > longest_streak:
                longest_streak = current_streak

        activities_per_day["current_streak"] = current_streak
        activities_per_day["longest_streak"] = longest_streak
        activities_per_day["activities"] = activities

        return activities_per_day

    def get_weekly_activites(self,habit_quota,dates,nr_of_dates):
        weeks = {}
        activities_per_week = {}
        current_streak = 0
        longest_streak = 0
        activities = []
        streak_list = []

        for d in range(0, nr_of_dates):
            today = datetime.today()
            last_sunday_offset = today.weekday()  # convert day format mon-sun=0-6 => sun-sat=0-6
            last_sunday = today - timedelta(days=last_sunday_offset)
            date_mod = last_sunday - timedelta(weeks=d)
            weeks[date_mod.strftime("%y-%m-%d")] = []


        for date in reversed(dates):
            d1 = datetime.strptime(date[2], '%Y-%m-%d %H:%S')
            for key, value in weeks.items():
                d2 = datetime.strptime(key, '%y-%m-%d')
                if d1.isocalendar()[1] == d2.isocalendar()[1]:
                    get_list = weeks[d2.strftime("%y-%m-%d")]
                    get_list.append(date)

        for key, value in weeks.items():
            if reduce(lambda x, y: x + 1, value, 0) > 0:
                activities_per_week[key] = str(reduce(lambda x, y: x + 1, value, 0))
            else:
                activities_per_week[key] = 0

        for key, value in activities_per_week.items():
            streak_list.append(value)
            if int(value)>=int(habit_quota):
                activities.append("yes")
            elif int(value) > 0:
                activities.append("part")
            else:
                activities.append("no")

        for x in reversed(streak_list):
            if int(x) >= int(habit_quota):
                current_streak += 1
            else:
                if longest_streak == 0:
                    longest_streak = current_streak
                elif current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 0

            if current_streak > longest_streak:
                longest_streak = current_streak

        activities_per_week["current_streak"] = current_streak
        activities_per_week["longest_streak"] = longest_streak
        activities_per_week["activities"] = activities

        return activities_per_week

    def get_monthly_activites(self,habit_quota,dates,nr_of_dates):
        months = {}
        activities_per_month = {}
        current_streak = 0
        longest_streak = 0
        activities = []
        streak_list = []

        for d in range(0, nr_of_dates):
            today = datetime.today()
            a_month = relativedelta.relativedelta(months=d)
            date_minus_month = today - a_month
            months[date_minus_month.strftime("%Y-%m")] = []

        for date in reversed(dates):
            d = datetime.strptime(date[2], '%Y-%m-%d %H:%S')
            if d.month > 9:
                s = ""
            else:
                s = "0"
            if str(d.year) + "-"+s+str(d.month) in months:
                get_list = months[str(d.year) + "-"+s+str(d.month)]
                get_list.append(date)
            else:
                months[str(d.year) + "-"+s+str(d.month)] = [date]

        for key, value in months.items():
            if reduce(lambda x, y: x + 1, value, 0) > 0:
                activities_per_month[key] = str(reduce(lambda x, y: x + 1, value, 0))
            else:
                activities_per_month[key] = 0

        for key, value in activities_per_month.items():
            streak_list.append(value)
            if int(value)>=int(habit_quota):
                activities.append("yes")
            elif int(value) > 0:
                activities.append("part")
            else:
                activities.append("no")

        for x in reversed(streak_list):
            if int(x) >= int(habit_quota):
                current_streak += 1
            else:
                if longest_streak == 0:
                    longest_streak = current_streak
                elif current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 0

            if current_streak > longest_streak:
                longest_streak = current_streak


        activities_per_month["current_streak"] = current_streak
        activities_per_month["longest_streak"] = longest_streak
        activities_per_month["activities"] = activities

        return activities_per_month


