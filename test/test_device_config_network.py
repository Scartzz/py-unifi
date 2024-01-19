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

from unifi_client.models.device_config_network import DeviceConfigNetwork

class TestDeviceConfigNetwork(unittest.TestCase):
    """DeviceConfigNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceConfigNetwork:
        """Test DeviceConfigNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceConfigNetwork`
        """
        model = DeviceConfigNetwork()
        if include_optional:
            return DeviceConfigNetwork(
                bonding_enabled = True,
                dns1 = '',
                dns2 = '',
                dnssuffix = '',
                gateway = '',
                ip = '',
                netmask = '',
                type = ''
            )
        else:
            return DeviceConfigNetwork(
        )
        """

    def testDeviceConfigNetwork(self):
        """Test DeviceConfigNetwork"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
