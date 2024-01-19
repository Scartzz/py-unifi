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

from openapi_client.models.setting_ips_suppression import SettingIpsSuppression

class TestSettingIpsSuppression(unittest.TestCase):
    """SettingIpsSuppression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingIpsSuppression:
        """Test SettingIpsSuppression
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingIpsSuppression`
        """
        model = SettingIpsSuppression()
        if include_optional:
            return SettingIpsSuppression(
                alerts = [
                    openapi_client.models.setting_ips_alerts.SettingIpsAlerts(
                        category = '', 
                        gid = 56, 
                        id = 56, 
                        signature = '', 
                        tracking = [
                            openapi_client.models.setting_ips_tracking.SettingIpsTracking(
                                direction = '', 
                                mode = '', 
                                value = '', )
                            ], 
                        type = '', )
                    ],
                whitelist = [
                    openapi_client.models.setting_ips_whitelist.SettingIpsWhitelist(
                        direction = '', 
                        mode = '', 
                        value = '', )
                    ]
            )
        else:
            return SettingIpsSuppression(
        )
        """

    def testSettingIpsSuppression(self):
        """Test SettingIpsSuppression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
