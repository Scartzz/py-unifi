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

from openapi_client.models.hotspot2_conf_description import Hotspot2ConfDescription

class TestHotspot2ConfDescription(unittest.TestCase):
    """Hotspot2ConfDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Hotspot2ConfDescription:
        """Test Hotspot2ConfDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Hotspot2ConfDescription`
        """
        model = Hotspot2ConfDescription()
        if include_optional:
            return Hotspot2ConfDescription(
                language = '',
                text = ''
            )
        else:
            return Hotspot2ConfDescription(
        )
        """

    def testHotspot2ConfDescription(self):
        """Test Hotspot2ConfDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
