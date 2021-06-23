import re
import datetime
TODAY = datetime.date.today()

def filter_cards(cards, pattern='', 
	   tags_include={}, tags_exclude={}, # specify a SET of tags
	   create_date_min=None, create_date_max=None,
	   seen_date_min=None, seen_date_max=None,
	   due_date_min=None, due_date_max=None,
	   editor=None, reviewer=None, scheduler=None,
	   deleted_only=False, show_deleted=False,
	   due_only=False,
	   new_only=False,
	   invert=False):
	
	if due_only: due_date_max = TODAY
	# compile the regex pattern for faster searching
	p = re.compile(f'({pattern})')  # wrap in parens to create regex group \1

	f = lambda card: ((not tags_include or tags_include & card.tags) and
			(not tags_exclude or not tags_exclude & card.tags) and
			(not create_date_min or create_date_min <= card.create_date) and
			(not create_date_max or create_date_max >= card.create_date) and 
			(not seen_date_min or seen_date_min <= card.seen_date) and
			(not seen_date_max or seen_date_max >= card.seen_date) and 
			(not due_date_min or due_date_min <= card.due_date) and
			(not due_date_max or due_date_max >= card.due_date) and 
			(not editor or editor == card.editor) and
			(not reviewer or reviewer == card.reviewer) and
			(not scheduler or scheduler == card.scheduler) and
			(not card.deleted or deleted_only or show_deleted) and
			(card.deleted or not deleted_only) and
			(not new_only or card.new) and
			(not pattern or p.search(card.string)) and
			(not due_only or card.due) ^
			invert)
	
	matches = [c for c in cards if f(c)]
	matches.sort(key=lambda card: card.seen_date, reverse=True)

	return matches
