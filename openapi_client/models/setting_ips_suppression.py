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
from pydantic import BaseModel
from openapi_client.models.setting_ips_alerts import SettingIpsAlerts
from openapi_client.models.setting_ips_whitelist import SettingIpsWhitelist
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SettingIpsSuppression(BaseModel):
    """
    SettingIpsSuppression
    """ # noqa: E501
    alerts: Optional[List[SettingIpsAlerts]] = None
    whitelist: Optional[List[SettingIpsWhitelist]] = None
    __properties: ClassVar[List[str]] = ["alerts", "whitelist"]

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
        """Create an instance of SettingIpsSuppression from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in alerts (list)
        _items = []
        if self.alerts:
            for _item in self.alerts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alerts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in whitelist (list)
        _items = []
        if self.whitelist:
            for _item in self.whitelist:
                if _item:
                    _items.append(_item.to_dict())
            _dict['whitelist'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SettingIpsSuppression from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alerts": [SettingIpsAlerts.from_dict(_item) for _item in obj.get("alerts")] if obj.get("alerts") is not None else None,
            "whitelist": [SettingIpsWhitelist.from_dict(_item) for _item in obj.get("whitelist")] if obj.get("whitelist") is not None else None
        })
        return _obj


