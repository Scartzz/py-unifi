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

from openapi_client.models.setting_mgmt import SettingMgmt

class TestSettingMgmt(unittest.TestCase):
    """SettingMgmt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingMgmt:
        """Test SettingMgmt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingMgmt`
        """
        model = SettingMgmt()
        if include_optional:
            return SettingMgmt(
                id = '',
                advanced_feature_enabled = True,
                alert_enabled = True,
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                auto_upgrade = True,
                auto_upgrade_hour = 56,
                boot_sound = True,
                debug_tools_enabled = True,
                direct_connect_enabled = True,
                key = '',
                led_enabled = True,
                outdoor_mode_enabled = True,
                site_id = '',
                unifi_idp_enabled = True,
                wifiman_enabled = True,
                x_mgmt_key = '',
                x_ssh_auth_password_enabled = True,
                x_ssh_bind_wildcard = True,
                x_ssh_enabled = True,
                x_ssh_keys = [
                    openapi_client.models.setting_mgmt_x_ssh_keys.SettingMgmtXSshKeys(
                        comment = '', 
                        date = '', 
                        fingerprint = '', 
                        key = '', 
                        name = '', 
                        type = '', )
                    ],
                x_ssh_md5passwd = '',
                x_ssh_password = '',
                x_ssh_sha512passwd = '',
                x_ssh_username = ''
            )
        else:
            return SettingMgmt(
        )
        """

    def testSettingMgmt(self):
        """Test SettingMgmt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
