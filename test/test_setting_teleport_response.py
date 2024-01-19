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

from unifi_client.models.setting_teleport_response import SettingTeleportResponse

class TestSettingTeleportResponse(unittest.TestCase):
    """SettingTeleportResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingTeleportResponse:
        """Test SettingTeleportResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingTeleportResponse`
        """
        model = SettingTeleportResponse()
        if include_optional:
            return SettingTeleportResponse(
                data = [
                    unifi_client.models.setting_teleport.SettingTeleport(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        enabled = True, 
                        key = '', 
                        site_id = '', 
                        subnet_cidr = '', )
                    ],
                meta = unifi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return SettingTeleportResponse(
        )
        """

    def testSettingTeleportResponse(self):
        """Test SettingTeleportResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
