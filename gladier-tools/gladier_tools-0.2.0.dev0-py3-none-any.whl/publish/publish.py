from gladier import GladierBaseTool, generate_flow_definition


def publish_gather_metadata(data):
    """This function uses the globus-pilot tool to generate metadata compatible with
    portals on petreldata.net. Requires globus_pilot>=0.6.0.
    Requires input:
    * ``dataset`` -- Path to file or directory
    * ``destination`` -- relative location under project directory to place dataset (Default `/`)
    * ``source_globus_endpoint`` -- The endpoint of the machine where you are executing
    * ``index`` -- The index to ingest this dataset
    * ``project`` -- The pilot project to use for this dataset
    * ``groups`` -- A list of additional groups to make these records visible_to

    Requires: the 'globus-pilot' package to be installed.
    """
    from pilot.client import PilotClient

    dataset, destination = data['dataset'], data.get('destination', '/')
    index, project, groups = data['index'], data['project'], data.get('groups', [])

    # Bootstrap Pilot
    pc = PilotClient(config_file=None, index_uuid=index)
    pc.project.set_project(project)
    # short_path is how pilot internally refers to datasets, implicitly accounting for
    # the endpoint and base project path. After publication, you may refer to your
    # dataset via the short path -- ``pilot describe short_path``
    short_path = pc.build_short_path(dataset, destination)
    return {
        'search': {
            'id': data.get('id', 'metadata'),
            'content': pc.gather_metadata(dataset, destination,
                                          custom_metadata=data.get('metadata')),
            'subject': pc.get_subject_url(short_path),
            'visible_to': [f'urn:globus:groups:id:{g}' for g in groups + [pc.get_group()]],
            'search_index': index
        },
        'transfer': {
            'source_endpoint_id': data['source_globus_endpoint'],
            'destination_endpoint_id': pc.get_endpoint(),
            'transfer_items': [{
                'source_path': src,
                'destination_path': dest,
                # 'recursive': False,  # each file is explicit in pilot, no directories
            } for src, dest in pc.get_globus_transfer_paths(dataset, destination)]
        }
    }


class Publish(GladierBaseTool):

    flow_definition = {
        'Comment': 'Publish metadata to Globus Search, with data from the result.',
        'StartAt': 'PublishGatherMetadata',
        'States': {
            'PublishGatherMetadata': {
                'Comment': 'Say something to start the conversation',
                'Type': 'Action',
                'ActionUrl': 'https://api.funcx.org/automate',
                'ActionScope': 'https://auth.globus.org/scopes/facd7ccc-c5f4-42aa-916b-a0e270e2c2a9/automate2',
                'ExceptionOnActionFailure': False,
                'Parameters': {
                    'tasks': [{
                        'endpoint.$': '$.input.funcx_endpoint_non_compute',
                        'func.$': '$.input.publish_gather_metadata_funcx_id',
                        'payload.$': '$.input.pilot',
                    }]
                },
                'ResultPath': '$.PublishGatherMetadata',
                'WaitTime': 60,
                'Next': 'PublishTransfer',
            },
            'PublishTransfer': {
                'Comment': 'Transfer files for publication',
                'Type': 'Action',
                'ActionUrl': 'https://actions.automate.globus.org/transfer/transfer',
                'InputPath': '$.PublishGatherMetadata.details.result.transfer',
                'ResultPath': '$.PublishTransfer',
                'WaitTime': 600,
                'Next': 'PublishIngest',
            },
            'PublishIngest': {
                'Comment': 'Ingest the search document',
                'Type': 'Action',
                'ActionUrl': 'https://actions.globus.org/search/ingest',
                'ExceptionOnActionFailure': False,
                'InputPath': '$.PublishGatherMetadata.details.result.search',
                'ResultPath': '$.PublishIngest',
                'WaitTime': 300,
                'End': True
            },
        }
    }

    required_input = [
        'pilot',
        'funcx_endpoint_non_compute',
    ]

    flow_input = {

    }

    funcx_functions = [
        publish_gather_metadata,
    ]
