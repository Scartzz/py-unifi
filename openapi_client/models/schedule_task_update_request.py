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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from openapi_client.models.schedule_task_upgrade_targets import ScheduleTaskUpgradeTargets
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScheduleTaskUpdateRequest(BaseModel):
    """
    ScheduleTaskUpdateRequest
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    action: Optional[StrictStr] = None
    attr_hidden: Optional[StrictBool] = None
    attr_hidden_id: Optional[StrictStr] = None
    attr_no_delete: Optional[StrictBool] = None
    attr_no_edit: Optional[StrictBool] = None
    cron_expr: Optional[StrictStr] = None
    execute_only_once: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    site_id: Optional[StrictStr] = None
    upgrade_targets: Optional[List[ScheduleTaskUpgradeTargets]] = None
    __properties: ClassVar[List[str]] = ["_id", "action", "attr_hidden", "attr_hidden_id", "attr_no_delete", "attr_no_edit", "cron_expr", "execute_only_once", "name", "site_id", "upgrade_targets"]

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
        """Create an instance of ScheduleTaskUpdateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in upgrade_targets (list)
        _items = []
        if self.upgrade_targets:
            for _item in self.upgrade_targets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['upgrade_targets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScheduleTaskUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "action": obj.get("action"),
            "attr_hidden": obj.get("attr_hidden"),
            "attr_hidden_id": obj.get("attr_hidden_id"),
            "attr_no_delete": obj.get("attr_no_delete"),
            "attr_no_edit": obj.get("attr_no_edit"),
            "cron_expr": obj.get("cron_expr"),
            "execute_only_once": obj.get("execute_only_once"),
            "name": obj.get("name"),
            "site_id": obj.get("site_id"),
            "upgrade_targets": [ScheduleTaskUpgradeTargets.from_dict(_item) for _item in obj.get("upgrade_targets")] if obj.get("upgrade_targets") is not None else None
        })
        return _obj


