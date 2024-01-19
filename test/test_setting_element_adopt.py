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

from unifi_client.models.setting_element_adopt import SettingElementAdopt

class TestSettingElementAdopt(unittest.TestCase):
    """SettingElementAdopt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingElementAdopt:
        """Test SettingElementAdopt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingElementAdopt`
        """
        model = SettingElementAdopt()
        if include_optional:
            return SettingElementAdopt(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                enabled = True,
                key = '',
                site_id = '',
                x_element_essid = '',
                x_element_psk = ''
            )
        else:
            return SettingElementAdopt(
        )
        """

    def testSettingElementAdopt(self):
        """Test SettingElementAdopt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
