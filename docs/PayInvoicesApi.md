# salarydk.PayInvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pay_invoice**](PayInvoicesApi.md#get_pay_invoice) | **GET** /v2/payInvoices/{id} | 
[**get_pay_invoice_pdf**](PayInvoicesApi.md#get_pay_invoice_pdf) | **GET** /v2/payInvoicesPDF/{id} | 
[**get_pay_invoices**](PayInvoicesApi.md#get_pay_invoices) | **GET** /v2/payInvoices | 


# **get_pay_invoice**
> InlineResponse20060 get_pay_invoice(id)



Gets a single pay invoice

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
api_instance = salarydk.PayInvoicesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_pay_invoice(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInvoicesApi->get_pay_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_invoice_pdf**
> file get_pay_invoice_pdf(id, disposition=disposition)



get a pay invoice by id

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
api_instance = salarydk.PayInvoicesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
disposition = 'disposition_example' # str |  (optional)

try:
    api_response = api_instance.get_pay_invoice_pdf(id, disposition=disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInvoicesApi->get_pay_invoice_pdf: %s\n" % e)
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

# **get_pay_invoices**
> InlineResponse20059 get_pay_invoices(employee_id=employee_id, pay_roll_id=pay_roll_id)



Gets pay invoices as filtered

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
api_instance = salarydk.PayInvoicesApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)
pay_roll_id = 'pay_roll_id_example' # str |  (optional)

try:
    api_response = api_instance.get_pay_invoices(employee_id=employee_id, pay_roll_id=pay_roll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInvoicesApi->get_pay_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 
 **pay_roll_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

