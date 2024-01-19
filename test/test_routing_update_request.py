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

from openapi_client.models.routing_update_request import RoutingUpdateRequest

class TestRoutingUpdateRequest(unittest.TestCase):
    """RoutingUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoutingUpdateRequest:
        """Test RoutingUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingUpdateRequest`
        """
        model = RoutingUpdateRequest()
        if include_optional:
            return RoutingUpdateRequest(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                enabled = True,
                gateway_device = '',
                gateway_type = '',
                name = '',
                site_id = '',
                static_route_distance = 56,
                static_route_interface = '',
                static_route_network = '',
                static_route_nexthop = '',
                static_route_type = '',
                type = ''
            )
        else:
            return RoutingUpdateRequest(
        )
        """

    def testRoutingUpdateRequest(self):
        """Test RoutingUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
