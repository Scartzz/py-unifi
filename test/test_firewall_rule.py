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

from unifi_client.models.firewall_rule import FirewallRule

class TestFirewallRule(unittest.TestCase):
    """FirewallRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FirewallRule:
        """Test FirewallRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FirewallRule`
        """
        model = FirewallRule()
        if include_optional:
            return FirewallRule(
                id = '',
                action = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                contiguous = True,
                dst_address = '',
                dst_address_ipv6 = '',
                dst_firewallgroup_ids = [
                    ''
                    ],
                dst_networkconf_id = '',
                dst_networkconf_type = '',
                dst_port = '',
                enabled = True,
                icmp_typename = '',
                icmpv6_typename = '',
                ipsec = '',
                logging = True,
                monthdays = '',
                monthdays_negate = True,
                name = '',
                protocol = '',
                protocol_match_excepted = True,
                protocol_v6 = '',
                rule_index = 56,
                ruleset = '',
                setting_preference = '',
                site_id = '',
                src_address = '',
                src_address_ipv6 = '',
                src_firewallgroup_ids = [
                    ''
                    ],
                src_mac_address = '',
                src_networkconf_id = '',
                src_networkconf_type = '',
                src_port = '',
                startdate = '',
                starttime = '',
                state_established = True,
                state_invalid = True,
                state_new = True,
                state_related = True,
                stopdate = '',
                stoptime = '',
                utc = True,
                weekdays = '',
                weekdays_negate = True
            )
        else:
            return FirewallRule(
        )
        """

    def testFirewallRule(self):
        """Test FirewallRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
