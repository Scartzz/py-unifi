# openapi_client.SettingSuperMgmtApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_mgmt**](SettingSuperMgmtApi.md#get_setting_super_mgmt) | **GET** /get/setting/super_mgmt | 
[**update_setting_super_mgmt**](SettingSuperMgmtApi.md#update_setting_super_mgmt) | **PUT** /set/setting/super_mgmt | 


# **get_setting_super_mgmt**
> SettingSuperMgmtResponse get_setting_super_mgmt()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_mgmt_response import SettingSuperMgmtResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SettingSuperMgmtApi(api_client)

    try:
        api_response = api_instance.get_setting_super_mgmt()
        print("The response of SettingSuperMgmtApi->get_setting_super_mgmt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperMgmtApi->get_setting_super_mgmt: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperMgmtResponse**](SettingSuperMgmtResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting_super_mgmt**
> SettingSuperMgmtResponse update_setting_super_mgmt(setting_super_mgmt=setting_super_mgmt)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_mgmt import SettingSuperMgmt
from openapi_client.models.setting_super_mgmt_response import SettingSuperMgmtResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SettingSuperMgmtApi(api_client)
    setting_super_mgmt = openapi_client.SettingSuperMgmt() # SettingSuperMgmt |  (optional)

    try:
        api_response = api_instance.update_setting_super_mgmt(setting_super_mgmt=setting_super_mgmt)
        print("The response of SettingSuperMgmtApi->update_setting_super_mgmt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperMgmtApi->update_setting_super_mgmt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_mgmt** | [**SettingSuperMgmt**](SettingSuperMgmt.md)|  | [optional] 

### Return type

[**SettingSuperMgmtResponse**](SettingSuperMgmtResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
