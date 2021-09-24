# salarydk.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_pdf**](InvoicesApi.md#get_invoice_pdf) | **GET** /v2/invoicesPDF/{id} | 
[**get_invoices**](InvoicesApi.md#get_invoices) | **GET** /v2/invoices | 


# **get_invoice_pdf**
> file get_invoice_pdf(id, disposition=disposition)



get a invoice by id

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
api_instance = salarydk.InvoicesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
disposition = 'disposition_example' # str |  (optional)

try:
    api_response = api_instance.get_invoice_pdf(id, disposition=disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **disposition** | **str**|  | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> InlineResponse20053 get_invoices(company_id=company_id, pay_roll_id=pay_roll_id)



Gets all invoices, filtered by companyID or payRollID

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
api_instance = salarydk.InvoicesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str |  (optional)
pay_roll_id = 'pay_roll_id_example' # str |  (optional)

try:
    api_response = api_instance.get_invoices(company_id=company_id, pay_roll_id=pay_roll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | [optional] 
 **pay_roll_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

