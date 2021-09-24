# salarydk.UserProfileImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_profile_image**](UserProfileImagesApi.md#delete_user_profile_image) | **DELETE** /v2/userProfileImages/{userID} | 
[**set_user_profile_image**](UserProfileImagesApi.md#set_user_profile_image) | **PUT** /v2/userProfileImages/{userID} | 


# **delete_user_profile_image**
> delete_user_profile_image(user_id)



Delete the user profile image

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
api_instance = salarydk.UserProfileImagesApi(salarydk.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_instance.delete_user_profile_image(user_id)
except ApiException as e:
    print("Exception when calling UserProfileImagesApi->delete_user_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_profile_image**
> set_user_profile_image(user_id, image=image)



Set the user profile image

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
api_instance = salarydk.UserProfileImagesApi(salarydk.ApiClient(configuration))
user_id = 'user_id_example' # str | 
image = salarydk.InlineObject45() # InlineObject45 |  (optional)

try:
    api_instance.set_user_profile_image(user_id, image=image)
except ApiException as e:
    print("Exception when calling UserProfileImagesApi->set_user_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 
 **image** | [**InlineObject45**](InlineObject45.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

