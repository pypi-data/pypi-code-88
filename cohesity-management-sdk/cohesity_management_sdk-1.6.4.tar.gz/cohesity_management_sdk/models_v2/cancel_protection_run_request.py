# -*- coding: utf-8 -*-


class CancelProtectionRunRequest(object):

    """Implementation of the 'Cancel protection run request.' model.

    Specifies the request to cancel a protection run.

    Attributes:
        local_task_id (string): Specifies the task id of the local run.
        replication_task_id (list of string): Specifies the task id of the
            replication run.
        archival_task_id (list of string): Specifies the task id of the
            archival run.
        cloud_spin_task_id (list of string): Specifies the task id of the
            cloudSpin run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "local_task_id":'localTaskId',
        "replication_task_id":'replicationTaskId',
        "archival_task_id":'archivalTaskId',
        "cloud_spin_task_id":'cloudSpinTaskId'
    }

    def __init__(self,
                 local_task_id=None,
                 replication_task_id=None,
                 archival_task_id=None,
                 cloud_spin_task_id=None):
        """Constructor for the CancelProtectionRunRequest class"""

        # Initialize members of the class
        self.local_task_id = local_task_id
        self.replication_task_id = replication_task_id
        self.archival_task_id = archival_task_id
        self.cloud_spin_task_id = cloud_spin_task_id


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        local_task_id = dictionary.get('localTaskId')
        replication_task_id = dictionary.get('replicationTaskId')
        archival_task_id = dictionary.get('archivalTaskId')
        cloud_spin_task_id = dictionary.get('cloudSpinTaskId')

        # Return an object of this model
        return cls(local_task_id,
                   replication_task_id,
                   archival_task_id,
                   cloud_spin_task_id)


