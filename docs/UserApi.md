# salarydk.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_change**](UserApi.md#email_change) | **POST** /v2/emailChange/{token} | 
[**password_reset**](UserApi.md#password_reset) | **POST** /v2/passwordReset/{token} | 
[**request_email_change**](UserApi.md#request_email_change) | **POST** /v2/emailChange | 
[**request_password_reset**](UserApi.md#request_password_reset) | **POST** /v2/passwordReset | 


# **email_change**
> InlineResponse20038 email_change(token)



Updates the email as requested

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.UserApi()
token = 'token_example' # str | An email change token

try:
    api_response = api_instance.email_change(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->email_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**str**](.md)| An email change token | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_reset**
> password_reset(token, user=user)



Resets a password, using the provided password reset token.

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.UserApi()
token = 'token_example' # str | A reset password token
user = salarydk.InlineObject29() # InlineObject29 |  (optional)

try:
    api_instance.password_reset(token, user=user)
except ApiException as e:
    print("Exception when calling UserApi->password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**str**](.md)| A reset password token | 
 **user** | [**InlineObject29**](InlineObject29.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_email_change**
> request_email_change(user=user)



Request a change of email for the logged in user

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
api_instance = salarydk.UserApi(salarydk.ApiClient(configuration))
user = salarydk.InlineObject10() # InlineObject10 |  (optional)

try:
    api_instance.request_email_change(user=user)
except ApiException as e:
    print("Exception when calling UserApi->request_email_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**InlineObject10**](InlineObject10.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_reset**
> request_password_reset(user=user)



Requests a reset password email sent to the address provided

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.UserApi()
user = salarydk.InlineObject28() # InlineObject28 |  (optional)

try:
    api_instance.request_password_reset(user=user)
except ApiException as e:
    print("Exception when calling UserApi->request_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**InlineObject28**](InlineObject28.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

