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

from openapi_client.models.dashboard import Dashboard

class TestDashboard(unittest.TestCase):
    """Dashboard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dashboard:
        """Test Dashboard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dashboard`
        """
        model = Dashboard()
        if include_optional:
            return Dashboard(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                controller_version = '',
                desc = '',
                is_public = True,
                modules = [
                    openapi_client.models.dashboard_modules.DashboardModules(
                        config = '', 
                        id = '', 
                        module_id = '', 
                        restrictions = '', )
                    ],
                name = '',
                site_id = ''
            )
        else:
            return Dashboard(
        )
        """

    def testDashboard(self):
        """Test Dashboard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
