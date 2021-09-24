# salarydk.HarvestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**harvest_information**](HarvestApi.md#harvest_information) | **POST** /v2/harvest | 
[**register_user_interest**](HarvestApi.md#register_user_interest) | **POST** /v2/userInterest | 


# **harvest_information**
> harvest_information(harvest)



Harvest information for user or company

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
api_instance = salarydk.HarvestApi(salarydk.ApiClient(configuration))
harvest = NULL # list[HarvestInformation] | 

try:
    api_instance.harvest_information(harvest)
except ApiException as e:
    print("Exception when calling HarvestApi->harvest_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvest** | [**list[HarvestInformation]**](list.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user_interest**
> register_user_interest(harvest=harvest)



Register user interest

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.HarvestApi()
harvest = salarydk.InlineObject43() # InlineObject43 |  (optional)

try:
    api_instance.register_user_interest(harvest=harvest)
except ApiException as e:
    print("Exception when calling HarvestApi->register_user_interest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvest** | [**InlineObject43**](InlineObject43.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

