# salarydk.StartBalancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_start_balance**](StartBalancesApi.md#get_start_balance) | **GET** /v2/startBalances/{employmentID} | 
[**update_start_balance**](StartBalancesApi.md#update_start_balance) | **PUT** /v2/startBalances/{employmentID} | 


# **get_start_balance**
> InlineResponse20080 get_start_balance(employment_id)



Gets the registrered start balance for this employment

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
api_instance = salarydk.StartBalancesApi(salarydk.ApiClient(configuration))
employment_id = 'employment_id_example' # str | 

try:
    api_response = api_instance.get_start_balance(employment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StartBalancesApi->get_start_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employment_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_start_balance**
> InlineResponse20080 update_start_balance(employment_id, start_balance)



Updates the registrered start balance for this employment

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
api_instance = salarydk.StartBalancesApi(salarydk.ApiClient(configuration))
employment_id = 'employment_id_example' # str | 
start_balance = salarydk.StartBalance() # StartBalance | 

try:
    api_response = api_instance.update_start_balance(employment_id, start_balance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StartBalancesApi->update_start_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employment_id** | [**str**](.md)|  | 
 **start_balance** | [**StartBalance**](StartBalance.md)|  | 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

