# salarydk.EmployeeProfileImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_employee_profile_image**](EmployeeProfileImagesApi.md#delete_employee_profile_image) | **DELETE** /v2/employeeProfileImages/{employeeID} | 
[**get_employee_profile_image**](EmployeeProfileImagesApi.md#get_employee_profile_image) | **GET** /v2/profileImages/{id} | 
[**get_employee_profile_image_list**](EmployeeProfileImagesApi.md#get_employee_profile_image_list) | **GET** /v2/standardProfileImages | 
[**new_employee_standard_profile_image**](EmployeeProfileImagesApi.md#new_employee_standard_profile_image) | **POST** /v2/standardProfileImages | 
[**set_employee_profile_image**](EmployeeProfileImagesApi.md#set_employee_profile_image) | **PUT** /v2/employeeProfileImages/{employeeID} | 


# **delete_employee_profile_image**
> delete_employee_profile_image(employee_id)



Delete the employee profile image

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
api_instance = salarydk.EmployeeProfileImagesApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str | 

try:
    api_instance.delete_employee_profile_image(employee_id)
except ApiException as e:
    print("Exception when calling EmployeeProfileImagesApi->delete_employee_profile_image: %s\n" % e)
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

# **get_employee_profile_image**
> file get_employee_profile_image(id)



Gets a raw profile image

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.EmployeeProfileImagesApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_employee_profile_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeProfileImagesApi->get_employee_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_profile_image_list**
> InlineResponse20079 get_employee_profile_image_list()



Gets a list of standard employee profile images

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
api_instance = salarydk.EmployeeProfileImagesApi(salarydk.ApiClient(configuration))

try:
    api_response = api_instance.get_employee_profile_image_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeProfileImagesApi->get_employee_profile_image_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_employee_standard_profile_image**
> StandardProfileImage new_employee_standard_profile_image(image=image)



Create a new standard profile image (admin only)

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
api_instance = salarydk.EmployeeProfileImagesApi(salarydk.ApiClient(configuration))
image = salarydk.InlineObject34() # InlineObject34 |  (optional)

try:
    api_response = api_instance.new_employee_standard_profile_image(image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeProfileImagesApi->new_employee_standard_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**InlineObject34**](InlineObject34.md)|  | [optional] 

### Return type

[**StandardProfileImage**](StandardProfileImage.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_employee_profile_image**
> set_employee_profile_image(employee_id, image=image)



Set the employee profile image

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
api_instance = salarydk.EmployeeProfileImagesApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str | 
image = salarydk.InlineObject16() # InlineObject16 |  (optional)

try:
    api_instance.set_employee_profile_image(employee_id, image=image)
except ApiException as e:
    print("Exception when calling EmployeeProfileImagesApi->set_employee_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 
 **image** | [**InlineObject16**](InlineObject16.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

