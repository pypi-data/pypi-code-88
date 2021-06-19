from datetime import datetime

from pgsaw.UPC import UPC


class Item:
	basePrice: int = None
	tagPrice: int = None
	description: str = None
	upc: UPC = None
	promoEnd: datetime = None
	weighted: bool = False
	"""
	:param basePrice: Base price in cents. Not nullable. This should always be an int. For items which use partial cents (ex fuel), one can use a custom field if desired, or simply leave it off.
	:param tagPrice: Retail/tagged price in cents (what the item is actually sold at). Not nullable; items which only have one price should have the base and tag set to the same.
	:param description: Store provided name for the Item.
	:param upc: UPC or EAN-13 in format AB1234567890 where
	A is the first lead of EAN-13,
	B is lead of UPC or second lead of EAN-13,
	12345 is the company,
	67890 is the item.
	A and B are both optional and the check digit should NEVER be included.
	Nullable (for Items such as fuel, or for stores which do not provide one).
	:param promoEnd: Datetime of when the tagged price is expected to end. Not necessarily when it will happen, and does not mean that the new price will be the base. Nullable.
	:param weighted: Whether the object is priced based on weight
	"""
	def __init__(self):
		pass
