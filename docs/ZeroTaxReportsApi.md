# salarydk.ZeroTaxReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_zero_tax_report**](ZeroTaxReportsApi.md#file_zero_tax_report) | **POST** /v2/zeroTaxReports | 


# **file_zero_tax_report**
> InlineResponse20062 file_zero_tax_report(zero_tax_report=zero_tax_report)



Perform a zero tax report for a given month

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
api_instance = salarydk.ZeroTaxReportsApi(salarydk.ApiClient(configuration))
zero_tax_report = salarydk.InlineObject48() # InlineObject48 |  (optional)

try:
    api_response = api_instance.file_zero_tax_report(zero_tax_report=zero_tax_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZeroTaxReportsApi->file_zero_tax_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zero_tax_report** | [**InlineObject48**](InlineObject48.md)|  | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

