# salarydk.ClockApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rebase_clock**](ClockApi.md#rebase_clock) | **PUT** /v2/clock | 
[**time_now**](ClockApi.md#time_now) | **GET** /v2/clock | 


# **rebase_clock**
> InlineResponse20014 rebase_clock(rebase_ts)



rebase the clock, sets the current time on the server.

### Example

* Api Key Authentication (authorizedUser): 
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# Configure API key authorization: authorizedUser
configuration = salarydk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = salarydk.ClockApi(salarydk.ApiClient(configuration))
rebase_ts = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.rebase_clock(rebase_ts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClockApi->rebase_clock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rebase_ts** | **datetime**|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_now**
> InlineResponse20014 time_now()



get the current time on server.

### Example

* Api Key Authentication (authorizedUser): 
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# Configure API key authorization: authorizedUser
configuration = salarydk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = salarydk.ClockApi(salarydk.ApiClient(configuration))

try:
    api_response = api_instance.time_now()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClockApi->time_now: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

