# salarydk.StagedImportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_staged_import**](StagedImportsApi.md#apply_staged_import) | **POST** /v2/stagedImports/{id} | 
[**created_staged_import**](StagedImportsApi.md#created_staged_import) | **POST** /v2/stagedImports | 
[**import_from_other_system**](StagedImportsApi.md#import_from_other_system) | **POST** /v2/systemImport | 


# **apply_staged_import**
> apply_staged_import(id)



Applies the staged data

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
api_instance = salarydk.StagedImportsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.apply_staged_import(id)
except ApiException as e:
    print("Exception when calling StagedImportsApi->apply_staged_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **created_staged_import**
> InlineResponse20078 created_staged_import(import_data=import_data)



Stages an import from a file

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
api_instance = salarydk.StagedImportsApi(salarydk.ApiClient(configuration))
import_data = salarydk.InlineObject33() # InlineObject33 |  (optional)

try:
    api_response = api_instance.created_staged_import(import_data=import_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagedImportsApi->created_staged_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_data** | [**InlineObject33**](InlineObject33.md)|  | [optional] 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_from_other_system**
> InlineResponse20078 import_from_other_system(importdata=importdata)



Import from a traditional pay roll system

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
api_instance = salarydk.StagedImportsApi(salarydk.ApiClient(configuration))
importdata = salarydk.InlineObject36() # InlineObject36 |  (optional)

try:
    api_response = api_instance.import_from_other_system(importdata=importdata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagedImportsApi->import_from_other_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **importdata** | [**InlineObject36**](InlineObject36.md)|  | [optional] 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

