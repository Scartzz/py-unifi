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

from openapi_client.models.port_forward_update_request import PortForwardUpdateRequest

class TestPortForwardUpdateRequest(unittest.TestCase):
    """PortForwardUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortForwardUpdateRequest:
        """Test PortForwardUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortForwardUpdateRequest`
        """
        model = PortForwardUpdateRequest()
        if include_optional:
            return PortForwardUpdateRequest(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                destination_ip = '',
                dst_port = '',
                enabled = True,
                fwd = '',
                fwd_port = '',
                log = True,
                name = '',
                pfwd_interface = '',
                proto = '',
                site_id = '',
                src = ''
            )
        else:
            return PortForwardUpdateRequest(
        )
        """

    def testPortForwardUpdateRequest(self):
        """Test PortForwardUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
