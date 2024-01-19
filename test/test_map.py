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

from unifi_client.models.map import Map

class TestMap(unittest.TestCase):
    """Map unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Map:
        """Test Map
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Map`
        """
        model = Map()
        if include_optional:
            return Map(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                lat = '',
                lng = '',
                map_type_id = '',
                name = '',
                offset_left = 1.337,
                offset_top = 1.337,
                opacity = 1.337,
                selected = True,
                site_id = '',
                tilt = 56,
                type = '',
                unit = '',
                upp = 1.337,
                zoom = 56
            )
        else:
            return Map(
        )
        """

    def testMap(self):
        """Test Map"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
