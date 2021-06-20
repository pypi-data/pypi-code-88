import os
import importlib.util
from termcolor import cprint as print

from ..enums import EnvironmentType, HookTypes
from ..ihook import IHook


class HooksManager(object):
	""" Manager for the executing of all hooks
	"""
	def __init__(self):
		""" Initialize
		"""
		# A place to save all the hook per type
		self.hooks = {}

	def readHooks(self):
		""" Read all the hooks
		"""
		# Check if there is an hooks directory
		if os.path.exists(".pete/hooks") is False:
			return

		# Read the hook files
		hooks = os.listdir(".pete/hooks")

		print("Found %s hooks, checking now" % len(hooks), "blue")

		# Walk throught the hooks
		for fileName in hooks:
			# Check if it is an py file
			if os.path.splitext(fileName)[1] != ".py":
				continue

			# Import the file
			spec = importlib.util.spec_from_file_location(os.path.splitext(fileName)[0], os.path.join(".pete", "hooks", fileName))
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)

			# Create a hook
			try:
				hook: IHook = module.Hook()
			except AttributeError:
				print("There is no Hook class in %s" % fileName, "red")
				return False

			# Check if it is an DeploymentHook
			if isinstance(hook, IHook) is False:
				print("Hook %s is not a DeploymentHook subclass" % fileName, "red")
				return False

			# Check if there is an Environments is a list
			if isinstance(hook.ON_ENVIRONMENT, list) is False:
				print("Hook %s does not have a list of environments to be executed on" % fileName, "red")
				return False

			# Loop trough the types
			for environmentType in hook.ON_ENVIRONMENT:
				# Check if it is an HookType
				if isinstance(environmentType, EnvironmentType) is False:
					print("Hook %s does not have a valid EnvironmentYype" % fileName, "red")
					return False

				# Check if the type exists
				if environmentType not in self.hooks:
					# Add the type to the hooks
					self.hooks[environmentType] = {}

				# Check if the HookType is the valid type
				if isinstance(hook.ON_TYPE, HookTypes) is False:
					print("Hook %s does not have a valid HookType" % fileName, "red")
					return False

				# Check if the hook types exists in the hooks
				if hook.ON_TYPE not in self.hooks[environmentType]:
					# Add the hook type
					self.hooks[environmentType][hook.ON_TYPE] = []

				# Add the hook
				self.hooks[environmentType][hook.ON_TYPE].append(hook)

	def executeHooks(self, environmentType: EnvironmentType, hookType: HookTypes):
		""" Execute the hooks
		"""
		# Check if the environment type exists
		if environmentType not in self.hooks:
			# Stop right here, there is nothing to do
			return

		# Check if the hook type exists
		if hookType not in self.hooks[environmentType]:
			# Stop right here, there is nothing to do
			return

		# Loop trough the hooks
		for hook in self.hooks[environmentType][hookType]:
			# Tell the people we are running this hook
			print("Executing hook %s" % hook.NAME, "blue")

			# Execute the hook
			hook.execute(environmentType)


# Make the HooksManager a singleton
hooksManager = HooksManager()
