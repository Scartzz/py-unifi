# coding: utf-8

"""
    Unifi API

    Unifi Controller API

    The version of the OpenAPI document: 8.0.26
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.wlan_private_preshared_keys import WLANPrivatePresharedKeys
from openapi_client.models.wlan_sae_psk import WLANSaePsk
from openapi_client.models.wlan_schedule_with_duration import WLANScheduleWithDuration
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WLANUpdateRequest(BaseModel):
    """
    WLANUpdateRequest
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    ap_group_ids: Optional[List[StrictStr]] = None
    ap_group_mode: Optional[StrictStr] = None
    attr_hidden: Optional[StrictBool] = None
    attr_hidden_id: Optional[StrictStr] = None
    attr_no_delete: Optional[StrictBool] = None
    attr_no_edit: Optional[StrictBool] = None
    auth_cache: Optional[StrictBool] = None
    b_supported: Optional[StrictBool] = None
    bc_filter_enabled: Optional[StrictBool] = None
    bc_filter_list: Optional[List[StrictStr]] = None
    bss_transition: Optional[StrictBool] = None
    country_beacon: Optional[StrictBool] = None
    dpi_enabled: Optional[StrictBool] = None
    dpigroup_id: Optional[StrictStr] = None
    dtim_6e: Optional[StrictInt] = None
    dtim_mode: Optional[StrictStr] = None
    dtim_na: Optional[StrictInt] = None
    dtim_ng: Optional[StrictInt] = None
    element_adopt: Optional[StrictBool] = None
    enabled: Optional[StrictBool] = None
    fast_roaming_enabled: Optional[StrictBool] = None
    group_rekey: Optional[StrictInt] = None
    hide_ssid: Optional[StrictBool] = None
    hotspot2conf_enabled: Optional[StrictBool] = None
    hotspot2conf_id: Optional[StrictStr] = None
    iapp_enabled: Optional[StrictBool] = None
    is_guest: Optional[StrictBool] = None
    l2_isolation: Optional[StrictBool] = None
    log_level: Optional[StrictStr] = None
    mac_filter_enabled: Optional[StrictBool] = None
    mac_filter_list: Optional[List[StrictStr]] = None
    mac_filter_policy: Optional[StrictStr] = None
    mcastenhance_enabled: Optional[StrictBool] = None
    minrate_na_advertising_rates: Optional[StrictBool] = None
    minrate_na_data_rate_kbps: Optional[StrictInt] = None
    minrate_na_enabled: Optional[StrictBool] = None
    minrate_ng_advertising_rates: Optional[StrictBool] = None
    minrate_ng_data_rate_kbps: Optional[StrictInt] = None
    minrate_ng_enabled: Optional[StrictBool] = None
    minrate_setting_preference: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    name_combine_enabled: Optional[StrictBool] = None
    name_combine_suffix: Optional[StrictStr] = None
    networkconf_id: Optional[StrictStr] = None
    no2ghz_oui: Optional[StrictBool] = None
    optimize_iot_wifi_connectivity: Optional[StrictBool] = None
    p2p: Optional[StrictBool] = None
    p2p_cross_connect: Optional[StrictBool] = None
    pmf_cipher: Optional[StrictStr] = None
    pmf_mode: Optional[StrictStr] = None
    priority: Optional[StrictStr] = None
    private_preshared_keys: Optional[List[WLANPrivatePresharedKeys]] = None
    private_preshared_keys_enabled: Optional[StrictBool] = None
    proxy_arp: Optional[StrictBool] = None
    radius_das_enabled: Optional[StrictBool] = None
    radius_mac_auth_enabled: Optional[StrictBool] = None
    radius_macacl_empty_password: Optional[StrictBool] = None
    radius_macacl_format: Optional[StrictStr] = None
    radiusprofile_id: Optional[StrictStr] = None
    roam_cluster_id: Optional[StrictInt] = None
    rrm_enabled: Optional[StrictBool] = None
    sae_anti_clogging: Optional[StrictInt] = None
    sae_groups: Optional[List[StrictInt]] = None
    sae_psk: Optional[List[WLANSaePsk]] = None
    sae_psk_vlan_required: Optional[StrictBool] = None
    sae_sync: Optional[StrictInt] = None
    schedule: Optional[List[StrictStr]] = None
    schedule_enabled: Optional[StrictBool] = None
    schedule_reversed: Optional[StrictBool] = None
    schedule_with_duration: Optional[List[WLANScheduleWithDuration]] = None
    security: Optional[StrictStr] = None
    setting_preference: Optional[StrictStr] = None
    site_id: Optional[StrictStr] = None
    tdls_prohibit: Optional[StrictBool] = None
    uapsd_enabled: Optional[StrictBool] = None
    uid_workspace_url: Optional[StrictStr] = None
    usergroup_id: Optional[StrictStr] = None
    vlan: Optional[StrictInt] = None
    vlan_enabled: Optional[StrictBool] = None
    wep_idx: Optional[StrictInt] = None
    wlan_band: Optional[StrictStr] = None
    wlan_bands: Optional[List[StrictStr]] = None
    wlangroup_id: Optional[StrictStr] = None
    wpa_enc: Optional[StrictStr] = None
    wpa_mode: Optional[StrictStr] = None
    wpa_psk_radius: Optional[StrictStr] = None
    wpa3_enhanced_192: Optional[StrictBool] = None
    wpa3_fast_roaming: Optional[StrictBool] = None
    wpa3_support: Optional[StrictBool] = None
    wpa3_transition: Optional[StrictBool] = None
    x_iapp_key: Optional[StrictStr] = None
    x_passphrase: Optional[StrictStr] = None
    x_wep: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_id", "ap_group_ids", "ap_group_mode", "attr_hidden", "attr_hidden_id", "attr_no_delete", "attr_no_edit", "auth_cache", "b_supported", "bc_filter_enabled", "bc_filter_list", "bss_transition", "country_beacon", "dpi_enabled", "dpigroup_id", "dtim_6e", "dtim_mode", "dtim_na", "dtim_ng", "element_adopt", "enabled", "fast_roaming_enabled", "group_rekey", "hide_ssid", "hotspot2conf_enabled", "hotspot2conf_id", "iapp_enabled", "is_guest", "l2_isolation", "log_level", "mac_filter_enabled", "mac_filter_list", "mac_filter_policy", "mcastenhance_enabled", "minrate_na_advertising_rates", "minrate_na_data_rate_kbps", "minrate_na_enabled", "minrate_ng_advertising_rates", "minrate_ng_data_rate_kbps", "minrate_ng_enabled", "minrate_setting_preference", "name", "name_combine_enabled", "name_combine_suffix", "networkconf_id", "no2ghz_oui", "optimize_iot_wifi_connectivity", "p2p", "p2p_cross_connect", "pmf_cipher", "pmf_mode", "priority", "private_preshared_keys", "private_preshared_keys_enabled", "proxy_arp", "radius_das_enabled", "radius_mac_auth_enabled", "radius_macacl_empty_password", "radius_macacl_format", "radiusprofile_id", "roam_cluster_id", "rrm_enabled", "sae_anti_clogging", "sae_groups", "sae_psk", "sae_psk_vlan_required", "sae_sync", "schedule", "schedule_enabled", "schedule_reversed", "schedule_with_duration", "security", "setting_preference", "site_id", "tdls_prohibit", "uapsd_enabled", "uid_workspace_url", "usergroup_id", "vlan", "vlan_enabled", "wep_idx", "wlan_band", "wlan_bands", "wlangroup_id", "wpa_enc", "wpa_mode", "wpa_psk_radius", "wpa3_enhanced_192", "wpa3_fast_roaming", "wpa3_support", "wpa3_transition", "x_iapp_key", "x_passphrase", "x_wep"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WLANUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in private_preshared_keys (list)
        _items = []
        if self.private_preshared_keys:
            for _item in self.private_preshared_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['private_preshared_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sae_psk (list)
        _items = []
        if self.sae_psk:
            for _item in self.sae_psk:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sae_psk'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in schedule_with_duration (list)
        _items = []
        if self.schedule_with_duration:
            for _item in self.schedule_with_duration:
                if _item:
                    _items.append(_item.to_dict())
            _dict['schedule_with_duration'] = _items
        # set to None if schedule_with_duration (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_with_duration is None and "schedule_with_duration" in self.model_fields_set:
            _dict['schedule_with_duration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WLANUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "ap_group_ids": obj.get("ap_group_ids"),
            "ap_group_mode": obj.get("ap_group_mode"),
            "attr_hidden": obj.get("attr_hidden"),
            "attr_hidden_id": obj.get("attr_hidden_id"),
            "attr_no_delete": obj.get("attr_no_delete"),
            "attr_no_edit": obj.get("attr_no_edit"),
            "auth_cache": obj.get("auth_cache"),
            "b_supported": obj.get("b_supported"),
            "bc_filter_enabled": obj.get("bc_filter_enabled"),
            "bc_filter_list": obj.get("bc_filter_list"),
            "bss_transition": obj.get("bss_transition"),
            "country_beacon": obj.get("country_beacon"),
            "dpi_enabled": obj.get("dpi_enabled"),
            "dpigroup_id": obj.get("dpigroup_id"),
            "dtim_6e": obj.get("dtim_6e"),
            "dtim_mode": obj.get("dtim_mode"),
            "dtim_na": obj.get("dtim_na"),
            "dtim_ng": obj.get("dtim_ng"),
            "element_adopt": obj.get("element_adopt"),
            "enabled": obj.get("enabled"),
            "fast_roaming_enabled": obj.get("fast_roaming_enabled"),
            "group_rekey": obj.get("group_rekey"),
            "hide_ssid": obj.get("hide_ssid"),
            "hotspot2conf_enabled": obj.get("hotspot2conf_enabled"),
            "hotspot2conf_id": obj.get("hotspot2conf_id"),
            "iapp_enabled": obj.get("iapp_enabled"),
            "is_guest": obj.get("is_guest"),
            "l2_isolation": obj.get("l2_isolation"),
            "log_level": obj.get("log_level"),
            "mac_filter_enabled": obj.get("mac_filter_enabled"),
            "mac_filter_list": obj.get("mac_filter_list"),
            "mac_filter_policy": obj.get("mac_filter_policy"),
            "mcastenhance_enabled": obj.get("mcastenhance_enabled"),
            "minrate_na_advertising_rates": obj.get("minrate_na_advertising_rates"),
            "minrate_na_data_rate_kbps": obj.get("minrate_na_data_rate_kbps"),
            "minrate_na_enabled": obj.get("minrate_na_enabled"),
            "minrate_ng_advertising_rates": obj.get("minrate_ng_advertising_rates"),
            "minrate_ng_data_rate_kbps": obj.get("minrate_ng_data_rate_kbps"),
            "minrate_ng_enabled": obj.get("minrate_ng_enabled"),
            "minrate_setting_preference": obj.get("minrate_setting_preference"),
            "name": obj.get("name"),
            "name_combine_enabled": obj.get("name_combine_enabled"),
            "name_combine_suffix": obj.get("name_combine_suffix"),
            "networkconf_id": obj.get("networkconf_id"),
            "no2ghz_oui": obj.get("no2ghz_oui"),
            "optimize_iot_wifi_connectivity": obj.get("optimize_iot_wifi_connectivity"),
            "p2p": obj.get("p2p"),
            "p2p_cross_connect": obj.get("p2p_cross_connect"),
            "pmf_cipher": obj.get("pmf_cipher"),
            "pmf_mode": obj.get("pmf_mode"),
            "priority": obj.get("priority"),
            "private_preshared_keys": [WLANPrivatePresharedKeys.from_dict(_item) for _item in obj.get("private_preshared_keys")] if obj.get("private_preshared_keys") is not None else None,
            "private_preshared_keys_enabled": obj.get("private_preshared_keys_enabled"),
            "proxy_arp": obj.get("proxy_arp"),
            "radius_das_enabled": obj.get("radius_das_enabled"),
            "radius_mac_auth_enabled": obj.get("radius_mac_auth_enabled"),
            "radius_macacl_empty_password": obj.get("radius_macacl_empty_password"),
            "radius_macacl_format": obj.get("radius_macacl_format"),
            "radiusprofile_id": obj.get("radiusprofile_id"),
            "roam_cluster_id": obj.get("roam_cluster_id"),
            "rrm_enabled": obj.get("rrm_enabled"),
            "sae_anti_clogging": obj.get("sae_anti_clogging"),
            "sae_groups": obj.get("sae_groups"),
            "sae_psk": [WLANSaePsk.from_dict(_item) for _item in obj.get("sae_psk")] if obj.get("sae_psk") is not None else None,
            "sae_psk_vlan_required": obj.get("sae_psk_vlan_required"),
            "sae_sync": obj.get("sae_sync"),
            "schedule": obj.get("schedule"),
            "schedule_enabled": obj.get("schedule_enabled"),
            "schedule_reversed": obj.get("schedule_reversed"),
            "schedule_with_duration": [WLANScheduleWithDuration.from_dict(_item) for _item in obj.get("schedule_with_duration")] if obj.get("schedule_with_duration") is not None else None,
            "security": obj.get("security"),
            "setting_preference": obj.get("setting_preference"),
            "site_id": obj.get("site_id"),
            "tdls_prohibit": obj.get("tdls_prohibit"),
            "uapsd_enabled": obj.get("uapsd_enabled"),
            "uid_workspace_url": obj.get("uid_workspace_url"),
            "usergroup_id": obj.get("usergroup_id"),
            "vlan": obj.get("vlan"),
            "vlan_enabled": obj.get("vlan_enabled"),
            "wep_idx": obj.get("wep_idx"),
            "wlan_band": obj.get("wlan_band"),
            "wlan_bands": obj.get("wlan_bands"),
            "wlangroup_id": obj.get("wlangroup_id"),
            "wpa_enc": obj.get("wpa_enc"),
            "wpa_mode": obj.get("wpa_mode"),
            "wpa_psk_radius": obj.get("wpa_psk_radius"),
            "wpa3_enhanced_192": obj.get("wpa3_enhanced_192"),
            "wpa3_fast_roaming": obj.get("wpa3_fast_roaming"),
            "wpa3_support": obj.get("wpa3_support"),
            "wpa3_transition": obj.get("wpa3_transition"),
            "x_iapp_key": obj.get("x_iapp_key"),
            "x_passphrase": obj.get("x_passphrase"),
            "x_wep": obj.get("x_wep")
        })
        return _obj


