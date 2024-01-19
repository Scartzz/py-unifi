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

from openapi_client.models.network_update_request import NetworkUpdateRequest

class TestNetworkUpdateRequest(unittest.TestCase):
    """NetworkUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkUpdateRequest:
        """Test NetworkUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkUpdateRequest`
        """
        model = NetworkUpdateRequest()
        if include_optional:
            return NetworkUpdateRequest(
                id = '',
                attr_hidden = True,
                attr_hidden_id = '',
                attr_no_delete = True,
                attr_no_edit = True,
                auto_scale_enabled = True,
                dhcp_relay_enabled = True,
                dhcpd_boot_enabled = True,
                dhcpd_boot_filename = '',
                dhcpd_boot_server = '',
                dhcpd_dns_1 = '',
                dhcpd_dns_2 = '',
                dhcpd_dns_3 = '',
                dhcpd_dns_4 = '',
                dhcpd_dns_enabled = True,
                dhcpd_enabled = True,
                dhcpd_gateway = '',
                dhcpd_gateway_enabled = True,
                dhcpd_ip_1 = '',
                dhcpd_ip_2 = '',
                dhcpd_ip_3 = '',
                dhcpd_leasetime = 56,
                dhcpd_mac_1 = '',
                dhcpd_mac_2 = '',
                dhcpd_mac_3 = '',
                dhcpd_ntp_1 = '',
                dhcpd_ntp_2 = '',
                dhcpd_ntp_enabled = True,
                dhcpd_start = '',
                dhcpd_stop = '',
                dhcpd_tftp_server = '',
                dhcpd_time_offset = 56,
                dhcpd_time_offset_enabled = True,
                dhcpd_unifi_controller = '',
                dhcpd_wins_1 = '',
                dhcpd_wins_2 = '',
                dhcpd_wins_enabled = True,
                dhcpd_wpad_url = '',
                dhcpdv6_allow_slaac = True,
                dhcpdv6_dns_1 = '',
                dhcpdv6_dns_2 = '',
                dhcpdv6_dns_3 = '',
                dhcpdv6_dns_4 = '',
                dhcpdv6_dns_auto = True,
                dhcpdv6_enabled = True,
                dhcpdv6_leasetime = 56,
                dhcpdv6_start = '',
                dhcpdv6_stop = '',
                dhcpguard_enabled = True,
                domain_name = '',
                dpi_enabled = True,
                dpigroup_id = '',
                enabled = True,
                exposed_to_site_vpn = True,
                gateway_device = '',
                gateway_type = '',
                igmp_fastleave = True,
                igmp_groupmembership = 56,
                igmp_maxresponse = 56,
                igmp_mcrtrexpiretime = 56,
                igmp_proxy_downstream = True,
                igmp_proxy_upstream = True,
                igmp_querier = '',
                igmp_snooping = True,
                igmp_supression = True,
                interface_mtu = 56,
                interface_mtu_enabled = True,
                internet_access_enabled = True,
                ip_subnet = '',
                ipsec_dh_group = 56,
                ipsec_dynamic_routing = True,
                ipsec_encryption = '',
                ipsec_esp_dh_group = 56,
                ipsec_esp_encryption = '',
                ipsec_esp_hash = '',
                ipsec_esp_lifetime = '',
                ipsec_hash = '',
                ipsec_ike_dh_group = 56,
                ipsec_ike_encryption = '',
                ipsec_ike_hash = '',
                ipsec_ike_lifetime = '',
                ipsec_interface = '',
                ipsec_key_exchange = '',
                ipsec_local_identifier = '',
                ipsec_local_identifier_enabled = True,
                ipsec_local_ip = '',
                ipsec_peer_ip = '',
                ipsec_pfs = True,
                ipsec_profile = '',
                ipsec_remote_identifier = '',
                ipsec_remote_identifier_enabled = True,
                ipsec_separate_ikev2_networks = True,
                ipv6_client_address_assignment = '',
                ipv6_interface_type = '',
                ipv6_pd_auto_prefixid_enabled = True,
                ipv6_pd_interface = '',
                ipv6_pd_prefixid = '',
                ipv6_pd_start = '',
                ipv6_pd_stop = '',
                ipv6_ra_enabled = True,
                ipv6_ra_preferred_lifetime = 56,
                ipv6_ra_priority = '',
                ipv6_ra_valid_lifetime = 56,
                ipv6_setting_preference = '',
                ipv6_single_network_interface = '',
                ipv6_subnet = '',
                ipv6_wan_delegation_type = '',
                is_nat = True,
                l2tp_allow_weak_ciphers = True,
                l2tp_interface = '',
                l2tp_local_wan_ip = '',
                local_port = 56,
                lte_lan_enabled = True,
                mac_override = '',
                mac_override_enabled = True,
                mdns_enabled = True,
                name = '',
                nat_outbound_ip_addresses = [
                    openapi_client.models.network_nat_outbound_ip_addresses.NetworkNATOutboundIPAddresses(
                        ip_address = '', 
                        wan_network_group = '', )
                    ],
                network_isolation_enabled = True,
                networkgroup = '',
                openvpn_configuration = '',
                openvpn_configuration_filename = '',
                openvpn_interface = '',
                openvpn_local_address = '',
                openvpn_local_port = 56,
                openvpn_local_wan_ip = '',
                openvpn_mode = '',
                openvpn_remote_address = '',
                openvpn_remote_host = '',
                openvpn_remote_port = 56,
                openvpn_username = '',
                pptpc_require_mppe = True,
                pptpc_route_distance = 56,
                pptpc_server_ip = '',
                pptpc_username = '',
                priority = 56,
                purpose = '',
                radiusprofile_id = '',
                remote_site_id = '',
                remote_site_subnets = [
                    ''
                    ],
                remote_vpn_subnets = [
                    ''
                    ],
                report_wan_event = True,
                require_mschapv2 = True,
                route_distance = 56,
                setting_preference = '',
                single_network_lan = '',
                site_id = '',
                uid_policy_enabled = True,
                uid_policy_name = '',
                uid_public_gateway_port = 56,
                uid_traffic_rules_allowed_ips_and_hostnames = [
                    ''
                    ],
                uid_traffic_rules_enabled = True,
                uid_vpn_custom_routing = [
                    ''
                    ],
                uid_vpn_default_dns_suffix = '',
                uid_vpn_masquerade_enabled = True,
                uid_vpn_max_connection_time_seconds = 56,
                uid_vpn_sync_public_ip = True,
                uid_vpn_type = '',
                uid_workspace_url = '',
                upnp_lan_enabled = True,
                usergroup_id = '',
                vlan = 56,
                vlan_enabled = True,
                vpn_client_configuration_remote_ip_override = '',
                vpn_client_configuration_remote_ip_override_enabled = True,
                vpn_client_default_route = True,
                vpn_client_pull_dns = True,
                vpn_protocol = '',
                vpn_type = '',
                vrrp_ip_subnet_gw1 = '',
                vrrp_ip_subnet_gw2 = '',
                vrrp_vrid = 56,
                wan_dhcp_cos = 56,
                wan_dhcp_options = [
                    openapi_client.models.network_wandhcp_options.NetworkWANDHCPOptions(
                        option_number = 56, 
                        value = '', )
                    ],
                wan_dhcpv6_pd_size = 56,
                wan_dns_preference = '',
                wan_dns1 = '',
                wan_dns2 = '',
                wan_dns3 = '',
                wan_dns4 = '',
                wan_dslite_remote_host = '',
                wan_egress_qos = 56,
                wan_gateway = '',
                wan_gateway_v6 = '',
                wan_ip = '',
                wan_ip_aliases = [
                    ''
                    ],
                wan_ipv6 = '',
                wan_ipv6_dns_preference = '',
                wan_ipv6_dns1 = '',
                wan_ipv6_dns2 = '',
                wan_load_balance_type = '',
                wan_load_balance_weight = 56,
                wan_netmask = '',
                wan_networkgroup = '',
                wan_pppoe_password_enabled = True,
                wan_pppoe_username_enabled = True,
                wan_prefixlen = 56,
                wan_provider_capabilities = openapi_client.models.network_wan_provider_capabilities.NetworkWANProviderCapabilities(
                    download_kilobits_per_second = 56, 
                    upload_kilobits_per_second = 56, ),
                wan_smartq_down_rate = 56,
                wan_smartq_enabled = True,
                wan_smartq_up_rate = 56,
                wan_type = '',
                wan_type_v6 = '',
                wan_username = '',
                wan_vlan = 56,
                wan_vlan_enabled = True,
                wireguard_client_configuration_file = '',
                wireguard_client_configuration_filename = '',
                wireguard_client_mode = '',
                wireguard_client_peer_ip = '',
                wireguard_client_peer_port = 56,
                wireguard_client_peer_public_key = '',
                wireguard_client_preshared_key = '',
                wireguard_client_preshared_key_enabled = True,
                wireguard_interface = '',
                wireguard_local_wan_ip = '',
                wireguard_public_key = '',
                x_auth_key = '',
                x_ca_crt = '',
                x_ca_key = '',
                x_dh_key = '',
                x_ipsec_pre_shared_key = '',
                x_openvpn_password = '',
                x_openvpn_shared_secret_key = '',
                x_pptpc_password = '',
                x_server_crt = '',
                x_server_key = '',
                x_shared_client_crt = '',
                x_shared_client_key = '',
                x_wan_password = '',
                x_wireguard_private_key = ''
            )
        else:
            return NetworkUpdateRequest(
        )
        """

    def testNetworkUpdateRequest(self):
        """Test NetworkUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
