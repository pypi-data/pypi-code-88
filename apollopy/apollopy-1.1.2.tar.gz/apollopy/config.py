import os
import json

class Config:
	"""
	base class for configurations.
	"""
	def __init__(self) -> None:
		self.config_path = os.path.join(os.path.expanduser("~"), "apollo_config.json")
		if not os.path.exists(self.config_path):
			self.config = {
				"eyes_timeout": 15 * 60,
				"water_timeout": 30 * 60,
				"exercise_timeout": 40 * 60
			}
			with open(self.config_path, 'w') as f:
				f.write(json.dumps(self.config))

		else:
			with open(self.config_path) as f:
				self.config = json.loads(f.read())

	def load_config(self) -> dict:
		return self.config

	def set_config(self, config: dict) -> None:
		with open(self.config_path, 'w') as f:
			f.write(json.dumps(config))