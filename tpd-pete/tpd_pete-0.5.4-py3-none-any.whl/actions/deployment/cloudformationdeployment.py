import json
import os
import sys
import time
import zipfile

from PyInquirer import prompt
from termcolor import cprint as print

from ...enums import EnvironmentType, HookTypes
from ...tools.hooksmanager import hooksManager
from ...tools.configuration import ConfigurationTool, ConfigKey, ConfigType
from ...tools.template import TemplateTool
from ...tools.boto import BotoTool
from ...tools.spinner import Spinner
from .ideploymentaction import IDeploymentAction


class CloudFormationDeployment(IDeploymentAction):
	""" Deployment through AWS CloudFormation
	"""

	@classmethod
	def shouldExecute(cls):
		""" Check if the Action should be deployed
		"""
		# Check if there is an template
		return os.path.exists("template.yaml")

	def start(self, environType, **kwargs):
		""" Start the deployment
		"""
		# Get the configs
		ConfigurationTool.readConfig()

		# Check if there is an template
		if os.path.exists("template.yaml") is False:
			raise Exception("Cant find CloudFormation template: 'template.yaml'")

		# Save the environment type
		self.environment = environType

		# Execute the PRE_COMPILE hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_COMPILE)

		# Create a temporary directory
		with Spinner(text="Creating environment") as spinner:
			self._createTempDir()
			spinner.succeed()

		# Create a new temporary template
		with Spinner(text="Creating template") as spinner:
			try:
				parameters = self._createTemporaryTemplate()
			except Exception as e:
				spinner.fail()
				print(e, "red")
				return False
			else:
				spinner.succeed()

		# Check if there are other parameters
		parameters = self._checkParameters(parameters)

		# Execute the POST_COMPILE hooks
		hooksManager.executeHooks(environType, HookTypes.POST_COMPILE)

		# Execute the PRE_INSTALL hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_INSTALL)

		# Check the dependencies
		with Spinner(text="Installing dependencies") as spinner:
			self._checkDependencies()
			spinner.succeed()

		# Execute the POST_INSTALL hooks
		hooksManager.executeHooks(environType, HookTypes.POST_INSTALL)

		# Execute the PRE_UPLOAD hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_UPLOAD)

		# Zip it all
		with Spinner(text="Zipping content") as spinner:
			zipName = self._zipContent()
			spinner.succeed()

		# Upload the zip
		with Spinner(text="Uploading to S3") as spinner:
			s3Location = self._uploadToS3(zipName)
			spinner.succeed()

		# Execute the POST_UPLOAD hooks
		hooksManager.executeHooks(environType, HookTypes.POST_UPLOAD)

		# Execute the PRE_DEPLOYMENT hooks
		hooksManager.executeHooks(environType, HookTypes.PRE_DEPLOYMENT)

		# Send it to CloudFormation
		with Spinner(text="CloudFormation deploying") as spinner:
			# Execute CloudFormation
			status = self._cloudformationDeploy(parameters, s3Location)

			# Execute the PRE_DEPLOYMENT hooks
			hooksManager.executeHooks(environType, HookTypes.POST_DEPLOYMENT)

			# Check if all is well
			if status is True:
				spinner.succeed()
			else:
				spinner.fail()
				return False
		return True

	def _createTemporaryTemplate(self):
		""" Create a temporary template

			Returns a dict with the parameters
		"""
		# Get the template
		f = open("template.yaml", "r")
		template = f.read()
		f.close()
		template = TemplateTool.parseTemplate(template)

		# Check the environment
		if self.environment == EnvironmentType.DEVELOPMENT:
			if ConfigurationTool.getConfig(ConfigKey.DEV_SUFFIX) is True:
				# Add the dev suffix to the items
				template = TemplateTool.addSuffixToItems(template)

		# Add the tags
		template = TemplateTool.addTagsToItems(template)

		# Check the parameters
		template, parameters = TemplateTool.checkVariables(template)

		# Save the template
		f = open(os.path.join(self.location, ".deployment.template.json"), "w")
		f.write(json.dumps(template))
		f.close()

		# Add the basic parameters
		parameters['environment'] = self.environment
		parameters['stackName'] = ConfigurationTool.getConfig(ConfigKey.STACK_NAME) + ("_development" if ConfigurationTool.getConfig(ConfigKey.DEV_SUFFIX) is True and self.environment == EnvironmentType.DEVELOPMENT else "")
		parameters['projectName'] = ConfigurationTool.getConfig(ConfigKey.STACK_NAME)

		return parameters

	def _zipContent(self):
		""" Zip the current directory

			Returns the zip filename
		"""
		# Create a list of ignored folders
		ignoredFolders = [".git", ".svn", ".pete", ".vscode", "seeders"]

		# Create a filename
		zipFileName = "pete_%s.zip" % int(time.time())

		# Create the zip file
		with zipfile.ZipFile(os.path.join(self.location, zipFileName), "w", zipfile.ZIP_DEFLATED) as zipFile:
			# Walk through all the files
			for root, dirs, files in os.walk(self.location):
				# Check the ignored folders
				goToNext = False
				for ignoredFolderName in ignoredFolders:
					if ignoredFolderName in root:
						goToNext = True
						break

				# Check if we found a ignored folder
				if goToNext is True:
					continue

				# Walk throught the files of the directory
				for fileName in files:
					# Check if this is an zip
					if ".zip" in fileName:
						continue

					# Add them to the zip file
					arcname = os.path.join(root, fileName)[len(self.location):]
					zipFile.write(os.path.join(root, fileName), arcname=arcname)

		return zipFileName

	def _uploadToS3(self, zipName):
		""" Upload the zip file to S3
		"""
		# Create a full filename
		fullFileName = "%s/%s" % ((ConfigurationTool.getConfig(ConfigKey.STACK_NAME).lower()), zipName)

		# Get the bucket name and profile
		bucketName = self._getDeploymentBucketName()
		profileName = self._getDeploymentProfile()
		region = self._getDeploymentRegion()

		# Upload the file
		BotoTool.uploadToS3(
			fromPath=os.path.join(self.location, zipName),
			toBucket=bucketName,
			toKey=fullFileName,
			region=region,
			profile=profileName
		)

		return fullFileName

	def _getDeploymentBucketName(self):
		""" Get the deployment Bucket name from the config

			Returns name of the bucket
		"""
		# Check if we use the development environment
		if self.environment == EnvironmentType.DEVELOPMENT:
			# Check if the DEV_BUCKET is in the projectConfig
			bucketName = ConfigurationTool.getConfig(ConfigKey.DEV_BUCKET)

		# This is the production environment
		else:
			# Check if the PROD_BUCKET is in the projectConfig
			bucketName = ConfigurationTool.getConfig(ConfigKey.PROD_BUCKET)

		return bucketName.strip()

	def _getDeploymentProfile(self):
		""" Get the deployment AWS Profile

			Returns name of profile
		"""
		# Check if we use the development environment
		if self.environment == EnvironmentType.DEVELOPMENT:
			# Check if the DEV_PROFILE is in the projectConfig
			profileName = ConfigurationTool.getConfig(ConfigKey.DEV_PROFILE)

		# This is the production environment
		else:
			# Check if the PROD_PROFILE is in the projectConfig
			profileName = ConfigurationTool.getConfig(ConfigKey.PROD_PROFILE)

		return profileName.strip()

	def _getDeploymentRegion(self):
		""" Get the deployment AWS Region

			Returns name of region
		"""
		# Default option for region
		region = None

		# Check if we use the development environment
		if self.environment == EnvironmentType.DEVELOPMENT:
			# Check if the DEV_REGION is in the projectConfig
			region = ConfigurationTool.getConfig(ConfigKey.DEV_REGION)

		# This is the production environment
		else:
			# Check if the PROD_REGION is in the projectConfig
			region = ConfigurationTool.getConfig(ConfigKey.PROD_REGION)

		return region

	def _cloudformationDeploy(self, parameters, s3Location):
		""" Deploy to CloudFormation
		"""
		# Get the information
		deploymentBucket = self._getDeploymentBucketName()
		profileName = self._getDeploymentProfile()
		region = self._getDeploymentRegion()
		stackName = ConfigurationTool.getConfig(ConfigKey.STACK_NAME)

		# Get the boto client
		client = BotoTool._getClient("cloudformation", region=region, profile=profileName)

		# Check if the stack exists
		stackExists = False
		try:
			client.describe_stacks(StackName=stackName)
		except Exception:
			# There are currently no stacks in CloudFormation
			pass
		else:
			# The stack exists
			stackExists = True

		# Upload the file to S3
		templatePath = os.path.join(self.location, ".deployment.template.json")
		templateName = "%s/template-%s.json" % (stackName.lower(), str(int(time.time())))
		templateUrl = BotoTool.uploadToS3(
			fromPath=templatePath,
			toBucket=deploymentBucket,
			toKey=templateName,
			region=region,
			profile=profileName
		)

		# Create a change set name
		changeStackName = "%s%s" % (stackName, str(int(time.time())))

		# Create the change set parameters
		changeStackParameters = [
			{"ParameterKey": "deploymentBucket", "ParameterValue": deploymentBucket},
			{"ParameterKey": "s3FileName", "ParameterValue": s3Location}
		]

		# Add extra parameters
		for key, value in parameters.items():
			changeStackParameters.append({"ParameterKey": key, "ParameterValue": str(value)})

		# Check if the stack exists
		if stackExists is False:
			# Create the stack
			client.create_stack(
				StackName=stackName,
				TemplateURL=templateUrl,
				Parameters=changeStackParameters,
				Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
				Tags=[
					{"Key": "Stack", "Value": stackName},
				]
			)

		else:
			# Create a change set
			client.create_change_set(
				StackName=stackName,
				ChangeSetName=changeStackName,
				TemplateURL=templateUrl,
				Parameters=changeStackParameters,
				Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
				Tags=[
					{"Key": "Stack", "Value": stackName},
				]
			)

			# Wait for the results
			while True:
				# Get the change set
				changeSet = client.describe_change_set(StackName=stackName, ChangeSetName=changeStackName)

				# Try to get the status
				try:
					stackStatus = changeSet["Status"]
					if "StatusReason" in changeSet:
						statusText = changeSet["StatusReason"]
					else:
						statusText = ""
				except Exception:
					stackStatus = "CREATE_IN_PROGRESS"

				# Check the status
				if stackStatus[-7:] == "_FAILED" or stackStatus == "FAILED":
					print(statusText, "red")
					return False
				elif stackStatus[-9:] == "_COMPLETE":
					break

				# Wait a little
				time.sleep(15)

			# Apply the change set
			client.execute_change_set(
				ChangeSetName=changeStackName,
				StackName=stackName
			)

		# Wait for the results
		while True:
			# Get the stack
			stack = client.describe_stacks(StackName=stackName)

			# Try to get the status
			try:
				stackStatus = stack["Stacks"][0]["StackStatus"]
			except Exception:
				stackStatus = "CREATE_IN_PROGRESS"

			# Check the status
			if "IN_PROGRESS" in stackStatus:
				pass
			elif stackStatus[-7:] == "_FAILED" or "ROLLBACK" in stackStatus:
				return False
			elif stackStatus[-9:] == "_COMPLETE":
				return True

			# Wait a little
			time.sleep(15)

	def _checkParameters(self, parameters):
		""" Check if there are other parameters we need information about
		"""
		# Walk through the parameters
		for parameterName in parameters:
			# Check if there is an value
			if parameters[parameterName] in ["String", "Number", "List", "CommaDelimitedList"]:
				# Check if we have the parameter in de project config
				parametersConfig = ConfigurationTool.getConfig(ConfigKey.PARAMETERS)
				if parametersConfig is None:
					parametersConfig = {}

				# Check if the environment exists in the config
				if str(self.environment) in parametersConfig:
					if parameterName in parametersConfig[str(self.environment)]:
						parameters[parameterName] = parametersConfig[str(self.environment)][parameterName]
						continue

				# Ask for the value
				parameterValue, save = self._askForParameterValue(parameterName)

				# Save the value
				parameters[parameterName] = parameterValue

				# Check if we should save the value
				if save is True:
					# Check if the environment exists
					if str(self.environment) not in parametersConfig:
						parametersConfig[str(self.environment)] = {}

					# Set the value in de config
					parametersConfig[str(self.environment)][parameterName] = parameterValue

					# Save the value
					ConfigurationTool.setConfig(ConfigKey.PARAMETERS, parametersConfig, ConfigType.PROJECT)
					ConfigurationTool.saveConfig(ConfigType.PROJECT)

		return parameters

	def _askForParameterValue(self, parameterName):
		""" Ask for the value of an parameter

			Parameters:
				parameterName: Name of the parameter

			Returns tuple (parameterValue, save)
		"""
		# Ask the questions
		answer = prompt([{
			"type": "input",
			"name": "value",
			"message": "What is the value of parameter %s?" % parameterName
		}, {
			"type": "confirm",
			"message": "Do you want to save this value?",
			"name": "save"
		}])

		# Check if there is an answer
		if answer == {}:
			sys.exit()

		return (answer['value'], answer['save'])
