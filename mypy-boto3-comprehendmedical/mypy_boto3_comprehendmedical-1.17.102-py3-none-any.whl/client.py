"""
Type annotations for comprehendmedical service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehendmedical import ComprehendMedicalClient

    client: ComprehendMedicalClient = boto3.client("comprehendmedical")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .type_defs import (
    ComprehendMedicalAsyncJobFilterTypeDef,
    DescribeEntitiesDetectionV2JobResponseResponseTypeDef,
    DescribeICD10CMInferenceJobResponseResponseTypeDef,
    DescribePHIDetectionJobResponseResponseTypeDef,
    DescribeRxNormInferenceJobResponseResponseTypeDef,
    DetectEntitiesResponseResponseTypeDef,
    DetectEntitiesV2ResponseResponseTypeDef,
    DetectPHIResponseResponseTypeDef,
    InferICD10CMResponseResponseTypeDef,
    InferRxNormResponseResponseTypeDef,
    InputDataConfigTypeDef,
    ListEntitiesDetectionV2JobsResponseResponseTypeDef,
    ListICD10CMInferenceJobsResponseResponseTypeDef,
    ListPHIDetectionJobsResponseResponseTypeDef,
    ListRxNormInferenceJobsResponseResponseTypeDef,
    OutputDataConfigTypeDef,
    StartEntitiesDetectionV2JobResponseResponseTypeDef,
    StartICD10CMInferenceJobResponseResponseTypeDef,
    StartPHIDetectionJobResponseResponseTypeDef,
    StartRxNormInferenceJobResponseResponseTypeDef,
    StopEntitiesDetectionV2JobResponseResponseTypeDef,
    StopICD10CMInferenceJobResponseResponseTypeDef,
    StopPHIDetectionJobResponseResponseTypeDef,
    StopRxNormInferenceJobResponseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComprehendMedicalClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidEncodingException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ComprehendMedicalClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#can_paginate)
        """

    def describe_entities_detection_v2_job(
        self, *, JobId: str
    ) -> DescribeEntitiesDetectionV2JobResponseResponseTypeDef:
        """
        Gets the properties associated with a medical entities detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_entities_detection_v2_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#describe_entities_detection_v2_job)
        """

    def describe_icd10_cm_inference_job(
        self, *, JobId: str
    ) -> DescribeICD10CMInferenceJobResponseResponseTypeDef:
        """
        Gets the properties associated with an InferICD10CM job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_icd10_cm_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#describe_icd10_cm_inference_job)
        """

    def describe_phi_detection_job(
        self, *, JobId: str
    ) -> DescribePHIDetectionJobResponseResponseTypeDef:
        """
        Gets the properties associated with a protected health information (PHI)
        detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_phi_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#describe_phi_detection_job)
        """

    def describe_rx_norm_inference_job(
        self, *, JobId: str
    ) -> DescribeRxNormInferenceJobResponseResponseTypeDef:
        """
        Gets the properties associated with an InferRxNorm job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_rx_norm_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#describe_rx_norm_inference_job)
        """

    def detect_entities(self, *, Text: str) -> DetectEntitiesResponseResponseTypeDef:
        """
        The `DetectEntities` operation is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#detect_entities)
        """

    def detect_entities_v2(self, *, Text: str) -> DetectEntitiesV2ResponseResponseTypeDef:
        """
        Inspects the clinical text for a variety of medical entities and returns
        specific information about them such as entity category, location, and
        confidence score on that information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#detect_entities_v2)
        """

    def detect_phi(self, *, Text: str) -> DetectPHIResponseResponseTypeDef:
        """
        Inspects the clinical text for protected health information (PHI) entities and
        returns the entity category, location, and confidence score for each entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_phi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#detect_phi)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#generate_presigned_url)
        """

    def infer_icd10_cm(self, *, Text: str) -> InferICD10CMResponseResponseTypeDef:
        """
        InferICD10CM detects medical conditions as entities listed in a patient record
        and links those entities to normalized concept identifiers in the ICD-10-CM
        knowledge base from the Centers for Disease Control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_icd10_cm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#infer_icd10_cm)
        """

    def infer_rx_norm(self, *, Text: str) -> InferRxNormResponseResponseTypeDef:
        """
        InferRxNorm detects medications as entities listed in a patient record and links
        to the normalized concept identifiers in the RxNorm database from the National
        Library of Medicine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_rx_norm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#infer_rx_norm)
        """

    def list_entities_detection_v2_jobs(
        self,
        *,
        Filter: "ComprehendMedicalAsyncJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntitiesDetectionV2JobsResponseResponseTypeDef:
        """
        Gets a list of medical entity detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_entities_detection_v2_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#list_entities_detection_v2_jobs)
        """

    def list_icd10_cm_inference_jobs(
        self,
        *,
        Filter: "ComprehendMedicalAsyncJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListICD10CMInferenceJobsResponseResponseTypeDef:
        """
        Gets a list of InferICD10CM jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_icd10_cm_inference_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#list_icd10_cm_inference_jobs)
        """

    def list_phi_detection_jobs(
        self,
        *,
        Filter: "ComprehendMedicalAsyncJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPHIDetectionJobsResponseResponseTypeDef:
        """
        Gets a list of protected health information (PHI) detection jobs that you have
        submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_phi_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#list_phi_detection_jobs)
        """

    def list_rx_norm_inference_jobs(
        self,
        *,
        Filter: "ComprehendMedicalAsyncJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListRxNormInferenceJobsResponseResponseTypeDef:
        """
        Gets a list of InferRxNorm jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_rx_norm_inference_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#list_rx_norm_inference_jobs)
        """

    def start_entities_detection_v2_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None
    ) -> StartEntitiesDetectionV2JobResponseResponseTypeDef:
        """
        Starts an asynchronous medical entity detection job for a collection of
        documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_entities_detection_v2_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#start_entities_detection_v2_job)
        """

    def start_icd10_cm_inference_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None
    ) -> StartICD10CMInferenceJobResponseResponseTypeDef:
        """
        Starts an asynchronous job to detect medical conditions and link them to the
        ICD-10-CM ontology.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_icd10_cm_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#start_icd10_cm_inference_job)
        """

    def start_phi_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None
    ) -> StartPHIDetectionJobResponseResponseTypeDef:
        """
        Starts an asynchronous job to detect protected health information (PHI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_phi_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#start_phi_detection_job)
        """

    def start_rx_norm_inference_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None
    ) -> StartRxNormInferenceJobResponseResponseTypeDef:
        """
        Starts an asynchronous job to detect medication entities and link them to the
        RxNorm ontology.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_rx_norm_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#start_rx_norm_inference_job)
        """

    def stop_entities_detection_v2_job(
        self, *, JobId: str
    ) -> StopEntitiesDetectionV2JobResponseResponseTypeDef:
        """
        Stops a medical entities detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_entities_detection_v2_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#stop_entities_detection_v2_job)
        """

    def stop_icd10_cm_inference_job(
        self, *, JobId: str
    ) -> StopICD10CMInferenceJobResponseResponseTypeDef:
        """
        Stops an InferICD10CM inference job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_icd10_cm_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#stop_icd10_cm_inference_job)
        """

    def stop_phi_detection_job(self, *, JobId: str) -> StopPHIDetectionJobResponseResponseTypeDef:
        """
        Stops a protected health information (PHI) detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_phi_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#stop_phi_detection_job)
        """

    def stop_rx_norm_inference_job(
        self, *, JobId: str
    ) -> StopRxNormInferenceJobResponseResponseTypeDef:
        """
        Stops an InferRxNorm inference job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_rx_norm_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/client.html#stop_rx_norm_inference_job)
        """
