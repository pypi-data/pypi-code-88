import os
import importlib.util

from termcolor import cprint as print

from .ideploymentaction import IDeploymentAction
from ...tools.configuration import ConfigurationTool
from ...ihook import DeploymentHook, IHook


class HookDeployment(IDeploymentAction):
	""" Deployment through Custom hooks
	"""
	@classmethod
	def shouldExecute(cls):
		""" Check if the Action should be deployed
		"""
		# Check if there are any custom hooks
		return os.path.exists(".pete/hooks")

	def start(self, environType, **kwargs):
		""" Start the deployment
		"""
		# Get the configs
		ConfigurationTool.readConfig()

		# Save the environment type
		self.environment = environType

		# Check if there is an hooks directory
		if os.path.exists(".pete/hooks") is False:
			return

		# Read the hook files
		hooks = os.listdir(".pete/hooks")

		# Walk throught the hooks
		for fileName in hooks:
			# Check if it is an py file
			if os.path.splitext(fileName)[1] != ".py":
				continue

			print("Running hook %s" % fileName, "blue")

			# Import the file
			spec = importlib.util.spec_from_file_location(os.path.splitext(fileName)[0], os.path.join(".pete", "hooks", fileName))
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)

			# Create a hook
			try:
				hook = module.Hook()
			except AttributeError:
				print("There is no Hook class in %s" % fileName, "red")
				return False

			# Check if it is an DeploymentHook
			if isinstance(hook, DeploymentHook) is False:
				if isinstance(hook, IHook) is True:
					continue

				print("Hook %s is not a DeploymentHook subclass" % fileName, "red")
				return False

			# Run the execute
			hook.execute(self.environment)
