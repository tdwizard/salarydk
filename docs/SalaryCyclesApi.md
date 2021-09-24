# openapi_client.SalaryCyclesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_salary_cycles**](SalaryCyclesApi.md#get_salary_cycles) | **GET** /v2/salaryCycles | List Salary Cycles


# **get_salary_cycles**
> InlineResponse20014 get_salary_cycles(include_salary_periods=include_salary_periods, company_id=company_id, limit=limit, offset=offset)

List Salary Cycles

Gets the list of salary cycles

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
    api_instance = openapi_client.SalaryCyclesApi(api_client)
    include_salary_periods = True # bool | If true, all periods for each cycle will be returned. (optional)
company_id = 'company_id_example' # str | If included and `includeSalaryPeriods` is true, each period will have a disposition date and a flag telling if today is early enough to run a salary for it. (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # List Salary Cycles
        api_response = api_instance.get_salary_cycles(include_salary_periods=include_salary_periods, company_id=company_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalaryCyclesApi->get_salary_cycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_salary_periods** | **bool**| If true, all periods for each cycle will be returned. | [optional] 
 **company_id** | [**str**](.md)| If included and &#x60;includeSalaryPeriods&#x60; is true, each period will have a disposition date and a flag telling if today is early enough to run a salary for it. | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The salary cycles are returned. |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

