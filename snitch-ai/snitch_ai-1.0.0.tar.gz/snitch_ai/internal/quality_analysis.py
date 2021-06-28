from snitch_ai.internal.guid import GUID
from snitch_ai.internal.api_client import ApiClient
from snitch_ai.internal.analysis_status import AnalysisState, AnalysisStatus

class QualityAnalysis:

    def __init__(self, project_id: GUID, version_id: GUID):
        self.project_id = project_id
        self.version_id = version_id


    def get_status(self) -> AnalysisStatus:
        """
        Gets the status of this Quality analysis.
        :return: The status of the analysis.
        """
        client = ApiClient()
        resp = client.get(f"project/{self.project_id}/version/{self.version_id}/quality/status")
        if resp.status_code != 200:
            raise Exception(f"Error while waiting on analysis: {resp} {resp.text}")

        json = resp.json()

        return AnalysisStatus(AnalysisState(json["state"]), json["error"])


    def get_json(self):
        """
        Gets the JSON results for this Quality analysis.
        :return: The JSON results.
        """
        client = ApiClient()
        resp = client.get(f"project/{self.project_id}/version/{self.version_id}/quality/json")
        if resp.status_code != 200:
            raise Exception(f"Error while getting quality analysis JSON: {resp.text}")

        return resp.json()


    def save_pdf(self, path):
        """
        Saves the PDF report of this Quality analysis to the specified path.
        :param path: The path to save the PDF report to.
        """
        client = ApiClient()
        resp = client.get(f"project/{self.project_id}/version/{self.version_id}/quality/pdf")
        if resp.status_code != 200:
            raise Exception(f"Error while getting quality analysis PDF: {resp.text}")

        with open(path, "wb") as f:
            f.write(resp.content)


    def __str__(self):
        return f"Quality Analysis {self.version_id}"
