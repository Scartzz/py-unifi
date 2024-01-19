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

from unifi_client.models.setting_super_identity_response import SettingSuperIdentityResponse

class TestSettingSuperIdentityResponse(unittest.TestCase):
    """SettingSuperIdentityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingSuperIdentityResponse:
        """Test SettingSuperIdentityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingSuperIdentityResponse`
        """
        model = SettingSuperIdentityResponse()
        if include_optional:
            return SettingSuperIdentityResponse(
                data = [
                    unifi_client.models.setting_super_identity.SettingSuperIdentity(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        hostname = '', 
                        key = '', 
                        name = '', 
                        site_id = '', )
                    ],
                meta = unifi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return SettingSuperIdentityResponse(
        )
        """

    def testSettingSuperIdentityResponse(self):
        """Test SettingSuperIdentityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
