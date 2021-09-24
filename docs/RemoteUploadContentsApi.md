# salarydk.RemoteUploadContentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_remote_upload_content**](RemoteUploadContentsApi.md#get_remote_upload_content) | **GET** /v2/remoteUploadContents/{id} | 


# **get_remote_upload_content**
> InlineResponse20068 get_remote_upload_content(id)



Get the content of a shipment

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
api_instance = salarydk.RemoteUploadContentsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_remote_upload_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteUploadContentsApi->get_remote_upload_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

