# salarydk.CompanyUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_company**](CompanyUsersApi.md#delete_user_company) | **DELETE** /v2/companyUsers | 
[**get_company_users**](CompanyUsersApi.md#get_company_users) | **GET** /v2/companyUsers | 
[**grant_company_user_permission**](CompanyUsersApi.md#grant_company_user_permission) | **POST** /v2/userCompanyPermissions | 
[**revoke_company_user_permission**](CompanyUsersApi.md#revoke_company_user_permission) | **DELETE** /v2/userCompanyPermissions/{permissionID} | 


# **delete_user_company**
> delete_user_company(user_id, company_id)



Remove user access for company

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
api_instance = salarydk.CompanyUsersApi(salarydk.ApiClient(configuration))
user_id = 'user_id_example' # str | 
company_id = 'company_id_example' # str | 

try:
    api_instance.delete_user_company(user_id, company_id)
except ApiException as e:
    print("Exception when calling CompanyUsersApi->delete_user_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 
 **company_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_users**
> InlineResponse20031 get_company_users(company_id=company_id, user_id=user_id)



Get all users with access to this company

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
api_instance = salarydk.CompanyUsersApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get user list for. (optional)
user_id = 'user_id_example' # str | The user to get companies for. Admin only. (optional)

try:
    api_response = api_instance.get_company_users(company_id=company_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyUsersApi->get_company_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get user list for. | [optional] 
 **user_id** | [**str**](.md)| The user to get companies for. Admin only. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_company_user_permission**
> InlineResponse20093 grant_company_user_permission(user_company_id, permission=permission)



Grant a new permission to a user

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
api_instance = salarydk.CompanyUsersApi(salarydk.ApiClient(configuration))
user_company_id = 'user_company_id_example' # str | The user company access to grant permissions
permission = salarydk.InlineObject42() # InlineObject42 |  (optional)

try:
    api_response = api_instance.grant_company_user_permission(user_company_id, permission=permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyUsersApi->grant_company_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_company_id** | [**str**](.md)| The user company access to grant permissions | 
 **permission** | [**InlineObject42**](InlineObject42.md)|  | [optional] 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_company_user_permission**
> revoke_company_user_permission(permission_id)



Revoke a permission

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
api_instance = salarydk.CompanyUsersApi(salarydk.ApiClient(configuration))
permission_id = 'permission_id_example' # str | The permission to revoke

try:
    api_instance.revoke_company_user_permission(permission_id)
except ApiException as e:
    print("Exception when calling CompanyUsersApi->revoke_company_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | [**str**](.md)| The permission to revoke | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

