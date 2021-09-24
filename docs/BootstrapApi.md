# salarydk.BootstrapApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bootstrap**](BootstrapApi.md#get_bootstrap) | **GET** /v2/bootstrap | 


# **get_bootstrap**
> InlineResponse20012 get_bootstrap(company_id=company_id)



Bootstrap the frontend with a lot of data

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
api_instance = salarydk.BootstrapApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | If provided, also return data for a company (optional)

try:
    api_response = api_instance.get_bootstrap(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootstrapApi->get_bootstrap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| If provided, also return data for a company | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

