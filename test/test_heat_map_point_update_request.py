# coding: utf-8

"""
    Unifi API

    Unifi Controller API

    The version of the OpenAPI document: 8.0.26
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.heat_map_point_update_request import HeatMapPointUpdateRequest

class TestHeatMapPointUpdateRequest(unittest.TestCase):
    """HeatMapPointUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HeatMapPointUpdateRequest:
        """Test HeatMapPointUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HeatMapPointUpdateRequest`
        """
        model = HeatMapPointUpdateRequest()
        if include_optional:
            return HeatMapPointUpdateRequest(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                download_speed = 1.337,
                heatmap_id = '',
                site_id = '',
                upload_speed = 1.337,
                x = 1.337,
                y = 1.337
            )
        else:
            return HeatMapPointUpdateRequest(
        )
        """

    def testHeatMapPointUpdateRequest(self):
        """Test HeatMapPointUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()