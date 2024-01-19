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

from openapi_client.models.spatial_record_response import SpatialRecordResponse

class TestSpatialRecordResponse(unittest.TestCase):
    """SpatialRecordResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpatialRecordResponse:
        """Test SpatialRecordResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpatialRecordResponse`
        """
        model = SpatialRecordResponse()
        if include_optional:
            return SpatialRecordResponse(
                data = [
                    openapi_client.models.spatial_record.SpatialRecord(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        devices = [
                            openapi_client.models.spatial_record_devices.SpatialRecordDevices(
                                mac = '', 
                                position = openapi_client.models.spatial_record_position.SpatialRecordPosition(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, ), )
                            ], 
                        name = '', 
                        site_id = '', )
                    ],
                meta = openapi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return SpatialRecordResponse(
        )
        """

    def testSpatialRecordResponse(self):
        """Test SpatialRecordResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
