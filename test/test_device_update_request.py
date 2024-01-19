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

from unifi_client.models.device_update_request import DeviceUpdateRequest

class TestDeviceUpdateRequest(unittest.TestCase):
    """DeviceUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceUpdateRequest:
        """Test DeviceUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceUpdateRequest`
        """
        model = DeviceUpdateRequest()
        if include_optional:
            return DeviceUpdateRequest(
                id = '',
                adopted = True,
                atf_enabled = True,
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                bandsteering_mode = '',
                baresip_auth_user = '',
                baresip_enabled = True,
                baresip_extension = '',
                config_network = unifi_client.models.device_config_network.DeviceConfigNetwork(
                    bonding_enabled = True, 
                    dns1 = '', 
                    dns2 = '', 
                    dnssuffix = '', 
                    gateway = '', 
                    ip = '', 
                    netmask = '', 
                    type = '', ),
                connected_battery_overrides = [
                    unifi_client.models.device_connected_battery_overrides.DeviceConnectedBatteryOverrides(
                        mac = '', )
                    ],
                disabled = True,
                dot1x_fallback_networkconf_id = '',
                dot1x_portctrl_enabled = True,
                dpi_enabled = True,
                ether_lighting = unifi_client.models.device_ether_lighting.DeviceEtherLighting(
                    brightness = 56, 
                    mode = '', ),
                ethernet_overrides = [
                    unifi_client.models.device_ethernet_overrides.DeviceEthernetOverrides(
                        ifname = '', 
                        networkgroup = '', )
                    ],
                flowctrl_enabled = True,
                gateway_vrrp_mode = '',
                gateway_vrrp_priority = 56,
                height_in_meters = 1.337,
                hostname = '',
                jumboframe_enabled = True,
                lcm_brightness = 56,
                lcm_brightness_override = True,
                lcm_idle_timeout = 56,
                lcm_idle_timeout_override = True,
                lcm_night_mode_begins = '',
                lcm_night_mode_ends = '',
                lcm_settings_restricted_access = True,
                lcm_tracker_enabled = True,
                lcm_tracker_seed = '',
                led_override = '',
                led_override_color = '',
                led_override_color_brightness = 56,
                locked = True,
                lowpfmode_override = True,
                lte_apn = '',
                lte_auth_type = '',
                lte_data_limit_enabled = True,
                lte_data_warning_enabled = True,
                lte_ext_ant = True,
                lte_hard_limit = 56,
                lte_password = '',
                lte_poe = True,
                lte_roaming_allowed = True,
                lte_sim_pin = 56,
                lte_soft_limit = 56,
                lte_username = '',
                mac = '',
                map_id = '',
                mesh_sta_vap_enabled = True,
                mgmt_network_id = '',
                model = '',
                name = '',
                outdoor_mode_override = '',
                outlet_enabled = True,
                outlet_overrides = [
                    unifi_client.models.device_outlet_overrides.DeviceOutletOverrides(
                        cycle_enabled = True, 
                        index = 56, 
                        name = '', 
                        relay_state = True, )
                    ],
                outlet_power_cycle_enabled = True,
                port_overrides = [
                    unifi_client.models.device_port_overrides.DevicePortOverrides(
                        aggregate_num_ports = 56, 
                        autoneg = True, 
                        dot1x_ctrl = '', 
                        dot1x_idle_timeout = 56, 
                        egress_rate_limit_kbps = 56, 
                        egress_rate_limit_kbps_enabled = True, 
                        excluded_networkconf_ids = [
                            ''
                            ], 
                        forward = '', 
                        full_duplex = True, 
                        isolation = True, 
                        lldpmed_enabled = True, 
                        lldpmed_notify_enabled = True, 
                        mirror_port_idx = 56, 
                        name = '', 
                        native_networkconf_id = '', 
                        op_mode = '', 
                        poe_mode = '', 
                        port_idx = 56, 
                        port_keepalive_enabled = True, 
                        port_security_enabled = True, 
                        port_security_mac_address = [
                            ''
                            ], 
                        portconf_id = '', 
                        priority_queue1_level = 56, 
                        priority_queue2_level = 56, 
                        priority_queue3_level = 56, 
                        priority_queue4_level = 56, 
                        setting_preference = '', 
                        speed = 56, 
                        stormctrl_bcast_enabled = True, 
                        stormctrl_bcast_level = 56, 
                        stormctrl_bcast_rate = 56, 
                        stormctrl_mcast_enabled = True, 
                        stormctrl_mcast_level = 56, 
                        stormctrl_mcast_rate = 56, 
                        stormctrl_type = '', 
                        stormctrl_ucast_enabled = True, 
                        stormctrl_ucast_level = 56, 
                        stormctrl_ucast_rate = 56, 
                        stp_port_mode = True, 
                        tagged_vlan_mgmt = '', 
                        voice_networkconf_id = '', )
                    ],
                power_source_ctrl = '',
                power_source_ctrl_budget = 56,
                power_source_ctrl_enabled = True,
                radio_table = [
                    unifi_client.models.device_radio_table.DeviceRadioTable(
                        antenna_gain = 56, 
                        antenna_id = 56, 
                        backup_channel = '', 
                        channel = '', 
                        channel_optimization_enabled = True, 
                        hard_noise_floor_enabled = True, 
                        ht = 56, 
                        loadbalance_enabled = True, 
                        maxsta = 56, 
                        min_rssi = 56, 
                        min_rssi_enabled = True, 
                        name = '', 
                        radio = '', 
                        radio_identifiers = [
                            unifi_client.models.device_radio_i_dentifiers.DeviceRadioIDentifiers(
                                device_id = '', 
                                radio_name = '', )
                            ], 
                        sens_level = 56, 
                        sens_level_enabled = True, 
                        tx_power = '', 
                        tx_power_mode = '', 
                        vwire_enabled = True, )
                    ],
                radiusprofile_id = '',
                resetbtn_enabled = '',
                rps_override = unifi_client.models.device_rps_override.DeviceRpsOverride(
                    power_management_mode = '', 
                    rps_port_table = [
                        unifi_client.models.device_rps_port_table.DeviceRpsPortTable(
                            name = '', 
                            port_idx = 56, 
                            port_mode = '', )
                        ], ),
                site_id = '',
                snmp_contact = '',
                snmp_location = '',
                state = 56,
                stp_priority = '',
                stp_version = '',
                switch_vlan_enabled = True,
                type = '',
                ubb_pair_name = '',
                volume = 56,
                x = 1.337,
                x_baresip_password = '',
                y = 1.337
            )
        else:
            return DeviceUpdateRequest(
        )
        """

    def testDeviceUpdateRequest(self):
        """Test DeviceUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
