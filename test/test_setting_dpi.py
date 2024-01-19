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

from unifi_client.models.setting_dpi import SettingDpi

class TestSettingDpi(unittest.TestCase):
    """SettingDpi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingDpi:
        """Test SettingDpi
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingDpi`
        """
        model = SettingDpi()
        if include_optional:
            return SettingDpi(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                enabled = True,
                fingerprinting_enabled = True,
                key = '',
                site_id = ''
            )
        else:
            return SettingDpi(
        )
        """

    def testSettingDpi(self):
        """Test SettingDpi"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
