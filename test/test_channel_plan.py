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

from openapi_client.models.channel_plan import ChannelPlan

class TestChannelPlan(unittest.TestCase):
    """ChannelPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelPlan:
        """Test ChannelPlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelPlan`
        """
        model = ChannelPlan()
        if include_optional:
            return ChannelPlan(
                id = '',
                ap_blacklisted_channels = [
                    openapi_client.models.channel_plan_ap_blacklisted_channels.ChannelPlanApBlacklistedChannels(
                        channel = 56, 
                        mac = '', 
                        timestamp = 56, )
                    ],
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                conf_source = '',
                coupling = [
                    openapi_client.models.channel_plan_coupling.ChannelPlanCoupling(
                        rssi = 56, 
                        source = '', 
                        target = '', )
                    ],
                var_date = '',
                fitness = 1.337,
                note = '',
                radio = '',
                radio_table = [
                    openapi_client.models.channel_plan_radio_table.ChannelPlanRadioTable(
                        backup_channel = '', 
                        channel = '', 
                        device_mac = '', 
                        name = '', 
                        tx_power = '', 
                        tx_power_mode = '', 
                        width = 56, )
                    ],
                satisfaction = 1.337,
                satisfaction_table = [
                    openapi_client.models.channel_plan_satisfaction_table.ChannelPlanSatisfactionTable(
                        device_mac = '', 
                        satisfaction = 1.337, )
                    ],
                site_blacklisted_channels = [
                    openapi_client.models.channel_plan_site_blacklisted_channels.ChannelPlanSiteBlacklistedChannels(
                        channel = 56, 
                        timestamp = 56, )
                    ],
                site_id = ''
            )
        else:
            return ChannelPlan(
        )
        """

    def testChannelPlan(self):
        """Test ChannelPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()