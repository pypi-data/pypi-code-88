from pyapacheatlas.core import PurviewClient, AtlasException
import requests
import time
class ExtendedPurviewClient(PurviewClient):
    """
    Provides communication between your application and the Azure Purview
    service. Simplifies the requirements for knowing the endpoint url and
    requires only the Purview account name.

    :param str account_name:
        Your Purview account name.
    :param authentication:
        The method of authentication.
    :type authentication:
        :class:`~pyapacheatlas.auth.base.AtlasAuthBase`
    """

    def __init__(self, account_name, authentication=None):
        super().__init__(account_name, authentication)
    
    def delete_glossary_term(self, termguid):
        """
        Delete one or many termguid from your Apache Atlas server.

        :param termguid: The termguid you want to remove.
        :type guid: Union(str,list(str))
        :return:
            204 No Content OK. If glossary term delete was successful.
            404 Not Found
            If glossary term guid in invalid.
        :rtype: int
        """
        atlas_endpoint = self.endpoint_url + \
            "/glossary/term/{termguid}".format(termguid=termguid)
        delete_response = requests.delete(
            atlas_endpoint,
            headers=self.authentication.get_authentication_headers())

        try:
            delete_response.raise_for_status()
            return delete_response.status_code
        except requests.RequestException:
            if "errorCode" in delete_response:
                raise AtlasException(delete_response.text)
            else:
                raise requests.RequestException(delete_response.text)

    def delete_all_terms(self, termguids):
        """
        Delete one or many termguid from your Apache Atlas server.

        :param termguids: List of termguid you want to remove.
        :type termguids: Union(str,list(str))
        :return:
            204 No Content OK. If glossary term delete was successful.
            404 Not Found
            If glossary term guid in invalid.
        :rtype: int
        """
        for termguid in termguids:
            self.delete_glossary_term(termguid)
            time.sleep(3)

    def get_all_term_templates(self):
        atlas_endpoint = self.endpoint_url + "/types/typedefs"
        # TODO: Implement paging with offset and limit
        getResult = requests.get(
            atlas_endpoint,
            params={"type": "term_template"},
            headers=self.authentication.get_authentication_headers()
        )
        return self._handle_response(getResult)

    def import_term_templates(self, term_templates):
        atlas_endpoint = self.endpoint_url + "/types/typedefs"
        # TODO: Implement paging with offset and limit
        import json
        getResult = requests.post(
            atlas_endpoint,
            data=json.dumps(term_templates),
            headers=self.authentication.get_authentication_headers()
        )
        return self._handle_response(getResult)
    
    def delete_term_templates(self, term_templates):
        atlas_endpoint = self.endpoint_url + "/types/typedefs"
        # TODO: Implement paging with offset and limit
        import json
        delete_response = requests.delete(
            atlas_endpoint,
            data=json.dumps(term_templates),
            headers=self.authentication.get_authentication_headers()
        )
        try:
            delete_response.raise_for_status()
            return delete_response.status_code
        except requests.RequestException:
            if "errorCode" in delete_response:
                raise AtlasException(delete_response.text)
            else:
                raise requests.RequestException(delete_response.text)
    
    def create_glossary(self, name):
        atlas_endpoint = self.endpoint_url + "/glossary"
        import json
        res = requests.post(
            atlas_endpoint,
            data=json.dumps(
                {"qualifiedName": name, "name": name,
                "terms": []}),
            headers=self.authentication.get_authentication_headers()
        )
        return self._handle_response(res)