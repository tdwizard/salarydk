# salarydk.EmploymentPositionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employment_positions**](EmploymentPositionsApi.md#get_employment_positions) | **GET** /v2/employmentPositions | 


# **get_employment_positions**
> InlineResponse20045 get_employment_positions(country=country)



Get a list of standard employment positions.

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
api_instance = salarydk.EmploymentPositionsApi(salarydk.ApiClient(configuration))
country = 'country_example' # str |  (optional)

try:
    api_response = api_instance.get_employment_positions(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmploymentPositionsApi->get_employment_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

