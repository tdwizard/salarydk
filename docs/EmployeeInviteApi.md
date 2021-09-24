# salarydk.EmployeeInviteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_user**](EmployeeInviteApi.md#create_employee_user) | **POST** /v2/employeeInvite/{token} | 
[**delete_employee_user**](EmployeeInviteApi.md#delete_employee_user) | **DELETE** /v2/employeeUsers/{employeeID} | 
[**get_employee_invite_token**](EmployeeInviteApi.md#get_employee_invite_token) | **GET** /v2/employeeInvite/{token} | 
[**get_employee_users**](EmployeeInviteApi.md#get_employee_users) | **GET** /v2/employeeUsers/{employeeID} | 
[**send_employee_invite**](EmployeeInviteApi.md#send_employee_invite) | **POST** /v2/employeeInvite | 


# **create_employee_user**
> InlineResponse20010 create_employee_user(token, user=user)



Creates a new user based on a employee invitation token

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.EmployeeInviteApi()
token = 'token_example' # str | An employee invitation token
user = salarydk.InlineObject15() # InlineObject15 |  (optional)

try:
    api_response = api_instance.create_employee_user(token, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeInviteApi->create_employee_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**str**](.md)| An employee invitation token | 
 **user** | [**InlineObject15**](InlineObject15.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_user**
> delete_employee_user(employee_id)



Delete an employee user

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
api_instance = salarydk.EmployeeInviteApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str | 

try:
    api_instance.delete_employee_user(employee_id)
except ApiException as e:
    print("Exception when calling EmployeeInviteApi->delete_employee_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_invite_token**
> InlineResponse20041 get_employee_invite_token(token)



Get employee and company information for employee invitation token

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.EmployeeInviteApi()
token = 'token_example' # str | An employee invitation token

try:
    api_response = api_instance.get_employee_invite_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeInviteApi->get_employee_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**str**](.md)| An employee invitation token | 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_users**
> InlineResponse20042 get_employee_users(employee_id)



Get users for an employee

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
api_instance = salarydk.EmployeeInviteApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str | 

try:
    api_response = api_instance.get_employee_users(employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeInviteApi->get_employee_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_employee_invite**
> send_employee_invite(employee=employee)



Send invitation information to an employee

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
api_instance = salarydk.EmployeeInviteApi(salarydk.ApiClient(configuration))
employee = salarydk.InlineObject14() # InlineObject14 |  (optional)

try:
    api_instance.send_employee_invite(employee=employee)
except ApiException as e:
    print("Exception when calling EmployeeInviteApi->send_employee_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee** | [**InlineObject14**](InlineObject14.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

