# A dummy scheduler that always schedules for the next day
import datetime
today = datetime.date.today()
day = datetime.timedelta(days=1)

def schedule(card):
	
	if len(card.history) == 0:
		raise RuntimeError(f'Card #{card.id} has no review history.')
	if len(card.history) == 1:
		card.set_due_date(today)
		return 0

	if card.last_grade == 0:
		due_date = today + 7*day
	if card.last_grade == 1:
		card.set_due_date(today)
		return 5
	if card.last_grade == 2:
		due_date = today + max(day, card.last_interval / 2)
	elif card.last_grade == 3:
		due_date = today + card.last_interval * 2 + day
	elif card.last_grade == 4:
		due_date = today + card.last_interval * 3 + day*2

	card.set_due_date(due_date)
	return 0		
