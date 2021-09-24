# openapi_client.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_csv**](ReportsApi.md#get_report_csv) | **GET** /v2/reportCSV | 
[**get_report_excel**](ReportsApi.md#get_report_excel) | **GET** /v2/reportExcel | 


# **get_report_csv**
> get_report_csv(_from, to, type, company_id=company_id, company_group_id=company_group_id, pay_roll_id=pay_roll_id)



Generate a report as CSV. Specify the report type with `type`. Each report requires some extra parameters.  - Reports starting with `Period*` requires `from` and `to`. - Reports starting with `PayRoll*` requires `payRollID`. - `TimeRegistrations`, `LeaveRegistrations`, `Reimbursements`, `CarAllowance`, `LeaveBalances`, `SalaryAccountsMonthly*` requires `from` and `to`.  The generated report is returned directly as a CSV text file. Not all report types are implemented on this endpoint.  Note that this endpoints takes authorization as a query parameter instead of a header. [Details](#section/Authentication/authorizedUser) 

### Example

* Api Key Authentication (authorizedUserQuery):
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

# Configure API key authorization: authorizedUserQuery
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ReportsApi(api_client)
    _from = '2013-10-20' # date | Some reports requires a date span. This is the beginning of that span. The date is included in the span.
to = '2013-10-20' # date | Some reports requires a date span. This is the end of that span. The date is included in the span.
type = 'type_example' # str | The type of report to generate.
company_id = ['company_id_example'] # list[str] | The company to generate the report for.  Can take an array of company IDs, only available for `SalaryAccountsMonthlyFiltered1`, `PeriodEmployees`, `PeriodIncomeTaxReport`. (optional)
company_group_id = 'company_group_id_example' # str | The company group to generate the report for.  Only available for `SalaryAccountsMonthlyFiltered1`, `PeriodEmployees`, `PeriodIncomeTaxReport`. (optional)
pay_roll_id = 'pay_roll_id_example' # str | Some reports require a specific pay roll to include data for. This is that pay roll ID. (optional)

    try:
        api_instance.get_report_csv(_from, to, type, company_id=company_id, company_group_id=company_group_id, pay_roll_id=pay_roll_id)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_report_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Some reports requires a date span. This is the beginning of that span. The date is included in the span. | 
 **to** | **date**| Some reports requires a date span. This is the end of that span. The date is included in the span. | 
 **type** | **str**| The type of report to generate. | 
 **company_id** | [**list[str]**](str.md)| The company to generate the report for.  Can take an array of company IDs, only available for &#x60;SalaryAccountsMonthlyFiltered1&#x60;, &#x60;PeriodEmployees&#x60;, &#x60;PeriodIncomeTaxReport&#x60;. | [optional] 
 **company_group_id** | [**str**](.md)| The company group to generate the report for.  Only available for &#x60;SalaryAccountsMonthlyFiltered1&#x60;, &#x60;PeriodEmployees&#x60;, &#x60;PeriodIncomeTaxReport&#x60;. | [optional] 
 **pay_roll_id** | [**str**](.md)| Some reports require a specific pay roll to include data for. This is that pay roll ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned CSV of report, as a textual file. |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_excel**
> file get_report_excel(_from, to, type, company_id=company_id, company_group_id=company_group_id, pay_roll_id=pay_roll_id)



Generate a report as Excel. Specify the report type with `type`. Each report requires some extra parameters.  - Reports starting with `Period*` requires `from` and `to`. - Reports starting with `PayRoll*` requires `payRollID`. - `TimeRegistrations`, `LeaveRegistrations`, `Reimbursements`, `CarAllowance`, `LeaveBalances`, `SalaryAccountsMonthly*` requires `from` and `to`.  The generated report is returned directly as a Excel binary file.  Note that this endpoints takes authorization as a query parameter instead of a header. [Details](#section/Authentication/authorizedUser) 

### Example

* Api Key Authentication (authorizedUserQuery):
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

# Configure API key authorization: authorizedUserQuery
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ReportsApi(api_client)
    _from = '2013-10-20' # date | Some reports requires a date span. This is the beginning of that span. The date is included in the span.
to = '2013-10-20' # date | Some reports requires a date span. This is the end of that span. The date is included in the span.
type = 'type_example' # str | The type of report to generate.
company_id = ['company_id_example'] # list[str] | The company to generate the report for.  Can take an array of company IDs, only available for `SalaryAccountsMonthlyFiltered1`, `PeriodEmployees`, `PeriodIncomeTaxReport`. (optional)
company_group_id = 'company_group_id_example' # str | The company group to generate the report for.  Only available for `SalaryAccountsMonthlyFiltered1`, `PeriodEmployees`, `PeriodIncomeTaxReport`. (optional)
pay_roll_id = 'pay_roll_id_example' # str | Some reports require a specific pay roll to include data for. This is that pay roll ID. (optional)

    try:
        api_response = api_instance.get_report_excel(_from, to, type, company_id=company_id, company_group_id=company_group_id, pay_roll_id=pay_roll_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_report_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Some reports requires a date span. This is the beginning of that span. The date is included in the span. | 
 **to** | **date**| Some reports requires a date span. This is the end of that span. The date is included in the span. | 
 **type** | **str**| The type of report to generate. | 
 **company_id** | [**list[str]**](str.md)| The company to generate the report for.  Can take an array of company IDs, only available for &#x60;SalaryAccountsMonthlyFiltered1&#x60;, &#x60;PeriodEmployees&#x60;, &#x60;PeriodIncomeTaxReport&#x60;. | [optional] 
 **company_group_id** | [**str**](.md)| The company group to generate the report for.  Only available for &#x60;SalaryAccountsMonthlyFiltered1&#x60;, &#x60;PeriodEmployees&#x60;, &#x60;PeriodIncomeTaxReport&#x60;. | [optional] 
 **pay_roll_id** | [**str**](.md)| Some reports require a specific pay roll to include data for. This is that pay roll ID. | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Excel of report, as a binary file. |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

