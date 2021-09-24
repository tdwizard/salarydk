# salarydk.IncomeTaxReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_income_tax_reply**](IncomeTaxReportsApi.md#create_income_tax_reply) | **POST** /v2/incomeTaxReportReplies | 
[**get_income_tax_reports**](IncomeTaxReportsApi.md#get_income_tax_reports) | **GET** /v2/incomeTaxReports | 


# **create_income_tax_reply**
> create_income_tax_reply(reply=reply)



Creates a reply from eIndkomst for testing purposes

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
api_instance = salarydk.IncomeTaxReportsApi(salarydk.ApiClient(configuration))
reply = salarydk.InlineObject25() # InlineObject25 |  (optional)

try:
    api_instance.create_income_tax_reply(reply=reply)
except ApiException as e:
    print("Exception when calling IncomeTaxReportsApi->create_income_tax_reply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply** | [**InlineObject25**](InlineObject25.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_tax_reports**
> InlineResponse20050 get_income_tax_reports(pay_roll_id)



Gets raw income tax report details for a pay roll.

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
api_instance = salarydk.IncomeTaxReportsApi(salarydk.ApiClient(configuration))
pay_roll_id = 'pay_roll_id_example' # str | 

try:
    api_response = api_instance.get_income_tax_reports(pay_roll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomeTaxReportsApi->get_income_tax_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_roll_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

