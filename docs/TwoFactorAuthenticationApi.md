# salarydk.TwoFactorAuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_two_factor_authentication**](TwoFactorAuthenticationApi.md#complete_two_factor_authentication) | **PATCH** /v2/twoFactorAuthentication | 
[**start_two_factor_authentication**](TwoFactorAuthenticationApi.md#start_two_factor_authentication) | **POST** /v2/twoFactorAuthentication | 


# **complete_two_factor_authentication**
> InlineResponse20092 complete_two_factor_authentication(two_factor_authentication_response=two_factor_authentication_response)



Deliver a two-factor response from the user to upgrade the access token with access to secured operations.

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
api_instance = salarydk.TwoFactorAuthenticationApi(salarydk.ApiClient(configuration))
two_factor_authentication_response = salarydk.InlineObject41() # InlineObject41 |  (optional)

try:
    api_response = api_instance.complete_two_factor_authentication(two_factor_authentication_response=two_factor_authentication_response)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwoFactorAuthenticationApi->complete_two_factor_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_authentication_response** | [**InlineObject41**](InlineObject41.md)|  | [optional] 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_two_factor_authentication**
> start_two_factor_authentication(two_factor_authentication_request=two_factor_authentication_request)



Starts a two-factor authentication flow, for granting access to secured operations.

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
api_instance = salarydk.TwoFactorAuthenticationApi(salarydk.ApiClient(configuration))
two_factor_authentication_request = salarydk.InlineObject40() # InlineObject40 |  (optional)

try:
    api_instance.start_two_factor_authentication(two_factor_authentication_request=two_factor_authentication_request)
except ApiException as e:
    print("Exception when calling TwoFactorAuthenticationApi->start_two_factor_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_authentication_request** | [**InlineObject40**](InlineObject40.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

