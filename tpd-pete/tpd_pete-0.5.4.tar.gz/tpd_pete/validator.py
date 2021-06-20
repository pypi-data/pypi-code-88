import os

from .tools.configuration import ConfigurationTool


class Validator(object):
	@classmethod
	def findCloudformationTemplate(cls):
		""" Search for an Cloudformation Template

			Returns path to template
		"""
		pass

	@classmethod
	def hasPeteSetup(cls):
		""" Check if pete configure has been run
		"""
		# Check if the CI env var exists
		if "PETE_CI" in os.environ:
			# We are going to use the CI environment variables
			return True

		# Check the path
		path = ConfigurationTool._getGlobalPath()

		# Check if the path exists
		if os.path.exists(path) is False:
			return False
		return True

	@classmethod
	def hasPeteProjectSetup(cls):
		""" Check if pete init has been run
		"""
		# Check the path
		path = ConfigurationTool._getProjectPath()

		# Check if the path exists
		if os.path.exists(path) is False:
			return False
		return True
