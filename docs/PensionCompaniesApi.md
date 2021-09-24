# salarydk.PensionCompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pension_companies**](PensionCompaniesApi.md#get_pension_companies) | **GET** /v2/pensionCompanies | 


# **get_pension_companies**
> InlineResponse20066 get_pension_companies()



Get all pension companies

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
api_instance = salarydk.PensionCompaniesApi(salarydk.ApiClient(configuration))

try:
    api_response = api_instance.get_pension_companies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PensionCompaniesApi->get_pension_companies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

