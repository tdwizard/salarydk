# openapi_client.EmployeeContractsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_contract**](EmployeeContractsApi.md#create_employee_contract) | **POST** /v2/employeeContracts | 
[**create_leave_for_employee**](EmployeeContractsApi.md#create_leave_for_employee) | **POST** /v2/employees/{employeeID}/leave | 
[**delete_employee_contract**](EmployeeContractsApi.md#delete_employee_contract) | **DELETE** /v2/employeeContracts/{employeeContractID} | 
[**get_employee_contract**](EmployeeContractsApi.md#get_employee_contract) | **GET** /v2/employeeContracts/{employeeContractID} | 
[**get_employee_contracts**](EmployeeContractsApi.md#get_employee_contracts) | **GET** /v2/employeeContracts | 
[**remove_leave_for_employee_contract**](EmployeeContractsApi.md#remove_leave_for_employee_contract) | **DELETE** /v2/employeeContracts/{employeeContractID}/leave | 


# **create_employee_contract**
> InlineResponse2005 create_employee_contract(employee_contract)



Create new employee contract.

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
    api_instance = openapi_client.EmployeeContractsApi(api_client)
    employee_contract = openapi_client.EmployeeContract() # EmployeeContract | 

    try:
        api_response = api_instance.create_employee_contract(employee_contract)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeeContractsApi->create_employee_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_contract** | [**EmployeeContract**](EmployeeContract.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created employeeContract |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_leave_for_employee**
> InlineResponse2008 create_leave_for_employee(employee_id, leave_period)



Create leave for employee. `leaveFrom` and `leaveTo` will create a hole in the employee's contracts.  The contract valid at `leaveFrom` will have its `validTo` changed to `leaveFrom` - 1 day; and the contract valid at `leaveTo` will have its `validFrom` changed to `leaveTo` + 1 day.  Any contract in between will be deleted.  If any contract is immutable in the time provided, the call fails.  If the result would create two contracts in the same period, the call fails. See [remove leave endpoint](#operation/RemoveLeaveForEmployeeContract) to remove the leave again.

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
    api_instance = openapi_client.EmployeeContractsApi(api_client)
    employee_id = 'employee_id_example' # str | 
leave_period = openapi_client.InlineObject2() # InlineObject2 | 

    try:
        api_response = api_instance.create_leave_for_employee(employee_id, leave_period)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeeContractsApi->create_leave_for_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 
 **leave_period** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created leave |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | EmployeeContract not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_contract**
> delete_employee_contract(employee_contract_id)



Delete employeeContract on id.

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
    api_instance = openapi_client.EmployeeContractsApi(api_client)
    employee_contract_id = 'employee_contract_id_example' # str | 

    try:
        api_instance.delete_employee_contract(employee_contract_id)
    except ApiException as e:
        print("Exception when calling EmployeeContractsApi->delete_employee_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_contract_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | EmployeeContract deleted ok |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | EmployeeContract not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_contract**
> InlineResponse2005 get_employee_contract(employee_contract_id)



Get employeeContract by id

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
    api_instance = openapi_client.EmployeeContractsApi(api_client)
    employee_contract_id = 'employee_contract_id_example' # str | 

    try:
        api_response = api_instance.get_employee_contract(employee_contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeeContractsApi->get_employee_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_contract_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned employeeContract |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | EmployeeContract not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_contracts**
> InlineResponse2004 get_employee_contracts(company_id=company_id, employee_id=employee_id, employment_id=employment_id, employment_type=employment_type, limit=limit, offset=offset)



Get all employeeContracts filtered by companyID, employeeID or employmentID

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
    api_instance = openapi_client.EmployeeContractsApi(api_client)
    company_id = 'company_id_example' # str |  (optional)
employee_id = 'employee_id_example' # str |  (optional)
employment_id = 'employment_id_example' # str |  (optional)
employment_type = 'employment_type_example' # str |  (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        api_response = api_instance.get_employee_contracts(company_id=company_id, employee_id=employee_id, employment_id=employment_id, employment_type=employment_type, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeeContractsApi->get_employee_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | [optional] 
 **employee_id** | [**str**](.md)|  | [optional] 
 **employment_id** | [**str**](.md)|  | [optional] 
 **employment_type** | **str**|  | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned employeeContracts |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_leave_for_employee_contract**
> InlineResponse2005 remove_leave_for_employee_contract(employee_contract_id, leave_period=leave_period)



Removes a leave period that exists just before this contract. The given contract will be extended forwards to cover the removed leave period, or to `validTo` if provided (for contracts before leave period) or 'validFrom` (for contracts after leave period). See [create leave endpoint](#operation/CreateLeaveForEmployee) to create another leave.

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
    api_instance = openapi_client.EmployeeContractsApi(api_client)
    employee_contract_id = 'employee_contract_id_example' # str | 
leave_period = openapi_client.InlineObject1() # InlineObject1 |  (optional)

    try:
        api_response = api_instance.remove_leave_for_employee_contract(employee_contract_id, leave_period=leave_period)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeeContractsApi->remove_leave_for_employee_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_contract_id** | [**str**](.md)|  | 
 **leave_period** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated employeeContract |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | EmployeeContract not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

