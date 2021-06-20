import sys
from termcolor import cprint as print

from .iaction import IAction
from .deployment.cloudformationdeployment import CloudFormationDeployment
from .deployment.amplifydeployment import AmplifyDeployment
from .deployment.hookdeployment import HookDeployment
from .deployment.zappadeployment import ZappaDeployment
from ..enums import EnvironmentType, HookTypes
from ..tools.hooksmanager import hooksManager


class DeploymentAction(IAction):
	""" The deployment action
	"""

	def __init__(self):
		""" Init the action
		"""
		# Initialize the parent
		super().__init__()

		# Set the default environment to development
		self.environment = EnvironmentType.DEVELOPMENT

	def start(self, environType, **kwargs):
		""" Start the deployment
		"""
		# Read all the hooks
		result = hooksManager.readHooks()
		if result is False:
			sys.exit(1)

		# Remember if we found a deployment option
		found = False
		error = False

		# Execute the PRE_FLIGHT hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_FLIGHT)

		# Check if we should execute CloudFormationDeployment
		if CloudFormationDeployment.shouldExecute() is True:
			print("Starting CloudFormation deployment", "blue")
			result = CloudFormationDeployment().start(environType, **kwargs)
			if result is False:
				error = True
			found = True

		# Check if we should execute AmplifyDeployment
		if AmplifyDeployment.shouldExecute() is True:
			print("Starting Amplify deployment", "blue")
			result = AmplifyDeployment().start(environType, **kwargs)
			if result is False:
				error = True
			found = True

		# Check if we should execute ZappaDeployment
		if ZappaDeployment.shouldExecute() is True:
			print("Starting Zappa deployment", "blue")
			result = ZappaDeployment().start(environType, **kwargs)
			if result is False:
				error = True
			found = True

		# Check if we should execute HookDeployment
		if HookDeployment.shouldExecute() is True:
			print("Starting Custom hooks deployment", "blue")
			result = HookDeployment().start(environType, **kwargs)
			if result is False:
				error = True
			found = True

		# Execute the PRE_FLIGHT hooks
		hooksManager.executeHooks(environType, HookTypes.POST_FLIGHT)

		# Check if we found a deployment option
		if found is False:
			print("Could not find any supported deployment methodes. Use Amplify, CloudFormation or Zappa", "red")
			sys.exit(1)

		# Check if an error occured
		if error is True:
			# Set the exit code
			sys.exit(1)
