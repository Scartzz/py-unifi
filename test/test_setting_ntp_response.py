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

from openapi_client.models.setting_ntp_response import SettingNtpResponse

class TestSettingNtpResponse(unittest.TestCase):
    """SettingNtpResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingNtpResponse:
        """Test SettingNtpResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingNtpResponse`
        """
        model = SettingNtpResponse()
        if include_optional:
            return SettingNtpResponse(
                data = [
                    openapi_client.models.setting_ntp.SettingNtp(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        key = '', 
                        ntp_server_1 = '', 
                        ntp_server_2 = '', 
                        ntp_server_3 = '', 
                        ntp_server_4 = '', 
                        setting_preference = '', 
                        site_id = '', )
                    ],
                meta = openapi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return SettingNtpResponse(
        )
        """

    def testSettingNtpResponse(self):
        """Test SettingNtpResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()