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

from openapi_client.models.hotspot2_conf_roaming_consortium_list import Hotspot2ConfRoamingConsortiumList

class TestHotspot2ConfRoamingConsortiumList(unittest.TestCase):
    """Hotspot2ConfRoamingConsortiumList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Hotspot2ConfRoamingConsortiumList:
        """Test Hotspot2ConfRoamingConsortiumList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Hotspot2ConfRoamingConsortiumList`
        """
        model = Hotspot2ConfRoamingConsortiumList()
        if include_optional:
            return Hotspot2ConfRoamingConsortiumList(
                name = '',
                oid = ''
            )
        else:
            return Hotspot2ConfRoamingConsortiumList(
        )
        """

    def testHotspot2ConfRoamingConsortiumList(self):
        """Test Hotspot2ConfRoamingConsortiumList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
