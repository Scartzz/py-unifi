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

from openapi_client.models.get_setting_auto_speedtest_default_response import GetSettingAutoSpeedtestDefaultResponse

class TestGetSettingAutoSpeedtestDefaultResponse(unittest.TestCase):
    """GetSettingAutoSpeedtestDefaultResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSettingAutoSpeedtestDefaultResponse:
        """Test GetSettingAutoSpeedtestDefaultResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSettingAutoSpeedtestDefaultResponse`
        """
        model = GetSettingAutoSpeedtestDefaultResponse()
        if include_optional:
            return GetSettingAutoSpeedtestDefaultResponse(
                data = [
                    openapi_client.models.get_setting_auto_speedtest_default_response_data_inner.GetSettingAutoSpeedtest_default_response_data_inner(
                        meta = openapi_client.models.meta.Meta(
                            msg = '', 
                            rc = '', ), )
                    ],
                meta = openapi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return GetSettingAutoSpeedtestDefaultResponse(
        )
        """

    def testGetSettingAutoSpeedtestDefaultResponse(self):
        """Test GetSettingAutoSpeedtestDefaultResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
