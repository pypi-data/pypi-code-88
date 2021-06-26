from datetime import datetime, timedelta

# today = datetime.now()
# yesterday = today - timedelta(days=1)
#
#
# def datetime_to_ds(dt):
#     return dt.strftime('%Y-%m-%d')
#
#
# def datetime_to_ds_nodash(dt):
#     return dt.strftime('%Y-%m-%d')
#
#
# def get_default_params():
#     return {
#         'ds': datetime_to_ds(yesterday),
#         'ds_nodash': datetime_to_ds_nodash(yesterday),
#         'tomorrow_ds_nodash': datetime_to_ds_nodash(today),
#         'tomorrow_ds': datetime_to_ds(today)
#     }


class Config:

    def __init__(self):
        self.today = datetime.now()
        self.yesterday = self.today - timedelta(days=1)

    def datetime_to_ds(self, dt):
        return dt.strftime('%Y-%m-%d')

    def datetime_to_ds_nodash(self, dt):
        return dt.strftime('%Y-%m-%d')

    def get_default_params(self):
        return {
            'ds': self.datetime_to_ds(self.yesterday),
            'ds_nodash': self.datetime_to_ds_nodash(self.yesterday),
            'tomorrow_ds_nodash': self.datetime_to_ds_nodash(self.today),
            'tomorrow_ds': self.datetime_to_ds(self.today)
        }
