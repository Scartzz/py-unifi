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

from openapi_client.models.hotspot2_conf_icon import Hotspot2ConfIcon

class TestHotspot2ConfIcon(unittest.TestCase):
    """Hotspot2ConfIcon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Hotspot2ConfIcon:
        """Test Hotspot2ConfIcon
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Hotspot2ConfIcon`
        """
        model = Hotspot2ConfIcon()
        if include_optional:
            return Hotspot2ConfIcon(
                name = ''
            )
        else:
            return Hotspot2ConfIcon(
        )
        """

    def testHotspot2ConfIcon(self):
        """Test Hotspot2ConfIcon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
