from .enums import EnvironmentType, HookTypes


class IHook(object):
	""" Basis for all Hooks
	"""
	# Name of the hook
	NAME: str = None

	# What moment should the hook be executed at
	# This is a HookTypes
	ON_TYPE: HookTypes = None

	# What environment should the hook be execute at
	# This is a list of EnvironmentType
	#
	ON_ENVIRONMENT: list = None

	def execute(self, environmentType: EnvironmentType):
		""" Execute the hook
		"""
		raise NotImplementedError


class DeploymentHook(IHook):
	""" A special hook for deployments
	"""
