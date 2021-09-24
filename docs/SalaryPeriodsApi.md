# openapi_client.SalaryPeriodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_salary_periods**](SalaryPeriodsApi.md#get_salary_periods) | **GET** /v2/salaryPeriods | List Salary Periods


# **get_salary_periods**
> InlineResponse20015 get_salary_periods(salary_cycle_id=salary_cycle_id, company_id=company_id, employee_id=employee_id, date=date, limit=limit, offset=offset)

List Salary Periods

Gets the list of salary periods, filtered by cycle.

### Example

* Api Key Authentication (authorizedUser):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authorizedUser
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SalaryPeriodsApi(api_client)
    salary_cycle_id = 'salary_cycle_id_example' # str | Required if `employeeID` not provided. (optional)
company_id = 'company_id_example' # str | If included, each period will have a disposition date and a flag telling if today is early enough to run a salary for it. (optional)
employee_id = 'employee_id_example' # str | Ignored if `salaryCycleID` is provided.  Finds the `salaryCycleID` matching the employee's current contract.  If `date` is also provided, it will use the `salaryCycleID` for the contract that was valid on that date. (optional)
date = '2013-10-20' # date | If included, will restrict the list of salary periods to the one that would include the given date. (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # List Salary Periods
        api_response = api_instance.get_salary_periods(salary_cycle_id=salary_cycle_id, company_id=company_id, employee_id=employee_id, date=date, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalaryPeriodsApi->get_salary_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salary_cycle_id** | [**str**](.md)| Required if &#x60;employeeID&#x60; not provided. | [optional] 
 **company_id** | [**str**](.md)| If included, each period will have a disposition date and a flag telling if today is early enough to run a salary for it. | [optional] 
 **employee_id** | [**str**](.md)| Ignored if &#x60;salaryCycleID&#x60; is provided.  Finds the &#x60;salaryCycleID&#x60; matching the employee&#39;s current contract.  If &#x60;date&#x60; is also provided, it will use the &#x60;salaryCycleID&#x60; for the contract that was valid on that date. | [optional] 
 **date** | **date**| If included, will restrict the list of salary periods to the one that would include the given date. | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The salary periods for the cycle are returned |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

