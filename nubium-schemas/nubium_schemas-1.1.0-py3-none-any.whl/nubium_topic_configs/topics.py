from copy import deepcopy

def hrs_to_ms(hours):
    return 1000 * 60 * 60 * hours

def mb_to_bytes(mb):
    return 1024 * 1024 * mb

config_default = {
    "cleanup.policy": "delete",
    "retention.ms": hrs_to_ms(48),
    "segment.ms": hrs_to_ms(48),
    "segment.bytes": mb_to_bytes(100)
}

config_changelog = {
  **config_default,
  "cleanup.policy": "compact"
}

class TopicConfig:
    def __init__(self, parts, rep_factor=5, config=None):
        self.partitions = parts
        self.replication_factor = rep_factor
        if not config:
          config = deepcopy(config_default)
        self.config = config


primary_topic_configs = {
    "PeopleStream": {
        "Canon": [
            TopicConfig(parts=40),
            {"Input": TopicConfig(parts=40)}
        ],
        "PeopleStreamFromEloqua": {
            "ContactRetriever": {"Timestamps": TopicConfig(parts=1)},
            "ContactToCanon": TopicConfig(parts=20),
            "UnsubscribeRetriever": {"Timestamps": TopicConfig(parts=1)},
            "UnsubscribeToCanon": TopicConfig(parts=5)
        },
        "DataWashingMachine": {
            "ProcessedRecords": TopicConfig(parts=20),
            "Prewash": TopicConfig(parts=20),
            "DeptJobrolePersona": TopicConfig(parts=20),
            "AddressMsa": TopicConfig(parts=20),
            "Privacy": TopicConfig(parts=20)
        }
    },

    "CampaignResponse": {
        "Canon": [
            TopicConfig(parts=10),
            {"Input": TopicConfig(parts=10)}
        ],
        "CampaignResponseFromEloqua": {
            "InquiriesRetriever": {"Timestamps": TopicConfig(parts=1)},
            "InquiriesToCanon": TopicConfig(parts=10),
        },
        "CampaignResponseToSalesforce": {
            "CampaignMembersToUpsert": {
                "FirstTry": TopicConfig(parts=10),
                "Retry1": TopicConfig(parts=3),
                "Retry2": TopicConfig(parts=1),
                "Retry3": TopicConfig(parts=1),
                "Failure": TopicConfig(parts=1)
            }
        }
    },

    "NubiumIntegrations": {
        "DynamicForm": {
            "FormSubmissions": TopicConfig(parts=10),
            "SpamFilter": {
                "CheckEmailAddress": TopicConfig(parts=10),
                "CheckVerifyId": TopicConfig(parts=10),
                "CheckSubmitId": TopicConfig(parts=10)
            },
            "SpamPosts": TopicConfig(parts=5),
            "ErrorPosts": TopicConfig(parts=1)
        },
        "Eloqua": {
            "EbbController": TopicConfig(parts=5),
            "EbbWorkerTasks": TopicConfig(parts=20),
            "FormPoster": {
                "FromDyfo": {
                    "FirstTry": TopicConfig(parts=10)},
                "FirstTry": TopicConfig(parts=10),
                "Retry1": TopicConfig(parts=1),
                "Retry2": TopicConfig(parts=1),
                "Retry3": TopicConfig(parts=1),
                "Failure": TopicConfig(parts=1)
            },
            "CdoUpdates": {
                "FirstTry": TopicConfig(parts=10),
                "Retry1": TopicConfig(parts=1),
                "Retry2": TopicConfig(parts=1),
                "Retry3": TopicConfig(parts=1),
                "Failure": TopicConfig(parts=1)
            },
            "ContactUpdates": {
                "FirstTry": TopicConfig(parts=50),
                "Retry1": TopicConfig(parts=1),
                "Retry2": TopicConfig(parts=1),
                "Retry3": TopicConfig(parts=1),
                "Failure": TopicConfig(parts=1)
            }
        },
        "Partner": {
            "BulkReceiver": {"Chunks": TopicConfig(parts=1)},
            "BulkProcessor": {"Records": TopicConfig(parts=5)}
        },
        "Vivastream": {
            "ContactsVivastreamRetriever": {"Timestamps": TopicConfig(parts=1)},
            "CdoToFormTransform": TopicConfig(parts=5)
        },
        "UploadWizard": {
            "ContactsUploadsMembersRetriever": {"Timestamps": TopicConfig(parts=1)},
            "CdoToFormTransform": TopicConfig(parts=5)
        }
    },

    "PathFactory": {
        "PathFactory": {
            "DuplicatesFilter": TopicConfig(parts=5),
            "DuplicateClosedSessions": TopicConfig(parts=1),
            "ClosedSessions": {
                "FirstTry": TopicConfig(parts=5),
                "Retry1": TopicConfig(parts=1),
                "Retry2": TopicConfig(parts=1),
                "Failure": TopicConfig(parts=1)
            }
        }
    }
}

internal_topic_configs = {}


def unpack_topic_dict(topic_dict, prev_layer=''):
    if isinstance(topic_dict, dict):
        return {
            name: config
            for key, value in topic_dict.items()
            for name, config in unpack_topic_dict(value, f'{prev_layer}_{key}' if prev_layer else key).items()
        }
    elif isinstance(topic_dict, list):
        return {
            name: config
            for item in topic_dict
            for name, config in unpack_topic_dict(item, prev_layer).items()
        }
    elif isinstance(topic_dict, TopicConfig):
       return {prev_layer: topic_dict}
    raise ValueError(f"unsupported type for topic_dict: {type(topic_dict)}")


primary_topics = unpack_topic_dict(primary_topic_configs)
internal_topics = unpack_topic_dict(internal_topic_configs)
