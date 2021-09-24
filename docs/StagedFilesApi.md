# salarydk.StagedFilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_staged_file**](StagedFilesApi.md#upload_staged_file) | **POST** /v2/stagedFiles | 


# **upload_staged_file**
> InlineResponse20077 upload_staged_file(file_data)



Upload a file to be referred in another request. The file will be removed after 5 minutes.

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
api_instance = salarydk.StagedFilesApi(salarydk.ApiClient(configuration))
file_data = '/path/to/file' # file | 

try:
    api_response = api_instance.upload_staged_file(file_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagedFilesApi->upload_staged_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_data** | **file**|  | 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

