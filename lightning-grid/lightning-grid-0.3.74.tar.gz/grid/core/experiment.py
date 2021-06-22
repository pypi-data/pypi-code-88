from typing import Dict, Iterable, List, Optional

from grid.core.artifact import Artifact
from grid.core.base import GridObject
from grid.exceptions import ResourceNotFound


class Experiment(GridObject):
    """
    Grid experiment object. This object contains all the properties that a
    given artifact should have. This also encapsulates special methods
    for interactive with experiment properties.

    Parameters
    ----------
    name: str
        Experiment name
    """
    terminal_statuses = ('failed', 'succeeded', 'cancelled')
    queued_statuses = ('queued', 'pending')

    def __init__(self, name: Optional[str] = None, identifier: Optional[str] = None):
        self._data: Optional[Dict[str, str]] = {}
        if identifier:
            self.identifier = identifier
        elif not name:
            raise RuntimeError("Either name or identifier is required")
        self.name = name
        super().__init__()

        # get experiment ID upon instantiation if class doesn't have one
        if not hasattr(self, "identifier"):
            self.identifier = self._experiment_id_from_name(self.name)

        # log handling attributes
        self._archive_log_current_page: int
        self._archive_log_total_pages: int

    def _experiment_id_from_name(self, name: str) -> str:
        """Retrieves experiment ID from an experiment name."""

        # User can pass experiments as username:experiment_name to fetch other users experiments
        username = None
        split = name.split(":")
        if len(split) > 2:
            raise ValueError(f"Error while parsing {name}. Use the format <username>:<experiment-name>")
        elif len(split) == 2:
            username = split[0]
            name = split[1]

        query = """
        query ($experimentName: String!, $username: String) {
            getExperimentId(experimentName: $experimentName, username: $username) {
                success
                message
                experimentId
            }
        }
        """
        params = {"experimentName": name, "username": username}
        result = self.client.query(query, **params)

        if not result["getExperimentId"]["success"]:
            if "Cannot find experiment" in result["getExperimentId"]["message"]:
                raise ResourceNotFound(
                    f"Experiment {name} does not exist\nIf you wish to fetch an experiment for somebody in your team, use <username>:<experiment-name> format"
                )
            raise ValueError(f"{result['getExperimentId']['message']}")

        return result["getExperimentId"]["experimentId"]

    def refresh(self) -> None:
        """
        Updates object metadata. This makes a query to Grid to fetch the
        object"s latest data.
        """
        query = """
        query GetExperimentDetails ($experimentId: ID!) {
            getExperimentDetails(experimentId: $experimentId) {
                name
                githubId
                desiredState
                commitSha
                entrypoint
                invocationCommands
                createdAt
                startedRunningAt
                finishedAt
                run {
                    runId
                    name
                }
                parameters {
                    name
                    value
                }
            }
        }
        """
        result = self.client.query(query, experimentId=self.identifier)
        self._data = result["getExperimentDetails"]
        self._update_meta()

    def _archive_logs(self, page: int = 0) -> List[Dict[str, str]]:
        query = """
        query GetLogs ($experimentId: ID!, $page: Int) {
            getArchiveExperimentLogs(experimentId: $experimentId, page: $page) {
                lines {
                    message
                    timestamp
                }
                currentPage
                totalPages
            }
        }
        """
        params = {'experimentId': self.identifier, 'page': page}
        result = self.client.query(query, **params)

        # set metadata
        self._archive_log_current_page = result["getArchiveExperimentLogs"]["currentPage"]
        self._archive_log_total_pages = result["getArchiveExperimentLogs"]["totalPages"]

        # return just log lines
        return result["getArchiveExperimentLogs"]["lines"]

    def _live_logs(self) -> Dict[str, str]:
        """Streams real-time experiment logs."""
        subscription = """
        subscription GetLogs ($experimentId: ID!) {
            getLiveExperimentLogs(
                experimentId: $experimentId) {
                    message
                    timestamp
            }
        }
        """
        params = {'experimentId': self.identifier}
        stream = self.client.subscribe(query=subscription, **params)
        for element in stream:
            yield element["getLiveExperimentLogs"]

    def logs(self) -> Iterable[Dict[str, str]]:
        """
        Iterate over experiment logs

        Returns
        -------
        iteration over individual log lines

        """
        if self.is_terminal:
            for element in self._archive_logs():
                yield element
        else:
            # instantiate a websocket transport
            self.client._init_client(websocket=True)
            for element in self._live_logs():
                for entry in element:
                    yield entry

    @property
    def is_terminal(self):
        """Determines if an experiment is in terminal status."""
        return self.status in self.terminal_statuses

    @property
    def is_queued(self):
        """Determines if an experiment is in queued status."""
        return self.status in self.queued_statuses

    @property
    def status(self) -> str:
        query = """
        query GetExperimentDetails ($experimentId: ID!) {
            getExperimentDetails(experimentId: $experimentId) {
                status
            }
        }
        """
        result = self.client.query(query, experimentId=self.identifier)
        return result["getExperimentDetails"]["status"]

    @property
    def artifacts(self) -> List[Artifact]:
        """Fetches artifacts from a given experiments. Artifacts are"""
        query = """
        query (
            $experimentId: ID!
        ) {
            getArtifacts(experimentId: $experimentId) {
                signedUrl
                downloadToPath
                downloadToFilename
            }
        }
        """
        result = self.client.query(query, experimentId=self.identifier)
        return [Artifact(*a.values()) for a in result.get("getArtifacts")]
