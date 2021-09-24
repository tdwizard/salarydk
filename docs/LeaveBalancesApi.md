# salarydk.LeaveBalancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_leave_balances**](LeaveBalancesApi.md#get_leave_balances) | **GET** /v2/leaveBalances | 


# **get_leave_balances**
> InlineResponse20054 get_leave_balances(employee_id=employee_id, company_id=company_id)



Gets the leave balances for an employee or company

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
api_instance = salarydk.LeaveBalancesApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_leave_balances(employee_id=employee_id, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaveBalancesApi->get_leave_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

