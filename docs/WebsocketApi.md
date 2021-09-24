# salarydk.WebsocketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_update_socket**](WebsocketApi.md#get_update_socket) | **GET** /v2/ws | 


# **get_update_socket**
> get_update_socket()



Websocket for getting realtime updates

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.WebsocketApi()

try:
    api_instance.get_update_socket()
except ApiException as e:
    print("Exception when calling WebsocketApi->get_update_socket: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

