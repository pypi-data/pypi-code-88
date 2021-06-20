import os
from halo import Halo
from termcolor import cprint as print


class Spinner(object):
	""" Show a Spinner.
		But hide it in CI mode
	"""

	def __init__(self, *args, **kwargs):
		""" Initialize
		"""
		# Save the data
		self.args = args
		self.kwargs = kwargs

	def __enter__(self):
		""" Open the spinner
		"""
		# Check if we are in CI mode
		if "PETE_CI" in os.environ:
			# Make a fake spinner
			self.spinner = DummySpinner(*self.args, **self.kwargs)
		else:
			# Make a real spinner
			self.spinner = Halo(*self.args, **self.kwargs)

		# Start the spinner
		self.spinner.start()

		return self.spinner

	def __exit__(self, *args, **kwargs):
		""" Close the spinner
		"""
		self.spinner.stop()


class DummySpinner(object):
	""" This does nothing
	"""
	def __init__(self, *args, **kwargs):
		self.text = ""
		if "text" in kwargs:
			self.text = kwargs["text"]
		print("(EXECUTING) %s" % self.text, "yellow")

	def start(self, *args, **kwargs):
		return

	def stop(self, *args, **kwargs):
		return

	def succeed(self, *args, **kwargs):
		print("(SUCCESS) %s" % self.text, "yellow")

	def fail(self, *args, **kwargs):
		print("(FAILURE) %s" % self.text, "yellow")
