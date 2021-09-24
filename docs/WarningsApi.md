# salarydk.WarningsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_warning**](WarningsApi.md#acknowledge_warning) | **DELETE** /v2/warnings/{id} | 
[**get_warnings**](WarningsApi.md#get_warnings) | **GET** /v2/warnings | 


# **acknowledge_warning**
> acknowledge_warning(id)



Acknowledge a warning

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
api_instance = salarydk.WarningsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | The ID of the warning to acknowledge

try:
    api_instance.acknowledge_warning(id)
except ApiException as e:
    print("Exception when calling WarningsApi->acknowledge_warning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the warning to acknowledge | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warnings**
> InlineResponse20099 get_warnings(company_id)



Get warnings for a company

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
api_instance = salarydk.WarningsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_warnings(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningsApi->get_warnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

