from datetime import datetime


def str_to_timestamp(time_str):
	return int(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S').strftime("%s"))


def timestamp_to_str(timestamp):
	return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def millisecond_timestamp_to_str(m_timestamp):
	return datetime.fromtimestamp(m_timestamp/1000).strftime("%Y-%m-%d %H:%M:%S") + '.{:03}'.format(m_timestamp % 1000)


def iso_to_str(timestamp):
	d = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
	return d.strftime("%Y-%m-%d %H:%M:%S")


def get_today_begin_timestamp():
	today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
	return int(today.strftime("%s"))


def get_id_now_timestamp():
	return int(datetime.now().strftime("%s")) + 7*3600


if __name__ == "__main__":
	print(millisecond_timestamp_to_str(1610455370620))
