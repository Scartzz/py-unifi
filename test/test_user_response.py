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

from unifi_client.models.user_response import UserResponse

class TestUserResponse(unittest.TestCase):
    """UserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserResponse:
        """Test UserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserResponse`
        """
        model = UserResponse()
        if include_optional:
            return UserResponse(
                data = [
                    unifi_client.models.user.User(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        blocked = True, 
                        dev_id_override = 56, 
                        fixed_ap_enabled = True, 
                        fixed_ap_mac = '', 
                        fixed_ip = '', 
                        hostname = '', 
                        ip = '', 
                        last_seen = 56, 
                        local_dns_record = '', 
                        local_dns_record_enabled = True, 
                        mac = '', 
                        name = '', 
                        network_id = '', 
                        note = '', 
                        site_id = '', 
                        use_fixedip = True, 
                        usergroup_id = '', 
                        virtual_network_override_enabled = True, 
                        virtual_network_override_id = '', )
                    ],
                meta = unifi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return UserResponse(
        )
        """

    def testUserResponse(self):
        """Test UserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
