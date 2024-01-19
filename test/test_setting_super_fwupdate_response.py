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

from unifi_client.models.setting_super_fwupdate_response import SettingSuperFwupdateResponse

class TestSettingSuperFwupdateResponse(unittest.TestCase):
    """SettingSuperFwupdateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingSuperFwupdateResponse:
        """Test SettingSuperFwupdateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingSuperFwupdateResponse`
        """
        model = SettingSuperFwupdateResponse()
        if include_optional:
            return SettingSuperFwupdateResponse(
                data = [
                    unifi_client.models.setting_super_fwupdate.SettingSuperFwupdate(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        controller_channel = '', 
                        firmware_channel = '', 
                        key = '', 
                        site_id = '', 
                        sso_enabled = True, )
                    ],
                meta = unifi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return SettingSuperFwupdateResponse(
        )
        """

    def testSettingSuperFwupdateResponse(self):
        """Test SettingSuperFwupdateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
