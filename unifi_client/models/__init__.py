# coding: utf-8

# flake8: noqa
"""
    Unifi API

    Unifi Controller API

    The version of the OpenAPI document: 8.0.26
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from unifi_client.models.account import Account
from unifi_client.models.account_response import AccountResponse
from unifi_client.models.account_update_request import AccountUpdateRequest
from unifi_client.models.broadcast_group import BroadcastGroup
from unifi_client.models.broadcast_group_response import BroadcastGroupResponse
from unifi_client.models.broadcast_group_update_request import BroadcastGroupUpdateRequest
from unifi_client.models.channel_plan import ChannelPlan
from unifi_client.models.channel_plan_ap_blacklisted_channels import ChannelPlanApBlacklistedChannels
from unifi_client.models.channel_plan_coupling import ChannelPlanCoupling
from unifi_client.models.channel_plan_radio_table import ChannelPlanRadioTable
from unifi_client.models.channel_plan_response import ChannelPlanResponse
from unifi_client.models.channel_plan_satisfaction_table import ChannelPlanSatisfactionTable
from unifi_client.models.channel_plan_site_blacklisted_channels import ChannelPlanSiteBlacklistedChannels
from unifi_client.models.channel_plan_update_request import ChannelPlanUpdateRequest
from unifi_client.models.dhcp_option import DHCPOption
from unifi_client.models.dhcp_option_response import DHCPOptionResponse
from unifi_client.models.dhcp_option_update_request import DHCPOptionUpdateRequest
from unifi_client.models.dashboard import Dashboard
from unifi_client.models.dashboard_modules import DashboardModules
from unifi_client.models.dashboard_response import DashboardResponse
from unifi_client.models.dashboard_update_request import DashboardUpdateRequest
from unifi_client.models.device import Device
from unifi_client.models.device_config_network import DeviceConfigNetwork
from unifi_client.models.device_connected_battery_overrides import DeviceConnectedBatteryOverrides
from unifi_client.models.device_ether_lighting import DeviceEtherLighting
from unifi_client.models.device_ethernet_overrides import DeviceEthernetOverrides
from unifi_client.models.device_outlet_overrides import DeviceOutletOverrides
from unifi_client.models.device_port_overrides import DevicePortOverrides
from unifi_client.models.device_radio_i_dentifiers import DeviceRadioIDentifiers
from unifi_client.models.device_radio_table import DeviceRadioTable
from unifi_client.models.device_response import DeviceResponse
from unifi_client.models.device_rps_override import DeviceRpsOverride
from unifi_client.models.device_rps_port_table import DeviceRpsPortTable
from unifi_client.models.device_update_request import DeviceUpdateRequest
from unifi_client.models.dpi_app import DpiApp
from unifi_client.models.dpi_app_response import DpiAppResponse
from unifi_client.models.dpi_app_update_request import DpiAppUpdateRequest
from unifi_client.models.dpi_group import DpiGroup
from unifi_client.models.dpi_group_response import DpiGroupResponse
from unifi_client.models.dpi_group_update_request import DpiGroupUpdateRequest
from unifi_client.models.dynamic_dns import DynamicDNS
from unifi_client.models.dynamic_dns_response import DynamicDNSResponse
from unifi_client.models.dynamic_dns_update_request import DynamicDNSUpdateRequest
from unifi_client.models.firewall_group import FirewallGroup
from unifi_client.models.firewall_group_response import FirewallGroupResponse
from unifi_client.models.firewall_group_update_request import FirewallGroupUpdateRequest
from unifi_client.models.firewall_rule import FirewallRule
from unifi_client.models.firewall_rule_response import FirewallRuleResponse
from unifi_client.models.firewall_rule_update_request import FirewallRuleUpdateRequest
from unifi_client.models.get_setting_auto_speedtest_default_response import GetSettingAutoSpeedtestDefaultResponse
from unifi_client.models.get_setting_auto_speedtest_default_response_data_inner import GetSettingAutoSpeedtestDefaultResponseDataInner
from unifi_client.models.heat_map import HeatMap
from unifi_client.models.heat_map_point import HeatMapPoint
from unifi_client.models.heat_map_point_response import HeatMapPointResponse
from unifi_client.models.heat_map_point_update_request import HeatMapPointUpdateRequest
from unifi_client.models.heat_map_response import HeatMapResponse
from unifi_client.models.heat_map_update_request import HeatMapUpdateRequest
from unifi_client.models.hotspot2_conf import Hotspot2Conf
from unifi_client.models.hotspot2_conf_capab import Hotspot2ConfCapab
from unifi_client.models.hotspot2_conf_cellular_network_list import Hotspot2ConfCellularNetworkList
from unifi_client.models.hotspot2_conf_description import Hotspot2ConfDescription
from unifi_client.models.hotspot2_conf_friendly_name import Hotspot2ConfFriendlyName
from unifi_client.models.hotspot2_conf_icon import Hotspot2ConfIcon
from unifi_client.models.hotspot2_conf_icons import Hotspot2ConfIcons
from unifi_client.models.hotspot2_conf_nai_realm_list import Hotspot2ConfNaiRealmList
from unifi_client.models.hotspot2_conf_osu import Hotspot2ConfOsu
from unifi_client.models.hotspot2_conf_qos_map_dcsp import Hotspot2ConfQOSMapDcsp
from unifi_client.models.hotspot2_conf_qos_map_exceptions import Hotspot2ConfQOSMapExceptions
from unifi_client.models.hotspot2_conf_response import Hotspot2ConfResponse
from unifi_client.models.hotspot2_conf_roaming_consortium_list import Hotspot2ConfRoamingConsortiumList
from unifi_client.models.hotspot2_conf_update_request import Hotspot2ConfUpdateRequest
from unifi_client.models.hotspot2_conf_venue_name import Hotspot2ConfVenueName
from unifi_client.models.hotspot_op import HotspotOp
from unifi_client.models.hotspot_op_response import HotspotOpResponse
from unifi_client.models.hotspot_op_update_request import HotspotOpUpdateRequest
from unifi_client.models.hotspot_package import HotspotPackage
from unifi_client.models.hotspot_package_response import HotspotPackageResponse
from unifi_client.models.hotspot_package_update_request import HotspotPackageUpdateRequest
from unifi_client.models.map import Map
from unifi_client.models.map_response import MapResponse
from unifi_client.models.map_update_request import MapUpdateRequest
from unifi_client.models.media_file import MediaFile
from unifi_client.models.media_file_response import MediaFileResponse
from unifi_client.models.media_file_update_request import MediaFileUpdateRequest
from unifi_client.models.meta import Meta
from unifi_client.models.network import Network
from unifi_client.models.network_nat_outbound_ip_addresses import NetworkNATOutboundIPAddresses
from unifi_client.models.network_response import NetworkResponse
from unifi_client.models.network_update_request import NetworkUpdateRequest
from unifi_client.models.network_wandhcp_options import NetworkWANDHCPOptions
from unifi_client.models.network_wan_provider_capabilities import NetworkWANProviderCapabilities
from unifi_client.models.port_forward import PortForward
from unifi_client.models.port_forward_response import PortForwardResponse
from unifi_client.models.port_forward_update_request import PortForwardUpdateRequest
from unifi_client.models.port_profile import PortProfile
from unifi_client.models.port_profile_response import PortProfileResponse
from unifi_client.models.port_profile_update_request import PortProfileUpdateRequest
from unifi_client.models.radius_profile import RADIUSProfile
from unifi_client.models.radius_profile_acct_servers import RADIUSProfileAcctServers
from unifi_client.models.radius_profile_auth_servers import RADIUSProfileAuthServers
from unifi_client.models.radius_profile_response import RADIUSProfileResponse
from unifi_client.models.radius_profile_update_request import RADIUSProfileUpdateRequest
from unifi_client.models.routing import Routing
from unifi_client.models.routing_response import RoutingResponse
from unifi_client.models.routing_update_request import RoutingUpdateRequest
from unifi_client.models.schedule_task import ScheduleTask
from unifi_client.models.schedule_task_response import ScheduleTaskResponse
from unifi_client.models.schedule_task_update_request import ScheduleTaskUpdateRequest
from unifi_client.models.schedule_task_upgrade_targets import ScheduleTaskUpgradeTargets
from unifi_client.models.setting_auto_speedtest import SettingAutoSpeedtest
from unifi_client.models.setting_auto_speedtest_response import SettingAutoSpeedtestResponse
from unifi_client.models.setting_baresip import SettingBaresip
from unifi_client.models.setting_baresip_response import SettingBaresipResponse
from unifi_client.models.setting_broadcast import SettingBroadcast
from unifi_client.models.setting_broadcast_response import SettingBroadcastResponse
from unifi_client.models.setting_connectivity import SettingConnectivity
from unifi_client.models.setting_connectivity_response import SettingConnectivityResponse
from unifi_client.models.setting_country import SettingCountry
from unifi_client.models.setting_country_response import SettingCountryResponse
from unifi_client.models.setting_doh import SettingDoh
from unifi_client.models.setting_doh_response import SettingDohResponse
from unifi_client.models.setting_dpi import SettingDpi
from unifi_client.models.setting_dpi_response import SettingDpiResponse
from unifi_client.models.setting_element_adopt import SettingElementAdopt
from unifi_client.models.setting_element_adopt_response import SettingElementAdoptResponse
from unifi_client.models.setting_ether_lighting import SettingEtherLighting
from unifi_client.models.setting_ether_lighting_network_overrides import SettingEtherLightingNetworkOverrides
from unifi_client.models.setting_ether_lighting_response import SettingEtherLightingResponse
from unifi_client.models.setting_ether_lighting_speed_overrides import SettingEtherLightingSpeedOverrides
from unifi_client.models.setting_global_ap import SettingGlobalAp
from unifi_client.models.setting_global_ap_response import SettingGlobalApResponse
from unifi_client.models.setting_global_switch import SettingGlobalSwitch
from unifi_client.models.setting_global_switch_response import SettingGlobalSwitchResponse
from unifi_client.models.setting_guest_access import SettingGuestAccess
from unifi_client.models.setting_guest_access_response import SettingGuestAccessResponse
from unifi_client.models.setting_ips import SettingIps
from unifi_client.models.setting_ips_ad_blocking_configurations import SettingIpsAdBlockingConfigurations
from unifi_client.models.setting_ips_alerts import SettingIpsAlerts
from unifi_client.models.setting_ips_dns_filters import SettingIpsDNSFilters
from unifi_client.models.setting_ips_honeypot import SettingIpsHoneypot
from unifi_client.models.setting_ips_response import SettingIpsResponse
from unifi_client.models.setting_ips_suppression import SettingIpsSuppression
from unifi_client.models.setting_ips_tracking import SettingIpsTracking
from unifi_client.models.setting_ips_whitelist import SettingIpsWhitelist
from unifi_client.models.setting_lcm import SettingLcm
from unifi_client.models.setting_lcm_response import SettingLcmResponse
from unifi_client.models.setting_locale import SettingLocale
from unifi_client.models.setting_locale_response import SettingLocaleResponse
from unifi_client.models.setting_magic_site_to_site_vpn import SettingMagicSiteToSiteVpn
from unifi_client.models.setting_magic_site_to_site_vpn_response import SettingMagicSiteToSiteVpnResponse
from unifi_client.models.setting_mgmt import SettingMgmt
from unifi_client.models.setting_mgmt_response import SettingMgmtResponse
from unifi_client.models.setting_mgmt_x_ssh_keys import SettingMgmtXSshKeys
from unifi_client.models.setting_network_optimization import SettingNetworkOptimization
from unifi_client.models.setting_network_optimization_response import SettingNetworkOptimizationResponse
from unifi_client.models.setting_ntp import SettingNtp
from unifi_client.models.setting_ntp_response import SettingNtpResponse
from unifi_client.models.setting_porta import SettingPorta
from unifi_client.models.setting_porta_response import SettingPortaResponse
from unifi_client.models.setting_radio_ai import SettingRadioAi
from unifi_client.models.setting_radio_ai_response import SettingRadioAiResponse
from unifi_client.models.setting_radius import SettingRadius
from unifi_client.models.setting_radius_response import SettingRadiusResponse
from unifi_client.models.setting_rsyslogd import SettingRsyslogd
from unifi_client.models.setting_rsyslogd_response import SettingRsyslogdResponse
from unifi_client.models.setting_snmp import SettingSnmp
from unifi_client.models.setting_snmp_response import SettingSnmpResponse
from unifi_client.models.setting_super_cloudaccess import SettingSuperCloudaccess
from unifi_client.models.setting_super_cloudaccess_response import SettingSuperCloudaccessResponse
from unifi_client.models.setting_super_events import SettingSuperEvents
from unifi_client.models.setting_super_events_response import SettingSuperEventsResponse
from unifi_client.models.setting_super_fwupdate import SettingSuperFwupdate
from unifi_client.models.setting_super_fwupdate_response import SettingSuperFwupdateResponse
from unifi_client.models.setting_super_identity import SettingSuperIdentity
from unifi_client.models.setting_super_identity_response import SettingSuperIdentityResponse
from unifi_client.models.setting_super_mail import SettingSuperMail
from unifi_client.models.setting_super_mail_response import SettingSuperMailResponse
from unifi_client.models.setting_super_mgmt import SettingSuperMgmt
from unifi_client.models.setting_super_mgmt_response import SettingSuperMgmtResponse
from unifi_client.models.setting_super_sdn import SettingSuperSdn
from unifi_client.models.setting_super_sdn_response import SettingSuperSdnResponse
from unifi_client.models.setting_super_smtp import SettingSuperSmtp
from unifi_client.models.setting_super_smtp_response import SettingSuperSmtpResponse
from unifi_client.models.setting_teleport import SettingTeleport
from unifi_client.models.setting_teleport_response import SettingTeleportResponse
from unifi_client.models.setting_usg import SettingUsg
from unifi_client.models.setting_usg_response import SettingUsgResponse
from unifi_client.models.setting_usw import SettingUsw
from unifi_client.models.setting_usw_response import SettingUswResponse
from unifi_client.models.spatial_record import SpatialRecord
from unifi_client.models.spatial_record_devices import SpatialRecordDevices
from unifi_client.models.spatial_record_position import SpatialRecordPosition
from unifi_client.models.spatial_record_response import SpatialRecordResponse
from unifi_client.models.spatial_record_update_request import SpatialRecordUpdateRequest
from unifi_client.models.tag import Tag
from unifi_client.models.tag_response import TagResponse
from unifi_client.models.tag_update_request import TagUpdateRequest
from unifi_client.models.user import User
from unifi_client.models.user_group import UserGroup
from unifi_client.models.user_group_response import UserGroupResponse
from unifi_client.models.user_group_update_request import UserGroupUpdateRequest
from unifi_client.models.user_response import UserResponse
from unifi_client.models.user_update_request import UserUpdateRequest
from unifi_client.models.virtual_device import VirtualDevice
from unifi_client.models.virtual_device_response import VirtualDeviceResponse
from unifi_client.models.virtual_device_update_request import VirtualDeviceUpdateRequest
from unifi_client.models.wlan import WLAN
from unifi_client.models.wlan_group import WLANGroup
from unifi_client.models.wlan_group_response import WLANGroupResponse
from unifi_client.models.wlan_group_update_request import WLANGroupUpdateRequest
from unifi_client.models.wlan_private_preshared_keys import WLANPrivatePresharedKeys
from unifi_client.models.wlan_response import WLANResponse
from unifi_client.models.wlan_sae_psk import WLANSaePsk
from unifi_client.models.wlan_schedule_with_duration import WLANScheduleWithDuration
from unifi_client.models.wlan_update_request import WLANUpdateRequest
