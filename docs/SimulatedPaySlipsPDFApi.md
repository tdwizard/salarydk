# salarydk.SimulatedPaySlipsPDFApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simulate_pay_slip_pdf**](SimulatedPaySlipsPDFApi.md#simulate_pay_slip_pdf) | **GET** /v2/simulatedPaySlipsPDF | 


# **simulate_pay_slip_pdf**
> file simulate_pay_slip_pdf(employee_id, disposition=disposition)



simulate the next payslip for an employee

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
api_instance = salarydk.SimulatedPaySlipsPDFApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str | 
disposition = 'disposition_example' # str |  (optional)

try:
    api_response = api_instance.simulate_pay_slip_pdf(employee_id, disposition=disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulatedPaySlipsPDFApi->simulate_pay_slip_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 
 **disposition** | **str**|  | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

