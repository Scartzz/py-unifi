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

from unifi_client.models.network_nat_outbound_ip_addresses import NetworkNATOutboundIPAddresses

class TestNetworkNATOutboundIPAddresses(unittest.TestCase):
    """NetworkNATOutboundIPAddresses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkNATOutboundIPAddresses:
        """Test NetworkNATOutboundIPAddresses
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkNATOutboundIPAddresses`
        """
        model = NetworkNATOutboundIPAddresses()
        if include_optional:
            return NetworkNATOutboundIPAddresses(
                ip_address = '',
                wan_network_group = ''
            )
        else:
            return NetworkNATOutboundIPAddresses(
        )
        """

    def testNetworkNATOutboundIPAddresses(self):
        """Test NetworkNATOutboundIPAddresses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
