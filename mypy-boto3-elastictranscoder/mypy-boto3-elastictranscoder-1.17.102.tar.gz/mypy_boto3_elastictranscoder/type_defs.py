"""
Type annotations for elastictranscoder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elastictranscoder.type_defs import ArtworkTypeDef

    data: ArtworkTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArtworkTypeDef",
    "AudioCodecOptionsTypeDef",
    "AudioParametersTypeDef",
    "CancelJobRequestTypeDef",
    "CaptionFormatTypeDef",
    "CaptionSourceTypeDef",
    "CaptionsTypeDef",
    "ClipTypeDef",
    "CreateJobOutputTypeDef",
    "CreateJobPlaylistTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResponseResponseTypeDef",
    "CreatePipelineRequestTypeDef",
    "CreatePipelineResponseResponseTypeDef",
    "CreatePresetRequestTypeDef",
    "CreatePresetResponseResponseTypeDef",
    "DeletePipelineRequestTypeDef",
    "DeletePresetRequestTypeDef",
    "DetectedPropertiesTypeDef",
    "EncryptionTypeDef",
    "HlsContentProtectionTypeDef",
    "InputCaptionsTypeDef",
    "JobAlbumArtTypeDef",
    "JobInputTypeDef",
    "JobOutputTypeDef",
    "JobTypeDef",
    "JobWatermarkTypeDef",
    "ListJobsByPipelineRequestTypeDef",
    "ListJobsByPipelineResponseResponseTypeDef",
    "ListJobsByStatusRequestTypeDef",
    "ListJobsByStatusResponseResponseTypeDef",
    "ListPipelinesRequestTypeDef",
    "ListPipelinesResponseResponseTypeDef",
    "ListPresetsRequestTypeDef",
    "ListPresetsResponseResponseTypeDef",
    "NotificationsTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PipelineOutputConfigTypeDef",
    "PipelineTypeDef",
    "PlayReadyDrmTypeDef",
    "PlaylistTypeDef",
    "PresetTypeDef",
    "PresetWatermarkTypeDef",
    "ReadJobRequestTypeDef",
    "ReadJobResponseResponseTypeDef",
    "ReadPipelineRequestTypeDef",
    "ReadPipelineResponseResponseTypeDef",
    "ReadPresetRequestTypeDef",
    "ReadPresetResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TestRoleRequestTypeDef",
    "TestRoleResponseResponseTypeDef",
    "ThumbnailsTypeDef",
    "TimeSpanTypeDef",
    "TimingTypeDef",
    "UpdatePipelineNotificationsRequestTypeDef",
    "UpdatePipelineNotificationsResponseResponseTypeDef",
    "UpdatePipelineRequestTypeDef",
    "UpdatePipelineResponseResponseTypeDef",
    "UpdatePipelineStatusRequestTypeDef",
    "UpdatePipelineStatusResponseResponseTypeDef",
    "VideoParametersTypeDef",
    "WaiterConfigTypeDef",
    "WarningTypeDef",
)

ArtworkTypeDef = TypedDict(
    "ArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": "EncryptionTypeDef",
    },
    total=False,
)

AudioCodecOptionsTypeDef = TypedDict(
    "AudioCodecOptionsTypeDef",
    {
        "Profile": str,
        "BitDepth": str,
        "BitOrder": str,
        "Signed": str,
    },
    total=False,
)

AudioParametersTypeDef = TypedDict(
    "AudioParametersTypeDef",
    {
        "Codec": str,
        "SampleRate": str,
        "BitRate": str,
        "Channels": str,
        "AudioPackingMode": str,
        "CodecOptions": "AudioCodecOptionsTypeDef",
    },
    total=False,
)

CancelJobRequestTypeDef = TypedDict(
    "CancelJobRequestTypeDef",
    {
        "Id": str,
    },
)

CaptionFormatTypeDef = TypedDict(
    "CaptionFormatTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": "EncryptionTypeDef",
    },
    total=False,
)

CaptionSourceTypeDef = TypedDict(
    "CaptionSourceTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": "EncryptionTypeDef",
    },
    total=False,
)

CaptionsTypeDef = TypedDict(
    "CaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List["CaptionSourceTypeDef"],
        "CaptionFormats": List["CaptionFormatTypeDef"],
    },
    total=False,
)

ClipTypeDef = TypedDict(
    "ClipTypeDef",
    {
        "TimeSpan": "TimeSpanTypeDef",
    },
    total=False,
)

CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": "EncryptionTypeDef",
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Watermarks": List["JobWatermarkTypeDef"],
        "AlbumArt": "JobAlbumArtTypeDef",
        "Composition": List["ClipTypeDef"],
        "Captions": "CaptionsTypeDef",
        "Encryption": "EncryptionTypeDef",
    },
    total=False,
)

CreateJobPlaylistTypeDef = TypedDict(
    "CreateJobPlaylistTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": "HlsContentProtectionTypeDef",
        "PlayReadyDrm": "PlayReadyDrmTypeDef",
    },
    total=False,
)

_RequiredCreateJobRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestTypeDef",
    {
        "PipelineId": str,
    },
)
_OptionalCreateJobRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestTypeDef",
    {
        "Input": "JobInputTypeDef",
        "Inputs": List["JobInputTypeDef"],
        "Output": "CreateJobOutputTypeDef",
        "Outputs": List["CreateJobOutputTypeDef"],
        "OutputKeyPrefix": str,
        "Playlists": List["CreateJobPlaylistTypeDef"],
        "UserMetadata": Dict[str, str],
    },
    total=False,
)


class CreateJobRequestTypeDef(_RequiredCreateJobRequestTypeDef, _OptionalCreateJobRequestTypeDef):
    pass


CreateJobResponseResponseTypeDef = TypedDict(
    "CreateJobResponseResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestTypeDef",
    {
        "Name": str,
        "InputBucket": str,
        "Role": str,
    },
)
_OptionalCreatePipelineRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestTypeDef",
    {
        "OutputBucket": str,
        "AwsKmsKeyArn": str,
        "Notifications": "NotificationsTypeDef",
        "ContentConfig": "PipelineOutputConfigTypeDef",
        "ThumbnailConfig": "PipelineOutputConfigTypeDef",
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
        "Pipeline": "PipelineTypeDef",
        "Warnings": List["WarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePresetRequestTypeDef = TypedDict(
    "_RequiredCreatePresetRequestTypeDef",
    {
        "Name": str,
        "Container": str,
    },
)
_OptionalCreatePresetRequestTypeDef = TypedDict(
    "_OptionalCreatePresetRequestTypeDef",
    {
        "Description": str,
        "Video": "VideoParametersTypeDef",
        "Audio": "AudioParametersTypeDef",
        "Thumbnails": "ThumbnailsTypeDef",
    },
    total=False,
)


class CreatePresetRequestTypeDef(
    _RequiredCreatePresetRequestTypeDef, _OptionalCreatePresetRequestTypeDef
):
    pass


CreatePresetResponseResponseTypeDef = TypedDict(
    "CreatePresetResponseResponseTypeDef",
    {
        "Preset": "PresetTypeDef",
        "Warning": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePipelineRequestTypeDef = TypedDict(
    "DeletePipelineRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePresetRequestTypeDef = TypedDict(
    "DeletePresetRequestTypeDef",
    {
        "Id": str,
    },
)

DetectedPropertiesTypeDef = TypedDict(
    "DetectedPropertiesTypeDef",
    {
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
    },
    total=False,
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "Mode": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
    },
    total=False,
)

HlsContentProtectionTypeDef = TypedDict(
    "HlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)

InputCaptionsTypeDef = TypedDict(
    "InputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List["CaptionSourceTypeDef"],
    },
    total=False,
)

JobAlbumArtTypeDef = TypedDict(
    "JobAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List["ArtworkTypeDef"],
    },
    total=False,
)

JobInputTypeDef = TypedDict(
    "JobInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": "EncryptionTypeDef",
        "TimeSpan": "TimeSpanTypeDef",
        "InputCaptions": "InputCaptionsTypeDef",
        "DetectedProperties": "DetectedPropertiesTypeDef",
    },
    total=False,
)

JobOutputTypeDef = TypedDict(
    "JobOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": "EncryptionTypeDef",
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List["JobWatermarkTypeDef"],
        "AlbumArt": "JobAlbumArtTypeDef",
        "Composition": List["ClipTypeDef"],
        "Captions": "CaptionsTypeDef",
        "Encryption": "EncryptionTypeDef",
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": "JobInputTypeDef",
        "Inputs": List["JobInputTypeDef"],
        "Output": "JobOutputTypeDef",
        "Outputs": List["JobOutputTypeDef"],
        "OutputKeyPrefix": str,
        "Playlists": List["PlaylistTypeDef"],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": "TimingTypeDef",
    },
    total=False,
)

JobWatermarkTypeDef = TypedDict(
    "JobWatermarkTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": "EncryptionTypeDef",
    },
    total=False,
)

_RequiredListJobsByPipelineRequestTypeDef = TypedDict(
    "_RequiredListJobsByPipelineRequestTypeDef",
    {
        "PipelineId": str,
    },
)
_OptionalListJobsByPipelineRequestTypeDef = TypedDict(
    "_OptionalListJobsByPipelineRequestTypeDef",
    {
        "Ascending": str,
        "PageToken": str,
    },
    total=False,
)


class ListJobsByPipelineRequestTypeDef(
    _RequiredListJobsByPipelineRequestTypeDef, _OptionalListJobsByPipelineRequestTypeDef
):
    pass


ListJobsByPipelineResponseResponseTypeDef = TypedDict(
    "ListJobsByPipelineResponseResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsByStatusRequestTypeDef = TypedDict(
    "_RequiredListJobsByStatusRequestTypeDef",
    {
        "Status": str,
    },
)
_OptionalListJobsByStatusRequestTypeDef = TypedDict(
    "_OptionalListJobsByStatusRequestTypeDef",
    {
        "Ascending": str,
        "PageToken": str,
    },
    total=False,
)


class ListJobsByStatusRequestTypeDef(
    _RequiredListJobsByStatusRequestTypeDef, _OptionalListJobsByStatusRequestTypeDef
):
    pass


ListJobsByStatusResponseResponseTypeDef = TypedDict(
    "ListJobsByStatusResponseResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestTypeDef = TypedDict(
    "ListPipelinesRequestTypeDef",
    {
        "Ascending": str,
        "PageToken": str,
    },
    total=False,
)

ListPipelinesResponseResponseTypeDef = TypedDict(
    "ListPipelinesResponseResponseTypeDef",
    {
        "Pipelines": List["PipelineTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPresetsRequestTypeDef = TypedDict(
    "ListPresetsRequestTypeDef",
    {
        "Ascending": str,
        "PageToken": str,
    },
    total=False,
)

ListPresetsResponseResponseTypeDef = TypedDict(
    "ListPresetsResponseResponseTypeDef",
    {
        "Presets": List["PresetTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationsTypeDef = TypedDict(
    "NotificationsTypeDef",
    {
        "Progressing": str,
        "Completed": str,
        "Warning": str,
        "Error": str,
    },
    total=False,
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeType": str,
        "Grantee": str,
        "Access": List[str],
    },
    total=False,
)

PipelineOutputConfigTypeDef = TypedDict(
    "PipelineOutputConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List["PermissionTypeDef"],
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": "NotificationsTypeDef",
        "ContentConfig": "PipelineOutputConfigTypeDef",
        "ThumbnailConfig": "PipelineOutputConfigTypeDef",
    },
    total=False,
)

PlayReadyDrmTypeDef = TypedDict(
    "PlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)

PlaylistTypeDef = TypedDict(
    "PlaylistTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": "HlsContentProtectionTypeDef",
        "PlayReadyDrm": "PlayReadyDrmTypeDef",
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)

PresetTypeDef = TypedDict(
    "PresetTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Container": str,
        "Audio": "AudioParametersTypeDef",
        "Video": "VideoParametersTypeDef",
        "Thumbnails": "ThumbnailsTypeDef",
        "Type": str,
    },
    total=False,
)

PresetWatermarkTypeDef = TypedDict(
    "PresetWatermarkTypeDef",
    {
        "Id": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "HorizontalAlign": str,
        "HorizontalOffset": str,
        "VerticalAlign": str,
        "VerticalOffset": str,
        "Opacity": str,
        "Target": str,
    },
    total=False,
)

ReadJobRequestTypeDef = TypedDict(
    "ReadJobRequestTypeDef",
    {
        "Id": str,
    },
)

ReadJobResponseResponseTypeDef = TypedDict(
    "ReadJobResponseResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReadPipelineRequestTypeDef = TypedDict(
    "ReadPipelineRequestTypeDef",
    {
        "Id": str,
    },
)

ReadPipelineResponseResponseTypeDef = TypedDict(
    "ReadPipelineResponseResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "Warnings": List["WarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReadPresetRequestTypeDef = TypedDict(
    "ReadPresetRequestTypeDef",
    {
        "Id": str,
    },
)

ReadPresetResponseResponseTypeDef = TypedDict(
    "ReadPresetResponseResponseTypeDef",
    {
        "Preset": "PresetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TestRoleRequestTypeDef = TypedDict(
    "TestRoleRequestTypeDef",
    {
        "Role": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Topics": List[str],
    },
)

TestRoleResponseResponseTypeDef = TypedDict(
    "TestRoleResponseResponseTypeDef",
    {
        "Success": str,
        "Messages": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThumbnailsTypeDef = TypedDict(
    "ThumbnailsTypeDef",
    {
        "Format": str,
        "Interval": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
    },
    total=False,
)

TimeSpanTypeDef = TypedDict(
    "TimeSpanTypeDef",
    {
        "StartTime": str,
        "Duration": str,
    },
    total=False,
)

TimingTypeDef = TypedDict(
    "TimingTypeDef",
    {
        "SubmitTimeMillis": int,
        "StartTimeMillis": int,
        "FinishTimeMillis": int,
    },
    total=False,
)

UpdatePipelineNotificationsRequestTypeDef = TypedDict(
    "UpdatePipelineNotificationsRequestTypeDef",
    {
        "Id": str,
        "Notifications": "NotificationsTypeDef",
    },
)

UpdatePipelineNotificationsResponseResponseTypeDef = TypedDict(
    "UpdatePipelineNotificationsResponseResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePipelineRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdatePipelineRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineRequestTypeDef",
    {
        "Name": str,
        "InputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": "NotificationsTypeDef",
        "ContentConfig": "PipelineOutputConfigTypeDef",
        "ThumbnailConfig": "PipelineOutputConfigTypeDef",
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
        "Pipeline": "PipelineTypeDef",
        "Warnings": List["WarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePipelineStatusRequestTypeDef = TypedDict(
    "UpdatePipelineStatusRequestTypeDef",
    {
        "Id": str,
        "Status": str,
    },
)

UpdatePipelineStatusResponseResponseTypeDef = TypedDict(
    "UpdatePipelineStatusResponseResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoParametersTypeDef = TypedDict(
    "VideoParametersTypeDef",
    {
        "Codec": str,
        "CodecOptions": Dict[str, str],
        "KeyframesMaxDist": str,
        "FixedGOP": str,
        "BitRate": str,
        "FrameRate": str,
        "MaxFrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "DisplayAspectRatio": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "Watermarks": List["PresetWatermarkTypeDef"],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)
