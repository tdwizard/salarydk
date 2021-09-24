# salarydk.RemoteUploadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_remote_uploads**](RemoteUploadsApi.md#get_remote_uploads) | **GET** /v2/remoteUploads | 
[**patch_remote_upload**](RemoteUploadsApi.md#patch_remote_upload) | **PATCH** /v2/remoteUploads/{id} | 


# **get_remote_uploads**
> InlineResponse20069 get_remote_uploads(approval_status)



Get all remote uploads, filtered by status

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
api_instance = salarydk.RemoteUploadsApi(salarydk.ApiClient(configuration))
approval_status = 'approval_status_example' # str | 

try:
    api_response = api_instance.get_remote_uploads(approval_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteUploadsApi->get_remote_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_status** | **str**|  | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_remote_upload**
> patch_remote_upload(id, operation)



Alters the state of a remote upload

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
api_instance = salarydk.RemoteUploadsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
operation = 'operation_example' # str | 

try:
    api_instance.patch_remote_upload(id, operation)
except ApiException as e:
    print("Exception when calling RemoteUploadsApi->patch_remote_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **operation** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

