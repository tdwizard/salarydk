# salarydk.AccountingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounting_voucher_pdf**](AccountingApi.md#get_accounting_voucher_pdf) | **GET** /v2/accountingVoucherPDF/{id} | 


# **get_accounting_voucher_pdf**
> file get_accounting_voucher_pdf(id, disposition=disposition)



Gets an accounting voucher by id

### Example

* Api Key Authentication (authorizedUserQuery): 
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# Configure API key authorization: authorizedUserQuery
configuration = salarydk.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = salarydk.AccountingApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | The voucher ID
disposition = 'disposition_example' # str |  (optional)

try:
    api_response = api_instance.get_accounting_voucher_pdf(id, disposition=disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_accounting_voucher_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The voucher ID | 
 **disposition** | **str**|  | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

