# salarydk.NetsMessagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nets_messages**](NetsMessagesApi.md#get_nets_messages) | **GET** /v2/netsMessages | 


# **get_nets_messages**
> InlineResponse20056 get_nets_messages(company_id=company_id)



Get all messages from NETS for a company

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
api_instance = salarydk.NetsMessagesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_nets_messages(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetsMessagesApi->get_nets_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

