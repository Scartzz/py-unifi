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

from openapi_client.models.dynamic_dns_update_request import DynamicDNSUpdateRequest

class TestDynamicDNSUpdateRequest(unittest.TestCase):
    """DynamicDNSUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DynamicDNSUpdateRequest:
        """Test DynamicDNSUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DynamicDNSUpdateRequest`
        """
        model = DynamicDNSUpdateRequest()
        if include_optional:
            return DynamicDNSUpdateRequest(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                custom_service = '',
                host_name = '',
                interface = '',
                login = '',
                options = [
                    ''
                    ],
                server = '',
                service = '',
                site_id = '',
                x_password = ''
            )
        else:
            return DynamicDNSUpdateRequest(
        )
        """

    def testDynamicDNSUpdateRequest(self):
        """Test DynamicDNSUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
