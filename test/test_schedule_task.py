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

from openapi_client.models.schedule_task import ScheduleTask

class TestScheduleTask(unittest.TestCase):
    """ScheduleTask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleTask:
        """Test ScheduleTask
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleTask`
        """
        model = ScheduleTask()
        if include_optional:
            return ScheduleTask(
                id = '',
                action = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                cron_expr = '',
                execute_only_once = True,
                name = '',
                site_id = '',
                upgrade_targets = [
                    openapi_client.models.schedule_task_upgrade_targets.ScheduleTaskUpgradeTargets(
                        mac = '', )
                    ]
            )
        else:
            return ScheduleTask(
        )
        """

    def testScheduleTask(self):
        """Test ScheduleTask"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
