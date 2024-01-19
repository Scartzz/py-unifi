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

from openapi_client.models.device_rps_port_table import DeviceRpsPortTable

class TestDeviceRpsPortTable(unittest.TestCase):
    """DeviceRpsPortTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceRpsPortTable:
        """Test DeviceRpsPortTable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceRpsPortTable`
        """
        model = DeviceRpsPortTable()
        if include_optional:
            return DeviceRpsPortTable(
                name = '',
                port_idx = 56,
                port_mode = ''
            )
        else:
            return DeviceRpsPortTable(
        )
        """

    def testDeviceRpsPortTable(self):
        """Test DeviceRpsPortTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
