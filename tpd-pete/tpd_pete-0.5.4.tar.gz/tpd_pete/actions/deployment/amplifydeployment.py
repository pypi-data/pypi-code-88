import os
import subprocess

from termcolor import cprint as print
from .ideploymentaction import IDeploymentAction
from ...tools.hooksmanager import hooksManager
from ...enums import EnvironmentType, HookTypes
from ...tools.spinner import Spinner


class AmplifyDeployment(IDeploymentAction):
	""" Deployment through AWS Amplify
	"""
	@classmethod
	def shouldExecute(cls):
		""" Check if the Action should be deployed
		"""
		# Check if there is an amplify folder
		return os.path.exists("amplify")

	def start(self, environType, **kwargs):
		""" Execute AWS Amplify deployment
		"""
		# Check if it is the production environment
		if environType != EnvironmentType.PRODUCTION:
			raise Exception("AWS Amplify can only be deployed in production mode")

		# Execute the PRE_INSTALL hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_INSTALL)

		# Check the dependencies
		with Spinner(text="Installing dependencies") as spinner:
			self._checkDependencies()
			spinner.succeed()

		# Execute the POST_INSTALL hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_INSTALL)

		# Execute the PRE_DEPLOYMENT hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_DEPLOYMENT)

		# Send it to AWS Amplify
		with Spinner(text="AWS Amplify deploying") as spinner:
			status = self._amplifyDeploy()

			# Execute the POST_DEPLOYMENT hooks
			hooksManager.executeHooks(environType, HookTypes.POST_DEPLOYMENT)

			if status is True:
				spinner.succeed()
			else:
				spinner.fail()
			return status

	def _amplifyDeploy(self):
		""" Deploy with AWS Amplify
		"""
		# List with command to run
		listCommands = ["amplify push", "amplify publish"]

		# Execute the command
		for amplifyCommand in listCommands:
			# Create the command
			command = "cd %s && " % self.location
			command = command + amplifyCommand

			print(command)

			# Run the command
			try:
				subprocess.check_call(command, shell=True)
			except Exception:
				return False
		return True
