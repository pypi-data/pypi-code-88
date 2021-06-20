from enum import Enum


class EnvironmentType(Enum):
	""" Different Environment types
	"""
	DEVELOPMENT = 1
	PRODUCTION = 2


class HookTypes(Enum):
	""" Enum with all the different moment when a hook can be executed
	"""
	# First step of the deployment
	PRE_FLIGHT = 1
	POST_FLIGHT = 2

	# Before things are being uploaded; Example: CloudFormation S3 Upload
	PRE_UPLOAD = 3
	POST_UPLOAD = 4

	# Before files are being compiles; Example: CloudFormation template check
	PRE_COMPILE = 5
	POST_COMPILE = 6

	# Before things are being executed; Example: CloudFormation is being executed
	PRE_DEPLOYMENT = 7
	POST_DEPLOYMENT = 8

	# Before things are installed; Example: Dependency install
	PRE_INSTALL = 9
	POST_INSTALL = 10
