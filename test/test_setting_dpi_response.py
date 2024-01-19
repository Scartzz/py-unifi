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

from openapi_client.models.setting_dpi_response import SettingDpiResponse

class TestSettingDpiResponse(unittest.TestCase):
    """SettingDpiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingDpiResponse:
        """Test SettingDpiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingDpiResponse`
        """
        model = SettingDpiResponse()
        if include_optional:
            return SettingDpiResponse(
                data = [
                    openapi_client.models.setting_dpi.SettingDpi(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        enabled = True, 
                        fingerprinting_enabled = True, 
                        key = '', 
                        site_id = '', )
                    ],
                meta = openapi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return SettingDpiResponse(
        )
        """

    def testSettingDpiResponse(self):
        """Test SettingDpiResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
