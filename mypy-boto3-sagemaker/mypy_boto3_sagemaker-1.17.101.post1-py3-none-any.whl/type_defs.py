"""
Type annotations for sagemaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker.type_defs import ActionSourceTypeDef

    data: ActionSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionStatusType,
    AlgorithmSortByType,
    AlgorithmStatusType,
    AppImageConfigSortKeyType,
    AppInstanceTypeType,
    AppNetworkAccessTypeType,
    AppStatusType,
    AppTypeType,
    ArtifactSourceIdTypeType,
    AssemblyTypeType,
    AssociationEdgeTypeType,
    AthenaResultCompressionTypeType,
    AthenaResultFormatType,
    AuthModeType,
    AutoMLJobObjectiveTypeType,
    AutoMLJobSecondaryStatusType,
    AutoMLJobStatusType,
    AutoMLMetricEnumType,
    AutoMLS3DataTypeType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    AwsManagedHumanLoopRequestSourceType,
    BatchStrategyType,
    BooleanOperatorType,
    CandidateSortByType,
    CandidateStatusType,
    CandidateStepTypeType,
    CapacitySizeTypeType,
    CaptureModeType,
    CaptureStatusType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    CompressionTypeType,
    ConditionOutcomeType,
    ContainerModeType,
    ContentClassifierType,
    DataDistributionTypeType,
    DetailedAlgorithmStatusType,
    DetailedModelPackageStatusType,
    DirectInternetAccessType,
    DomainStatusType,
    EdgePackagingJobStatusType,
    EdgePresetDeploymentStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    FeatureTypeType,
    FileSystemAccessModeType,
    FileSystemTypeType,
    FlowDefinitionStatusType,
    FrameworkType,
    HumanTaskUiStatusType,
    HyperParameterScalingTypeType,
    HyperParameterTuningJobObjectiveTypeType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    HyperParameterTuningJobStrategyTypeType,
    HyperParameterTuningJobWarmStartTypeType,
    ImageSortByType,
    ImageSortOrderType,
    ImageStatusType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    ImageVersionStatusType,
    InferenceExecutionModeType,
    InputModeType,
    InstanceTypeType,
    JoinSourceType,
    LabelingJobStatusType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgePackagingJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    ModelApprovalStatusType,
    ModelCacheSettingType,
    ModelPackageGroupSortByType,
    ModelPackageGroupStatusType,
    ModelPackageSortByType,
    ModelPackageStatusType,
    ModelPackageTypeType,
    ModelSortKeyType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringProblemTypeType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    NotebookOutputOptionType,
    ObjectiveStatusType,
    OfflineStoreStatusValueType,
    OperatorType,
    OrderKeyType,
    ParameterTypeType,
    PipelineExecutionStatusType,
    ProblemTypeType,
    ProcessingInstanceTypeType,
    ProcessingJobStatusType,
    ProcessingS3CompressionTypeType,
    ProcessingS3DataDistributionTypeType,
    ProcessingS3DataTypeType,
    ProcessingS3InputModeType,
    ProcessingS3UploadModeType,
    ProductionVariantAcceleratorTypeType,
    ProductionVariantInstanceTypeType,
    ProfilingStatusType,
    ProjectSortByType,
    ProjectSortOrderType,
    ProjectStatusType,
    RecordWrapperType,
    RedshiftResultCompressionTypeType,
    RedshiftResultFormatType,
    RepositoryAccessModeType,
    ResourceTypeType,
    RetentionTypeType,
    RootAccessType,
    RuleEvaluationStatusType,
    S3DataDistributionType,
    S3DataTypeType,
    SagemakerServicecatalogStatusType,
    ScheduleStatusType,
    SearchSortOrderType,
    SecondaryStatusType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SplitTypeType,
    StepStatusType,
    TargetDeviceType,
    TargetPlatformAcceleratorType,
    TargetPlatformArchType,
    TargetPlatformOsType,
    TrafficRoutingConfigTypeType,
    TrainingInputModeType,
    TrainingInstanceTypeType,
    TrainingJobEarlyStoppingTypeType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformInstanceTypeType,
    TransformJobStatusType,
    TrialComponentPrimaryStatusType,
    UserProfileSortKeyType,
    UserProfileStatusType,
    VariantPropertyTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionSourceTypeDef",
    "ActionSummaryTypeDef",
    "AddAssociationRequestTypeDef",
    "AddAssociationResponseResponseTypeDef",
    "AddTagsInputTypeDef",
    "AddTagsOutputResponseTypeDef",
    "AgentVersionTypeDef",
    "AlarmTypeDef",
    "AlgorithmSpecificationTypeDef",
    "AlgorithmStatusDetailsTypeDef",
    "AlgorithmStatusItemTypeDef",
    "AlgorithmSummaryTypeDef",
    "AlgorithmValidationProfileTypeDef",
    "AlgorithmValidationSpecificationTypeDef",
    "AnnotationConsolidationConfigTypeDef",
    "AppDetailsTypeDef",
    "AppImageConfigDetailsTypeDef",
    "AppSpecificationTypeDef",
    "ArtifactSourceTypeDef",
    "ArtifactSourceTypeTypeDef",
    "ArtifactSummaryTypeDef",
    "AssociateTrialComponentRequestTypeDef",
    "AssociateTrialComponentResponseResponseTypeDef",
    "AssociationSummaryTypeDef",
    "AthenaDatasetDefinitionTypeDef",
    "AutoMLCandidateStepTypeDef",
    "AutoMLCandidateTypeDef",
    "AutoMLChannelTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "AutoMLDataSourceTypeDef",
    "AutoMLJobArtifactsTypeDef",
    "AutoMLJobCompletionCriteriaTypeDef",
    "AutoMLJobConfigTypeDef",
    "AutoMLJobObjectiveTypeDef",
    "AutoMLJobSummaryTypeDef",
    "AutoMLOutputDataConfigTypeDef",
    "AutoMLPartialFailureReasonTypeDef",
    "AutoMLS3DataSourceTypeDef",
    "AutoMLSecurityConfigTypeDef",
    "AutoRollbackConfigTypeDef",
    "BiasTypeDef",
    "BlueGreenUpdatePolicyTypeDef",
    "CacheHitResultTypeDef",
    "CallbackStepMetadataTypeDef",
    "CandidateArtifactLocationsTypeDef",
    "CandidatePropertiesTypeDef",
    "CapacitySizeTypeDef",
    "CaptureContentTypeHeaderTypeDef",
    "CaptureOptionTypeDef",
    "CategoricalParameterRangeSpecificationTypeDef",
    "CategoricalParameterRangeTypeDef",
    "ChannelSpecificationTypeDef",
    "ChannelTypeDef",
    "CheckpointConfigTypeDef",
    "CodeRepositorySummaryTypeDef",
    "CognitoConfigTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "CollectionConfigurationTypeDef",
    "CompilationJobSummaryTypeDef",
    "ConditionStepMetadataTypeDef",
    "ContainerDefinitionTypeDef",
    "ContextSourceTypeDef",
    "ContextSummaryTypeDef",
    "ContinuousParameterRangeSpecificationTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateActionRequestTypeDef",
    "CreateActionResponseResponseTypeDef",
    "CreateAlgorithmInputTypeDef",
    "CreateAlgorithmOutputResponseTypeDef",
    "CreateAppImageConfigRequestTypeDef",
    "CreateAppImageConfigResponseResponseTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResponseResponseTypeDef",
    "CreateArtifactRequestTypeDef",
    "CreateArtifactResponseResponseTypeDef",
    "CreateAutoMLJobRequestTypeDef",
    "CreateAutoMLJobResponseResponseTypeDef",
    "CreateCodeRepositoryInputTypeDef",
    "CreateCodeRepositoryOutputResponseTypeDef",
    "CreateCompilationJobRequestTypeDef",
    "CreateCompilationJobResponseResponseTypeDef",
    "CreateContextRequestTypeDef",
    "CreateContextResponseResponseTypeDef",
    "CreateDataQualityJobDefinitionRequestTypeDef",
    "CreateDataQualityJobDefinitionResponseResponseTypeDef",
    "CreateDeviceFleetRequestTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseResponseTypeDef",
    "CreateEdgePackagingJobRequestTypeDef",
    "CreateEndpointConfigInputTypeDef",
    "CreateEndpointConfigOutputResponseTypeDef",
    "CreateEndpointInputTypeDef",
    "CreateEndpointOutputResponseTypeDef",
    "CreateExperimentRequestTypeDef",
    "CreateExperimentResponseResponseTypeDef",
    "CreateFeatureGroupRequestTypeDef",
    "CreateFeatureGroupResponseResponseTypeDef",
    "CreateFlowDefinitionRequestTypeDef",
    "CreateFlowDefinitionResponseResponseTypeDef",
    "CreateHumanTaskUiRequestTypeDef",
    "CreateHumanTaskUiResponseResponseTypeDef",
    "CreateHyperParameterTuningJobRequestTypeDef",
    "CreateHyperParameterTuningJobResponseResponseTypeDef",
    "CreateImageRequestTypeDef",
    "CreateImageResponseResponseTypeDef",
    "CreateImageVersionRequestTypeDef",
    "CreateImageVersionResponseResponseTypeDef",
    "CreateLabelingJobRequestTypeDef",
    "CreateLabelingJobResponseResponseTypeDef",
    "CreateModelBiasJobDefinitionRequestTypeDef",
    "CreateModelBiasJobDefinitionResponseResponseTypeDef",
    "CreateModelExplainabilityJobDefinitionRequestTypeDef",
    "CreateModelExplainabilityJobDefinitionResponseResponseTypeDef",
    "CreateModelInputTypeDef",
    "CreateModelOutputResponseTypeDef",
    "CreateModelPackageGroupInputTypeDef",
    "CreateModelPackageGroupOutputResponseTypeDef",
    "CreateModelPackageInputTypeDef",
    "CreateModelPackageOutputResponseTypeDef",
    "CreateModelQualityJobDefinitionRequestTypeDef",
    "CreateModelQualityJobDefinitionResponseResponseTypeDef",
    "CreateMonitoringScheduleRequestTypeDef",
    "CreateMonitoringScheduleResponseResponseTypeDef",
    "CreateNotebookInstanceInputTypeDef",
    "CreateNotebookInstanceLifecycleConfigInputTypeDef",
    "CreateNotebookInstanceLifecycleConfigOutputResponseTypeDef",
    "CreateNotebookInstanceOutputResponseTypeDef",
    "CreatePipelineRequestTypeDef",
    "CreatePipelineResponseResponseTypeDef",
    "CreatePresignedDomainUrlRequestTypeDef",
    "CreatePresignedDomainUrlResponseResponseTypeDef",
    "CreatePresignedNotebookInstanceUrlInputTypeDef",
    "CreatePresignedNotebookInstanceUrlOutputResponseTypeDef",
    "CreateProcessingJobRequestTypeDef",
    "CreateProcessingJobResponseResponseTypeDef",
    "CreateProjectInputTypeDef",
    "CreateProjectOutputResponseTypeDef",
    "CreateTrainingJobRequestTypeDef",
    "CreateTrainingJobResponseResponseTypeDef",
    "CreateTransformJobRequestTypeDef",
    "CreateTransformJobResponseResponseTypeDef",
    "CreateTrialComponentRequestTypeDef",
    "CreateTrialComponentResponseResponseTypeDef",
    "CreateTrialRequestTypeDef",
    "CreateTrialResponseResponseTypeDef",
    "CreateUserProfileRequestTypeDef",
    "CreateUserProfileResponseResponseTypeDef",
    "CreateWorkforceRequestTypeDef",
    "CreateWorkforceResponseResponseTypeDef",
    "CreateWorkteamRequestTypeDef",
    "CreateWorkteamResponseResponseTypeDef",
    "CustomImageTypeDef",
    "DataCaptureConfigSummaryTypeDef",
    "DataCaptureConfigTypeDef",
    "DataCatalogConfigTypeDef",
    "DataProcessingTypeDef",
    "DataQualityAppSpecificationTypeDef",
    "DataQualityBaselineConfigTypeDef",
    "DataQualityJobInputTypeDef",
    "DataSourceTypeDef",
    "DatasetDefinitionTypeDef",
    "DebugHookConfigTypeDef",
    "DebugRuleConfigurationTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "DeleteActionRequestTypeDef",
    "DeleteActionResponseResponseTypeDef",
    "DeleteAlgorithmInputTypeDef",
    "DeleteAppImageConfigRequestTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteArtifactRequestTypeDef",
    "DeleteArtifactResponseResponseTypeDef",
    "DeleteAssociationRequestTypeDef",
    "DeleteAssociationResponseResponseTypeDef",
    "DeleteCodeRepositoryInputTypeDef",
    "DeleteContextRequestTypeDef",
    "DeleteContextResponseResponseTypeDef",
    "DeleteDataQualityJobDefinitionRequestTypeDef",
    "DeleteDeviceFleetRequestTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteEndpointConfigInputTypeDef",
    "DeleteEndpointInputTypeDef",
    "DeleteExperimentRequestTypeDef",
    "DeleteExperimentResponseResponseTypeDef",
    "DeleteFeatureGroupRequestTypeDef",
    "DeleteFlowDefinitionRequestTypeDef",
    "DeleteHumanTaskUiRequestTypeDef",
    "DeleteImageRequestTypeDef",
    "DeleteImageVersionRequestTypeDef",
    "DeleteModelBiasJobDefinitionRequestTypeDef",
    "DeleteModelExplainabilityJobDefinitionRequestTypeDef",
    "DeleteModelInputTypeDef",
    "DeleteModelPackageGroupInputTypeDef",
    "DeleteModelPackageGroupPolicyInputTypeDef",
    "DeleteModelPackageInputTypeDef",
    "DeleteModelQualityJobDefinitionRequestTypeDef",
    "DeleteMonitoringScheduleRequestTypeDef",
    "DeleteNotebookInstanceInputTypeDef",
    "DeleteNotebookInstanceLifecycleConfigInputTypeDef",
    "DeletePipelineRequestTypeDef",
    "DeletePipelineResponseResponseTypeDef",
    "DeleteProjectInputTypeDef",
    "DeleteTagsInputTypeDef",
    "DeleteTrialComponentRequestTypeDef",
    "DeleteTrialComponentResponseResponseTypeDef",
    "DeleteTrialRequestTypeDef",
    "DeleteTrialResponseResponseTypeDef",
    "DeleteUserProfileRequestTypeDef",
    "DeleteWorkforceRequestTypeDef",
    "DeleteWorkteamRequestTypeDef",
    "DeleteWorkteamResponseResponseTypeDef",
    "DeployedImageTypeDef",
    "DeploymentConfigTypeDef",
    "DeregisterDevicesRequestTypeDef",
    "DescribeActionRequestTypeDef",
    "DescribeActionResponseResponseTypeDef",
    "DescribeAlgorithmInputTypeDef",
    "DescribeAlgorithmOutputResponseTypeDef",
    "DescribeAppImageConfigRequestTypeDef",
    "DescribeAppImageConfigResponseResponseTypeDef",
    "DescribeAppRequestTypeDef",
    "DescribeAppResponseResponseTypeDef",
    "DescribeArtifactRequestTypeDef",
    "DescribeArtifactResponseResponseTypeDef",
    "DescribeAutoMLJobRequestTypeDef",
    "DescribeAutoMLJobResponseResponseTypeDef",
    "DescribeCodeRepositoryInputTypeDef",
    "DescribeCodeRepositoryOutputResponseTypeDef",
    "DescribeCompilationJobRequestTypeDef",
    "DescribeCompilationJobResponseResponseTypeDef",
    "DescribeContextRequestTypeDef",
    "DescribeContextResponseResponseTypeDef",
    "DescribeDataQualityJobDefinitionRequestTypeDef",
    "DescribeDataQualityJobDefinitionResponseResponseTypeDef",
    "DescribeDeviceFleetRequestTypeDef",
    "DescribeDeviceFleetResponseResponseTypeDef",
    "DescribeDeviceRequestTypeDef",
    "DescribeDeviceResponseResponseTypeDef",
    "DescribeDomainRequestTypeDef",
    "DescribeDomainResponseResponseTypeDef",
    "DescribeEdgePackagingJobRequestTypeDef",
    "DescribeEdgePackagingJobResponseResponseTypeDef",
    "DescribeEndpointConfigInputTypeDef",
    "DescribeEndpointConfigOutputResponseTypeDef",
    "DescribeEndpointInputTypeDef",
    "DescribeEndpointOutputResponseTypeDef",
    "DescribeExperimentRequestTypeDef",
    "DescribeExperimentResponseResponseTypeDef",
    "DescribeFeatureGroupRequestTypeDef",
    "DescribeFeatureGroupResponseResponseTypeDef",
    "DescribeFlowDefinitionRequestTypeDef",
    "DescribeFlowDefinitionResponseResponseTypeDef",
    "DescribeHumanTaskUiRequestTypeDef",
    "DescribeHumanTaskUiResponseResponseTypeDef",
    "DescribeHyperParameterTuningJobRequestTypeDef",
    "DescribeHyperParameterTuningJobResponseResponseTypeDef",
    "DescribeImageRequestTypeDef",
    "DescribeImageResponseResponseTypeDef",
    "DescribeImageVersionRequestTypeDef",
    "DescribeImageVersionResponseResponseTypeDef",
    "DescribeLabelingJobRequestTypeDef",
    "DescribeLabelingJobResponseResponseTypeDef",
    "DescribeModelBiasJobDefinitionRequestTypeDef",
    "DescribeModelBiasJobDefinitionResponseResponseTypeDef",
    "DescribeModelExplainabilityJobDefinitionRequestTypeDef",
    "DescribeModelExplainabilityJobDefinitionResponseResponseTypeDef",
    "DescribeModelInputTypeDef",
    "DescribeModelOutputResponseTypeDef",
    "DescribeModelPackageGroupInputTypeDef",
    "DescribeModelPackageGroupOutputResponseTypeDef",
    "DescribeModelPackageInputTypeDef",
    "DescribeModelPackageOutputResponseTypeDef",
    "DescribeModelQualityJobDefinitionRequestTypeDef",
    "DescribeModelQualityJobDefinitionResponseResponseTypeDef",
    "DescribeMonitoringScheduleRequestTypeDef",
    "DescribeMonitoringScheduleResponseResponseTypeDef",
    "DescribeNotebookInstanceInputTypeDef",
    "DescribeNotebookInstanceLifecycleConfigInputTypeDef",
    "DescribeNotebookInstanceLifecycleConfigOutputResponseTypeDef",
    "DescribeNotebookInstanceOutputResponseTypeDef",
    "DescribePipelineDefinitionForExecutionRequestTypeDef",
    "DescribePipelineDefinitionForExecutionResponseResponseTypeDef",
    "DescribePipelineExecutionRequestTypeDef",
    "DescribePipelineExecutionResponseResponseTypeDef",
    "DescribePipelineRequestTypeDef",
    "DescribePipelineResponseResponseTypeDef",
    "DescribeProcessingJobRequestTypeDef",
    "DescribeProcessingJobResponseResponseTypeDef",
    "DescribeProjectInputTypeDef",
    "DescribeProjectOutputResponseTypeDef",
    "DescribeSubscribedWorkteamRequestTypeDef",
    "DescribeSubscribedWorkteamResponseResponseTypeDef",
    "DescribeTrainingJobRequestTypeDef",
    "DescribeTrainingJobResponseResponseTypeDef",
    "DescribeTransformJobRequestTypeDef",
    "DescribeTransformJobResponseResponseTypeDef",
    "DescribeTrialComponentRequestTypeDef",
    "DescribeTrialComponentResponseResponseTypeDef",
    "DescribeTrialRequestTypeDef",
    "DescribeTrialResponseResponseTypeDef",
    "DescribeUserProfileRequestTypeDef",
    "DescribeUserProfileResponseResponseTypeDef",
    "DescribeWorkforceRequestTypeDef",
    "DescribeWorkforceResponseResponseTypeDef",
    "DescribeWorkteamRequestTypeDef",
    "DescribeWorkteamResponseResponseTypeDef",
    "DesiredWeightAndCapacityTypeDef",
    "DeviceFleetSummaryTypeDef",
    "DeviceStatsTypeDef",
    "DeviceSummaryTypeDef",
    "DeviceTypeDef",
    "DisassociateTrialComponentRequestTypeDef",
    "DisassociateTrialComponentResponseResponseTypeDef",
    "DomainDetailsTypeDef",
    "EdgeModelStatTypeDef",
    "EdgeModelSummaryTypeDef",
    "EdgeModelTypeDef",
    "EdgeOutputConfigTypeDef",
    "EdgePackagingJobSummaryTypeDef",
    "EdgePresetDeploymentOutputTypeDef",
    "EndpointConfigSummaryTypeDef",
    "EndpointInputTypeDef",
    "EndpointSummaryTypeDef",
    "EndpointTypeDef",
    "ExperimentConfigTypeDef",
    "ExperimentSourceTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTypeDef",
    "ExplainabilityTypeDef",
    "FeatureDefinitionTypeDef",
    "FeatureGroupSummaryTypeDef",
    "FeatureGroupTypeDef",
    "FileSystemConfigTypeDef",
    "FileSystemDataSourceTypeDef",
    "FilterTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "FlowDefinitionOutputConfigTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "GetDeviceFleetReportRequestTypeDef",
    "GetDeviceFleetReportResponseResponseTypeDef",
    "GetModelPackageGroupPolicyInputTypeDef",
    "GetModelPackageGroupPolicyOutputResponseTypeDef",
    "GetSagemakerServicecatalogPortfolioStatusOutputResponseTypeDef",
    "GetSearchSuggestionsRequestTypeDef",
    "GetSearchSuggestionsResponseResponseTypeDef",
    "GitConfigForUpdateTypeDef",
    "GitConfigTypeDef",
    "HumanLoopActivationConditionsConfigTypeDef",
    "HumanLoopActivationConfigTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopRequestSourceTypeDef",
    "HumanTaskConfigTypeDef",
    "HumanTaskUiSummaryTypeDef",
    "HyperParameterAlgorithmSpecificationTypeDef",
    "HyperParameterSpecificationTypeDef",
    "HyperParameterTrainingJobDefinitionTypeDef",
    "HyperParameterTrainingJobSummaryTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "HyperParameterTuningJobObjectiveTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    "ImageConfigTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "InferenceExecutionConfigTypeDef",
    "InferenceSpecificationTypeDef",
    "InputConfigTypeDef",
    "IntegerParameterRangeSpecificationTypeDef",
    "IntegerParameterRangeTypeDef",
    "JupyterServerAppSettingsTypeDef",
    "KernelGatewayAppSettingsTypeDef",
    "KernelGatewayImageConfigTypeDef",
    "KernelSpecTypeDef",
    "LabelCountersForWorkteamTypeDef",
    "LabelCountersTypeDef",
    "LabelingJobAlgorithmsConfigTypeDef",
    "LabelingJobDataAttributesTypeDef",
    "LabelingJobDataSourceTypeDef",
    "LabelingJobForWorkteamSummaryTypeDef",
    "LabelingJobInputConfigTypeDef",
    "LabelingJobOutputConfigTypeDef",
    "LabelingJobOutputTypeDef",
    "LabelingJobResourceConfigTypeDef",
    "LabelingJobS3DataSourceTypeDef",
    "LabelingJobSnsDataSourceTypeDef",
    "LabelingJobStoppingConditionsTypeDef",
    "LabelingJobSummaryTypeDef",
    "ListActionsRequestTypeDef",
    "ListActionsResponseResponseTypeDef",
    "ListAlgorithmsInputTypeDef",
    "ListAlgorithmsOutputResponseTypeDef",
    "ListAppImageConfigsRequestTypeDef",
    "ListAppImageConfigsResponseResponseTypeDef",
    "ListAppsRequestTypeDef",
    "ListAppsResponseResponseTypeDef",
    "ListArtifactsRequestTypeDef",
    "ListArtifactsResponseResponseTypeDef",
    "ListAssociationsRequestTypeDef",
    "ListAssociationsResponseResponseTypeDef",
    "ListAutoMLJobsRequestTypeDef",
    "ListAutoMLJobsResponseResponseTypeDef",
    "ListCandidatesForAutoMLJobRequestTypeDef",
    "ListCandidatesForAutoMLJobResponseResponseTypeDef",
    "ListCodeRepositoriesInputTypeDef",
    "ListCodeRepositoriesOutputResponseTypeDef",
    "ListCompilationJobsRequestTypeDef",
    "ListCompilationJobsResponseResponseTypeDef",
    "ListContextsRequestTypeDef",
    "ListContextsResponseResponseTypeDef",
    "ListDataQualityJobDefinitionsRequestTypeDef",
    "ListDataQualityJobDefinitionsResponseResponseTypeDef",
    "ListDeviceFleetsRequestTypeDef",
    "ListDeviceFleetsResponseResponseTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResponseResponseTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseResponseTypeDef",
    "ListEdgePackagingJobsRequestTypeDef",
    "ListEdgePackagingJobsResponseResponseTypeDef",
    "ListEndpointConfigsInputTypeDef",
    "ListEndpointConfigsOutputResponseTypeDef",
    "ListEndpointsInputTypeDef",
    "ListEndpointsOutputResponseTypeDef",
    "ListExperimentsRequestTypeDef",
    "ListExperimentsResponseResponseTypeDef",
    "ListFeatureGroupsRequestTypeDef",
    "ListFeatureGroupsResponseResponseTypeDef",
    "ListFlowDefinitionsRequestTypeDef",
    "ListFlowDefinitionsResponseResponseTypeDef",
    "ListHumanTaskUisRequestTypeDef",
    "ListHumanTaskUisResponseResponseTypeDef",
    "ListHyperParameterTuningJobsRequestTypeDef",
    "ListHyperParameterTuningJobsResponseResponseTypeDef",
    "ListImageVersionsRequestTypeDef",
    "ListImageVersionsResponseResponseTypeDef",
    "ListImagesRequestTypeDef",
    "ListImagesResponseResponseTypeDef",
    "ListLabelingJobsForWorkteamRequestTypeDef",
    "ListLabelingJobsForWorkteamResponseResponseTypeDef",
    "ListLabelingJobsRequestTypeDef",
    "ListLabelingJobsResponseResponseTypeDef",
    "ListModelBiasJobDefinitionsRequestTypeDef",
    "ListModelBiasJobDefinitionsResponseResponseTypeDef",
    "ListModelExplainabilityJobDefinitionsRequestTypeDef",
    "ListModelExplainabilityJobDefinitionsResponseResponseTypeDef",
    "ListModelPackageGroupsInputTypeDef",
    "ListModelPackageGroupsOutputResponseTypeDef",
    "ListModelPackagesInputTypeDef",
    "ListModelPackagesOutputResponseTypeDef",
    "ListModelQualityJobDefinitionsRequestTypeDef",
    "ListModelQualityJobDefinitionsResponseResponseTypeDef",
    "ListModelsInputTypeDef",
    "ListModelsOutputResponseTypeDef",
    "ListMonitoringExecutionsRequestTypeDef",
    "ListMonitoringExecutionsResponseResponseTypeDef",
    "ListMonitoringSchedulesRequestTypeDef",
    "ListMonitoringSchedulesResponseResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsInputTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputResponseTypeDef",
    "ListNotebookInstancesInputTypeDef",
    "ListNotebookInstancesOutputResponseTypeDef",
    "ListPipelineExecutionStepsRequestTypeDef",
    "ListPipelineExecutionStepsResponseResponseTypeDef",
    "ListPipelineExecutionsRequestTypeDef",
    "ListPipelineExecutionsResponseResponseTypeDef",
    "ListPipelineParametersForExecutionRequestTypeDef",
    "ListPipelineParametersForExecutionResponseResponseTypeDef",
    "ListPipelinesRequestTypeDef",
    "ListPipelinesResponseResponseTypeDef",
    "ListProcessingJobsRequestTypeDef",
    "ListProcessingJobsResponseResponseTypeDef",
    "ListProjectsInputTypeDef",
    "ListProjectsOutputResponseTypeDef",
    "ListSubscribedWorkteamsRequestTypeDef",
    "ListSubscribedWorkteamsResponseResponseTypeDef",
    "ListTagsInputTypeDef",
    "ListTagsOutputResponseTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobRequestTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseResponseTypeDef",
    "ListTrainingJobsRequestTypeDef",
    "ListTrainingJobsResponseResponseTypeDef",
    "ListTransformJobsRequestTypeDef",
    "ListTransformJobsResponseResponseTypeDef",
    "ListTrialComponentsRequestTypeDef",
    "ListTrialComponentsResponseResponseTypeDef",
    "ListTrialsRequestTypeDef",
    "ListTrialsResponseResponseTypeDef",
    "ListUserProfilesRequestTypeDef",
    "ListUserProfilesResponseResponseTypeDef",
    "ListWorkforcesRequestTypeDef",
    "ListWorkforcesResponseResponseTypeDef",
    "ListWorkteamsRequestTypeDef",
    "ListWorkteamsResponseResponseTypeDef",
    "MemberDefinitionTypeDef",
    "MetadataPropertiesTypeDef",
    "MetricDataTypeDef",
    "MetricDefinitionTypeDef",
    "MetricsSourceTypeDef",
    "ModelArtifactsTypeDef",
    "ModelBiasAppSpecificationTypeDef",
    "ModelBiasBaselineConfigTypeDef",
    "ModelBiasJobInputTypeDef",
    "ModelClientConfigTypeDef",
    "ModelDataQualityTypeDef",
    "ModelDeployConfigTypeDef",
    "ModelDeployResultTypeDef",
    "ModelDigestsTypeDef",
    "ModelExplainabilityAppSpecificationTypeDef",
    "ModelExplainabilityBaselineConfigTypeDef",
    "ModelExplainabilityJobInputTypeDef",
    "ModelMetricsTypeDef",
    "ModelPackageContainerDefinitionTypeDef",
    "ModelPackageGroupSummaryTypeDef",
    "ModelPackageGroupTypeDef",
    "ModelPackageStatusDetailsTypeDef",
    "ModelPackageStatusItemTypeDef",
    "ModelPackageSummaryTypeDef",
    "ModelPackageTypeDef",
    "ModelPackageValidationProfileTypeDef",
    "ModelPackageValidationSpecificationTypeDef",
    "ModelQualityAppSpecificationTypeDef",
    "ModelQualityBaselineConfigTypeDef",
    "ModelQualityJobInputTypeDef",
    "ModelQualityTypeDef",
    "ModelStepMetadataTypeDef",
    "ModelSummaryTypeDef",
    "MonitoringAppSpecificationTypeDef",
    "MonitoringBaselineConfigTypeDef",
    "MonitoringClusterConfigTypeDef",
    "MonitoringConstraintsResourceTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "MonitoringGroundTruthS3InputTypeDef",
    "MonitoringInputTypeDef",
    "MonitoringJobDefinitionSummaryTypeDef",
    "MonitoringJobDefinitionTypeDef",
    "MonitoringNetworkConfigTypeDef",
    "MonitoringOutputConfigTypeDef",
    "MonitoringOutputTypeDef",
    "MonitoringResourcesTypeDef",
    "MonitoringS3OutputTypeDef",
    "MonitoringScheduleConfigTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "MonitoringScheduleTypeDef",
    "MonitoringStatisticsResourceTypeDef",
    "MonitoringStoppingConditionTypeDef",
    "MultiModelConfigTypeDef",
    "NestedFiltersTypeDef",
    "NetworkConfigTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "NotebookInstanceLifecycleHookTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "OfflineStoreConfigTypeDef",
    "OfflineStoreStatusTypeDef",
    "OidcConfigForResponseTypeDef",
    "OidcConfigTypeDef",
    "OidcMemberDefinitionTypeDef",
    "OnlineStoreConfigTypeDef",
    "OnlineStoreSecurityConfigTypeDef",
    "OutputConfigTypeDef",
    "OutputDataConfigTypeDef",
    "OutputParameterTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterRangeTypeDef",
    "ParameterRangesTypeDef",
    "ParameterTypeDef",
    "ParentHyperParameterTuningJobTypeDef",
    "ParentTypeDef",
    "PipelineExecutionStepMetadataTypeDef",
    "PipelineExecutionStepTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineExperimentConfigTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "ProcessingClusterConfigTypeDef",
    "ProcessingFeatureStoreOutputTypeDef",
    "ProcessingInputTypeDef",
    "ProcessingJobStepMetadataTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ProcessingJobTypeDef",
    "ProcessingOutputConfigTypeDef",
    "ProcessingOutputTypeDef",
    "ProcessingResourcesTypeDef",
    "ProcessingS3InputTypeDef",
    "ProcessingS3OutputTypeDef",
    "ProcessingStoppingConditionTypeDef",
    "ProductionVariantCoreDumpConfigTypeDef",
    "ProductionVariantSummaryTypeDef",
    "ProductionVariantTypeDef",
    "ProfilerConfigForUpdateTypeDef",
    "ProfilerConfigTypeDef",
    "ProfilerRuleConfigurationTypeDef",
    "ProfilerRuleEvaluationStatusTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNameQueryTypeDef",
    "PropertyNameSuggestionTypeDef",
    "ProvisioningParameterTypeDef",
    "PublicWorkforceTaskPriceTypeDef",
    "PutModelPackageGroupPolicyInputTypeDef",
    "PutModelPackageGroupPolicyOutputResponseTypeDef",
    "RedshiftDatasetDefinitionTypeDef",
    "RegisterDevicesRequestTypeDef",
    "RegisterModelStepMetadataTypeDef",
    "RenderUiTemplateRequestTypeDef",
    "RenderUiTemplateResponseResponseTypeDef",
    "RenderableTaskTypeDef",
    "RenderingErrorTypeDef",
    "RepositoryAuthConfigTypeDef",
    "ResolvedAttributesTypeDef",
    "ResourceConfigTypeDef",
    "ResourceLimitsTypeDef",
    "ResourceSpecTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPolicyTypeDef",
    "RetryStrategyTypeDef",
    "S3DataSourceTypeDef",
    "S3StorageConfigTypeDef",
    "ScheduleConfigTypeDef",
    "SearchExpressionTypeDef",
    "SearchRecordTypeDef",
    "SearchRequestTypeDef",
    "SearchResponseResponseTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "SendPipelineExecutionStepFailureRequestTypeDef",
    "SendPipelineExecutionStepFailureResponseResponseTypeDef",
    "SendPipelineExecutionStepSuccessRequestTypeDef",
    "SendPipelineExecutionStepSuccessResponseResponseTypeDef",
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    "ServiceCatalogProvisioningDetailsTypeDef",
    "SharingSettingsTypeDef",
    "ShuffleConfigTypeDef",
    "SourceAlgorithmSpecificationTypeDef",
    "SourceAlgorithmTypeDef",
    "SourceIpConfigTypeDef",
    "StartMonitoringScheduleRequestTypeDef",
    "StartNotebookInstanceInputTypeDef",
    "StartPipelineExecutionRequestTypeDef",
    "StartPipelineExecutionResponseResponseTypeDef",
    "StopAutoMLJobRequestTypeDef",
    "StopCompilationJobRequestTypeDef",
    "StopEdgePackagingJobRequestTypeDef",
    "StopHyperParameterTuningJobRequestTypeDef",
    "StopLabelingJobRequestTypeDef",
    "StopMonitoringScheduleRequestTypeDef",
    "StopNotebookInstanceInputTypeDef",
    "StopPipelineExecutionRequestTypeDef",
    "StopPipelineExecutionResponseResponseTypeDef",
    "StopProcessingJobRequestTypeDef",
    "StopTrainingJobRequestTypeDef",
    "StopTransformJobRequestTypeDef",
    "StoppingConditionTypeDef",
    "SubscribedWorkteamTypeDef",
    "SuggestionQueryTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "TensorBoardAppSettingsTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TrainingJobDefinitionTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "TrainingJobStepMetadataTypeDef",
    "TrainingJobSummaryTypeDef",
    "TrainingJobTypeDef",
    "TrainingSpecificationTypeDef",
    "TransformDataSourceTypeDef",
    "TransformInputTypeDef",
    "TransformJobDefinitionTypeDef",
    "TransformJobStepMetadataTypeDef",
    "TransformJobSummaryTypeDef",
    "TransformJobTypeDef",
    "TransformOutputTypeDef",
    "TransformResourcesTypeDef",
    "TransformS3DataSourceTypeDef",
    "TrialComponentArtifactTypeDef",
    "TrialComponentMetricSummaryTypeDef",
    "TrialComponentParameterValueTypeDef",
    "TrialComponentSimpleSummaryTypeDef",
    "TrialComponentSourceDetailTypeDef",
    "TrialComponentSourceTypeDef",
    "TrialComponentStatusTypeDef",
    "TrialComponentSummaryTypeDef",
    "TrialComponentTypeDef",
    "TrialSourceTypeDef",
    "TrialSummaryTypeDef",
    "TrialTypeDef",
    "TuningJobCompletionCriteriaTypeDef",
    "USDTypeDef",
    "UiConfigTypeDef",
    "UiTemplateInfoTypeDef",
    "UiTemplateTypeDef",
    "UpdateActionRequestTypeDef",
    "UpdateActionResponseResponseTypeDef",
    "UpdateAppImageConfigRequestTypeDef",
    "UpdateAppImageConfigResponseResponseTypeDef",
    "UpdateArtifactRequestTypeDef",
    "UpdateArtifactResponseResponseTypeDef",
    "UpdateCodeRepositoryInputTypeDef",
    "UpdateCodeRepositoryOutputResponseTypeDef",
    "UpdateContextRequestTypeDef",
    "UpdateContextResponseResponseTypeDef",
    "UpdateDeviceFleetRequestTypeDef",
    "UpdateDevicesRequestTypeDef",
    "UpdateDomainRequestTypeDef",
    "UpdateDomainResponseResponseTypeDef",
    "UpdateEndpointInputTypeDef",
    "UpdateEndpointOutputResponseTypeDef",
    "UpdateEndpointWeightsAndCapacitiesInputTypeDef",
    "UpdateEndpointWeightsAndCapacitiesOutputResponseTypeDef",
    "UpdateExperimentRequestTypeDef",
    "UpdateExperimentResponseResponseTypeDef",
    "UpdateImageRequestTypeDef",
    "UpdateImageResponseResponseTypeDef",
    "UpdateModelPackageInputTypeDef",
    "UpdateModelPackageOutputResponseTypeDef",
    "UpdateMonitoringScheduleRequestTypeDef",
    "UpdateMonitoringScheduleResponseResponseTypeDef",
    "UpdateNotebookInstanceInputTypeDef",
    "UpdateNotebookInstanceLifecycleConfigInputTypeDef",
    "UpdatePipelineExecutionRequestTypeDef",
    "UpdatePipelineExecutionResponseResponseTypeDef",
    "UpdatePipelineRequestTypeDef",
    "UpdatePipelineResponseResponseTypeDef",
    "UpdateTrainingJobRequestTypeDef",
    "UpdateTrainingJobResponseResponseTypeDef",
    "UpdateTrialComponentRequestTypeDef",
    "UpdateTrialComponentResponseResponseTypeDef",
    "UpdateTrialRequestTypeDef",
    "UpdateTrialResponseResponseTypeDef",
    "UpdateUserProfileRequestTypeDef",
    "UpdateUserProfileResponseResponseTypeDef",
    "UpdateWorkforceRequestTypeDef",
    "UpdateWorkforceResponseResponseTypeDef",
    "UpdateWorkteamRequestTypeDef",
    "UpdateWorkteamResponseResponseTypeDef",
    "UserContextTypeDef",
    "UserProfileDetailsTypeDef",
    "UserSettingsTypeDef",
    "VariantPropertyTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
    "WorkforceTypeDef",
    "WorkteamTypeDef",
)

_RequiredActionSourceTypeDef = TypedDict(
    "_RequiredActionSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalActionSourceTypeDef = TypedDict(
    "_OptionalActionSourceTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)


class ActionSourceTypeDef(_RequiredActionSourceTypeDef, _OptionalActionSourceTypeDef):
    pass


ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "ActionArn": str,
        "ActionName": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
        "Status": ActionStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredAddAssociationRequestTypeDef = TypedDict(
    "_RequiredAddAssociationRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)
_OptionalAddAssociationRequestTypeDef = TypedDict(
    "_OptionalAddAssociationRequestTypeDef",
    {
        "AssociationType": AssociationEdgeTypeType,
    },
    total=False,
)


class AddAssociationRequestTypeDef(
    _RequiredAddAssociationRequestTypeDef, _OptionalAddAssociationRequestTypeDef
):
    pass


AddAssociationResponseResponseTypeDef = TypedDict(
    "AddAssociationResponseResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputTypeDef = TypedDict(
    "AddTagsInputTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

AddTagsOutputResponseTypeDef = TypedDict(
    "AddTagsOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": str,
        "AgentCount": int,
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
    },
    total=False,
)

_RequiredAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "EnableSageMakerMetricsTimeSeries": bool,
    },
    total=False,
)


class AlgorithmSpecificationTypeDef(
    _RequiredAlgorithmSpecificationTypeDef, _OptionalAlgorithmSpecificationTypeDef
):
    pass


AlgorithmStatusDetailsTypeDef = TypedDict(
    "AlgorithmStatusDetailsTypeDef",
    {
        "ValidationStatuses": List["AlgorithmStatusItemTypeDef"],
        "ImageScanStatuses": List["AlgorithmStatusItemTypeDef"],
    },
    total=False,
)

_RequiredAlgorithmStatusItemTypeDef = TypedDict(
    "_RequiredAlgorithmStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedAlgorithmStatusType,
    },
)
_OptionalAlgorithmStatusItemTypeDef = TypedDict(
    "_OptionalAlgorithmStatusItemTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class AlgorithmStatusItemTypeDef(
    _RequiredAlgorithmStatusItemTypeDef, _OptionalAlgorithmStatusItemTypeDef
):
    pass


_RequiredAlgorithmSummaryTypeDef = TypedDict(
    "_RequiredAlgorithmSummaryTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "CreationTime": datetime,
        "AlgorithmStatus": AlgorithmStatusType,
    },
)
_OptionalAlgorithmSummaryTypeDef = TypedDict(
    "_OptionalAlgorithmSummaryTypeDef",
    {
        "AlgorithmDescription": str,
    },
    total=False,
)


class AlgorithmSummaryTypeDef(_RequiredAlgorithmSummaryTypeDef, _OptionalAlgorithmSummaryTypeDef):
    pass


_RequiredAlgorithmValidationProfileTypeDef = TypedDict(
    "_RequiredAlgorithmValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": "TrainingJobDefinitionTypeDef",
    },
)
_OptionalAlgorithmValidationProfileTypeDef = TypedDict(
    "_OptionalAlgorithmValidationProfileTypeDef",
    {
        "TransformJobDefinition": "TransformJobDefinitionTypeDef",
    },
    total=False,
)


class AlgorithmValidationProfileTypeDef(
    _RequiredAlgorithmValidationProfileTypeDef, _OptionalAlgorithmValidationProfileTypeDef
):
    pass


AlgorithmValidationSpecificationTypeDef = TypedDict(
    "AlgorithmValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List["AlgorithmValidationProfileTypeDef"],
    },
)

AnnotationConsolidationConfigTypeDef = TypedDict(
    "AnnotationConsolidationConfigTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
    },
)

AppDetailsTypeDef = TypedDict(
    "AppDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
        "Status": AppStatusType,
        "CreationTime": datetime,
    },
    total=False,
)

AppImageConfigDetailsTypeDef = TypedDict(
    "AppImageConfigDetailsTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)

_RequiredAppSpecificationTypeDef = TypedDict(
    "_RequiredAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalAppSpecificationTypeDef = TypedDict(
    "_OptionalAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
    },
    total=False,
)


class AppSpecificationTypeDef(_RequiredAppSpecificationTypeDef, _OptionalAppSpecificationTypeDef):
    pass


_RequiredArtifactSourceTypeDef = TypedDict(
    "_RequiredArtifactSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalArtifactSourceTypeDef = TypedDict(
    "_OptionalArtifactSourceTypeDef",
    {
        "SourceTypes": List["ArtifactSourceTypeTypeDef"],
    },
    total=False,
)


class ArtifactSourceTypeDef(_RequiredArtifactSourceTypeDef, _OptionalArtifactSourceTypeDef):
    pass


ArtifactSourceTypeTypeDef = TypedDict(
    "ArtifactSourceTypeTypeDef",
    {
        "SourceIdType": ArtifactSourceIdTypeType,
        "Value": str,
    },
)

ArtifactSummaryTypeDef = TypedDict(
    "ArtifactSummaryTypeDef",
    {
        "ArtifactArn": str,
        "ArtifactName": str,
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

AssociateTrialComponentRequestTypeDef = TypedDict(
    "AssociateTrialComponentRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

AssociateTrialComponentResponseResponseTypeDef = TypedDict(
    "AssociateTrialComponentResponseResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociationSummaryTypeDef = TypedDict(
    "AssociationSummaryTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "SourceName": str,
        "DestinationName": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
    },
    total=False,
)

_RequiredAthenaDatasetDefinitionTypeDef = TypedDict(
    "_RequiredAthenaDatasetDefinitionTypeDef",
    {
        "Catalog": str,
        "Database": str,
        "QueryString": str,
        "OutputS3Uri": str,
        "OutputFormat": AthenaResultFormatType,
    },
)
_OptionalAthenaDatasetDefinitionTypeDef = TypedDict(
    "_OptionalAthenaDatasetDefinitionTypeDef",
    {
        "WorkGroup": str,
        "KmsKeyId": str,
        "OutputCompression": AthenaResultCompressionTypeType,
    },
    total=False,
)


class AthenaDatasetDefinitionTypeDef(
    _RequiredAthenaDatasetDefinitionTypeDef, _OptionalAthenaDatasetDefinitionTypeDef
):
    pass


AutoMLCandidateStepTypeDef = TypedDict(
    "AutoMLCandidateStepTypeDef",
    {
        "CandidateStepType": CandidateStepTypeType,
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
)

_RequiredAutoMLCandidateTypeDef = TypedDict(
    "_RequiredAutoMLCandidateTypeDef",
    {
        "CandidateName": str,
        "ObjectiveStatus": ObjectiveStatusType,
        "CandidateSteps": List["AutoMLCandidateStepTypeDef"],
        "CandidateStatus": CandidateStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLCandidateTypeDef = TypedDict(
    "_OptionalAutoMLCandidateTypeDef",
    {
        "FinalAutoMLJobObjectiveMetric": "FinalAutoMLJobObjectiveMetricTypeDef",
        "InferenceContainers": List["AutoMLContainerDefinitionTypeDef"],
        "EndTime": datetime,
        "FailureReason": str,
        "CandidateProperties": "CandidatePropertiesTypeDef",
    },
    total=False,
)


class AutoMLCandidateTypeDef(_RequiredAutoMLCandidateTypeDef, _OptionalAutoMLCandidateTypeDef):
    pass


_RequiredAutoMLChannelTypeDef = TypedDict(
    "_RequiredAutoMLChannelTypeDef",
    {
        "DataSource": "AutoMLDataSourceTypeDef",
        "TargetAttributeName": str,
    },
)
_OptionalAutoMLChannelTypeDef = TypedDict(
    "_OptionalAutoMLChannelTypeDef",
    {
        "CompressionType": CompressionTypeType,
    },
    total=False,
)


class AutoMLChannelTypeDef(_RequiredAutoMLChannelTypeDef, _OptionalAutoMLChannelTypeDef):
    pass


_RequiredAutoMLContainerDefinitionTypeDef = TypedDict(
    "_RequiredAutoMLContainerDefinitionTypeDef",
    {
        "Image": str,
        "ModelDataUrl": str,
    },
)
_OptionalAutoMLContainerDefinitionTypeDef = TypedDict(
    "_OptionalAutoMLContainerDefinitionTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class AutoMLContainerDefinitionTypeDef(
    _RequiredAutoMLContainerDefinitionTypeDef, _OptionalAutoMLContainerDefinitionTypeDef
):
    pass


AutoMLDataSourceTypeDef = TypedDict(
    "AutoMLDataSourceTypeDef",
    {
        "S3DataSource": "AutoMLS3DataSourceTypeDef",
    },
)

AutoMLJobArtifactsTypeDef = TypedDict(
    "AutoMLJobArtifactsTypeDef",
    {
        "CandidateDefinitionNotebookLocation": str,
        "DataExplorationNotebookLocation": str,
    },
    total=False,
)

AutoMLJobCompletionCriteriaTypeDef = TypedDict(
    "AutoMLJobCompletionCriteriaTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

AutoMLJobConfigTypeDef = TypedDict(
    "AutoMLJobConfigTypeDef",
    {
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
        "SecurityConfig": "AutoMLSecurityConfigTypeDef",
    },
    total=False,
)

AutoMLJobObjectiveTypeDef = TypedDict(
    "AutoMLJobObjectiveTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
    },
)

_RequiredAutoMLJobSummaryTypeDef = TypedDict(
    "_RequiredAutoMLJobSummaryTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLJobSummaryTypeDef = TypedDict(
    "_OptionalAutoMLJobSummaryTypeDef",
    {
        "EndTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List["AutoMLPartialFailureReasonTypeDef"],
    },
    total=False,
)


class AutoMLJobSummaryTypeDef(_RequiredAutoMLJobSummaryTypeDef, _OptionalAutoMLJobSummaryTypeDef):
    pass


_RequiredAutoMLOutputDataConfigTypeDef = TypedDict(
    "_RequiredAutoMLOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalAutoMLOutputDataConfigTypeDef = TypedDict(
    "_OptionalAutoMLOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class AutoMLOutputDataConfigTypeDef(
    _RequiredAutoMLOutputDataConfigTypeDef, _OptionalAutoMLOutputDataConfigTypeDef
):
    pass


AutoMLPartialFailureReasonTypeDef = TypedDict(
    "AutoMLPartialFailureReasonTypeDef",
    {
        "PartialFailureMessage": str,
    },
    total=False,
)

AutoMLS3DataSourceTypeDef = TypedDict(
    "AutoMLS3DataSourceTypeDef",
    {
        "S3DataType": AutoMLS3DataTypeType,
        "S3Uri": str,
    },
)

AutoMLSecurityConfigTypeDef = TypedDict(
    "AutoMLSecurityConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "EnableInterContainerTrafficEncryption": bool,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

AutoRollbackConfigTypeDef = TypedDict(
    "AutoRollbackConfigTypeDef",
    {
        "Alarms": List["AlarmTypeDef"],
    },
    total=False,
)

BiasTypeDef = TypedDict(
    "BiasTypeDef",
    {
        "Report": "MetricsSourceTypeDef",
    },
    total=False,
)

_RequiredBlueGreenUpdatePolicyTypeDef = TypedDict(
    "_RequiredBlueGreenUpdatePolicyTypeDef",
    {
        "TrafficRoutingConfiguration": "TrafficRoutingConfigTypeDef",
    },
)
_OptionalBlueGreenUpdatePolicyTypeDef = TypedDict(
    "_OptionalBlueGreenUpdatePolicyTypeDef",
    {
        "TerminationWaitInSeconds": int,
        "MaximumExecutionTimeoutInSeconds": int,
    },
    total=False,
)


class BlueGreenUpdatePolicyTypeDef(
    _RequiredBlueGreenUpdatePolicyTypeDef, _OptionalBlueGreenUpdatePolicyTypeDef
):
    pass


CacheHitResultTypeDef = TypedDict(
    "CacheHitResultTypeDef",
    {
        "SourcePipelineExecutionArn": str,
    },
    total=False,
)

CallbackStepMetadataTypeDef = TypedDict(
    "CallbackStepMetadataTypeDef",
    {
        "CallbackToken": str,
        "SqsQueueUrl": str,
        "OutputParameters": List["OutputParameterTypeDef"],
    },
    total=False,
)

CandidateArtifactLocationsTypeDef = TypedDict(
    "CandidateArtifactLocationsTypeDef",
    {
        "Explainability": str,
    },
)

CandidatePropertiesTypeDef = TypedDict(
    "CandidatePropertiesTypeDef",
    {
        "CandidateArtifactLocations": "CandidateArtifactLocationsTypeDef",
    },
    total=False,
)

CapacitySizeTypeDef = TypedDict(
    "CapacitySizeTypeDef",
    {
        "Type": CapacitySizeTypeType,
        "Value": int,
    },
)

CaptureContentTypeHeaderTypeDef = TypedDict(
    "CaptureContentTypeHeaderTypeDef",
    {
        "CsvContentTypes": List[str],
        "JsonContentTypes": List[str],
    },
    total=False,
)

CaptureOptionTypeDef = TypedDict(
    "CaptureOptionTypeDef",
    {
        "CaptureMode": CaptureModeType,
    },
)

CategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "CategoricalParameterRangeSpecificationTypeDef",
    {
        "Values": List[str],
    },
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

_RequiredChannelSpecificationTypeDef = TypedDict(
    "_RequiredChannelSpecificationTypeDef",
    {
        "Name": str,
        "SupportedContentTypes": List[str],
        "SupportedInputModes": List[TrainingInputModeType],
    },
)
_OptionalChannelSpecificationTypeDef = TypedDict(
    "_OptionalChannelSpecificationTypeDef",
    {
        "Description": str,
        "IsRequired": bool,
        "SupportedCompressionTypes": List[CompressionTypeType],
    },
    total=False,
)


class ChannelSpecificationTypeDef(
    _RequiredChannelSpecificationTypeDef, _OptionalChannelSpecificationTypeDef
):
    pass


_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef",
    {
        "ChannelName": str,
        "DataSource": "DataSourceTypeDef",
    },
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "RecordWrapperType": RecordWrapperType,
        "InputMode": TrainingInputModeType,
        "ShuffleConfig": "ShuffleConfigTypeDef",
    },
    total=False,
)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


_RequiredCheckpointConfigTypeDef = TypedDict(
    "_RequiredCheckpointConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalCheckpointConfigTypeDef = TypedDict(
    "_OptionalCheckpointConfigTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)


class CheckpointConfigTypeDef(_RequiredCheckpointConfigTypeDef, _OptionalCheckpointConfigTypeDef):
    pass


_RequiredCodeRepositorySummaryTypeDef = TypedDict(
    "_RequiredCodeRepositorySummaryTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalCodeRepositorySummaryTypeDef = TypedDict(
    "_OptionalCodeRepositorySummaryTypeDef",
    {
        "GitConfig": "GitConfigTypeDef",
    },
    total=False,
)


class CodeRepositorySummaryTypeDef(
    _RequiredCodeRepositorySummaryTypeDef, _OptionalCodeRepositorySummaryTypeDef
):
    pass


CognitoConfigTypeDef = TypedDict(
    "CognitoConfigTypeDef",
    {
        "UserPool": str,
        "ClientId": str,
    },
)

CognitoMemberDefinitionTypeDef = TypedDict(
    "CognitoMemberDefinitionTypeDef",
    {
        "UserPool": str,
        "UserGroup": str,
        "ClientId": str,
    },
)

CollectionConfigurationTypeDef = TypedDict(
    "CollectionConfigurationTypeDef",
    {
        "CollectionName": str,
        "CollectionParameters": Dict[str, str],
    },
    total=False,
)

_RequiredCompilationJobSummaryTypeDef = TypedDict(
    "_RequiredCompilationJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationJobStatus": CompilationJobStatusType,
    },
)
_OptionalCompilationJobSummaryTypeDef = TypedDict(
    "_OptionalCompilationJobSummaryTypeDef",
    {
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": TargetDeviceType,
        "CompilationTargetPlatformOs": TargetPlatformOsType,
        "CompilationTargetPlatformArch": TargetPlatformArchType,
        "CompilationTargetPlatformAccelerator": TargetPlatformAcceleratorType,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class CompilationJobSummaryTypeDef(
    _RequiredCompilationJobSummaryTypeDef, _OptionalCompilationJobSummaryTypeDef
):
    pass


ConditionStepMetadataTypeDef = TypedDict(
    "ConditionStepMetadataTypeDef",
    {
        "Outcome": ConditionOutcomeType,
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageConfig": "ImageConfigTypeDef",
        "Mode": ContainerModeType,
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
        "MultiModelConfig": "MultiModelConfigTypeDef",
    },
    total=False,
)

_RequiredContextSourceTypeDef = TypedDict(
    "_RequiredContextSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalContextSourceTypeDef = TypedDict(
    "_OptionalContextSourceTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)


class ContextSourceTypeDef(_RequiredContextSourceTypeDef, _OptionalContextSourceTypeDef):
    pass


ContextSummaryTypeDef = TypedDict(
    "ContextSummaryTypeDef",
    {
        "ContextArn": str,
        "ContextName": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ContinuousParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

_RequiredContinuousParameterRangeTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalContinuousParameterRangeTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)


class ContinuousParameterRangeTypeDef(
    _RequiredContinuousParameterRangeTypeDef, _OptionalContinuousParameterRangeTypeDef
):
    pass


_RequiredCreateActionRequestTypeDef = TypedDict(
    "_RequiredCreateActionRequestTypeDef",
    {
        "ActionName": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
    },
)
_OptionalCreateActionRequestTypeDef = TypedDict(
    "_OptionalCreateActionRequestTypeDef",
    {
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateActionRequestTypeDef(
    _RequiredCreateActionRequestTypeDef, _OptionalCreateActionRequestTypeDef
):
    pass


CreateActionResponseResponseTypeDef = TypedDict(
    "CreateActionResponseResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAlgorithmInputTypeDef = TypedDict(
    "_RequiredCreateAlgorithmInputTypeDef",
    {
        "AlgorithmName": str,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
    },
)
_OptionalCreateAlgorithmInputTypeDef = TypedDict(
    "_OptionalCreateAlgorithmInputTypeDef",
    {
        "AlgorithmDescription": str,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "AlgorithmValidationSpecificationTypeDef",
        "CertifyForMarketplace": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAlgorithmInputTypeDef(
    _RequiredCreateAlgorithmInputTypeDef, _OptionalCreateAlgorithmInputTypeDef
):
    pass


CreateAlgorithmOutputResponseTypeDef = TypedDict(
    "CreateAlgorithmOutputResponseTypeDef",
    {
        "AlgorithmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppImageConfigRequestTypeDef = TypedDict(
    "_RequiredCreateAppImageConfigRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)
_OptionalCreateAppImageConfigRequestTypeDef = TypedDict(
    "_OptionalCreateAppImageConfigRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)


class CreateAppImageConfigRequestTypeDef(
    _RequiredCreateAppImageConfigRequestTypeDef, _OptionalCreateAppImageConfigRequestTypeDef
):
    pass


CreateAppImageConfigResponseResponseTypeDef = TypedDict(
    "CreateAppImageConfigResponseResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppRequestTypeDef = TypedDict(
    "_RequiredCreateAppRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalCreateAppRequestTypeDef = TypedDict(
    "_OptionalCreateAppRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResourceSpec": "ResourceSpecTypeDef",
    },
    total=False,
)


class CreateAppRequestTypeDef(_RequiredCreateAppRequestTypeDef, _OptionalCreateAppRequestTypeDef):
    pass


CreateAppResponseResponseTypeDef = TypedDict(
    "CreateAppResponseResponseTypeDef",
    {
        "AppArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArtifactRequestTypeDef = TypedDict(
    "_RequiredCreateArtifactRequestTypeDef",
    {
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
    },
)
_OptionalCreateArtifactRequestTypeDef = TypedDict(
    "_OptionalCreateArtifactRequestTypeDef",
    {
        "ArtifactName": str,
        "Properties": Dict[str, str],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateArtifactRequestTypeDef(
    _RequiredCreateArtifactRequestTypeDef, _OptionalCreateArtifactRequestTypeDef
):
    pass


CreateArtifactResponseResponseTypeDef = TypedDict(
    "CreateArtifactResponseResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAutoMLJobRequestTypeDef = TypedDict(
    "_RequiredCreateAutoMLJobRequestTypeDef",
    {
        "AutoMLJobName": str,
        "InputDataConfig": List["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateAutoMLJobRequestTypeDef = TypedDict(
    "_OptionalCreateAutoMLJobRequestTypeDef",
    {
        "ProblemType": ProblemTypeType,
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "AutoMLJobConfig": "AutoMLJobConfigTypeDef",
        "GenerateCandidateDefinitionsOnly": bool,
        "Tags": List["TagTypeDef"],
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
    },
    total=False,
)


class CreateAutoMLJobRequestTypeDef(
    _RequiredCreateAutoMLJobRequestTypeDef, _OptionalCreateAutoMLJobRequestTypeDef
):
    pass


CreateAutoMLJobResponseResponseTypeDef = TypedDict(
    "CreateAutoMLJobResponseResponseTypeDef",
    {
        "AutoMLJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCodeRepositoryInputTypeDef = TypedDict(
    "_RequiredCreateCodeRepositoryInputTypeDef",
    {
        "CodeRepositoryName": str,
        "GitConfig": "GitConfigTypeDef",
    },
)
_OptionalCreateCodeRepositoryInputTypeDef = TypedDict(
    "_OptionalCreateCodeRepositoryInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCodeRepositoryInputTypeDef(
    _RequiredCreateCodeRepositoryInputTypeDef, _OptionalCreateCodeRepositoryInputTypeDef
):
    pass


CreateCodeRepositoryOutputResponseTypeDef = TypedDict(
    "CreateCodeRepositoryOutputResponseTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCompilationJobRequestTypeDef = TypedDict(
    "_RequiredCreateCompilationJobRequestTypeDef",
    {
        "CompilationJobName": str,
        "RoleArn": str,
        "InputConfig": "InputConfigTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalCreateCompilationJobRequestTypeDef = TypedDict(
    "_OptionalCreateCompilationJobRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCompilationJobRequestTypeDef(
    _RequiredCreateCompilationJobRequestTypeDef, _OptionalCreateCompilationJobRequestTypeDef
):
    pass


CreateCompilationJobResponseResponseTypeDef = TypedDict(
    "CreateCompilationJobResponseResponseTypeDef",
    {
        "CompilationJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContextRequestTypeDef = TypedDict(
    "_RequiredCreateContextRequestTypeDef",
    {
        "ContextName": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
    },
)
_OptionalCreateContextRequestTypeDef = TypedDict(
    "_OptionalCreateContextRequestTypeDef",
    {
        "Description": str,
        "Properties": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateContextRequestTypeDef(
    _RequiredCreateContextRequestTypeDef, _OptionalCreateContextRequestTypeDef
):
    pass


CreateContextResponseResponseTypeDef = TypedDict(
    "CreateContextResponseResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataQualityJobDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateDataQualityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
        "DataQualityAppSpecification": "DataQualityAppSpecificationTypeDef",
        "DataQualityJobInput": "DataQualityJobInputTypeDef",
        "DataQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateDataQualityJobDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateDataQualityJobDefinitionRequestTypeDef",
    {
        "DataQualityBaselineConfig": "DataQualityBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDataQualityJobDefinitionRequestTypeDef(
    _RequiredCreateDataQualityJobDefinitionRequestTypeDef,
    _OptionalCreateDataQualityJobDefinitionRequestTypeDef,
):
    pass


CreateDataQualityJobDefinitionResponseResponseTypeDef = TypedDict(
    "CreateDataQualityJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeviceFleetRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceFleetRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
    },
)
_OptionalCreateDeviceFleetRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceFleetRequestTypeDef",
    {
        "RoleArn": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "EnableIotRoleAlias": bool,
    },
    total=False,
)


class CreateDeviceFleetRequestTypeDef(
    _RequiredCreateDeviceFleetRequestTypeDef, _OptionalCreateDeviceFleetRequestTypeDef
):
    pass


_RequiredCreateDomainRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestTypeDef",
    {
        "DomainName": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": "UserSettingsTypeDef",
        "SubnetIds": List[str],
        "VpcId": str,
    },
)
_OptionalCreateDomainRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "KmsKeyId": str,
    },
    total=False,
)


class CreateDomainRequestTypeDef(
    _RequiredCreateDomainRequestTypeDef, _OptionalCreateDomainRequestTypeDef
):
    pass


CreateDomainResponseResponseTypeDef = TypedDict(
    "CreateDomainResponseResponseTypeDef",
    {
        "DomainArn": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEdgePackagingJobRequestTypeDef = TypedDict(
    "_RequiredCreateEdgePackagingJobRequestTypeDef",
    {
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
    },
)
_OptionalCreateEdgePackagingJobRequestTypeDef = TypedDict(
    "_OptionalCreateEdgePackagingJobRequestTypeDef",
    {
        "ResourceKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEdgePackagingJobRequestTypeDef(
    _RequiredCreateEdgePackagingJobRequestTypeDef, _OptionalCreateEdgePackagingJobRequestTypeDef
):
    pass


_RequiredCreateEndpointConfigInputTypeDef = TypedDict(
    "_RequiredCreateEndpointConfigInputTypeDef",
    {
        "EndpointConfigName": str,
        "ProductionVariants": List["ProductionVariantTypeDef"],
    },
)
_OptionalCreateEndpointConfigInputTypeDef = TypedDict(
    "_OptionalCreateEndpointConfigInputTypeDef",
    {
        "DataCaptureConfig": "DataCaptureConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
    },
    total=False,
)


class CreateEndpointConfigInputTypeDef(
    _RequiredCreateEndpointConfigInputTypeDef, _OptionalCreateEndpointConfigInputTypeDef
):
    pass


CreateEndpointConfigOutputResponseTypeDef = TypedDict(
    "CreateEndpointConfigOutputResponseTypeDef",
    {
        "EndpointConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointInputTypeDef = TypedDict(
    "_RequiredCreateEndpointInputTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
    },
)
_OptionalCreateEndpointInputTypeDef = TypedDict(
    "_OptionalCreateEndpointInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEndpointInputTypeDef(
    _RequiredCreateEndpointInputTypeDef, _OptionalCreateEndpointInputTypeDef
):
    pass


CreateEndpointOutputResponseTypeDef = TypedDict(
    "CreateEndpointOutputResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExperimentRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentRequestTypeDef",
    {
        "ExperimentName": str,
    },
)
_OptionalCreateExperimentRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateExperimentRequestTypeDef(
    _RequiredCreateExperimentRequestTypeDef, _OptionalCreateExperimentRequestTypeDef
):
    pass


CreateExperimentResponseResponseTypeDef = TypedDict(
    "CreateExperimentResponseResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFeatureGroupRequestTypeDef = TypedDict(
    "_RequiredCreateFeatureGroupRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
    },
)
_OptionalCreateFeatureGroupRequestTypeDef = TypedDict(
    "_OptionalCreateFeatureGroupRequestTypeDef",
    {
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFeatureGroupRequestTypeDef(
    _RequiredCreateFeatureGroupRequestTypeDef, _OptionalCreateFeatureGroupRequestTypeDef
):
    pass


CreateFeatureGroupResponseResponseTypeDef = TypedDict(
    "CreateFeatureGroupResponseResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateFlowDefinitionRequestTypeDef",
    {
        "FlowDefinitionName": str,
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateFlowDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateFlowDefinitionRequestTypeDef",
    {
        "HumanLoopRequestSource": "HumanLoopRequestSourceTypeDef",
        "HumanLoopActivationConfig": "HumanLoopActivationConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFlowDefinitionRequestTypeDef(
    _RequiredCreateFlowDefinitionRequestTypeDef, _OptionalCreateFlowDefinitionRequestTypeDef
):
    pass


CreateFlowDefinitionResponseResponseTypeDef = TypedDict(
    "CreateFlowDefinitionResponseResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHumanTaskUiRequestTypeDef = TypedDict(
    "_RequiredCreateHumanTaskUiRequestTypeDef",
    {
        "HumanTaskUiName": str,
        "UiTemplate": "UiTemplateTypeDef",
    },
)
_OptionalCreateHumanTaskUiRequestTypeDef = TypedDict(
    "_OptionalCreateHumanTaskUiRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateHumanTaskUiRequestTypeDef(
    _RequiredCreateHumanTaskUiRequestTypeDef, _OptionalCreateHumanTaskUiRequestTypeDef
):
    pass


CreateHumanTaskUiResponseResponseTypeDef = TypedDict(
    "CreateHumanTaskUiResponseResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHyperParameterTuningJobRequestTypeDef = TypedDict(
    "_RequiredCreateHyperParameterTuningJobRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
    },
)
_OptionalCreateHyperParameterTuningJobRequestTypeDef = TypedDict(
    "_OptionalCreateHyperParameterTuningJobRequestTypeDef",
    {
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateHyperParameterTuningJobRequestTypeDef(
    _RequiredCreateHyperParameterTuningJobRequestTypeDef,
    _OptionalCreateHyperParameterTuningJobRequestTypeDef,
):
    pass


CreateHyperParameterTuningJobResponseResponseTypeDef = TypedDict(
    "CreateHyperParameterTuningJobResponseResponseTypeDef",
    {
        "HyperParameterTuningJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestTypeDef",
    {
        "ImageName": str,
        "RoleArn": str,
    },
)
_OptionalCreateImageRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateImageRequestTypeDef(
    _RequiredCreateImageRequestTypeDef, _OptionalCreateImageRequestTypeDef
):
    pass


CreateImageResponseResponseTypeDef = TypedDict(
    "CreateImageResponseResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageVersionRequestTypeDef = TypedDict(
    "CreateImageVersionRequestTypeDef",
    {
        "BaseImage": str,
        "ClientToken": str,
        "ImageName": str,
    },
)

CreateImageVersionResponseResponseTypeDef = TypedDict(
    "CreateImageVersionResponseResponseTypeDef",
    {
        "ImageVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLabelingJobRequestTypeDef = TypedDict(
    "_RequiredCreateLabelingJobRequestTypeDef",
    {
        "LabelingJobName": str,
        "LabelAttributeName": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
    },
)
_OptionalCreateLabelingJobRequestTypeDef = TypedDict(
    "_OptionalCreateLabelingJobRequestTypeDef",
    {
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": "LabelingJobStoppingConditionsTypeDef",
        "LabelingJobAlgorithmsConfig": "LabelingJobAlgorithmsConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateLabelingJobRequestTypeDef(
    _RequiredCreateLabelingJobRequestTypeDef, _OptionalCreateLabelingJobRequestTypeDef
):
    pass


CreateLabelingJobResponseResponseTypeDef = TypedDict(
    "CreateLabelingJobResponseResponseTypeDef",
    {
        "LabelingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelBiasJobDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateModelBiasJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelBiasAppSpecification": "ModelBiasAppSpecificationTypeDef",
        "ModelBiasJobInput": "ModelBiasJobInputTypeDef",
        "ModelBiasJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateModelBiasJobDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateModelBiasJobDefinitionRequestTypeDef",
    {
        "ModelBiasBaselineConfig": "ModelBiasBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelBiasJobDefinitionRequestTypeDef(
    _RequiredCreateModelBiasJobDefinitionRequestTypeDef,
    _OptionalCreateModelBiasJobDefinitionRequestTypeDef,
):
    pass


CreateModelBiasJobDefinitionResponseResponseTypeDef = TypedDict(
    "CreateModelBiasJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelExplainabilityJobDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateModelExplainabilityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelExplainabilityAppSpecification": "ModelExplainabilityAppSpecificationTypeDef",
        "ModelExplainabilityJobInput": "ModelExplainabilityJobInputTypeDef",
        "ModelExplainabilityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateModelExplainabilityJobDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateModelExplainabilityJobDefinitionRequestTypeDef",
    {
        "ModelExplainabilityBaselineConfig": "ModelExplainabilityBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelExplainabilityJobDefinitionRequestTypeDef(
    _RequiredCreateModelExplainabilityJobDefinitionRequestTypeDef,
    _OptionalCreateModelExplainabilityJobDefinitionRequestTypeDef,
):
    pass


CreateModelExplainabilityJobDefinitionResponseResponseTypeDef = TypedDict(
    "CreateModelExplainabilityJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelInputTypeDef = TypedDict(
    "_RequiredCreateModelInputTypeDef",
    {
        "ModelName": str,
        "ExecutionRoleArn": str,
    },
)
_OptionalCreateModelInputTypeDef = TypedDict(
    "_OptionalCreateModelInputTypeDef",
    {
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "InferenceExecutionConfig": "InferenceExecutionConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "EnableNetworkIsolation": bool,
    },
    total=False,
)


class CreateModelInputTypeDef(_RequiredCreateModelInputTypeDef, _OptionalCreateModelInputTypeDef):
    pass


CreateModelOutputResponseTypeDef = TypedDict(
    "CreateModelOutputResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelPackageGroupInputTypeDef = TypedDict(
    "_RequiredCreateModelPackageGroupInputTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)
_OptionalCreateModelPackageGroupInputTypeDef = TypedDict(
    "_OptionalCreateModelPackageGroupInputTypeDef",
    {
        "ModelPackageGroupDescription": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelPackageGroupInputTypeDef(
    _RequiredCreateModelPackageGroupInputTypeDef, _OptionalCreateModelPackageGroupInputTypeDef
):
    pass


CreateModelPackageGroupOutputResponseTypeDef = TypedDict(
    "CreateModelPackageGroupOutputResponseTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelPackageInputTypeDef = TypedDict(
    "CreateModelPackageInputTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageDescription": str,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "CertifyForMarketplace": bool,
        "Tags": List["TagTypeDef"],
        "ModelApprovalStatus": ModelApprovalStatusType,
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "ClientToken": str,
    },
    total=False,
)

CreateModelPackageOutputResponseTypeDef = TypedDict(
    "CreateModelPackageOutputResponseTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelQualityJobDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateModelQualityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelQualityAppSpecification": "ModelQualityAppSpecificationTypeDef",
        "ModelQualityJobInput": "ModelQualityJobInputTypeDef",
        "ModelQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateModelQualityJobDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateModelQualityJobDefinitionRequestTypeDef",
    {
        "ModelQualityBaselineConfig": "ModelQualityBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelQualityJobDefinitionRequestTypeDef(
    _RequiredCreateModelQualityJobDefinitionRequestTypeDef,
    _OptionalCreateModelQualityJobDefinitionRequestTypeDef,
):
    pass


CreateModelQualityJobDefinitionResponseResponseTypeDef = TypedDict(
    "CreateModelQualityJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMonitoringScheduleRequestTypeDef = TypedDict(
    "_RequiredCreateMonitoringScheduleRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
    },
)
_OptionalCreateMonitoringScheduleRequestTypeDef = TypedDict(
    "_OptionalCreateMonitoringScheduleRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateMonitoringScheduleRequestTypeDef(
    _RequiredCreateMonitoringScheduleRequestTypeDef, _OptionalCreateMonitoringScheduleRequestTypeDef
):
    pass


CreateMonitoringScheduleResponseResponseTypeDef = TypedDict(
    "CreateMonitoringScheduleResponseResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNotebookInstanceInputTypeDef = TypedDict(
    "_RequiredCreateNotebookInstanceInputTypeDef",
    {
        "NotebookInstanceName": str,
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
    },
)
_OptionalCreateNotebookInstanceInputTypeDef = TypedDict(
    "_OptionalCreateNotebookInstanceInputTypeDef",
    {
        "SubnetId": str,
        "SecurityGroupIds": List[str],
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "LifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": RootAccessType,
    },
    total=False,
)


class CreateNotebookInstanceInputTypeDef(
    _RequiredCreateNotebookInstanceInputTypeDef, _OptionalCreateNotebookInstanceInputTypeDef
):
    pass


_RequiredCreateNotebookInstanceLifecycleConfigInputTypeDef = TypedDict(
    "_RequiredCreateNotebookInstanceLifecycleConfigInputTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)
_OptionalCreateNotebookInstanceLifecycleConfigInputTypeDef = TypedDict(
    "_OptionalCreateNotebookInstanceLifecycleConfigInputTypeDef",
    {
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
    },
    total=False,
)


class CreateNotebookInstanceLifecycleConfigInputTypeDef(
    _RequiredCreateNotebookInstanceLifecycleConfigInputTypeDef,
    _OptionalCreateNotebookInstanceLifecycleConfigInputTypeDef,
):
    pass


CreateNotebookInstanceLifecycleConfigOutputResponseTypeDef = TypedDict(
    "CreateNotebookInstanceLifecycleConfigOutputResponseTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNotebookInstanceOutputResponseTypeDef = TypedDict(
    "CreateNotebookInstanceOutputResponseTypeDef",
    {
        "NotebookInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestTypeDef",
    {
        "PipelineName": str,
        "PipelineDefinition": str,
        "ClientRequestToken": str,
        "RoleArn": str,
    },
)
_OptionalCreatePipelineRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestTypeDef",
    {
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePipelineRequestTypeDef(
    _RequiredCreatePipelineRequestTypeDef, _OptionalCreatePipelineRequestTypeDef
):
    pass


CreatePipelineResponseResponseTypeDef = TypedDict(
    "CreatePipelineResponseResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePresignedDomainUrlRequestTypeDef = TypedDict(
    "_RequiredCreatePresignedDomainUrlRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalCreatePresignedDomainUrlRequestTypeDef = TypedDict(
    "_OptionalCreatePresignedDomainUrlRequestTypeDef",
    {
        "SessionExpirationDurationInSeconds": int,
        "ExpiresInSeconds": int,
    },
    total=False,
)


class CreatePresignedDomainUrlRequestTypeDef(
    _RequiredCreatePresignedDomainUrlRequestTypeDef, _OptionalCreatePresignedDomainUrlRequestTypeDef
):
    pass


CreatePresignedDomainUrlResponseResponseTypeDef = TypedDict(
    "CreatePresignedDomainUrlResponseResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePresignedNotebookInstanceUrlInputTypeDef = TypedDict(
    "_RequiredCreatePresignedNotebookInstanceUrlInputTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalCreatePresignedNotebookInstanceUrlInputTypeDef = TypedDict(
    "_OptionalCreatePresignedNotebookInstanceUrlInputTypeDef",
    {
        "SessionExpirationDurationInSeconds": int,
    },
    total=False,
)


class CreatePresignedNotebookInstanceUrlInputTypeDef(
    _RequiredCreatePresignedNotebookInstanceUrlInputTypeDef,
    _OptionalCreatePresignedNotebookInstanceUrlInputTypeDef,
):
    pass


CreatePresignedNotebookInstanceUrlOutputResponseTypeDef = TypedDict(
    "CreatePresignedNotebookInstanceUrlOutputResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProcessingJobRequestTypeDef = TypedDict(
    "_RequiredCreateProcessingJobRequestTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateProcessingJobRequestTypeDef = TypedDict(
    "_OptionalCreateProcessingJobRequestTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "ExperimentConfig": "ExperimentConfigTypeDef",
    },
    total=False,
)


class CreateProcessingJobRequestTypeDef(
    _RequiredCreateProcessingJobRequestTypeDef, _OptionalCreateProcessingJobRequestTypeDef
):
    pass


CreateProcessingJobResponseResponseTypeDef = TypedDict(
    "CreateProcessingJobResponseResponseTypeDef",
    {
        "ProcessingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectInputTypeDef = TypedDict(
    "_RequiredCreateProjectInputTypeDef",
    {
        "ProjectName": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
    },
)
_OptionalCreateProjectInputTypeDef = TypedDict(
    "_OptionalCreateProjectInputTypeDef",
    {
        "ProjectDescription": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProjectInputTypeDef(
    _RequiredCreateProjectInputTypeDef, _OptionalCreateProjectInputTypeDef
):
    pass


CreateProjectOutputResponseTypeDef = TypedDict(
    "CreateProjectOutputResponseTypeDef",
    {
        "ProjectArn": str,
        "ProjectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrainingJobRequestTypeDef = TypedDict(
    "_RequiredCreateTrainingJobRequestTypeDef",
    {
        "TrainingJobName": str,
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalCreateTrainingJobRequestTypeDef = TypedDict(
    "_OptionalCreateTrainingJobRequestTypeDef",
    {
        "HyperParameters": Dict[str, str],
        "InputDataConfig": List["ChannelTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProfilerConfig": "ProfilerConfigTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
        "Environment": Dict[str, str],
        "RetryStrategy": "RetryStrategyTypeDef",
    },
    total=False,
)


class CreateTrainingJobRequestTypeDef(
    _RequiredCreateTrainingJobRequestTypeDef, _OptionalCreateTrainingJobRequestTypeDef
):
    pass


CreateTrainingJobResponseResponseTypeDef = TypedDict(
    "CreateTrainingJobResponseResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransformJobRequestTypeDef = TypedDict(
    "_RequiredCreateTransformJobRequestTypeDef",
    {
        "TransformJobName": str,
        "ModelName": str,
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
    },
)
_OptionalCreateTransformJobRequestTypeDef = TypedDict(
    "_OptionalCreateTransformJobRequestTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "DataProcessing": "DataProcessingTypeDef",
        "Tags": List["TagTypeDef"],
        "ExperimentConfig": "ExperimentConfigTypeDef",
    },
    total=False,
)


class CreateTransformJobRequestTypeDef(
    _RequiredCreateTransformJobRequestTypeDef, _OptionalCreateTransformJobRequestTypeDef
):
    pass


CreateTransformJobResponseResponseTypeDef = TypedDict(
    "CreateTransformJobResponseResponseTypeDef",
    {
        "TransformJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrialComponentRequestTypeDef = TypedDict(
    "_RequiredCreateTrialComponentRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)
_OptionalCreateTrialComponentRequestTypeDef = TypedDict(
    "_OptionalCreateTrialComponentRequestTypeDef",
    {
        "DisplayName": str,
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTrialComponentRequestTypeDef(
    _RequiredCreateTrialComponentRequestTypeDef, _OptionalCreateTrialComponentRequestTypeDef
):
    pass


CreateTrialComponentResponseResponseTypeDef = TypedDict(
    "CreateTrialComponentResponseResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrialRequestTypeDef = TypedDict(
    "_RequiredCreateTrialRequestTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
    },
)
_OptionalCreateTrialRequestTypeDef = TypedDict(
    "_OptionalCreateTrialRequestTypeDef",
    {
        "DisplayName": str,
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTrialRequestTypeDef(
    _RequiredCreateTrialRequestTypeDef, _OptionalCreateTrialRequestTypeDef
):
    pass


CreateTrialResponseResponseTypeDef = TypedDict(
    "CreateTrialResponseResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserProfileRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalCreateUserProfileRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileRequestTypeDef",
    {
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "Tags": List["TagTypeDef"],
        "UserSettings": "UserSettingsTypeDef",
    },
    total=False,
)


class CreateUserProfileRequestTypeDef(
    _RequiredCreateUserProfileRequestTypeDef, _OptionalCreateUserProfileRequestTypeDef
):
    pass


CreateUserProfileResponseResponseTypeDef = TypedDict(
    "CreateUserProfileResponseResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkforceRequestTypeDef = TypedDict(
    "_RequiredCreateWorkforceRequestTypeDef",
    {
        "WorkforceName": str,
    },
)
_OptionalCreateWorkforceRequestTypeDef = TypedDict(
    "_OptionalCreateWorkforceRequestTypeDef",
    {
        "CognitoConfig": "CognitoConfigTypeDef",
        "OidcConfig": "OidcConfigTypeDef",
        "SourceIpConfig": "SourceIpConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWorkforceRequestTypeDef(
    _RequiredCreateWorkforceRequestTypeDef, _OptionalCreateWorkforceRequestTypeDef
):
    pass


CreateWorkforceResponseResponseTypeDef = TypedDict(
    "CreateWorkforceResponseResponseTypeDef",
    {
        "WorkforceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkteamRequestTypeDef = TypedDict(
    "_RequiredCreateWorkteamRequestTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "Description": str,
    },
)
_OptionalCreateWorkteamRequestTypeDef = TypedDict(
    "_OptionalCreateWorkteamRequestTypeDef",
    {
        "WorkforceName": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWorkteamRequestTypeDef(
    _RequiredCreateWorkteamRequestTypeDef, _OptionalCreateWorkteamRequestTypeDef
):
    pass


CreateWorkteamResponseResponseTypeDef = TypedDict(
    "CreateWorkteamResponseResponseTypeDef",
    {
        "WorkteamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomImageTypeDef = TypedDict(
    "_RequiredCustomImageTypeDef",
    {
        "ImageName": str,
        "AppImageConfigName": str,
    },
)
_OptionalCustomImageTypeDef = TypedDict(
    "_OptionalCustomImageTypeDef",
    {
        "ImageVersionNumber": int,
    },
    total=False,
)


class CustomImageTypeDef(_RequiredCustomImageTypeDef, _OptionalCustomImageTypeDef):
    pass


DataCaptureConfigSummaryTypeDef = TypedDict(
    "DataCaptureConfigSummaryTypeDef",
    {
        "EnableCapture": bool,
        "CaptureStatus": CaptureStatusType,
        "CurrentSamplingPercentage": int,
        "DestinationS3Uri": str,
        "KmsKeyId": str,
    },
)

_RequiredDataCaptureConfigTypeDef = TypedDict(
    "_RequiredDataCaptureConfigTypeDef",
    {
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "CaptureOptions": List["CaptureOptionTypeDef"],
    },
)
_OptionalDataCaptureConfigTypeDef = TypedDict(
    "_OptionalDataCaptureConfigTypeDef",
    {
        "EnableCapture": bool,
        "KmsKeyId": str,
        "CaptureContentTypeHeader": "CaptureContentTypeHeaderTypeDef",
    },
    total=False,
)


class DataCaptureConfigTypeDef(
    _RequiredDataCaptureConfigTypeDef, _OptionalDataCaptureConfigTypeDef
):
    pass


DataCatalogConfigTypeDef = TypedDict(
    "DataCatalogConfigTypeDef",
    {
        "TableName": str,
        "Catalog": str,
        "Database": str,
    },
)

DataProcessingTypeDef = TypedDict(
    "DataProcessingTypeDef",
    {
        "InputFilter": str,
        "OutputFilter": str,
        "JoinSource": JoinSourceType,
    },
    total=False,
)

_RequiredDataQualityAppSpecificationTypeDef = TypedDict(
    "_RequiredDataQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalDataQualityAppSpecificationTypeDef = TypedDict(
    "_OptionalDataQualityAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "Environment": Dict[str, str],
    },
    total=False,
)


class DataQualityAppSpecificationTypeDef(
    _RequiredDataQualityAppSpecificationTypeDef, _OptionalDataQualityAppSpecificationTypeDef
):
    pass


DataQualityBaselineConfigTypeDef = TypedDict(
    "DataQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
        "StatisticsResource": "MonitoringStatisticsResourceTypeDef",
    },
    total=False,
)

DataQualityJobInputTypeDef = TypedDict(
    "DataQualityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3DataSource": "S3DataSourceTypeDef",
        "FileSystemDataSource": "FileSystemDataSourceTypeDef",
    },
    total=False,
)

DatasetDefinitionTypeDef = TypedDict(
    "DatasetDefinitionTypeDef",
    {
        "AthenaDatasetDefinition": "AthenaDatasetDefinitionTypeDef",
        "RedshiftDatasetDefinition": "RedshiftDatasetDefinitionTypeDef",
        "LocalPath": str,
        "DataDistributionType": DataDistributionTypeType,
        "InputMode": InputModeType,
    },
    total=False,
)

_RequiredDebugHookConfigTypeDef = TypedDict(
    "_RequiredDebugHookConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalDebugHookConfigTypeDef = TypedDict(
    "_OptionalDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List["CollectionConfigurationTypeDef"],
    },
    total=False,
)


class DebugHookConfigTypeDef(_RequiredDebugHookConfigTypeDef, _OptionalDebugHookConfigTypeDef):
    pass


_RequiredDebugRuleConfigurationTypeDef = TypedDict(
    "_RequiredDebugRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalDebugRuleConfigurationTypeDef = TypedDict(
    "_OptionalDebugRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)


class DebugRuleConfigurationTypeDef(
    _RequiredDebugRuleConfigurationTypeDef, _OptionalDebugRuleConfigurationTypeDef
):
    pass


DebugRuleEvaluationStatusTypeDef = TypedDict(
    "DebugRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": RuleEvaluationStatusType,
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

DeleteActionRequestTypeDef = TypedDict(
    "DeleteActionRequestTypeDef",
    {
        "ActionName": str,
    },
)

DeleteActionResponseResponseTypeDef = TypedDict(
    "DeleteActionResponseResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlgorithmInputTypeDef = TypedDict(
    "DeleteAlgorithmInputTypeDef",
    {
        "AlgorithmName": str,
    },
)

DeleteAppImageConfigRequestTypeDef = TypedDict(
    "DeleteAppImageConfigRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

DeleteAppRequestTypeDef = TypedDict(
    "DeleteAppRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)

DeleteArtifactRequestTypeDef = TypedDict(
    "DeleteArtifactRequestTypeDef",
    {
        "ArtifactArn": str,
        "Source": "ArtifactSourceTypeDef",
    },
    total=False,
)

DeleteArtifactResponseResponseTypeDef = TypedDict(
    "DeleteArtifactResponseResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssociationRequestTypeDef = TypedDict(
    "DeleteAssociationRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)

DeleteAssociationResponseResponseTypeDef = TypedDict(
    "DeleteAssociationResponseResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCodeRepositoryInputTypeDef = TypedDict(
    "DeleteCodeRepositoryInputTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DeleteContextRequestTypeDef = TypedDict(
    "DeleteContextRequestTypeDef",
    {
        "ContextName": str,
    },
)

DeleteContextResponseResponseTypeDef = TypedDict(
    "DeleteContextResponseResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataQualityJobDefinitionRequestTypeDef = TypedDict(
    "DeleteDataQualityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteDeviceFleetRequestTypeDef = TypedDict(
    "DeleteDeviceFleetRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

_RequiredDeleteDomainRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalDeleteDomainRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainRequestTypeDef",
    {
        "RetentionPolicy": "RetentionPolicyTypeDef",
    },
    total=False,
)


class DeleteDomainRequestTypeDef(
    _RequiredDeleteDomainRequestTypeDef, _OptionalDeleteDomainRequestTypeDef
):
    pass


DeleteEndpointConfigInputTypeDef = TypedDict(
    "DeleteEndpointConfigInputTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DeleteEndpointInputTypeDef = TypedDict(
    "DeleteEndpointInputTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteExperimentRequestTypeDef = TypedDict(
    "DeleteExperimentRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DeleteExperimentResponseResponseTypeDef = TypedDict(
    "DeleteExperimentResponseResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFeatureGroupRequestTypeDef = TypedDict(
    "DeleteFeatureGroupRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)

DeleteFlowDefinitionRequestTypeDef = TypedDict(
    "DeleteFlowDefinitionRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DeleteHumanTaskUiRequestTypeDef = TypedDict(
    "DeleteHumanTaskUiRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DeleteImageRequestTypeDef = TypedDict(
    "DeleteImageRequestTypeDef",
    {
        "ImageName": str,
    },
)

DeleteImageVersionRequestTypeDef = TypedDict(
    "DeleteImageVersionRequestTypeDef",
    {
        "ImageName": str,
        "Version": int,
    },
)

DeleteModelBiasJobDefinitionRequestTypeDef = TypedDict(
    "DeleteModelBiasJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelExplainabilityJobDefinitionRequestTypeDef = TypedDict(
    "DeleteModelExplainabilityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelInputTypeDef = TypedDict(
    "DeleteModelInputTypeDef",
    {
        "ModelName": str,
    },
)

DeleteModelPackageGroupInputTypeDef = TypedDict(
    "DeleteModelPackageGroupInputTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageGroupPolicyInputTypeDef = TypedDict(
    "DeleteModelPackageGroupPolicyInputTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageInputTypeDef = TypedDict(
    "DeleteModelPackageInputTypeDef",
    {
        "ModelPackageName": str,
    },
)

DeleteModelQualityJobDefinitionRequestTypeDef = TypedDict(
    "DeleteModelQualityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteMonitoringScheduleRequestTypeDef = TypedDict(
    "DeleteMonitoringScheduleRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DeleteNotebookInstanceInputTypeDef = TypedDict(
    "DeleteNotebookInstanceInputTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DeleteNotebookInstanceLifecycleConfigInputTypeDef = TypedDict(
    "DeleteNotebookInstanceLifecycleConfigInputTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DeletePipelineRequestTypeDef = TypedDict(
    "DeletePipelineRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)

DeletePipelineResponseResponseTypeDef = TypedDict(
    "DeletePipelineResponseResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectInputTypeDef = TypedDict(
    "DeleteProjectInputTypeDef",
    {
        "ProjectName": str,
    },
)

DeleteTagsInputTypeDef = TypedDict(
    "DeleteTagsInputTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DeleteTrialComponentRequestTypeDef = TypedDict(
    "DeleteTrialComponentRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DeleteTrialComponentResponseResponseTypeDef = TypedDict(
    "DeleteTrialComponentResponseResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrialRequestTypeDef = TypedDict(
    "DeleteTrialRequestTypeDef",
    {
        "TrialName": str,
    },
)

DeleteTrialResponseResponseTypeDef = TypedDict(
    "DeleteTrialResponseResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserProfileRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DeleteWorkforceRequestTypeDef = TypedDict(
    "DeleteWorkforceRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DeleteWorkteamRequestTypeDef = TypedDict(
    "DeleteWorkteamRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DeleteWorkteamResponseResponseTypeDef = TypedDict(
    "DeleteWorkteamResponseResponseTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeployedImageTypeDef = TypedDict(
    "DeployedImageTypeDef",
    {
        "SpecifiedImage": str,
        "ResolvedImage": str,
        "ResolutionTime": datetime,
    },
    total=False,
)

_RequiredDeploymentConfigTypeDef = TypedDict(
    "_RequiredDeploymentConfigTypeDef",
    {
        "BlueGreenUpdatePolicy": "BlueGreenUpdatePolicyTypeDef",
    },
)
_OptionalDeploymentConfigTypeDef = TypedDict(
    "_OptionalDeploymentConfigTypeDef",
    {
        "AutoRollbackConfiguration": "AutoRollbackConfigTypeDef",
    },
    total=False,
)


class DeploymentConfigTypeDef(_RequiredDeploymentConfigTypeDef, _OptionalDeploymentConfigTypeDef):
    pass


DeregisterDevicesRequestTypeDef = TypedDict(
    "DeregisterDevicesRequestTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceNames": List[str],
    },
)

DescribeActionRequestTypeDef = TypedDict(
    "DescribeActionRequestTypeDef",
    {
        "ActionName": str,
    },
)

DescribeActionResponseResponseTypeDef = TypedDict(
    "DescribeActionResponseResponseTypeDef",
    {
        "ActionName": str,
        "ActionArn": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlgorithmInputTypeDef = TypedDict(
    "DescribeAlgorithmInputTypeDef",
    {
        "AlgorithmName": str,
    },
)

DescribeAlgorithmOutputResponseTypeDef = TypedDict(
    "DescribeAlgorithmOutputResponseTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "AlgorithmValidationSpecificationTypeDef",
        "AlgorithmStatus": AlgorithmStatusType,
        "AlgorithmStatusDetails": "AlgorithmStatusDetailsTypeDef",
        "ProductId": str,
        "CertifyForMarketplace": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppImageConfigRequestTypeDef = TypedDict(
    "DescribeAppImageConfigRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

DescribeAppImageConfigResponseResponseTypeDef = TypedDict(
    "DescribeAppImageConfigResponseResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppRequestTypeDef = TypedDict(
    "DescribeAppRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)

DescribeAppResponseResponseTypeDef = TypedDict(
    "DescribeAppResponseResponseTypeDef",
    {
        "AppArn": str,
        "AppType": AppTypeType,
        "AppName": str,
        "DomainId": str,
        "UserProfileName": str,
        "Status": AppStatusType,
        "LastHealthCheckTimestamp": datetime,
        "LastUserActivityTimestamp": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "ResourceSpec": "ResourceSpecTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArtifactRequestTypeDef = TypedDict(
    "DescribeArtifactRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)

DescribeArtifactResponseResponseTypeDef = TypedDict(
    "DescribeArtifactResponseResponseTypeDef",
    {
        "ArtifactName": str,
        "ArtifactArn": str,
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoMLJobRequestTypeDef = TypedDict(
    "DescribeAutoMLJobRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

DescribeAutoMLJobResponseResponseTypeDef = TypedDict(
    "DescribeAutoMLJobResponseResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "InputDataConfig": List["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": ProblemTypeType,
        "AutoMLJobConfig": "AutoMLJobConfigTypeDef",
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List["AutoMLPartialFailureReasonTypeDef"],
        "BestCandidate": "AutoMLCandidateTypeDef",
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "GenerateCandidateDefinitionsOnly": bool,
        "AutoMLJobArtifacts": "AutoMLJobArtifactsTypeDef",
        "ResolvedAttributes": "ResolvedAttributesTypeDef",
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
        "ModelDeployResult": "ModelDeployResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeRepositoryInputTypeDef = TypedDict(
    "DescribeCodeRepositoryInputTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DescribeCodeRepositoryOutputResponseTypeDef = TypedDict(
    "DescribeCodeRepositoryOutputResponseTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": "GitConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCompilationJobRequestTypeDef = TypedDict(
    "DescribeCompilationJobRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

DescribeCompilationJobResponseResponseTypeDef = TypedDict(
    "DescribeCompilationJobResponseResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": CompilationJobStatusType,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "ModelDigests": "ModelDigestsTypeDef",
        "RoleArn": str,
        "InputConfig": "InputConfigTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContextRequestTypeDef = TypedDict(
    "DescribeContextRequestTypeDef",
    {
        "ContextName": str,
    },
)

DescribeContextResponseResponseTypeDef = TypedDict(
    "DescribeContextResponseResponseTypeDef",
    {
        "ContextName": str,
        "ContextArn": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
        "Description": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataQualityJobDefinitionRequestTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeDataQualityJobDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "DataQualityBaselineConfig": "DataQualityBaselineConfigTypeDef",
        "DataQualityAppSpecification": "DataQualityAppSpecificationTypeDef",
        "DataQualityJobInput": "DataQualityJobInputTypeDef",
        "DataQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceFleetRequestTypeDef = TypedDict(
    "DescribeDeviceFleetRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

DescribeDeviceFleetResponseResponseTypeDef = TypedDict(
    "DescribeDeviceFleetResponseResponseTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceFleetArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "IotRoleAlias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDeviceRequestTypeDef = TypedDict(
    "_RequiredDescribeDeviceRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)
_OptionalDescribeDeviceRequestTypeDef = TypedDict(
    "_OptionalDescribeDeviceRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeDeviceRequestTypeDef(
    _RequiredDescribeDeviceRequestTypeDef, _OptionalDescribeDeviceRequestTypeDef
):
    pass


DescribeDeviceResponseResponseTypeDef = TypedDict(
    "DescribeDeviceResponseResponseTypeDef",
    {
        "DeviceArn": str,
        "DeviceName": str,
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List["EdgeModelTypeDef"],
        "MaxModels": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestTypeDef = TypedDict(
    "DescribeDomainRequestTypeDef",
    {
        "DomainId": str,
    },
)

DescribeDomainResponseResponseTypeDef = TypedDict(
    "DescribeDomainResponseResponseTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "HomeEfsFileSystemId": str,
        "SingleSignOnManagedApplicationInstanceId": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": "UserSettingsTypeDef",
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "SubnetIds": List[str],
        "Url": str,
        "VpcId": str,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEdgePackagingJobRequestTypeDef = TypedDict(
    "DescribeEdgePackagingJobRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

DescribeEdgePackagingJobResponseResponseTypeDef = TypedDict(
    "DescribeEdgePackagingJobResponseResponseTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "ResourceKey": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
        "EdgePackagingJobStatusMessage": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ModelArtifact": str,
        "ModelSignature": str,
        "PresetDeploymentOutput": "EdgePresetDeploymentOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointConfigInputTypeDef = TypedDict(
    "DescribeEndpointConfigInputTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DescribeEndpointConfigOutputResponseTypeDef = TypedDict(
    "DescribeEndpointConfigOutputResponseTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List["ProductionVariantTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigTypeDef",
        "KmsKeyId": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointInputTypeDef = TypedDict(
    "DescribeEndpointInputTypeDef",
    {
        "EndpointName": str,
    },
)

DescribeEndpointOutputResponseTypeDef = TypedDict(
    "DescribeEndpointOutputResponseTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "ProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigSummaryTypeDef",
        "EndpointStatus": EndpointStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastDeploymentConfig": "DeploymentConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExperimentRequestTypeDef = TypedDict(
    "DescribeExperimentRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DescribeExperimentResponseResponseTypeDef = TypedDict(
    "DescribeExperimentResponseResponseTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": "ExperimentSourceTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFeatureGroupRequestTypeDef = TypedDict(
    "_RequiredDescribeFeatureGroupRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)
_OptionalDescribeFeatureGroupRequestTypeDef = TypedDict(
    "_OptionalDescribeFeatureGroupRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeFeatureGroupRequestTypeDef(
    _RequiredDescribeFeatureGroupRequestTypeDef, _OptionalDescribeFeatureGroupRequestTypeDef
):
    pass


DescribeFeatureGroupResponseResponseTypeDef = TypedDict(
    "DescribeFeatureGroupResponseResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
        "CreationTime": datetime,
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
        "FailureReason": str,
        "Description": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowDefinitionRequestTypeDef = TypedDict(
    "DescribeFlowDefinitionRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DescribeFlowDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeFlowDefinitionResponseResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "FlowDefinitionName": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
        "HumanLoopRequestSource": "HumanLoopRequestSourceTypeDef",
        "HumanLoopActivationConfig": "HumanLoopActivationConfigTypeDef",
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHumanTaskUiRequestTypeDef = TypedDict(
    "DescribeHumanTaskUiRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DescribeHumanTaskUiResponseResponseTypeDef = TypedDict(
    "DescribeHumanTaskUiResponseResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "HumanTaskUiName": str,
        "HumanTaskUiStatus": HumanTaskUiStatusType,
        "CreationTime": datetime,
        "UiTemplate": "UiTemplateInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHyperParameterTuningJobRequestTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

DescribeHyperParameterTuningJobResponseResponseTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobResponseResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
        "BestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "OverallBestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageRequestTypeDef = TypedDict(
    "DescribeImageRequestTypeDef",
    {
        "ImageName": str,
    },
)

DescribeImageResponseResponseTypeDef = TypedDict(
    "DescribeImageResponseResponseTypeDef",
    {
        "CreationTime": datetime,
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageVersionRequestTypeDef = TypedDict(
    "_RequiredDescribeImageVersionRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageVersionRequestTypeDef = TypedDict(
    "_OptionalDescribeImageVersionRequestTypeDef",
    {
        "Version": int,
    },
    total=False,
)


class DescribeImageVersionRequestTypeDef(
    _RequiredDescribeImageVersionRequestTypeDef, _OptionalDescribeImageVersionRequestTypeDef
):
    pass


DescribeImageVersionResponseResponseTypeDef = TypedDict(
    "DescribeImageVersionResponseResponseTypeDef",
    {
        "BaseImage": str,
        "ContainerImage": str,
        "CreationTime": datetime,
        "FailureReason": str,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLabelingJobRequestTypeDef = TypedDict(
    "DescribeLabelingJobRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

DescribeLabelingJobResponseResponseTypeDef = TypedDict(
    "DescribeLabelingJobResponseResponseTypeDef",
    {
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": "LabelCountersTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "LabelAttributeName": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": "LabelingJobStoppingConditionsTypeDef",
        "LabelingJobAlgorithmsConfig": "LabelingJobAlgorithmsConfigTypeDef",
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "LabelingJobOutput": "LabelingJobOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelBiasJobDefinitionRequestTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelBiasJobDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelBiasBaselineConfig": "ModelBiasBaselineConfigTypeDef",
        "ModelBiasAppSpecification": "ModelBiasAppSpecificationTypeDef",
        "ModelBiasJobInput": "ModelBiasJobInputTypeDef",
        "ModelBiasJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelExplainabilityJobDefinitionRequestTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelExplainabilityJobDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelExplainabilityBaselineConfig": "ModelExplainabilityBaselineConfigTypeDef",
        "ModelExplainabilityAppSpecification": "ModelExplainabilityAppSpecificationTypeDef",
        "ModelExplainabilityJobInput": "ModelExplainabilityJobInputTypeDef",
        "ModelExplainabilityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelInputTypeDef = TypedDict(
    "DescribeModelInputTypeDef",
    {
        "ModelName": str,
    },
)

DescribeModelOutputResponseTypeDef = TypedDict(
    "DescribeModelOutputResponseTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "InferenceExecutionConfig": "InferenceExecutionConfigTypeDef",
        "ExecutionRoleArn": str,
        "VpcConfig": "VpcConfigTypeDef",
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackageGroupInputTypeDef = TypedDict(
    "DescribeModelPackageGroupInputTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DescribeModelPackageGroupOutputResponseTypeDef = TypedDict(
    "DescribeModelPackageGroupOutputResponseTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackageInputTypeDef = TypedDict(
    "DescribeModelPackageInputTypeDef",
    {
        "ModelPackageName": str,
    },
)

DescribeModelPackageOutputResponseTypeDef = TypedDict(
    "DescribeModelPackageOutputResponseTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": "ModelPackageStatusDetailsTypeDef",
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ApprovalDescription": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelQualityJobDefinitionRequestTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelQualityJobDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionResponseResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelQualityBaselineConfig": "ModelQualityBaselineConfigTypeDef",
        "ModelQualityAppSpecification": "ModelQualityAppSpecificationTypeDef",
        "ModelQualityJobInput": "ModelQualityJobInputTypeDef",
        "ModelQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMonitoringScheduleRequestTypeDef = TypedDict(
    "DescribeMonitoringScheduleRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DescribeMonitoringScheduleResponseResponseTypeDef = TypedDict(
    "DescribeMonitoringScheduleResponseResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "EndpointName": str,
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookInstanceInputTypeDef = TypedDict(
    "DescribeNotebookInstanceInputTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigInputTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigInputTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigOutputResponseTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigOutputResponseTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookInstanceOutputResponseTypeDef = TypedDict(
    "DescribeNotebookInstanceOutputResponseTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "FailureReason": str,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": RootAccessType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineDefinitionForExecutionRequestTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineDefinitionForExecutionResponseResponseTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionResponseResponseTypeDef",
    {
        "PipelineDefinition": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineExecutionRequestTypeDef = TypedDict(
    "DescribePipelineExecutionRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineExecutionResponseResponseTypeDef = TypedDict(
    "DescribePipelineExecutionResponseResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": "PipelineExperimentConfigTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineRequestTypeDef = TypedDict(
    "DescribePipelineRequestTypeDef",
    {
        "PipelineName": str,
    },
)

DescribePipelineResponseResponseTypeDef = TypedDict(
    "DescribePipelineResponseResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProcessingJobRequestTypeDef = TypedDict(
    "DescribeProcessingJobRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

DescribeProcessingJobResponseResponseTypeDef = TypedDict(
    "DescribeProcessingJobResponseResponseTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "RoleArn": str,
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectInputTypeDef = TypedDict(
    "DescribeProjectInputTypeDef",
    {
        "ProjectName": str,
    },
)

DescribeProjectOutputResponseTypeDef = TypedDict(
    "DescribeProjectOutputResponseTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "ProjectId": str,
        "ProjectDescription": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
        "ServiceCatalogProvisionedProductDetails": "ServiceCatalogProvisionedProductDetailsTypeDef",
        "ProjectStatus": ProjectStatusType,
        "CreatedBy": "UserContextTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscribedWorkteamRequestTypeDef = TypedDict(
    "DescribeSubscribedWorkteamRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)

DescribeSubscribedWorkteamResponseResponseTypeDef = TypedDict(
    "DescribeSubscribedWorkteamResponseResponseTypeDef",
    {
        "SubscribedWorkteam": "SubscribedWorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrainingJobRequestTypeDef = TypedDict(
    "DescribeTrainingJobRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

DescribeTrainingJobResponseResponseTypeDef = TypedDict(
    "DescribeTrainingJobResponseResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List["SecondaryStatusTransitionTypeDef"],
        "FinalMetricDataList": List["MetricDataTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "DebugRuleEvaluationStatuses": List["DebugRuleEvaluationStatusTypeDef"],
        "ProfilerConfig": "ProfilerConfigTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
        "ProfilerRuleEvaluationStatuses": List["ProfilerRuleEvaluationStatusTypeDef"],
        "ProfilingStatus": ProfilingStatusType,
        "RetryStrategy": "RetryStrategyTypeDef",
        "Environment": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransformJobRequestTypeDef = TypedDict(
    "DescribeTransformJobRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

DescribeTransformJobResponseResponseTypeDef = TypedDict(
    "DescribeTransformJobResponseResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": "DataProcessingTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrialComponentRequestTypeDef = TypedDict(
    "DescribeTrialComponentRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DescribeTrialComponentResponseResponseTypeDef = TypedDict(
    "DescribeTrialComponentResponseResponseTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "Source": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Metrics": List["TrialComponentMetricSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrialRequestTypeDef = TypedDict(
    "DescribeTrialRequestTypeDef",
    {
        "TrialName": str,
    },
)

DescribeTrialResponseResponseTypeDef = TypedDict(
    "DescribeTrialResponseResponseTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfileRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DescribeUserProfileResponseResponseTypeDef = TypedDict(
    "DescribeUserProfileResponseResponseTypeDef",
    {
        "DomainId": str,
        "UserProfileArn": str,
        "UserProfileName": str,
        "HomeEfsFileSystemUid": str,
        "Status": UserProfileStatusType,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "UserSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkforceRequestTypeDef = TypedDict(
    "DescribeWorkforceRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DescribeWorkforceResponseResponseTypeDef = TypedDict(
    "DescribeWorkforceResponseResponseTypeDef",
    {
        "Workforce": "WorkforceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkteamRequestTypeDef = TypedDict(
    "DescribeWorkteamRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DescribeWorkteamResponseResponseTypeDef = TypedDict(
    "DescribeWorkteamResponseResponseTypeDef",
    {
        "Workteam": "WorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDesiredWeightAndCapacityTypeDef = TypedDict(
    "_RequiredDesiredWeightAndCapacityTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalDesiredWeightAndCapacityTypeDef = TypedDict(
    "_OptionalDesiredWeightAndCapacityTypeDef",
    {
        "DesiredWeight": float,
        "DesiredInstanceCount": int,
    },
    total=False,
)


class DesiredWeightAndCapacityTypeDef(
    _RequiredDesiredWeightAndCapacityTypeDef, _OptionalDesiredWeightAndCapacityTypeDef
):
    pass


_RequiredDeviceFleetSummaryTypeDef = TypedDict(
    "_RequiredDeviceFleetSummaryTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
    },
)
_OptionalDeviceFleetSummaryTypeDef = TypedDict(
    "_OptionalDeviceFleetSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class DeviceFleetSummaryTypeDef(
    _RequiredDeviceFleetSummaryTypeDef, _OptionalDeviceFleetSummaryTypeDef
):
    pass


DeviceStatsTypeDef = TypedDict(
    "DeviceStatsTypeDef",
    {
        "ConnectedDeviceCount": int,
        "RegisteredDeviceCount": int,
    },
)

_RequiredDeviceSummaryTypeDef = TypedDict(
    "_RequiredDeviceSummaryTypeDef",
    {
        "DeviceName": str,
        "DeviceArn": str,
    },
)
_OptionalDeviceSummaryTypeDef = TypedDict(
    "_OptionalDeviceSummaryTypeDef",
    {
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List["EdgeModelSummaryTypeDef"],
    },
    total=False,
)


class DeviceSummaryTypeDef(_RequiredDeviceSummaryTypeDef, _OptionalDeviceSummaryTypeDef):
    pass


_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "DeviceName": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "Description": str,
        "IotThingName": str,
    },
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


DisassociateTrialComponentRequestTypeDef = TypedDict(
    "DisassociateTrialComponentRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

DisassociateTrialComponentResponseResponseTypeDef = TypedDict(
    "DisassociateTrialComponentResponseResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Url": str,
    },
    total=False,
)

EdgeModelStatTypeDef = TypedDict(
    "EdgeModelStatTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "OfflineDeviceCount": int,
        "ConnectedDeviceCount": int,
        "ActiveDeviceCount": int,
        "SamplingDeviceCount": int,
    },
)

EdgeModelSummaryTypeDef = TypedDict(
    "EdgeModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)

_RequiredEdgeModelTypeDef = TypedDict(
    "_RequiredEdgeModelTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)
_OptionalEdgeModelTypeDef = TypedDict(
    "_OptionalEdgeModelTypeDef",
    {
        "LatestSampleTime": datetime,
        "LatestInference": datetime,
    },
    total=False,
)


class EdgeModelTypeDef(_RequiredEdgeModelTypeDef, _OptionalEdgeModelTypeDef):
    pass


_RequiredEdgeOutputConfigTypeDef = TypedDict(
    "_RequiredEdgeOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalEdgeOutputConfigTypeDef = TypedDict(
    "_OptionalEdgeOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "PresetDeploymentType": Literal["GreengrassV2Component"],
        "PresetDeploymentConfig": str,
    },
    total=False,
)


class EdgeOutputConfigTypeDef(_RequiredEdgeOutputConfigTypeDef, _OptionalEdgeOutputConfigTypeDef):
    pass


_RequiredEdgePackagingJobSummaryTypeDef = TypedDict(
    "_RequiredEdgePackagingJobSummaryTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
    },
)
_OptionalEdgePackagingJobSummaryTypeDef = TypedDict(
    "_OptionalEdgePackagingJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class EdgePackagingJobSummaryTypeDef(
    _RequiredEdgePackagingJobSummaryTypeDef, _OptionalEdgePackagingJobSummaryTypeDef
):
    pass


_RequiredEdgePresetDeploymentOutputTypeDef = TypedDict(
    "_RequiredEdgePresetDeploymentOutputTypeDef",
    {
        "Type": Literal["GreengrassV2Component"],
    },
)
_OptionalEdgePresetDeploymentOutputTypeDef = TypedDict(
    "_OptionalEdgePresetDeploymentOutputTypeDef",
    {
        "Artifact": str,
        "Status": EdgePresetDeploymentStatusType,
        "StatusMessage": str,
    },
    total=False,
)


class EdgePresetDeploymentOutputTypeDef(
    _RequiredEdgePresetDeploymentOutputTypeDef, _OptionalEdgePresetDeploymentOutputTypeDef
):
    pass


EndpointConfigSummaryTypeDef = TypedDict(
    "EndpointConfigSummaryTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "CreationTime": datetime,
    },
)

_RequiredEndpointInputTypeDef = TypedDict(
    "_RequiredEndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
    },
)
_OptionalEndpointInputTypeDef = TypedDict(
    "_OptionalEndpointInputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
    },
    total=False,
)


class EndpointInputTypeDef(_RequiredEndpointInputTypeDef, _OptionalEndpointInputTypeDef):
    pass


EndpointSummaryTypeDef = TypedDict(
    "EndpointSummaryTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": EndpointStatusType,
    },
)

_RequiredEndpointTypeDef = TypedDict(
    "_RequiredEndpointTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "EndpointStatus": EndpointStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalEndpointTypeDef = TypedDict(
    "_OptionalEndpointTypeDef",
    {
        "ProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigSummaryTypeDef",
        "FailureReason": str,
        "MonitoringSchedules": List["MonitoringScheduleTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class EndpointTypeDef(_RequiredEndpointTypeDef, _OptionalEndpointTypeDef):
    pass


ExperimentConfigTypeDef = TypedDict(
    "ExperimentConfigTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "TrialComponentDisplayName": str,
    },
    total=False,
)

_RequiredExperimentSourceTypeDef = TypedDict(
    "_RequiredExperimentSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalExperimentSourceTypeDef = TypedDict(
    "_OptionalExperimentSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)


class ExperimentSourceTypeDef(_RequiredExperimentSourceTypeDef, _OptionalExperimentSourceTypeDef):
    pass


ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "ExperimentArn": str,
        "ExperimentName": str,
        "DisplayName": str,
        "ExperimentSource": "ExperimentSourceTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": "ExperimentSourceTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ExplainabilityTypeDef = TypedDict(
    "ExplainabilityTypeDef",
    {
        "Report": "MetricsSourceTypeDef",
    },
    total=False,
)

FeatureDefinitionTypeDef = TypedDict(
    "FeatureDefinitionTypeDef",
    {
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
    },
    total=False,
)

_RequiredFeatureGroupSummaryTypeDef = TypedDict(
    "_RequiredFeatureGroupSummaryTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureGroupArn": str,
        "CreationTime": datetime,
    },
)
_OptionalFeatureGroupSummaryTypeDef = TypedDict(
    "_OptionalFeatureGroupSummaryTypeDef",
    {
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
    },
    total=False,
)


class FeatureGroupSummaryTypeDef(
    _RequiredFeatureGroupSummaryTypeDef, _OptionalFeatureGroupSummaryTypeDef
):
    pass


FeatureGroupTypeDef = TypedDict(
    "FeatureGroupTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
        "CreationTime": datetime,
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
        "FailureReason": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "MountPath": str,
        "DefaultUid": int,
        "DefaultGid": int,
    },
    total=False,
)

FileSystemDataSourceTypeDef = TypedDict(
    "FileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": FileSystemAccessModeType,
        "FileSystemType": FileSystemTypeType,
        "DirectoryPath": str,
    },
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "Name": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Operator": OperatorType,
        "Value": str,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


_RequiredFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
        "Value": float,
    },
)
_OptionalFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "Type": AutoMLJobObjectiveTypeType,
    },
    total=False,
)


class FinalAutoMLJobObjectiveMetricTypeDef(
    _RequiredFinalAutoMLJobObjectiveMetricTypeDef, _OptionalFinalAutoMLJobObjectiveMetricTypeDef
):
    pass


_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "MetricName": str,
        "Value": float,
    },
)
_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
    },
    total=False,
)


class FinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef,
    _OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef,
):
    pass


_RequiredFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_RequiredFlowDefinitionOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_OptionalFlowDefinitionOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class FlowDefinitionOutputConfigTypeDef(
    _RequiredFlowDefinitionOutputConfigTypeDef, _OptionalFlowDefinitionOutputConfigTypeDef
):
    pass


_RequiredFlowDefinitionSummaryTypeDef = TypedDict(
    "_RequiredFlowDefinitionSummaryTypeDef",
    {
        "FlowDefinitionName": str,
        "FlowDefinitionArn": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
    },
)
_OptionalFlowDefinitionSummaryTypeDef = TypedDict(
    "_OptionalFlowDefinitionSummaryTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class FlowDefinitionSummaryTypeDef(
    _RequiredFlowDefinitionSummaryTypeDef, _OptionalFlowDefinitionSummaryTypeDef
):
    pass


GetDeviceFleetReportRequestTypeDef = TypedDict(
    "GetDeviceFleetReportRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

GetDeviceFleetReportResponseResponseTypeDef = TypedDict(
    "GetDeviceFleetReportResponseResponseTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "Description": str,
        "ReportGenerated": datetime,
        "DeviceStats": "DeviceStatsTypeDef",
        "AgentVersions": List["AgentVersionTypeDef"],
        "ModelStats": List["EdgeModelStatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelPackageGroupPolicyInputTypeDef = TypedDict(
    "GetModelPackageGroupPolicyInputTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

GetModelPackageGroupPolicyOutputResponseTypeDef = TypedDict(
    "GetModelPackageGroupPolicyOutputResponseTypeDef",
    {
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSagemakerServicecatalogPortfolioStatusOutputResponseTypeDef = TypedDict(
    "GetSagemakerServicecatalogPortfolioStatusOutputResponseTypeDef",
    {
        "Status": SagemakerServicecatalogStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSearchSuggestionsRequestTypeDef = TypedDict(
    "_RequiredGetSearchSuggestionsRequestTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalGetSearchSuggestionsRequestTypeDef = TypedDict(
    "_OptionalGetSearchSuggestionsRequestTypeDef",
    {
        "SuggestionQuery": "SuggestionQueryTypeDef",
    },
    total=False,
)


class GetSearchSuggestionsRequestTypeDef(
    _RequiredGetSearchSuggestionsRequestTypeDef, _OptionalGetSearchSuggestionsRequestTypeDef
):
    pass


GetSearchSuggestionsResponseResponseTypeDef = TypedDict(
    "GetSearchSuggestionsResponseResponseTypeDef",
    {
        "PropertyNameSuggestions": List["PropertyNameSuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitConfigForUpdateTypeDef = TypedDict(
    "GitConfigForUpdateTypeDef",
    {
        "SecretArn": str,
    },
    total=False,
)

_RequiredGitConfigTypeDef = TypedDict(
    "_RequiredGitConfigTypeDef",
    {
        "RepositoryUrl": str,
    },
)
_OptionalGitConfigTypeDef = TypedDict(
    "_OptionalGitConfigTypeDef",
    {
        "Branch": str,
        "SecretArn": str,
    },
    total=False,
)


class GitConfigTypeDef(_RequiredGitConfigTypeDef, _OptionalGitConfigTypeDef):
    pass


HumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "HumanLoopActivationConditionsConfigTypeDef",
    {
        "HumanLoopActivationConditions": str,
    },
)

HumanLoopActivationConfigTypeDef = TypedDict(
    "HumanLoopActivationConfigTypeDef",
    {
        "HumanLoopActivationConditionsConfig": "HumanLoopActivationConditionsConfigTypeDef",
    },
)

_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef",
    {
        "WorkteamArn": str,
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
    },
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {
        "TaskAvailabilityLifetimeInSeconds": int,
        "TaskTimeLimitInSeconds": int,
        "TaskKeywords": List[str],
        "PublicWorkforceTaskPrice": "PublicWorkforceTaskPriceTypeDef",
    },
    total=False,
)


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass


HumanLoopRequestSourceTypeDef = TypedDict(
    "HumanLoopRequestSourceTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": AwsManagedHumanLoopRequestSourceType,
    },
)

_RequiredHumanTaskConfigTypeDef = TypedDict(
    "_RequiredHumanTaskConfigTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": "UiConfigTypeDef",
        "PreHumanTaskLambdaArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "AnnotationConsolidationConfig": "AnnotationConsolidationConfigTypeDef",
    },
)
_OptionalHumanTaskConfigTypeDef = TypedDict(
    "_OptionalHumanTaskConfigTypeDef",
    {
        "TaskKeywords": List[str],
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "PublicWorkforceTaskPrice": "PublicWorkforceTaskPriceTypeDef",
    },
    total=False,
)


class HumanTaskConfigTypeDef(_RequiredHumanTaskConfigTypeDef, _OptionalHumanTaskConfigTypeDef):
    pass


HumanTaskUiSummaryTypeDef = TypedDict(
    "HumanTaskUiSummaryTypeDef",
    {
        "HumanTaskUiName": str,
        "HumanTaskUiArn": str,
        "CreationTime": datetime,
    },
)

_RequiredHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
    },
    total=False,
)


class HyperParameterAlgorithmSpecificationTypeDef(
    _RequiredHyperParameterAlgorithmSpecificationTypeDef,
    _OptionalHyperParameterAlgorithmSpecificationTypeDef,
):
    pass


_RequiredHyperParameterSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterSpecificationTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalHyperParameterSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterSpecificationTypeDef",
    {
        "Description": str,
        "Range": "ParameterRangeTypeDef",
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)


class HyperParameterSpecificationTypeDef(
    _RequiredHyperParameterSpecificationTypeDef, _OptionalHyperParameterSpecificationTypeDef
):
    pass


_RequiredHyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobDefinitionTypeDef",
    {
        "AlgorithmSpecification": "HyperParameterAlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalHyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobDefinitionTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": "HyperParameterTuningJobObjectiveTypeDef",
        "HyperParameterRanges": "ParameterRangesTypeDef",
        "StaticHyperParameters": Dict[str, str],
        "InputDataConfig": List["ChannelTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "RetryStrategy": "RetryStrategyTypeDef",
    },
    total=False,
)


class HyperParameterTrainingJobDefinitionTypeDef(
    _RequiredHyperParameterTrainingJobDefinitionTypeDef,
    _OptionalHyperParameterTrainingJobDefinitionTypeDef,
):
    pass


_RequiredHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
        "TunedHyperParameters": Dict[str, str],
    },
)
_OptionalHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TuningJobName": str,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
        "ObjectiveStatus": ObjectiveStatusType,
    },
    total=False,
)


class HyperParameterTrainingJobSummaryTypeDef(
    _RequiredHyperParameterTrainingJobSummaryTypeDef,
    _OptionalHyperParameterTrainingJobSummaryTypeDef,
):
    pass


_RequiredHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobConfigTypeDef",
    {
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "ResourceLimits": "ResourceLimitsTypeDef",
    },
)
_OptionalHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobConfigTypeDef",
    {
        "HyperParameterTuningJobObjective": "HyperParameterTuningJobObjectiveTypeDef",
        "ParameterRanges": "ParameterRangesTypeDef",
        "TrainingJobEarlyStoppingType": TrainingJobEarlyStoppingTypeType,
        "TuningJobCompletionCriteria": "TuningJobCompletionCriteriaTypeDef",
    },
    total=False,
)


class HyperParameterTuningJobConfigTypeDef(
    _RequiredHyperParameterTuningJobConfigTypeDef, _OptionalHyperParameterTuningJobConfigTypeDef
):
    pass


HyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
        "MetricName": str,
    },
)

_RequiredHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "CreationTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
    },
)
_OptionalHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "ResourceLimits": "ResourceLimitsTypeDef",
    },
    total=False,
)


class HyperParameterTuningJobSummaryTypeDef(
    _RequiredHyperParameterTuningJobSummaryTypeDef, _OptionalHyperParameterTuningJobSummaryTypeDef
):
    pass


HyperParameterTuningJobWarmStartConfigTypeDef = TypedDict(
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": List["ParentHyperParameterTuningJobTypeDef"],
        "WarmStartType": HyperParameterTuningJobWarmStartTypeType,
    },
)

_RequiredImageConfigTypeDef = TypedDict(
    "_RequiredImageConfigTypeDef",
    {
        "RepositoryAccessMode": RepositoryAccessModeType,
    },
)
_OptionalImageConfigTypeDef = TypedDict(
    "_OptionalImageConfigTypeDef",
    {
        "RepositoryAuthConfig": "RepositoryAuthConfigTypeDef",
    },
    total=False,
)


class ImageConfigTypeDef(_RequiredImageConfigTypeDef, _OptionalImageConfigTypeDef):
    pass


_RequiredImageTypeDef = TypedDict(
    "_RequiredImageTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
    },
)
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
    },
    total=False,
)


class ImageTypeDef(_RequiredImageTypeDef, _OptionalImageTypeDef):
    pass


_RequiredImageVersionTypeDef = TypedDict(
    "_RequiredImageVersionTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
    },
)
_OptionalImageVersionTypeDef = TypedDict(
    "_OptionalImageVersionTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class ImageVersionTypeDef(_RequiredImageVersionTypeDef, _OptionalImageVersionTypeDef):
    pass


InferenceExecutionConfigTypeDef = TypedDict(
    "InferenceExecutionConfigTypeDef",
    {
        "Mode": InferenceExecutionModeType,
    },
)

_RequiredInferenceSpecificationTypeDef = TypedDict(
    "_RequiredInferenceSpecificationTypeDef",
    {
        "Containers": List["ModelPackageContainerDefinitionTypeDef"],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
)
_OptionalInferenceSpecificationTypeDef = TypedDict(
    "_OptionalInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": List[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": List[ProductionVariantInstanceTypeType],
    },
    total=False,
)


class InferenceSpecificationTypeDef(
    _RequiredInferenceSpecificationTypeDef, _OptionalInferenceSpecificationTypeDef
):
    pass


_RequiredInputConfigTypeDef = TypedDict(
    "_RequiredInputConfigTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": FrameworkType,
    },
)
_OptionalInputConfigTypeDef = TypedDict(
    "_OptionalInputConfigTypeDef",
    {
        "FrameworkVersion": str,
    },
    total=False,
)


class InputConfigTypeDef(_RequiredInputConfigTypeDef, _OptionalInputConfigTypeDef):
    pass


IntegerParameterRangeSpecificationTypeDef = TypedDict(
    "IntegerParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

_RequiredIntegerParameterRangeTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalIntegerParameterRangeTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)


class IntegerParameterRangeTypeDef(
    _RequiredIntegerParameterRangeTypeDef, _OptionalIntegerParameterRangeTypeDef
):
    pass


JupyterServerAppSettingsTypeDef = TypedDict(
    "JupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
    },
    total=False,
)

KernelGatewayAppSettingsTypeDef = TypedDict(
    "KernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
        "CustomImages": List["CustomImageTypeDef"],
    },
    total=False,
)

_RequiredKernelGatewayImageConfigTypeDef = TypedDict(
    "_RequiredKernelGatewayImageConfigTypeDef",
    {
        "KernelSpecs": List["KernelSpecTypeDef"],
    },
)
_OptionalKernelGatewayImageConfigTypeDef = TypedDict(
    "_OptionalKernelGatewayImageConfigTypeDef",
    {
        "FileSystemConfig": "FileSystemConfigTypeDef",
    },
    total=False,
)


class KernelGatewayImageConfigTypeDef(
    _RequiredKernelGatewayImageConfigTypeDef, _OptionalKernelGatewayImageConfigTypeDef
):
    pass


_RequiredKernelSpecTypeDef = TypedDict(
    "_RequiredKernelSpecTypeDef",
    {
        "Name": str,
    },
)
_OptionalKernelSpecTypeDef = TypedDict(
    "_OptionalKernelSpecTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class KernelSpecTypeDef(_RequiredKernelSpecTypeDef, _OptionalKernelSpecTypeDef):
    pass


LabelCountersForWorkteamTypeDef = TypedDict(
    "LabelCountersForWorkteamTypeDef",
    {
        "HumanLabeled": int,
        "PendingHuman": int,
        "Total": int,
    },
    total=False,
)

LabelCountersTypeDef = TypedDict(
    "LabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)

_RequiredLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_RequiredLabelingJobAlgorithmsConfigTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
    },
)
_OptionalLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_OptionalLabelingJobAlgorithmsConfigTypeDef",
    {
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": "LabelingJobResourceConfigTypeDef",
    },
    total=False,
)


class LabelingJobAlgorithmsConfigTypeDef(
    _RequiredLabelingJobAlgorithmsConfigTypeDef, _OptionalLabelingJobAlgorithmsConfigTypeDef
):
    pass


LabelingJobDataAttributesTypeDef = TypedDict(
    "LabelingJobDataAttributesTypeDef",
    {
        "ContentClassifiers": List[ContentClassifierType],
    },
    total=False,
)

LabelingJobDataSourceTypeDef = TypedDict(
    "LabelingJobDataSourceTypeDef",
    {
        "S3DataSource": "LabelingJobS3DataSourceTypeDef",
        "SnsDataSource": "LabelingJobSnsDataSourceTypeDef",
    },
    total=False,
)

_RequiredLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobForWorkteamSummaryTypeDef",
    {
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
    },
)
_OptionalLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobForWorkteamSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelCounters": "LabelCountersForWorkteamTypeDef",
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)


class LabelingJobForWorkteamSummaryTypeDef(
    _RequiredLabelingJobForWorkteamSummaryTypeDef, _OptionalLabelingJobForWorkteamSummaryTypeDef
):
    pass


_RequiredLabelingJobInputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobInputConfigTypeDef",
    {
        "DataSource": "LabelingJobDataSourceTypeDef",
    },
)
_OptionalLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobInputConfigTypeDef",
    {
        "DataAttributes": "LabelingJobDataAttributesTypeDef",
    },
    total=False,
)


class LabelingJobInputConfigTypeDef(
    _RequiredLabelingJobInputConfigTypeDef, _OptionalLabelingJobInputConfigTypeDef
):
    pass


_RequiredLabelingJobOutputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalLabelingJobOutputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "SnsTopicArn": str,
    },
    total=False,
)


class LabelingJobOutputConfigTypeDef(
    _RequiredLabelingJobOutputConfigTypeDef, _OptionalLabelingJobOutputConfigTypeDef
):
    pass


_RequiredLabelingJobOutputTypeDef = TypedDict(
    "_RequiredLabelingJobOutputTypeDef",
    {
        "OutputDatasetS3Uri": str,
    },
)
_OptionalLabelingJobOutputTypeDef = TypedDict(
    "_OptionalLabelingJobOutputTypeDef",
    {
        "FinalActiveLearningModelArn": str,
    },
    total=False,
)


class LabelingJobOutputTypeDef(
    _RequiredLabelingJobOutputTypeDef, _OptionalLabelingJobOutputTypeDef
):
    pass


LabelingJobResourceConfigTypeDef = TypedDict(
    "LabelingJobResourceConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)

LabelingJobS3DataSourceTypeDef = TypedDict(
    "LabelingJobS3DataSourceTypeDef",
    {
        "ManifestS3Uri": str,
    },
)

LabelingJobSnsDataSourceTypeDef = TypedDict(
    "LabelingJobSnsDataSourceTypeDef",
    {
        "SnsTopicArn": str,
    },
)

LabelingJobStoppingConditionsTypeDef = TypedDict(
    "LabelingJobStoppingConditionsTypeDef",
    {
        "MaxHumanLabeledObjectCount": int,
        "MaxPercentageOfInputDatasetLabeled": int,
    },
    total=False,
)

_RequiredLabelingJobSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": "LabelCountersTypeDef",
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
    },
)
_OptionalLabelingJobSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobSummaryTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": "LabelingJobOutputTypeDef",
        "InputConfig": "LabelingJobInputConfigTypeDef",
    },
    total=False,
)


class LabelingJobSummaryTypeDef(
    _RequiredLabelingJobSummaryTypeDef, _OptionalLabelingJobSummaryTypeDef
):
    pass


ListActionsRequestTypeDef = TypedDict(
    "ListActionsRequestTypeDef",
    {
        "SourceUri": str,
        "ActionType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortActionsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListActionsResponseResponseTypeDef = TypedDict(
    "ListActionsResponseResponseTypeDef",
    {
        "ActionSummaries": List["ActionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlgorithmsInputTypeDef = TypedDict(
    "ListAlgorithmsInputTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": AlgorithmSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListAlgorithmsOutputResponseTypeDef = TypedDict(
    "ListAlgorithmsOutputResponseTypeDef",
    {
        "AlgorithmSummaryList": List["AlgorithmSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppImageConfigsRequestTypeDef = TypedDict(
    "ListAppImageConfigsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": AppImageConfigSortKeyType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListAppImageConfigsResponseResponseTypeDef = TypedDict(
    "ListAppImageConfigsResponseResponseTypeDef",
    {
        "NextToken": str,
        "AppImageConfigs": List["AppImageConfigDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppsRequestTypeDef = TypedDict(
    "ListAppsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": Literal["CreationTime"],
        "DomainIdEquals": str,
        "UserProfileNameEquals": str,
    },
    total=False,
)

ListAppsResponseResponseTypeDef = TypedDict(
    "ListAppsResponseResponseTypeDef",
    {
        "Apps": List["AppDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArtifactsRequestTypeDef = TypedDict(
    "ListArtifactsRequestTypeDef",
    {
        "SourceUri": str,
        "ArtifactType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListArtifactsResponseResponseTypeDef = TypedDict(
    "ListArtifactsResponseResponseTypeDef",
    {
        "ArtifactSummaries": List["ArtifactSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationsRequestTypeDef = TypedDict(
    "ListAssociationsRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortAssociationsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAssociationsResponseResponseTypeDef = TypedDict(
    "ListAssociationsResponseResponseTypeDef",
    {
        "AssociationSummaries": List["AssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutoMLJobsRequestTypeDef = TypedDict(
    "ListAutoMLJobsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": AutoMLJobStatusType,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": AutoMLSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAutoMLJobsResponseResponseTypeDef = TypedDict(
    "ListAutoMLJobsResponseResponseTypeDef",
    {
        "AutoMLJobSummaries": List["AutoMLJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCandidatesForAutoMLJobRequestTypeDef = TypedDict(
    "_RequiredListCandidatesForAutoMLJobRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)
_OptionalListCandidatesForAutoMLJobRequestTypeDef = TypedDict(
    "_OptionalListCandidatesForAutoMLJobRequestTypeDef",
    {
        "StatusEquals": CandidateStatusType,
        "CandidateNameEquals": str,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": CandidateSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCandidatesForAutoMLJobRequestTypeDef(
    _RequiredListCandidatesForAutoMLJobRequestTypeDef,
    _OptionalListCandidatesForAutoMLJobRequestTypeDef,
):
    pass


ListCandidatesForAutoMLJobResponseResponseTypeDef = TypedDict(
    "ListCandidatesForAutoMLJobResponseResponseTypeDef",
    {
        "Candidates": List["AutoMLCandidateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCodeRepositoriesInputTypeDef = TypedDict(
    "ListCodeRepositoriesInputTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": CodeRepositorySortByType,
        "SortOrder": CodeRepositorySortOrderType,
    },
    total=False,
)

ListCodeRepositoriesOutputResponseTypeDef = TypedDict(
    "ListCodeRepositoriesOutputResponseTypeDef",
    {
        "CodeRepositorySummaryList": List["CodeRepositorySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCompilationJobsRequestTypeDef = TypedDict(
    "ListCompilationJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": CompilationJobStatusType,
        "SortBy": ListCompilationJobsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListCompilationJobsResponseResponseTypeDef = TypedDict(
    "ListCompilationJobsResponseResponseTypeDef",
    {
        "CompilationJobSummaries": List["CompilationJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContextsRequestTypeDef = TypedDict(
    "ListContextsRequestTypeDef",
    {
        "SourceUri": str,
        "ContextType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortContextsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListContextsResponseResponseTypeDef = TypedDict(
    "ListContextsResponseResponseTypeDef",
    {
        "ContextSummaries": List["ContextSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityJobDefinitionsRequestTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListDataQualityJobDefinitionsResponseResponseTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsResponseResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceFleetsRequestTypeDef = TypedDict(
    "ListDeviceFleetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": ListDeviceFleetsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListDeviceFleetsResponseResponseTypeDef = TypedDict(
    "ListDeviceFleetsResponseResponseTypeDef",
    {
        "DeviceFleetSummaries": List["DeviceFleetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestTypeDef = TypedDict(
    "ListDevicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LatestHeartbeatAfter": Union[datetime, str],
        "ModelName": str,
        "DeviceFleetName": str,
    },
    total=False,
)

ListDevicesResponseResponseTypeDef = TypedDict(
    "ListDevicesResponseResponseTypeDef",
    {
        "DeviceSummaries": List["DeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestTypeDef = TypedDict(
    "ListDomainsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDomainsResponseResponseTypeDef = TypedDict(
    "ListDomainsResponseResponseTypeDef",
    {
        "Domains": List["DomainDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEdgePackagingJobsRequestTypeDef = TypedDict(
    "ListEdgePackagingJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "ModelNameContains": str,
        "StatusEquals": EdgePackagingJobStatusType,
        "SortBy": ListEdgePackagingJobsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListEdgePackagingJobsResponseResponseTypeDef = TypedDict(
    "ListEdgePackagingJobsResponseResponseTypeDef",
    {
        "EdgePackagingJobSummaries": List["EdgePackagingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointConfigsInputTypeDef = TypedDict(
    "ListEndpointConfigsInputTypeDef",
    {
        "SortBy": EndpointConfigSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListEndpointConfigsOutputResponseTypeDef = TypedDict(
    "ListEndpointConfigsOutputResponseTypeDef",
    {
        "EndpointConfigs": List["EndpointConfigSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsInputTypeDef = TypedDict(
    "ListEndpointsInputTypeDef",
    {
        "SortBy": EndpointSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": EndpointStatusType,
    },
    total=False,
)

ListEndpointsOutputResponseTypeDef = TypedDict(
    "ListEndpointsOutputResponseTypeDef",
    {
        "Endpoints": List["EndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentsRequestTypeDef = TypedDict(
    "ListExperimentsRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortExperimentsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListExperimentsResponseResponseTypeDef = TypedDict(
    "ListExperimentsResponseResponseTypeDef",
    {
        "ExperimentSummaries": List["ExperimentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFeatureGroupsRequestTypeDef = TypedDict(
    "ListFeatureGroupsRequestTypeDef",
    {
        "NameContains": str,
        "FeatureGroupStatusEquals": FeatureGroupStatusType,
        "OfflineStoreStatusEquals": OfflineStoreStatusValueType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": FeatureGroupSortOrderType,
        "SortBy": FeatureGroupSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFeatureGroupsResponseResponseTypeDef = TypedDict(
    "ListFeatureGroupsResponseResponseTypeDef",
    {
        "FeatureGroupSummaries": List["FeatureGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowDefinitionsRequestTypeDef = TypedDict(
    "ListFlowDefinitionsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFlowDefinitionsResponseResponseTypeDef = TypedDict(
    "ListFlowDefinitionsResponseResponseTypeDef",
    {
        "FlowDefinitionSummaries": List["FlowDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHumanTaskUisRequestTypeDef = TypedDict(
    "ListHumanTaskUisRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHumanTaskUisResponseResponseTypeDef = TypedDict(
    "ListHumanTaskUisResponseResponseTypeDef",
    {
        "HumanTaskUiSummaries": List["HumanTaskUiSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHyperParameterTuningJobsRequestTypeDef = TypedDict(
    "ListHyperParameterTuningJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": HyperParameterTuningJobSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "StatusEquals": HyperParameterTuningJobStatusType,
    },
    total=False,
)

ListHyperParameterTuningJobsResponseResponseTypeDef = TypedDict(
    "ListHyperParameterTuningJobsResponseResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List["HyperParameterTuningJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImageVersionsRequestTypeDef = TypedDict(
    "_RequiredListImageVersionsRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListImageVersionsRequestTypeDef = TypedDict(
    "_OptionalListImageVersionsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "SortBy": ImageVersionSortByType,
        "SortOrder": ImageVersionSortOrderType,
    },
    total=False,
)


class ListImageVersionsRequestTypeDef(
    _RequiredListImageVersionsRequestTypeDef, _OptionalListImageVersionsRequestTypeDef
):
    pass


ListImageVersionsResponseResponseTypeDef = TypedDict(
    "ListImageVersionsResponseResponseTypeDef",
    {
        "ImageVersions": List["ImageVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagesRequestTypeDef = TypedDict(
    "ListImagesRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ImageSortByType,
        "SortOrder": ImageSortOrderType,
    },
    total=False,
)

ListImagesResponseResponseTypeDef = TypedDict(
    "ListImagesResponseResponseTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLabelingJobsForWorkteamRequestTypeDef = TypedDict(
    "_RequiredListLabelingJobsForWorkteamRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalListLabelingJobsForWorkteamRequestTypeDef = TypedDict(
    "_OptionalListLabelingJobsForWorkteamRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "JobReferenceCodeContains": str,
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
    },
    total=False,
)


class ListLabelingJobsForWorkteamRequestTypeDef(
    _RequiredListLabelingJobsForWorkteamRequestTypeDef,
    _OptionalListLabelingJobsForWorkteamRequestTypeDef,
):
    pass


ListLabelingJobsForWorkteamResponseResponseTypeDef = TypedDict(
    "ListLabelingJobsForWorkteamResponseResponseTypeDef",
    {
        "LabelingJobSummaryList": List["LabelingJobForWorkteamSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLabelingJobsRequestTypeDef = TypedDict(
    "ListLabelingJobsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "StatusEquals": LabelingJobStatusType,
    },
    total=False,
)

ListLabelingJobsResponseResponseTypeDef = TypedDict(
    "ListLabelingJobsResponseResponseTypeDef",
    {
        "LabelingJobSummaryList": List["LabelingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelBiasJobDefinitionsRequestTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelBiasJobDefinitionsResponseResponseTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsResponseResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelExplainabilityJobDefinitionsRequestTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelExplainabilityJobDefinitionsResponseResponseTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsResponseResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackageGroupsInputTypeDef = TypedDict(
    "ListModelPackageGroupsInputTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ModelPackageGroupSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListModelPackageGroupsOutputResponseTypeDef = TypedDict(
    "ListModelPackageGroupsOutputResponseTypeDef",
    {
        "ModelPackageGroupSummaryList": List["ModelPackageGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackagesInputTypeDef = TypedDict(
    "ListModelPackagesInputTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "ModelPackageGroupName": str,
        "ModelPackageType": ModelPackageTypeType,
        "NextToken": str,
        "SortBy": ModelPackageSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListModelPackagesOutputResponseTypeDef = TypedDict(
    "ListModelPackagesOutputResponseTypeDef",
    {
        "ModelPackageSummaryList": List["ModelPackageSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelQualityJobDefinitionsRequestTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelQualityJobDefinitionsResponseResponseTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsResponseResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelsInputTypeDef = TypedDict(
    "ListModelsInputTypeDef",
    {
        "SortBy": ModelSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelsOutputResponseTypeDef = TypedDict(
    "ListModelsOutputResponseTypeDef",
    {
        "Models": List["ModelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringExecutionsRequestTypeDef = TypedDict(
    "ListMonitoringExecutionsRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "EndpointName": str,
        "SortBy": MonitoringExecutionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "ScheduledTimeBefore": Union[datetime, str],
        "ScheduledTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ExecutionStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
    },
    total=False,
)

ListMonitoringExecutionsResponseResponseTypeDef = TypedDict(
    "ListMonitoringExecutionsResponseResponseTypeDef",
    {
        "MonitoringExecutionSummaries": List["MonitoringExecutionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringSchedulesRequestTypeDef = TypedDict(
    "ListMonitoringSchedulesRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringScheduleSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ScheduleStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
    },
    total=False,
)

ListMonitoringSchedulesResponseResponseTypeDef = TypedDict(
    "ListMonitoringSchedulesResponseResponseTypeDef",
    {
        "MonitoringScheduleSummaries": List["MonitoringScheduleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookInstanceLifecycleConfigsInputTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": NotebookInstanceLifecycleConfigSortKeyType,
        "SortOrder": NotebookInstanceLifecycleConfigSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListNotebookInstanceLifecycleConfigsOutputResponseTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsOutputResponseTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List["NotebookInstanceLifecycleConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookInstancesInputTypeDef = TypedDict(
    "ListNotebookInstancesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": NotebookInstanceSortKeyType,
        "SortOrder": NotebookInstanceSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": NotebookInstanceStatusType,
        "NotebookInstanceLifecycleConfigNameContains": str,
        "DefaultCodeRepositoryContains": str,
        "AdditionalCodeRepositoryEquals": str,
    },
    total=False,
)

ListNotebookInstancesOutputResponseTypeDef = TypedDict(
    "ListNotebookInstancesOutputResponseTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List["NotebookInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineExecutionStepsRequestTypeDef = TypedDict(
    "ListPipelineExecutionStepsRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListPipelineExecutionStepsResponseResponseTypeDef = TypedDict(
    "ListPipelineExecutionStepsResponseResponseTypeDef",
    {
        "PipelineExecutionSteps": List["PipelineExecutionStepTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPipelineExecutionsRequestTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalListPipelineExecutionsRequestTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelineExecutionsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPipelineExecutionsRequestTypeDef(
    _RequiredListPipelineExecutionsRequestTypeDef, _OptionalListPipelineExecutionsRequestTypeDef
):
    pass


ListPipelineExecutionsResponseResponseTypeDef = TypedDict(
    "ListPipelineExecutionsResponseResponseTypeDef",
    {
        "PipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPipelineParametersForExecutionRequestTypeDef = TypedDict(
    "_RequiredListPipelineParametersForExecutionRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalListPipelineParametersForExecutionRequestTypeDef = TypedDict(
    "_OptionalListPipelineParametersForExecutionRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPipelineParametersForExecutionRequestTypeDef(
    _RequiredListPipelineParametersForExecutionRequestTypeDef,
    _OptionalListPipelineParametersForExecutionRequestTypeDef,
):
    pass


ListPipelineParametersForExecutionResponseResponseTypeDef = TypedDict(
    "ListPipelineParametersForExecutionResponseResponseTypeDef",
    {
        "PipelineParameters": List["ParameterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestTypeDef = TypedDict(
    "ListPipelinesRequestTypeDef",
    {
        "PipelineNamePrefix": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelinesByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPipelinesResponseResponseTypeDef = TypedDict(
    "ListPipelinesResponseResponseTypeDef",
    {
        "PipelineSummaries": List["PipelineSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProcessingJobsRequestTypeDef = TypedDict(
    "ListProcessingJobsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": ProcessingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProcessingJobsResponseResponseTypeDef = TypedDict(
    "ListProcessingJobsResponseResponseTypeDef",
    {
        "ProcessingJobSummaries": List["ProcessingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsInputTypeDef = TypedDict(
    "ListProjectsInputTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ProjectSortByType,
        "SortOrder": ProjectSortOrderType,
    },
    total=False,
)

ListProjectsOutputResponseTypeDef = TypedDict(
    "ListProjectsOutputResponseTypeDef",
    {
        "ProjectSummaryList": List["ProjectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribedWorkteamsRequestTypeDef = TypedDict(
    "ListSubscribedWorkteamsRequestTypeDef",
    {
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSubscribedWorkteamsResponseResponseTypeDef = TypedDict(
    "ListSubscribedWorkteamsResponseResponseTypeDef",
    {
        "SubscribedWorkteams": List["SubscribedWorkteamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsInputTypeDef = TypedDict(
    "_RequiredListTagsInputTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputTypeDef = TypedDict(
    "_OptionalListTagsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsInputTypeDef(_RequiredListTagsInputTypeDef, _OptionalListTagsInputTypeDef):
    pass


ListTagsOutputResponseTypeDef = TypedDict(
    "ListTagsOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrainingJobsForHyperParameterTuningJobRequestTypeDef = TypedDict(
    "_RequiredListTrainingJobsForHyperParameterTuningJobRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)
_OptionalListTrainingJobsForHyperParameterTuningJobRequestTypeDef = TypedDict(
    "_OptionalListTrainingJobsForHyperParameterTuningJobRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": TrainingJobSortByOptionsType,
        "SortOrder": SortOrderType,
    },
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobRequestTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobRequestTypeDef,
    _OptionalListTrainingJobsForHyperParameterTuningJobRequestTypeDef,
):
    pass


ListTrainingJobsForHyperParameterTuningJobResponseResponseTypeDef = TypedDict(
    "ListTrainingJobsForHyperParameterTuningJobResponseResponseTypeDef",
    {
        "TrainingJobSummaries": List["HyperParameterTrainingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrainingJobsRequestTypeDef = TypedDict(
    "ListTrainingJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListTrainingJobsResponseResponseTypeDef = TypedDict(
    "ListTrainingJobsResponseResponseTypeDef",
    {
        "TrainingJobSummaries": List["TrainingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransformJobsRequestTypeDef = TypedDict(
    "ListTransformJobsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TransformJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTransformJobsResponseResponseTypeDef = TypedDict(
    "ListTransformJobsResponseResponseTypeDef",
    {
        "TransformJobSummaries": List["TransformJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrialComponentsRequestTypeDef = TypedDict(
    "ListTrialComponentsRequestTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "SourceArn": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialComponentsByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTrialComponentsResponseResponseTypeDef = TypedDict(
    "ListTrialComponentsResponseResponseTypeDef",
    {
        "TrialComponentSummaries": List["TrialComponentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrialsRequestTypeDef = TypedDict(
    "ListTrialsRequestTypeDef",
    {
        "ExperimentName": str,
        "TrialComponentName": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialsByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTrialsResponseResponseTypeDef = TypedDict(
    "ListTrialsResponseResponseTypeDef",
    {
        "TrialSummaries": List["TrialSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserProfilesRequestTypeDef = TypedDict(
    "ListUserProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": UserProfileSortKeyType,
        "DomainIdEquals": str,
        "UserProfileNameContains": str,
    },
    total=False,
)

ListUserProfilesResponseResponseTypeDef = TypedDict(
    "ListUserProfilesResponseResponseTypeDef",
    {
        "UserProfiles": List["UserProfileDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkforcesRequestTypeDef = TypedDict(
    "ListWorkforcesRequestTypeDef",
    {
        "SortBy": ListWorkforcesSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkforcesResponseResponseTypeDef = TypedDict(
    "ListWorkforcesResponseResponseTypeDef",
    {
        "Workforces": List["WorkforceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkteamsRequestTypeDef = TypedDict(
    "ListWorkteamsRequestTypeDef",
    {
        "SortBy": ListWorkteamsSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkteamsResponseResponseTypeDef = TypedDict(
    "ListWorkteamsResponseResponseTypeDef",
    {
        "Workteams": List["WorkteamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberDefinitionTypeDef = TypedDict(
    "MemberDefinitionTypeDef",
    {
        "CognitoMemberDefinition": "CognitoMemberDefinitionTypeDef",
        "OidcMemberDefinition": "OidcMemberDefinitionTypeDef",
    },
    total=False,
)

MetadataPropertiesTypeDef = TypedDict(
    "MetadataPropertiesTypeDef",
    {
        "CommitId": str,
        "Repository": str,
        "GeneratedBy": str,
        "ProjectId": str,
    },
    total=False,
)

MetricDataTypeDef = TypedDict(
    "MetricDataTypeDef",
    {
        "MetricName": str,
        "Value": float,
        "Timestamp": datetime,
    },
    total=False,
)

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "Name": str,
        "Regex": str,
    },
)

_RequiredMetricsSourceTypeDef = TypedDict(
    "_RequiredMetricsSourceTypeDef",
    {
        "ContentType": str,
        "S3Uri": str,
    },
)
_OptionalMetricsSourceTypeDef = TypedDict(
    "_OptionalMetricsSourceTypeDef",
    {
        "ContentDigest": str,
    },
    total=False,
)


class MetricsSourceTypeDef(_RequiredMetricsSourceTypeDef, _OptionalMetricsSourceTypeDef):
    pass


ModelArtifactsTypeDef = TypedDict(
    "ModelArtifactsTypeDef",
    {
        "S3ModelArtifacts": str,
    },
)

_RequiredModelBiasAppSpecificationTypeDef = TypedDict(
    "_RequiredModelBiasAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelBiasAppSpecificationTypeDef = TypedDict(
    "_OptionalModelBiasAppSpecificationTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class ModelBiasAppSpecificationTypeDef(
    _RequiredModelBiasAppSpecificationTypeDef, _OptionalModelBiasAppSpecificationTypeDef
):
    pass


ModelBiasBaselineConfigTypeDef = TypedDict(
    "ModelBiasBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
    },
    total=False,
)

ModelBiasJobInputTypeDef = TypedDict(
    "ModelBiasJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "GroundTruthS3Input": "MonitoringGroundTruthS3InputTypeDef",
    },
)

ModelClientConfigTypeDef = TypedDict(
    "ModelClientConfigTypeDef",
    {
        "InvocationsTimeoutInSeconds": int,
        "InvocationsMaxRetries": int,
    },
    total=False,
)

ModelDataQualityTypeDef = TypedDict(
    "ModelDataQualityTypeDef",
    {
        "Statistics": "MetricsSourceTypeDef",
        "Constraints": "MetricsSourceTypeDef",
    },
    total=False,
)

ModelDeployConfigTypeDef = TypedDict(
    "ModelDeployConfigTypeDef",
    {
        "AutoGenerateEndpointName": bool,
        "EndpointName": str,
    },
    total=False,
)

ModelDeployResultTypeDef = TypedDict(
    "ModelDeployResultTypeDef",
    {
        "EndpointName": str,
    },
    total=False,
)

ModelDigestsTypeDef = TypedDict(
    "ModelDigestsTypeDef",
    {
        "ArtifactDigest": str,
    },
    total=False,
)

_RequiredModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "_RequiredModelExplainabilityAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "_OptionalModelExplainabilityAppSpecificationTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class ModelExplainabilityAppSpecificationTypeDef(
    _RequiredModelExplainabilityAppSpecificationTypeDef,
    _OptionalModelExplainabilityAppSpecificationTypeDef,
):
    pass


ModelExplainabilityBaselineConfigTypeDef = TypedDict(
    "ModelExplainabilityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
    },
    total=False,
)

ModelExplainabilityJobInputTypeDef = TypedDict(
    "ModelExplainabilityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
    },
)

ModelMetricsTypeDef = TypedDict(
    "ModelMetricsTypeDef",
    {
        "ModelQuality": "ModelQualityTypeDef",
        "ModelDataQuality": "ModelDataQualityTypeDef",
        "Bias": "BiasTypeDef",
        "Explainability": "ExplainabilityTypeDef",
    },
    total=False,
)

_RequiredModelPackageContainerDefinitionTypeDef = TypedDict(
    "_RequiredModelPackageContainerDefinitionTypeDef",
    {
        "Image": str,
    },
)
_OptionalModelPackageContainerDefinitionTypeDef = TypedDict(
    "_OptionalModelPackageContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)


class ModelPackageContainerDefinitionTypeDef(
    _RequiredModelPackageContainerDefinitionTypeDef, _OptionalModelPackageContainerDefinitionTypeDef
):
    pass


_RequiredModelPackageGroupSummaryTypeDef = TypedDict(
    "_RequiredModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "CreationTime": datetime,
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
    },
)
_OptionalModelPackageGroupSummaryTypeDef = TypedDict(
    "_OptionalModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupDescription": str,
    },
    total=False,
)


class ModelPackageGroupSummaryTypeDef(
    _RequiredModelPackageGroupSummaryTypeDef, _OptionalModelPackageGroupSummaryTypeDef
):
    pass


ModelPackageGroupTypeDef = TypedDict(
    "ModelPackageGroupTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredModelPackageStatusDetailsTypeDef = TypedDict(
    "_RequiredModelPackageStatusDetailsTypeDef",
    {
        "ValidationStatuses": List["ModelPackageStatusItemTypeDef"],
    },
)
_OptionalModelPackageStatusDetailsTypeDef = TypedDict(
    "_OptionalModelPackageStatusDetailsTypeDef",
    {
        "ImageScanStatuses": List["ModelPackageStatusItemTypeDef"],
    },
    total=False,
)


class ModelPackageStatusDetailsTypeDef(
    _RequiredModelPackageStatusDetailsTypeDef, _OptionalModelPackageStatusDetailsTypeDef
):
    pass


_RequiredModelPackageStatusItemTypeDef = TypedDict(
    "_RequiredModelPackageStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedModelPackageStatusType,
    },
)
_OptionalModelPackageStatusItemTypeDef = TypedDict(
    "_OptionalModelPackageStatusItemTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class ModelPackageStatusItemTypeDef(
    _RequiredModelPackageStatusItemTypeDef, _OptionalModelPackageStatusItemTypeDef
):
    pass


_RequiredModelPackageSummaryTypeDef = TypedDict(
    "_RequiredModelPackageSummaryTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": ModelPackageStatusType,
    },
)
_OptionalModelPackageSummaryTypeDef = TypedDict(
    "_OptionalModelPackageSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageDescription": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
    },
    total=False,
)


class ModelPackageSummaryTypeDef(
    _RequiredModelPackageSummaryTypeDef, _OptionalModelPackageSummaryTypeDef
):
    pass


ModelPackageTypeDef = TypedDict(
    "ModelPackageTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": "ModelPackageStatusDetailsTypeDef",
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ApprovalDescription": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ModelPackageValidationProfileTypeDef = TypedDict(
    "ModelPackageValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": "TransformJobDefinitionTypeDef",
    },
)

ModelPackageValidationSpecificationTypeDef = TypedDict(
    "ModelPackageValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List["ModelPackageValidationProfileTypeDef"],
    },
)

_RequiredModelQualityAppSpecificationTypeDef = TypedDict(
    "_RequiredModelQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalModelQualityAppSpecificationTypeDef = TypedDict(
    "_OptionalModelQualityAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "ProblemType": MonitoringProblemTypeType,
        "Environment": Dict[str, str],
    },
    total=False,
)


class ModelQualityAppSpecificationTypeDef(
    _RequiredModelQualityAppSpecificationTypeDef, _OptionalModelQualityAppSpecificationTypeDef
):
    pass


ModelQualityBaselineConfigTypeDef = TypedDict(
    "ModelQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
    },
    total=False,
)

ModelQualityJobInputTypeDef = TypedDict(
    "ModelQualityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "GroundTruthS3Input": "MonitoringGroundTruthS3InputTypeDef",
    },
)

ModelQualityTypeDef = TypedDict(
    "ModelQualityTypeDef",
    {
        "Statistics": "MetricsSourceTypeDef",
        "Constraints": "MetricsSourceTypeDef",
    },
    total=False,
)

ModelStepMetadataTypeDef = TypedDict(
    "ModelStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "CreationTime": datetime,
    },
)

_RequiredMonitoringAppSpecificationTypeDef = TypedDict(
    "_RequiredMonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalMonitoringAppSpecificationTypeDef = TypedDict(
    "_OptionalMonitoringAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)


class MonitoringAppSpecificationTypeDef(
    _RequiredMonitoringAppSpecificationTypeDef, _OptionalMonitoringAppSpecificationTypeDef
):
    pass


MonitoringBaselineConfigTypeDef = TypedDict(
    "MonitoringBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
        "StatisticsResource": "MonitoringStatisticsResourceTypeDef",
    },
    total=False,
)

_RequiredMonitoringClusterConfigTypeDef = TypedDict(
    "_RequiredMonitoringClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalMonitoringClusterConfigTypeDef = TypedDict(
    "_OptionalMonitoringClusterConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class MonitoringClusterConfigTypeDef(
    _RequiredMonitoringClusterConfigTypeDef, _OptionalMonitoringClusterConfigTypeDef
):
    pass


MonitoringConstraintsResourceTypeDef = TypedDict(
    "MonitoringConstraintsResourceTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

_RequiredMonitoringExecutionSummaryTypeDef = TypedDict(
    "_RequiredMonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": ExecutionStatusType,
    },
)
_OptionalMonitoringExecutionSummaryTypeDef = TypedDict(
    "_OptionalMonitoringExecutionSummaryTypeDef",
    {
        "ProcessingJobArn": str,
        "EndpointName": str,
        "FailureReason": str,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)


class MonitoringExecutionSummaryTypeDef(
    _RequiredMonitoringExecutionSummaryTypeDef, _OptionalMonitoringExecutionSummaryTypeDef
):
    pass


MonitoringGroundTruthS3InputTypeDef = TypedDict(
    "MonitoringGroundTruthS3InputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringInputTypeDef = TypedDict(
    "MonitoringInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
    },
)

MonitoringJobDefinitionSummaryTypeDef = TypedDict(
    "MonitoringJobDefinitionSummaryTypeDef",
    {
        "MonitoringJobDefinitionName": str,
        "MonitoringJobDefinitionArn": str,
        "CreationTime": datetime,
        "EndpointName": str,
    },
)

_RequiredMonitoringJobDefinitionTypeDef = TypedDict(
    "_RequiredMonitoringJobDefinitionTypeDef",
    {
        "MonitoringInputs": List["MonitoringInputTypeDef"],
        "MonitoringOutputConfig": "MonitoringOutputConfigTypeDef",
        "MonitoringResources": "MonitoringResourcesTypeDef",
        "MonitoringAppSpecification": "MonitoringAppSpecificationTypeDef",
        "RoleArn": str,
    },
)
_OptionalMonitoringJobDefinitionTypeDef = TypedDict(
    "_OptionalMonitoringJobDefinitionTypeDef",
    {
        "BaselineConfig": "MonitoringBaselineConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
    },
    total=False,
)


class MonitoringJobDefinitionTypeDef(
    _RequiredMonitoringJobDefinitionTypeDef, _OptionalMonitoringJobDefinitionTypeDef
):
    pass


MonitoringNetworkConfigTypeDef = TypedDict(
    "MonitoringNetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

_RequiredMonitoringOutputConfigTypeDef = TypedDict(
    "_RequiredMonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": List["MonitoringOutputTypeDef"],
    },
)
_OptionalMonitoringOutputConfigTypeDef = TypedDict(
    "_OptionalMonitoringOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class MonitoringOutputConfigTypeDef(
    _RequiredMonitoringOutputConfigTypeDef, _OptionalMonitoringOutputConfigTypeDef
):
    pass


MonitoringOutputTypeDef = TypedDict(
    "MonitoringOutputTypeDef",
    {
        "S3Output": "MonitoringS3OutputTypeDef",
    },
)

MonitoringResourcesTypeDef = TypedDict(
    "MonitoringResourcesTypeDef",
    {
        "ClusterConfig": "MonitoringClusterConfigTypeDef",
    },
)

_RequiredMonitoringS3OutputTypeDef = TypedDict(
    "_RequiredMonitoringS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
    },
)
_OptionalMonitoringS3OutputTypeDef = TypedDict(
    "_OptionalMonitoringS3OutputTypeDef",
    {
        "S3UploadMode": ProcessingS3UploadModeType,
    },
    total=False,
)


class MonitoringS3OutputTypeDef(
    _RequiredMonitoringS3OutputTypeDef, _OptionalMonitoringS3OutputTypeDef
):
    pass


MonitoringScheduleConfigTypeDef = TypedDict(
    "MonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": "ScheduleConfigTypeDef",
        "MonitoringJobDefinition": "MonitoringJobDefinitionTypeDef",
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)

_RequiredMonitoringScheduleSummaryTypeDef = TypedDict(
    "_RequiredMonitoringScheduleSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": ScheduleStatusType,
    },
)
_OptionalMonitoringScheduleSummaryTypeDef = TypedDict(
    "_OptionalMonitoringScheduleSummaryTypeDef",
    {
        "EndpointName": str,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)


class MonitoringScheduleSummaryTypeDef(
    _RequiredMonitoringScheduleSummaryTypeDef, _OptionalMonitoringScheduleSummaryTypeDef
):
    pass


MonitoringScheduleTypeDef = TypedDict(
    "MonitoringScheduleTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "EndpointName": str,
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

MonitoringStatisticsResourceTypeDef = TypedDict(
    "MonitoringStatisticsResourceTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringStoppingConditionTypeDef = TypedDict(
    "MonitoringStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

MultiModelConfigTypeDef = TypedDict(
    "MultiModelConfigTypeDef",
    {
        "ModelCacheSetting": ModelCacheSettingType,
    },
    total=False,
)

NestedFiltersTypeDef = TypedDict(
    "NestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": List["FilterTypeDef"],
    },
)

NetworkConfigTypeDef = TypedDict(
    "NetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
    },
)
_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class NotebookInstanceLifecycleConfigSummaryTypeDef(
    _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef,
    _OptionalNotebookInstanceLifecycleConfigSummaryTypeDef,
):
    pass


NotebookInstanceLifecycleHookTypeDef = TypedDict(
    "NotebookInstanceLifecycleHookTypeDef",
    {
        "Content": str,
    },
    total=False,
)

_RequiredNotebookInstanceSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
    },
)
_OptionalNotebookInstanceSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)


class NotebookInstanceSummaryTypeDef(
    _RequiredNotebookInstanceSummaryTypeDef, _OptionalNotebookInstanceSummaryTypeDef
):
    pass


NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "NotificationTopicArn": str,
    },
    total=False,
)

ObjectiveStatusCountersTypeDef = TypedDict(
    "ObjectiveStatusCountersTypeDef",
    {
        "Succeeded": int,
        "Pending": int,
        "Failed": int,
    },
    total=False,
)

_RequiredOfflineStoreConfigTypeDef = TypedDict(
    "_RequiredOfflineStoreConfigTypeDef",
    {
        "S3StorageConfig": "S3StorageConfigTypeDef",
    },
)
_OptionalOfflineStoreConfigTypeDef = TypedDict(
    "_OptionalOfflineStoreConfigTypeDef",
    {
        "DisableGlueTableCreation": bool,
        "DataCatalogConfig": "DataCatalogConfigTypeDef",
    },
    total=False,
)


class OfflineStoreConfigTypeDef(
    _RequiredOfflineStoreConfigTypeDef, _OptionalOfflineStoreConfigTypeDef
):
    pass


_RequiredOfflineStoreStatusTypeDef = TypedDict(
    "_RequiredOfflineStoreStatusTypeDef",
    {
        "Status": OfflineStoreStatusValueType,
    },
)
_OptionalOfflineStoreStatusTypeDef = TypedDict(
    "_OptionalOfflineStoreStatusTypeDef",
    {
        "BlockedReason": str,
    },
    total=False,
)


class OfflineStoreStatusTypeDef(
    _RequiredOfflineStoreStatusTypeDef, _OptionalOfflineStoreStatusTypeDef
):
    pass


OidcConfigForResponseTypeDef = TypedDict(
    "OidcConfigForResponseTypeDef",
    {
        "ClientId": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
    total=False,
)

OidcConfigTypeDef = TypedDict(
    "OidcConfigTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
)

OidcMemberDefinitionTypeDef = TypedDict(
    "OidcMemberDefinitionTypeDef",
    {
        "Groups": List[str],
    },
)

OnlineStoreConfigTypeDef = TypedDict(
    "OnlineStoreConfigTypeDef",
    {
        "SecurityConfig": "OnlineStoreSecurityConfigTypeDef",
        "EnableOnlineStore": bool,
    },
    total=False,
)

OnlineStoreSecurityConfigTypeDef = TypedDict(
    "OnlineStoreSecurityConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredOutputConfigTypeDef = TypedDict(
    "_RequiredOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalOutputConfigTypeDef = TypedDict(
    "_OptionalOutputConfigTypeDef",
    {
        "TargetDevice": TargetDeviceType,
        "TargetPlatform": "TargetPlatformTypeDef",
        "CompilerOptions": str,
        "KmsKeyId": str,
    },
    total=False,
)


class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, _OptionalOutputConfigTypeDef):
    pass


_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


OutputParameterTypeDef = TypedDict(
    "OutputParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterRangeTypeDef = TypedDict(
    "ParameterRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": "IntegerParameterRangeSpecificationTypeDef",
        "ContinuousParameterRangeSpecification": "ContinuousParameterRangeSpecificationTypeDef",
        "CategoricalParameterRangeSpecification": "CategoricalParameterRangeSpecificationTypeDef",
    },
    total=False,
)

ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List["IntegerParameterRangeTypeDef"],
        "ContinuousParameterRanges": List["ContinuousParameterRangeTypeDef"],
        "CategoricalParameterRanges": List["CategoricalParameterRangeTypeDef"],
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

ParentHyperParameterTuningJobTypeDef = TypedDict(
    "ParentHyperParameterTuningJobTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
    total=False,
)

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
    },
    total=False,
)

PipelineExecutionStepMetadataTypeDef = TypedDict(
    "PipelineExecutionStepMetadataTypeDef",
    {
        "TrainingJob": "TrainingJobStepMetadataTypeDef",
        "ProcessingJob": "ProcessingJobStepMetadataTypeDef",
        "TransformJob": "TransformJobStepMetadataTypeDef",
        "Model": "ModelStepMetadataTypeDef",
        "RegisterModel": "RegisterModelStepMetadataTypeDef",
        "Condition": "ConditionStepMetadataTypeDef",
        "Callback": "CallbackStepMetadataTypeDef",
    },
    total=False,
)

PipelineExecutionStepTypeDef = TypedDict(
    "PipelineExecutionStepTypeDef",
    {
        "StepName": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StepStatus": StepStatusType,
        "CacheHitResult": "CacheHitResultTypeDef",
        "FailureReason": str,
        "Metadata": "PipelineExecutionStepMetadataTypeDef",
    },
    total=False,
)

PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "PipelineExecutionArn": str,
        "StartTime": datetime,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExecutionDisplayName": str,
    },
    total=False,
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": "PipelineExperimentConfigTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "PipelineParameters": List["ParameterTypeDef"],
    },
    total=False,
)

PipelineExperimentConfigTypeDef = TypedDict(
    "PipelineExperimentConfigTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastExecutionTime": datetime,
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredProcessingClusterConfigTypeDef = TypedDict(
    "_RequiredProcessingClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalProcessingClusterConfigTypeDef = TypedDict(
    "_OptionalProcessingClusterConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ProcessingClusterConfigTypeDef(
    _RequiredProcessingClusterConfigTypeDef, _OptionalProcessingClusterConfigTypeDef
):
    pass


ProcessingFeatureStoreOutputTypeDef = TypedDict(
    "ProcessingFeatureStoreOutputTypeDef",
    {
        "FeatureGroupName": str,
    },
)

_RequiredProcessingInputTypeDef = TypedDict(
    "_RequiredProcessingInputTypeDef",
    {
        "InputName": str,
    },
)
_OptionalProcessingInputTypeDef = TypedDict(
    "_OptionalProcessingInputTypeDef",
    {
        "AppManaged": bool,
        "S3Input": "ProcessingS3InputTypeDef",
        "DatasetDefinition": "DatasetDefinitionTypeDef",
    },
    total=False,
)


class ProcessingInputTypeDef(_RequiredProcessingInputTypeDef, _OptionalProcessingInputTypeDef):
    pass


ProcessingJobStepMetadataTypeDef = TypedDict(
    "ProcessingJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredProcessingJobSummaryTypeDef = TypedDict(
    "_RequiredProcessingJobSummaryTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingJobStatus": ProcessingJobStatusType,
    },
)
_OptionalProcessingJobSummaryTypeDef = TypedDict(
    "_OptionalProcessingJobSummaryTypeDef",
    {
        "ProcessingEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ExitMessage": str,
    },
    total=False,
)


class ProcessingJobSummaryTypeDef(
    _RequiredProcessingJobSummaryTypeDef, _OptionalProcessingJobSummaryTypeDef
):
    pass


ProcessingJobTypeDef = TypedDict(
    "ProcessingJobTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "RoleArn": str,
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredProcessingOutputConfigTypeDef = TypedDict(
    "_RequiredProcessingOutputConfigTypeDef",
    {
        "Outputs": List["ProcessingOutputTypeDef"],
    },
)
_OptionalProcessingOutputConfigTypeDef = TypedDict(
    "_OptionalProcessingOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ProcessingOutputConfigTypeDef(
    _RequiredProcessingOutputConfigTypeDef, _OptionalProcessingOutputConfigTypeDef
):
    pass


_RequiredProcessingOutputTypeDef = TypedDict(
    "_RequiredProcessingOutputTypeDef",
    {
        "OutputName": str,
    },
)
_OptionalProcessingOutputTypeDef = TypedDict(
    "_OptionalProcessingOutputTypeDef",
    {
        "S3Output": "ProcessingS3OutputTypeDef",
        "FeatureStoreOutput": "ProcessingFeatureStoreOutputTypeDef",
        "AppManaged": bool,
    },
    total=False,
)


class ProcessingOutputTypeDef(_RequiredProcessingOutputTypeDef, _OptionalProcessingOutputTypeDef):
    pass


ProcessingResourcesTypeDef = TypedDict(
    "ProcessingResourcesTypeDef",
    {
        "ClusterConfig": "ProcessingClusterConfigTypeDef",
    },
)

_RequiredProcessingS3InputTypeDef = TypedDict(
    "_RequiredProcessingS3InputTypeDef",
    {
        "S3Uri": str,
        "S3DataType": ProcessingS3DataTypeType,
    },
)
_OptionalProcessingS3InputTypeDef = TypedDict(
    "_OptionalProcessingS3InputTypeDef",
    {
        "LocalPath": str,
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "S3CompressionType": ProcessingS3CompressionTypeType,
    },
    total=False,
)


class ProcessingS3InputTypeDef(
    _RequiredProcessingS3InputTypeDef, _OptionalProcessingS3InputTypeDef
):
    pass


ProcessingS3OutputTypeDef = TypedDict(
    "ProcessingS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3UploadMode": ProcessingS3UploadModeType,
    },
)

ProcessingStoppingConditionTypeDef = TypedDict(
    "ProcessingStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

_RequiredProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "_RequiredProductionVariantCoreDumpConfigTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "_OptionalProductionVariantCoreDumpConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ProductionVariantCoreDumpConfigTypeDef(
    _RequiredProductionVariantCoreDumpConfigTypeDef, _OptionalProductionVariantCoreDumpConfigTypeDef
):
    pass


_RequiredProductionVariantSummaryTypeDef = TypedDict(
    "_RequiredProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalProductionVariantSummaryTypeDef = TypedDict(
    "_OptionalProductionVariantSummaryTypeDef",
    {
        "DeployedImages": List["DeployedImageTypeDef"],
        "CurrentWeight": float,
        "DesiredWeight": float,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
    },
    total=False,
)


class ProductionVariantSummaryTypeDef(
    _RequiredProductionVariantSummaryTypeDef, _OptionalProductionVariantSummaryTypeDef
):
    pass


_RequiredProductionVariantTypeDef = TypedDict(
    "_RequiredProductionVariantTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
        "InitialInstanceCount": int,
        "InstanceType": ProductionVariantInstanceTypeType,
    },
)
_OptionalProductionVariantTypeDef = TypedDict(
    "_OptionalProductionVariantTypeDef",
    {
        "InitialVariantWeight": float,
        "AcceleratorType": ProductionVariantAcceleratorTypeType,
        "CoreDumpConfig": "ProductionVariantCoreDumpConfigTypeDef",
    },
    total=False,
)


class ProductionVariantTypeDef(
    _RequiredProductionVariantTypeDef, _OptionalProductionVariantTypeDef
):
    pass


ProfilerConfigForUpdateTypeDef = TypedDict(
    "ProfilerConfigForUpdateTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Dict[str, str],
        "DisableProfiler": bool,
    },
    total=False,
)

_RequiredProfilerConfigTypeDef = TypedDict(
    "_RequiredProfilerConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalProfilerConfigTypeDef = TypedDict(
    "_OptionalProfilerConfigTypeDef",
    {
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Dict[str, str],
    },
    total=False,
)


class ProfilerConfigTypeDef(_RequiredProfilerConfigTypeDef, _OptionalProfilerConfigTypeDef):
    pass


_RequiredProfilerRuleConfigurationTypeDef = TypedDict(
    "_RequiredProfilerRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalProfilerRuleConfigurationTypeDef = TypedDict(
    "_OptionalProfilerRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)


class ProfilerRuleConfigurationTypeDef(
    _RequiredProfilerRuleConfigurationTypeDef, _OptionalProfilerRuleConfigurationTypeDef
):
    pass


ProfilerRuleEvaluationStatusTypeDef = TypedDict(
    "ProfilerRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": RuleEvaluationStatusType,
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "ProjectName": str,
        "ProjectArn": str,
        "ProjectId": str,
        "CreationTime": datetime,
        "ProjectStatus": ProjectStatusType,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "ProjectDescription": str,
    },
    total=False,
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass


PropertyNameQueryTypeDef = TypedDict(
    "PropertyNameQueryTypeDef",
    {
        "PropertyNameHint": str,
    },
)

PropertyNameSuggestionTypeDef = TypedDict(
    "PropertyNameSuggestionTypeDef",
    {
        "PropertyName": str,
    },
    total=False,
)

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

PublicWorkforceTaskPriceTypeDef = TypedDict(
    "PublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": "USDTypeDef",
    },
    total=False,
)

PutModelPackageGroupPolicyInputTypeDef = TypedDict(
    "PutModelPackageGroupPolicyInputTypeDef",
    {
        "ModelPackageGroupName": str,
        "ResourcePolicy": str,
    },
)

PutModelPackageGroupPolicyOutputResponseTypeDef = TypedDict(
    "PutModelPackageGroupPolicyOutputResponseTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRedshiftDatasetDefinitionTypeDef = TypedDict(
    "_RequiredRedshiftDatasetDefinitionTypeDef",
    {
        "ClusterId": str,
        "Database": str,
        "DbUser": str,
        "QueryString": str,
        "ClusterRoleArn": str,
        "OutputS3Uri": str,
        "OutputFormat": RedshiftResultFormatType,
    },
)
_OptionalRedshiftDatasetDefinitionTypeDef = TypedDict(
    "_OptionalRedshiftDatasetDefinitionTypeDef",
    {
        "KmsKeyId": str,
        "OutputCompression": RedshiftResultCompressionTypeType,
    },
    total=False,
)


class RedshiftDatasetDefinitionTypeDef(
    _RequiredRedshiftDatasetDefinitionTypeDef, _OptionalRedshiftDatasetDefinitionTypeDef
):
    pass


_RequiredRegisterDevicesRequestTypeDef = TypedDict(
    "_RequiredRegisterDevicesRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": List["DeviceTypeDef"],
    },
)
_OptionalRegisterDevicesRequestTypeDef = TypedDict(
    "_OptionalRegisterDevicesRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RegisterDevicesRequestTypeDef(
    _RequiredRegisterDevicesRequestTypeDef, _OptionalRegisterDevicesRequestTypeDef
):
    pass


RegisterModelStepMetadataTypeDef = TypedDict(
    "RegisterModelStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredRenderUiTemplateRequestTypeDef = TypedDict(
    "_RequiredRenderUiTemplateRequestTypeDef",
    {
        "Task": "RenderableTaskTypeDef",
        "RoleArn": str,
    },
)
_OptionalRenderUiTemplateRequestTypeDef = TypedDict(
    "_OptionalRenderUiTemplateRequestTypeDef",
    {
        "UiTemplate": "UiTemplateTypeDef",
        "HumanTaskUiArn": str,
    },
    total=False,
)


class RenderUiTemplateRequestTypeDef(
    _RequiredRenderUiTemplateRequestTypeDef, _OptionalRenderUiTemplateRequestTypeDef
):
    pass


RenderUiTemplateResponseResponseTypeDef = TypedDict(
    "RenderUiTemplateResponseResponseTypeDef",
    {
        "RenderedContent": str,
        "Errors": List["RenderingErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenderableTaskTypeDef = TypedDict(
    "RenderableTaskTypeDef",
    {
        "Input": str,
    },
)

RenderingErrorTypeDef = TypedDict(
    "RenderingErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
)

RepositoryAuthConfigTypeDef = TypedDict(
    "RepositoryAuthConfigTypeDef",
    {
        "RepositoryCredentialsProviderArn": str,
    },
)

ResolvedAttributesTypeDef = TypedDict(
    "ResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": ProblemTypeType,
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
    },
    total=False,
)

_RequiredResourceConfigTypeDef = TypedDict(
    "_RequiredResourceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
    },
)
_OptionalResourceConfigTypeDef = TypedDict(
    "_OptionalResourceConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ResourceConfigTypeDef(_RequiredResourceConfigTypeDef, _OptionalResourceConfigTypeDef):
    pass


ResourceLimitsTypeDef = TypedDict(
    "ResourceLimitsTypeDef",
    {
        "MaxNumberOfTrainingJobs": int,
        "MaxParallelTrainingJobs": int,
    },
)

ResourceSpecTypeDef = TypedDict(
    "ResourceSpecTypeDef",
    {
        "SageMakerImageArn": str,
        "SageMakerImageVersionArn": str,
        "InstanceType": AppInstanceTypeType,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RetentionPolicyTypeDef = TypedDict(
    "RetentionPolicyTypeDef",
    {
        "HomeEfsFileSystem": RetentionTypeType,
    },
    total=False,
)

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "MaximumRetryAttempts": int,
    },
)

_RequiredS3DataSourceTypeDef = TypedDict(
    "_RequiredS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)
_OptionalS3DataSourceTypeDef = TypedDict(
    "_OptionalS3DataSourceTypeDef",
    {
        "S3DataDistributionType": S3DataDistributionType,
        "AttributeNames": List[str],
    },
    total=False,
)


class S3DataSourceTypeDef(_RequiredS3DataSourceTypeDef, _OptionalS3DataSourceTypeDef):
    pass


_RequiredS3StorageConfigTypeDef = TypedDict(
    "_RequiredS3StorageConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalS3StorageConfigTypeDef = TypedDict(
    "_OptionalS3StorageConfigTypeDef",
    {
        "KmsKeyId": str,
        "ResolvedOutputS3Uri": str,
    },
    total=False,
)


class S3StorageConfigTypeDef(_RequiredS3StorageConfigTypeDef, _OptionalS3StorageConfigTypeDef):
    pass


ScheduleConfigTypeDef = TypedDict(
    "ScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
    },
)

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NestedFilters": List["NestedFiltersTypeDef"],
        "SubExpressions": List[Dict[str, Any]],
        "Operator": BooleanOperatorType,
    },
    total=False,
)

SearchRecordTypeDef = TypedDict(
    "SearchRecordTypeDef",
    {
        "TrainingJob": "TrainingJobTypeDef",
        "Experiment": "ExperimentTypeDef",
        "Trial": "TrialTypeDef",
        "TrialComponent": "TrialComponentTypeDef",
        "Endpoint": "EndpointTypeDef",
        "ModelPackage": "ModelPackageTypeDef",
        "ModelPackageGroup": "ModelPackageGroupTypeDef",
        "Pipeline": "PipelineTypeDef",
        "PipelineExecution": "PipelineExecutionTypeDef",
        "FeatureGroup": "FeatureGroupTypeDef",
    },
    total=False,
)

_RequiredSearchRequestTypeDef = TypedDict(
    "_RequiredSearchRequestTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalSearchRequestTypeDef = TypedDict(
    "_OptionalSearchRequestTypeDef",
    {
        "SearchExpression": "SearchExpressionTypeDef",
        "SortBy": str,
        "SortOrder": SearchSortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchRequestTypeDef(_RequiredSearchRequestTypeDef, _OptionalSearchRequestTypeDef):
    pass


SearchResponseResponseTypeDef = TypedDict(
    "SearchResponseResponseTypeDef",
    {
        "Results": List["SearchRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSecondaryStatusTransitionTypeDef = TypedDict(
    "_RequiredSecondaryStatusTransitionTypeDef",
    {
        "Status": SecondaryStatusType,
        "StartTime": datetime,
    },
)
_OptionalSecondaryStatusTransitionTypeDef = TypedDict(
    "_OptionalSecondaryStatusTransitionTypeDef",
    {
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)


class SecondaryStatusTransitionTypeDef(
    _RequiredSecondaryStatusTransitionTypeDef, _OptionalSecondaryStatusTransitionTypeDef
):
    pass


_RequiredSendPipelineExecutionStepFailureRequestTypeDef = TypedDict(
    "_RequiredSendPipelineExecutionStepFailureRequestTypeDef",
    {
        "CallbackToken": str,
    },
)
_OptionalSendPipelineExecutionStepFailureRequestTypeDef = TypedDict(
    "_OptionalSendPipelineExecutionStepFailureRequestTypeDef",
    {
        "FailureReason": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class SendPipelineExecutionStepFailureRequestTypeDef(
    _RequiredSendPipelineExecutionStepFailureRequestTypeDef,
    _OptionalSendPipelineExecutionStepFailureRequestTypeDef,
):
    pass


SendPipelineExecutionStepFailureResponseResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepFailureResponseResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendPipelineExecutionStepSuccessRequestTypeDef = TypedDict(
    "_RequiredSendPipelineExecutionStepSuccessRequestTypeDef",
    {
        "CallbackToken": str,
    },
)
_OptionalSendPipelineExecutionStepSuccessRequestTypeDef = TypedDict(
    "_OptionalSendPipelineExecutionStepSuccessRequestTypeDef",
    {
        "OutputParameters": List["OutputParameterTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)


class SendPipelineExecutionStepSuccessRequestTypeDef(
    _RequiredSendPipelineExecutionStepSuccessRequestTypeDef,
    _OptionalSendPipelineExecutionStepSuccessRequestTypeDef,
):
    pass


SendPipelineExecutionStepSuccessResponseResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepSuccessResponseResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceCatalogProvisionedProductDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductStatusMessage": str,
    },
    total=False,
)

_RequiredServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "_RequiredServiceCatalogProvisioningDetailsTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "_OptionalServiceCatalogProvisioningDetailsTypeDef",
    {
        "PathId": str,
        "ProvisioningParameters": List["ProvisioningParameterTypeDef"],
    },
    total=False,
)


class ServiceCatalogProvisioningDetailsTypeDef(
    _RequiredServiceCatalogProvisioningDetailsTypeDef,
    _OptionalServiceCatalogProvisioningDetailsTypeDef,
):
    pass


SharingSettingsTypeDef = TypedDict(
    "SharingSettingsTypeDef",
    {
        "NotebookOutputOption": NotebookOutputOptionType,
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ShuffleConfigTypeDef = TypedDict(
    "ShuffleConfigTypeDef",
    {
        "Seed": int,
    },
)

SourceAlgorithmSpecificationTypeDef = TypedDict(
    "SourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": List["SourceAlgorithmTypeDef"],
    },
)

_RequiredSourceAlgorithmTypeDef = TypedDict(
    "_RequiredSourceAlgorithmTypeDef",
    {
        "AlgorithmName": str,
    },
)
_OptionalSourceAlgorithmTypeDef = TypedDict(
    "_OptionalSourceAlgorithmTypeDef",
    {
        "ModelDataUrl": str,
    },
    total=False,
)


class SourceAlgorithmTypeDef(_RequiredSourceAlgorithmTypeDef, _OptionalSourceAlgorithmTypeDef):
    pass


SourceIpConfigTypeDef = TypedDict(
    "SourceIpConfigTypeDef",
    {
        "Cidrs": List[str],
    },
)

StartMonitoringScheduleRequestTypeDef = TypedDict(
    "StartMonitoringScheduleRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StartNotebookInstanceInputTypeDef = TypedDict(
    "StartNotebookInstanceInputTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

_RequiredStartPipelineExecutionRequestTypeDef = TypedDict(
    "_RequiredStartPipelineExecutionRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)
_OptionalStartPipelineExecutionRequestTypeDef = TypedDict(
    "_OptionalStartPipelineExecutionRequestTypeDef",
    {
        "PipelineExecutionDisplayName": str,
        "PipelineParameters": List["ParameterTypeDef"],
        "PipelineExecutionDescription": str,
    },
    total=False,
)


class StartPipelineExecutionRequestTypeDef(
    _RequiredStartPipelineExecutionRequestTypeDef, _OptionalStartPipelineExecutionRequestTypeDef
):
    pass


StartPipelineExecutionResponseResponseTypeDef = TypedDict(
    "StartPipelineExecutionResponseResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAutoMLJobRequestTypeDef = TypedDict(
    "StopAutoMLJobRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

StopCompilationJobRequestTypeDef = TypedDict(
    "StopCompilationJobRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

StopEdgePackagingJobRequestTypeDef = TypedDict(
    "StopEdgePackagingJobRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

StopHyperParameterTuningJobRequestTypeDef = TypedDict(
    "StopHyperParameterTuningJobRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

StopLabelingJobRequestTypeDef = TypedDict(
    "StopLabelingJobRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

StopMonitoringScheduleRequestTypeDef = TypedDict(
    "StopMonitoringScheduleRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StopNotebookInstanceInputTypeDef = TypedDict(
    "StopNotebookInstanceInputTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

StopPipelineExecutionRequestTypeDef = TypedDict(
    "StopPipelineExecutionRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
    },
)

StopPipelineExecutionResponseResponseTypeDef = TypedDict(
    "StopPipelineExecutionResponseResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProcessingJobRequestTypeDef = TypedDict(
    "StopProcessingJobRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

StopTrainingJobRequestTypeDef = TypedDict(
    "StopTrainingJobRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

StopTransformJobRequestTypeDef = TypedDict(
    "StopTransformJobRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

StoppingConditionTypeDef = TypedDict(
    "StoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
        "MaxWaitTimeInSeconds": int,
    },
    total=False,
)

_RequiredSubscribedWorkteamTypeDef = TypedDict(
    "_RequiredSubscribedWorkteamTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalSubscribedWorkteamTypeDef = TypedDict(
    "_OptionalSubscribedWorkteamTypeDef",
    {
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)


class SubscribedWorkteamTypeDef(
    _RequiredSubscribedWorkteamTypeDef, _OptionalSubscribedWorkteamTypeDef
):
    pass


SuggestionQueryTypeDef = TypedDict(
    "SuggestionQueryTypeDef",
    {
        "PropertyNameQuery": "PropertyNameQueryTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTargetPlatformTypeDef = TypedDict(
    "_RequiredTargetPlatformTypeDef",
    {
        "Os": TargetPlatformOsType,
        "Arch": TargetPlatformArchType,
    },
)
_OptionalTargetPlatformTypeDef = TypedDict(
    "_OptionalTargetPlatformTypeDef",
    {
        "Accelerator": TargetPlatformAcceleratorType,
    },
    total=False,
)


class TargetPlatformTypeDef(_RequiredTargetPlatformTypeDef, _OptionalTargetPlatformTypeDef):
    pass


TensorBoardAppSettingsTypeDef = TypedDict(
    "TensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
    },
    total=False,
)

_RequiredTensorBoardOutputConfigTypeDef = TypedDict(
    "_RequiredTensorBoardOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTensorBoardOutputConfigTypeDef = TypedDict(
    "_OptionalTensorBoardOutputConfigTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)


class TensorBoardOutputConfigTypeDef(
    _RequiredTensorBoardOutputConfigTypeDef, _OptionalTensorBoardOutputConfigTypeDef
):
    pass


_RequiredTrafficRoutingConfigTypeDef = TypedDict(
    "_RequiredTrafficRoutingConfigTypeDef",
    {
        "Type": TrafficRoutingConfigTypeType,
        "WaitIntervalInSeconds": int,
    },
)
_OptionalTrafficRoutingConfigTypeDef = TypedDict(
    "_OptionalTrafficRoutingConfigTypeDef",
    {
        "CanarySize": "CapacitySizeTypeDef",
    },
    total=False,
)


class TrafficRoutingConfigTypeDef(
    _RequiredTrafficRoutingConfigTypeDef, _OptionalTrafficRoutingConfigTypeDef
):
    pass


_RequiredTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalTrainingJobDefinitionTypeDef",
    {
        "HyperParameters": Dict[str, str],
    },
    total=False,
)


class TrainingJobDefinitionTypeDef(
    _RequiredTrainingJobDefinitionTypeDef, _OptionalTrainingJobDefinitionTypeDef
):
    pass


TrainingJobStatusCountersTypeDef = TypedDict(
    "TrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)

TrainingJobStepMetadataTypeDef = TypedDict(
    "TrainingJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
    },
)
_OptionalTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalTrainingJobSummaryTypeDef",
    {
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class TrainingJobSummaryTypeDef(
    _RequiredTrainingJobSummaryTypeDef, _OptionalTrainingJobSummaryTypeDef
):
    pass


TrainingJobTypeDef = TypedDict(
    "TrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List["SecondaryStatusTransitionTypeDef"],
        "FinalMetricDataList": List["MetricDataTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "DebugRuleEvaluationStatuses": List["DebugRuleEvaluationStatusTypeDef"],
        "Environment": Dict[str, str],
        "RetryStrategy": "RetryStrategyTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredTrainingSpecificationTypeDef = TypedDict(
    "_RequiredTrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "SupportedTrainingInstanceTypes": List[TrainingInstanceTypeType],
        "TrainingChannels": List["ChannelSpecificationTypeDef"],
    },
)
_OptionalTrainingSpecificationTypeDef = TypedDict(
    "_OptionalTrainingSpecificationTypeDef",
    {
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List["HyperParameterSpecificationTypeDef"],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "SupportedTuningJobObjectiveMetrics": List["HyperParameterTuningJobObjectiveTypeDef"],
    },
    total=False,
)


class TrainingSpecificationTypeDef(
    _RequiredTrainingSpecificationTypeDef, _OptionalTrainingSpecificationTypeDef
):
    pass


TransformDataSourceTypeDef = TypedDict(
    "TransformDataSourceTypeDef",
    {
        "S3DataSource": "TransformS3DataSourceTypeDef",
    },
)

_RequiredTransformInputTypeDef = TypedDict(
    "_RequiredTransformInputTypeDef",
    {
        "DataSource": "TransformDataSourceTypeDef",
    },
)
_OptionalTransformInputTypeDef = TypedDict(
    "_OptionalTransformInputTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "SplitType": SplitTypeType,
    },
    total=False,
)


class TransformInputTypeDef(_RequiredTransformInputTypeDef, _OptionalTransformInputTypeDef):
    pass


_RequiredTransformJobDefinitionTypeDef = TypedDict(
    "_RequiredTransformJobDefinitionTypeDef",
    {
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
    },
)
_OptionalTransformJobDefinitionTypeDef = TypedDict(
    "_OptionalTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
    },
    total=False,
)


class TransformJobDefinitionTypeDef(
    _RequiredTransformJobDefinitionTypeDef, _OptionalTransformJobDefinitionTypeDef
):
    pass


TransformJobStepMetadataTypeDef = TypedDict(
    "TransformJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredTransformJobSummaryTypeDef = TypedDict(
    "_RequiredTransformJobSummaryTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformJobStatus": TransformJobStatusType,
    },
)
_OptionalTransformJobSummaryTypeDef = TypedDict(
    "_OptionalTransformJobSummaryTypeDef",
    {
        "TransformEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)


class TransformJobSummaryTypeDef(
    _RequiredTransformJobSummaryTypeDef, _OptionalTransformJobSummaryTypeDef
):
    pass


TransformJobTypeDef = TypedDict(
    "TransformJobTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": "DataProcessingTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredTransformOutputTypeDef = TypedDict(
    "_RequiredTransformOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTransformOutputTypeDef = TypedDict(
    "_OptionalTransformOutputTypeDef",
    {
        "Accept": str,
        "AssembleWith": AssemblyTypeType,
        "KmsKeyId": str,
    },
    total=False,
)


class TransformOutputTypeDef(_RequiredTransformOutputTypeDef, _OptionalTransformOutputTypeDef):
    pass


_RequiredTransformResourcesTypeDef = TypedDict(
    "_RequiredTransformResourcesTypeDef",
    {
        "InstanceType": TransformInstanceTypeType,
        "InstanceCount": int,
    },
)
_OptionalTransformResourcesTypeDef = TypedDict(
    "_OptionalTransformResourcesTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class TransformResourcesTypeDef(
    _RequiredTransformResourcesTypeDef, _OptionalTransformResourcesTypeDef
):
    pass


TransformS3DataSourceTypeDef = TypedDict(
    "TransformS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)

_RequiredTrialComponentArtifactTypeDef = TypedDict(
    "_RequiredTrialComponentArtifactTypeDef",
    {
        "Value": str,
    },
)
_OptionalTrialComponentArtifactTypeDef = TypedDict(
    "_OptionalTrialComponentArtifactTypeDef",
    {
        "MediaType": str,
    },
    total=False,
)


class TrialComponentArtifactTypeDef(
    _RequiredTrialComponentArtifactTypeDef, _OptionalTrialComponentArtifactTypeDef
):
    pass


TrialComponentMetricSummaryTypeDef = TypedDict(
    "TrialComponentMetricSummaryTypeDef",
    {
        "MetricName": str,
        "SourceArn": str,
        "TimeStamp": datetime,
        "Max": float,
        "Min": float,
        "Last": float,
        "Count": int,
        "Avg": float,
        "StdDev": float,
    },
    total=False,
)

TrialComponentParameterValueTypeDef = TypedDict(
    "TrialComponentParameterValueTypeDef",
    {
        "StringValue": str,
        "NumberValue": float,
    },
    total=False,
)

TrialComponentSimpleSummaryTypeDef = TypedDict(
    "TrialComponentSimpleSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "TrialComponentSource": "TrialComponentSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
    },
    total=False,
)

TrialComponentSourceDetailTypeDef = TypedDict(
    "TrialComponentSourceDetailTypeDef",
    {
        "SourceArn": str,
        "TrainingJob": "TrainingJobTypeDef",
        "ProcessingJob": "ProcessingJobTypeDef",
        "TransformJob": "TransformJobTypeDef",
    },
    total=False,
)

_RequiredTrialComponentSourceTypeDef = TypedDict(
    "_RequiredTrialComponentSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalTrialComponentSourceTypeDef = TypedDict(
    "_OptionalTrialComponentSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)


class TrialComponentSourceTypeDef(
    _RequiredTrialComponentSourceTypeDef, _OptionalTrialComponentSourceTypeDef
):
    pass


TrialComponentStatusTypeDef = TypedDict(
    "TrialComponentStatusTypeDef",
    {
        "PrimaryStatus": TrialComponentPrimaryStatusType,
        "Message": str,
    },
    total=False,
)

TrialComponentSummaryTypeDef = TypedDict(
    "TrialComponentSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "TrialComponentSource": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
    },
    total=False,
)

TrialComponentTypeDef = TypedDict(
    "TrialComponentTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": str,
        "TrialComponentArn": str,
        "Source": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "Metrics": List["TrialComponentMetricSummaryTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "SourceDetail": "TrialComponentSourceDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "Parents": List["ParentTypeDef"],
    },
    total=False,
)

_RequiredTrialSourceTypeDef = TypedDict(
    "_RequiredTrialSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalTrialSourceTypeDef = TypedDict(
    "_OptionalTrialSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)


class TrialSourceTypeDef(_RequiredTrialSourceTypeDef, _OptionalTrialSourceTypeDef):
    pass


TrialSummaryTypeDef = TypedDict(
    "TrialSummaryTypeDef",
    {
        "TrialArn": str,
        "TrialName": str,
        "DisplayName": str,
        "TrialSource": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

TrialTypeDef = TypedDict(
    "TrialTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
        "TrialComponentSummaries": List["TrialComponentSimpleSummaryTypeDef"],
    },
    total=False,
)

TuningJobCompletionCriteriaTypeDef = TypedDict(
    "TuningJobCompletionCriteriaTypeDef",
    {
        "TargetObjectiveMetricValue": float,
    },
)

USDTypeDef = TypedDict(
    "USDTypeDef",
    {
        "Dollars": int,
        "Cents": int,
        "TenthFractionsOfACent": int,
    },
    total=False,
)

UiConfigTypeDef = TypedDict(
    "UiConfigTypeDef",
    {
        "UiTemplateS3Uri": str,
        "HumanTaskUiArn": str,
    },
    total=False,
)

UiTemplateInfoTypeDef = TypedDict(
    "UiTemplateInfoTypeDef",
    {
        "Url": str,
        "ContentSha256": str,
    },
    total=False,
)

UiTemplateTypeDef = TypedDict(
    "UiTemplateTypeDef",
    {
        "Content": str,
    },
)

_RequiredUpdateActionRequestTypeDef = TypedDict(
    "_RequiredUpdateActionRequestTypeDef",
    {
        "ActionName": str,
    },
)
_OptionalUpdateActionRequestTypeDef = TypedDict(
    "_OptionalUpdateActionRequestTypeDef",
    {
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "PropertiesToRemove": List[str],
    },
    total=False,
)


class UpdateActionRequestTypeDef(
    _RequiredUpdateActionRequestTypeDef, _OptionalUpdateActionRequestTypeDef
):
    pass


UpdateActionResponseResponseTypeDef = TypedDict(
    "UpdateActionResponseResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppImageConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateAppImageConfigRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)
_OptionalUpdateAppImageConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateAppImageConfigRequestTypeDef",
    {
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)


class UpdateAppImageConfigRequestTypeDef(
    _RequiredUpdateAppImageConfigRequestTypeDef, _OptionalUpdateAppImageConfigRequestTypeDef
):
    pass


UpdateAppImageConfigResponseResponseTypeDef = TypedDict(
    "UpdateAppImageConfigResponseResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateArtifactRequestTypeDef = TypedDict(
    "_RequiredUpdateArtifactRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)
_OptionalUpdateArtifactRequestTypeDef = TypedDict(
    "_OptionalUpdateArtifactRequestTypeDef",
    {
        "ArtifactName": str,
        "Properties": Dict[str, str],
        "PropertiesToRemove": List[str],
    },
    total=False,
)


class UpdateArtifactRequestTypeDef(
    _RequiredUpdateArtifactRequestTypeDef, _OptionalUpdateArtifactRequestTypeDef
):
    pass


UpdateArtifactResponseResponseTypeDef = TypedDict(
    "UpdateArtifactResponseResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCodeRepositoryInputTypeDef = TypedDict(
    "_RequiredUpdateCodeRepositoryInputTypeDef",
    {
        "CodeRepositoryName": str,
    },
)
_OptionalUpdateCodeRepositoryInputTypeDef = TypedDict(
    "_OptionalUpdateCodeRepositoryInputTypeDef",
    {
        "GitConfig": "GitConfigForUpdateTypeDef",
    },
    total=False,
)


class UpdateCodeRepositoryInputTypeDef(
    _RequiredUpdateCodeRepositoryInputTypeDef, _OptionalUpdateCodeRepositoryInputTypeDef
):
    pass


UpdateCodeRepositoryOutputResponseTypeDef = TypedDict(
    "UpdateCodeRepositoryOutputResponseTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContextRequestTypeDef = TypedDict(
    "_RequiredUpdateContextRequestTypeDef",
    {
        "ContextName": str,
    },
)
_OptionalUpdateContextRequestTypeDef = TypedDict(
    "_OptionalUpdateContextRequestTypeDef",
    {
        "Description": str,
        "Properties": Dict[str, str],
        "PropertiesToRemove": List[str],
    },
    total=False,
)


class UpdateContextRequestTypeDef(
    _RequiredUpdateContextRequestTypeDef, _OptionalUpdateContextRequestTypeDef
):
    pass


UpdateContextResponseResponseTypeDef = TypedDict(
    "UpdateContextResponseResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDeviceFleetRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceFleetRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
    },
)
_OptionalUpdateDeviceFleetRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceFleetRequestTypeDef",
    {
        "RoleArn": str,
        "Description": str,
        "EnableIotRoleAlias": bool,
    },
    total=False,
)


class UpdateDeviceFleetRequestTypeDef(
    _RequiredUpdateDeviceFleetRequestTypeDef, _OptionalUpdateDeviceFleetRequestTypeDef
):
    pass


UpdateDevicesRequestTypeDef = TypedDict(
    "UpdateDevicesRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": List["DeviceTypeDef"],
    },
)

_RequiredUpdateDomainRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalUpdateDomainRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainRequestTypeDef",
    {
        "DefaultUserSettings": "UserSettingsTypeDef",
    },
    total=False,
)


class UpdateDomainRequestTypeDef(
    _RequiredUpdateDomainRequestTypeDef, _OptionalUpdateDomainRequestTypeDef
):
    pass


UpdateDomainResponseResponseTypeDef = TypedDict(
    "UpdateDomainResponseResponseTypeDef",
    {
        "DomainArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEndpointInputTypeDef = TypedDict(
    "_RequiredUpdateEndpointInputTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
    },
)
_OptionalUpdateEndpointInputTypeDef = TypedDict(
    "_OptionalUpdateEndpointInputTypeDef",
    {
        "RetainAllVariantProperties": bool,
        "ExcludeRetainedVariantProperties": List["VariantPropertyTypeDef"],
        "DeploymentConfig": "DeploymentConfigTypeDef",
    },
    total=False,
)


class UpdateEndpointInputTypeDef(
    _RequiredUpdateEndpointInputTypeDef, _OptionalUpdateEndpointInputTypeDef
):
    pass


UpdateEndpointOutputResponseTypeDef = TypedDict(
    "UpdateEndpointOutputResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointWeightsAndCapacitiesInputTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesInputTypeDef",
    {
        "EndpointName": str,
        "DesiredWeightsAndCapacities": List["DesiredWeightAndCapacityTypeDef"],
    },
)

UpdateEndpointWeightsAndCapacitiesOutputResponseTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesOutputResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateExperimentRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentRequestTypeDef",
    {
        "ExperimentName": str,
    },
)
_OptionalUpdateExperimentRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
    },
    total=False,
)


class UpdateExperimentRequestTypeDef(
    _RequiredUpdateExperimentRequestTypeDef, _OptionalUpdateExperimentRequestTypeDef
):
    pass


UpdateExperimentResponseResponseTypeDef = TypedDict(
    "UpdateExperimentResponseResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateImageRequestTypeDef = TypedDict(
    "_RequiredUpdateImageRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalUpdateImageRequestTypeDef = TypedDict(
    "_OptionalUpdateImageRequestTypeDef",
    {
        "DeleteProperties": List[str],
        "Description": str,
        "DisplayName": str,
        "RoleArn": str,
    },
    total=False,
)


class UpdateImageRequestTypeDef(
    _RequiredUpdateImageRequestTypeDef, _OptionalUpdateImageRequestTypeDef
):
    pass


UpdateImageResponseResponseTypeDef = TypedDict(
    "UpdateImageResponseResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelPackageInputTypeDef = TypedDict(
    "_RequiredUpdateModelPackageInputTypeDef",
    {
        "ModelPackageArn": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
    },
)
_OptionalUpdateModelPackageInputTypeDef = TypedDict(
    "_OptionalUpdateModelPackageInputTypeDef",
    {
        "ApprovalDescription": str,
    },
    total=False,
)


class UpdateModelPackageInputTypeDef(
    _RequiredUpdateModelPackageInputTypeDef, _OptionalUpdateModelPackageInputTypeDef
):
    pass


UpdateModelPackageOutputResponseTypeDef = TypedDict(
    "UpdateModelPackageOutputResponseTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMonitoringScheduleRequestTypeDef = TypedDict(
    "UpdateMonitoringScheduleRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
    },
)

UpdateMonitoringScheduleResponseResponseTypeDef = TypedDict(
    "UpdateMonitoringScheduleResponseResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNotebookInstanceInputTypeDef = TypedDict(
    "_RequiredUpdateNotebookInstanceInputTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalUpdateNotebookInstanceInputTypeDef = TypedDict(
    "_OptionalUpdateNotebookInstanceInputTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
        "LifecycleConfigName": str,
        "DisassociateLifecycleConfig": bool,
        "VolumeSizeInGB": int,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DisassociateAcceleratorTypes": bool,
        "DisassociateDefaultCodeRepository": bool,
        "DisassociateAdditionalCodeRepositories": bool,
        "RootAccess": RootAccessType,
    },
    total=False,
)


class UpdateNotebookInstanceInputTypeDef(
    _RequiredUpdateNotebookInstanceInputTypeDef, _OptionalUpdateNotebookInstanceInputTypeDef
):
    pass


_RequiredUpdateNotebookInstanceLifecycleConfigInputTypeDef = TypedDict(
    "_RequiredUpdateNotebookInstanceLifecycleConfigInputTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)
_OptionalUpdateNotebookInstanceLifecycleConfigInputTypeDef = TypedDict(
    "_OptionalUpdateNotebookInstanceLifecycleConfigInputTypeDef",
    {
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
    },
    total=False,
)


class UpdateNotebookInstanceLifecycleConfigInputTypeDef(
    _RequiredUpdateNotebookInstanceLifecycleConfigInputTypeDef,
    _OptionalUpdateNotebookInstanceLifecycleConfigInputTypeDef,
):
    pass


_RequiredUpdatePipelineExecutionRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineExecutionRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalUpdatePipelineExecutionRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineExecutionRequestTypeDef",
    {
        "PipelineExecutionDescription": str,
        "PipelineExecutionDisplayName": str,
    },
    total=False,
)


class UpdatePipelineExecutionRequestTypeDef(
    _RequiredUpdatePipelineExecutionRequestTypeDef, _OptionalUpdatePipelineExecutionRequestTypeDef
):
    pass


UpdatePipelineExecutionResponseResponseTypeDef = TypedDict(
    "UpdatePipelineExecutionResponseResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePipelineRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalUpdatePipelineRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineRequestTypeDef",
    {
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDescription": str,
        "RoleArn": str,
    },
    total=False,
)


class UpdatePipelineRequestTypeDef(
    _RequiredUpdatePipelineRequestTypeDef, _OptionalUpdatePipelineRequestTypeDef
):
    pass


UpdatePipelineResponseResponseTypeDef = TypedDict(
    "UpdatePipelineResponseResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrainingJobRequestTypeDef = TypedDict(
    "_RequiredUpdateTrainingJobRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)
_OptionalUpdateTrainingJobRequestTypeDef = TypedDict(
    "_OptionalUpdateTrainingJobRequestTypeDef",
    {
        "ProfilerConfig": "ProfilerConfigForUpdateTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
    },
    total=False,
)


class UpdateTrainingJobRequestTypeDef(
    _RequiredUpdateTrainingJobRequestTypeDef, _OptionalUpdateTrainingJobRequestTypeDef
):
    pass


UpdateTrainingJobResponseResponseTypeDef = TypedDict(
    "UpdateTrainingJobResponseResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrialComponentRequestTypeDef = TypedDict(
    "_RequiredUpdateTrialComponentRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)
_OptionalUpdateTrialComponentRequestTypeDef = TypedDict(
    "_OptionalUpdateTrialComponentRequestTypeDef",
    {
        "DisplayName": str,
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "ParametersToRemove": List[str],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "InputArtifactsToRemove": List[str],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifactsToRemove": List[str],
    },
    total=False,
)


class UpdateTrialComponentRequestTypeDef(
    _RequiredUpdateTrialComponentRequestTypeDef, _OptionalUpdateTrialComponentRequestTypeDef
):
    pass


UpdateTrialComponentResponseResponseTypeDef = TypedDict(
    "UpdateTrialComponentResponseResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrialRequestTypeDef = TypedDict(
    "_RequiredUpdateTrialRequestTypeDef",
    {
        "TrialName": str,
    },
)
_OptionalUpdateTrialRequestTypeDef = TypedDict(
    "_OptionalUpdateTrialRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class UpdateTrialRequestTypeDef(
    _RequiredUpdateTrialRequestTypeDef, _OptionalUpdateTrialRequestTypeDef
):
    pass


UpdateTrialResponseResponseTypeDef = TypedDict(
    "UpdateTrialResponseResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalUpdateUserProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileRequestTypeDef",
    {
        "UserSettings": "UserSettingsTypeDef",
    },
    total=False,
)


class UpdateUserProfileRequestTypeDef(
    _RequiredUpdateUserProfileRequestTypeDef, _OptionalUpdateUserProfileRequestTypeDef
):
    pass


UpdateUserProfileResponseResponseTypeDef = TypedDict(
    "UpdateUserProfileResponseResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkforceRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkforceRequestTypeDef",
    {
        "WorkforceName": str,
    },
)
_OptionalUpdateWorkforceRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkforceRequestTypeDef",
    {
        "SourceIpConfig": "SourceIpConfigTypeDef",
        "OidcConfig": "OidcConfigTypeDef",
    },
    total=False,
)


class UpdateWorkforceRequestTypeDef(
    _RequiredUpdateWorkforceRequestTypeDef, _OptionalUpdateWorkforceRequestTypeDef
):
    pass


UpdateWorkforceResponseResponseTypeDef = TypedDict(
    "UpdateWorkforceResponseResponseTypeDef",
    {
        "Workforce": "WorkforceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkteamRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkteamRequestTypeDef",
    {
        "WorkteamName": str,
    },
)
_OptionalUpdateWorkteamRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkteamRequestTypeDef",
    {
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "Description": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
    total=False,
)


class UpdateWorkteamRequestTypeDef(
    _RequiredUpdateWorkteamRequestTypeDef, _OptionalUpdateWorkteamRequestTypeDef
):
    pass


UpdateWorkteamResponseResponseTypeDef = TypedDict(
    "UpdateWorkteamResponseResponseTypeDef",
    {
        "Workteam": "WorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "UserProfileArn": str,
        "UserProfileName": str,
        "DomainId": str,
    },
    total=False,
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "Status": UserProfileStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": "SharingSettingsTypeDef",
        "JupyterServerAppSettings": "JupyterServerAppSettingsTypeDef",
        "KernelGatewayAppSettings": "KernelGatewayAppSettingsTypeDef",
        "TensorBoardAppSettings": "TensorBoardAppSettingsTypeDef",
    },
    total=False,
)

VariantPropertyTypeDef = TypedDict(
    "VariantPropertyTypeDef",
    {
        "VariantPropertyType": VariantPropertyTypeType,
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWorkforceTypeDef = TypedDict(
    "_RequiredWorkforceTypeDef",
    {
        "WorkforceName": str,
        "WorkforceArn": str,
    },
)
_OptionalWorkforceTypeDef = TypedDict(
    "_OptionalWorkforceTypeDef",
    {
        "LastUpdatedDate": datetime,
        "SourceIpConfig": "SourceIpConfigTypeDef",
        "SubDomain": str,
        "CognitoConfig": "CognitoConfigTypeDef",
        "OidcConfig": "OidcConfigForResponseTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)


class WorkforceTypeDef(_RequiredWorkforceTypeDef, _OptionalWorkforceTypeDef):
    pass


_RequiredWorkteamTypeDef = TypedDict(
    "_RequiredWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "WorkteamArn": str,
        "Description": str,
    },
)
_OptionalWorkteamTypeDef = TypedDict(
    "_OptionalWorkteamTypeDef",
    {
        "WorkforceArn": str,
        "ProductListingIds": List[str],
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
    total=False,
)


class WorkteamTypeDef(_RequiredWorkteamTypeDef, _OptionalWorkteamTypeDef):
    pass
