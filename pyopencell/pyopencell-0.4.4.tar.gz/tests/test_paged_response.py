import unittest
from pyopencell.responses.paged_response import PagedResponse
from pyopencell.resources.base_resource_list import BaseResourceList
from pyopencell.resources.base_resource import BaseResource


class Banana(BaseResource):
    _name = "banana"


class BananaList(BaseResourceList):
    items_resource_class = Banana
    _name = "bananas"


class NestedBananaList(BaseResourceList):
    items_resource_class = Banana
    _name = "bananas"

    @classmethod
    def get_instances_from_response(self, **response):
        return response['banana_tree']['bananas']


class PagedResponseTest(unittest.TestCase):
    def test_with_name_attribute(self):
        response = {
            "paging": {},
            "actionStatus": {},
            "bananas": [
                {"name": "one banana"},
                {"name": "two bananas"},
                {"name": "three bananas"}
            ]
        }

        paged_response = PagedResponse(BananaList, **response)

        self.assertEquals(
            [banana.name for banana in paged_response.bananas],
            [banana["name"] for banana in response["bananas"]]
        )

    def test_with_instances_from_response_method(self):
        response = {
            "paging": {},
            "actionStatus": {},
            "banana_tree": {
                "bananas": [
                    {"name": "one banana"},
                    {"name": "two bananas"},
                    {"name": "three bananas"}
                ]
            }
        }

        paged_response = PagedResponse(NestedBananaList, **response)

        self.assertEquals(
            [banana.name for banana in paged_response.bananas],
            [banana["name"] for banana in response["banana_tree"]["bananas"]]
        )
