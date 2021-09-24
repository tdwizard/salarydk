# openapi_client.EmployeesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee**](EmployeesApi.md#create_employee) | **POST** /v2/employees | 
[**delete_employee**](EmployeesApi.md#delete_employee) | **DELETE** /v2/employees/{employeeID} | 
[**get_employee**](EmployeesApi.md#get_employee) | **GET** /v2/employees/{employeeID} | 
[**get_employees**](EmployeesApi.md#get_employees) | **GET** /v2/employees | List employees
[**set_employee_pdf_password**](EmployeesApi.md#set_employee_pdf_password) | **POST** /v2/employees/{employeeID}/pdfPassword | 
[**update_employee**](EmployeesApi.md#update_employee) | **PUT** /v2/employees/{employeeID} | 


# **create_employee**
> InlineResponse2007 create_employee(employee)



Create new employee.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    employee = openapi_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

    try:
        api_response = api_instance.create_employee(employee)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created employee |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee**
> delete_employee(employee_id)



Delete employee on id.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | 

    try:
        api_instance.delete_employee(employee_id)
    except ApiException as e:
        print("Exception when calling EmployeesApi->delete_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 

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
**204** | employee deleted ok |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | Employee not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> InlineResponse2007 get_employee(employee_id)



Get employee by id

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
    api_instance = openapi_client.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | 

    try:
        api_response = api_instance.get_employee(employee_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned employee |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | Employee not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees**
> InlineResponse2006 get_employees(company_id=company_id, employee_number=employee_number, national_id=national_id, national_id_type=national_id_type, include_remuneration=include_remuneration, limit=limit, offset=offset)

List employees

Get all employees. With no filter, all employees this user has direct access to is returned. Otherwise filtered by companyID.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    company_id = 'company_id_example' # str | Only list employees for the given company. (optional)
employee_number = 'employee_number_example' # str | List only employees by this employeeNumber. (optional)
national_id = 'national_id_example' # str | List only employees with this nationalID. (optional)
national_id_type = 'national_id_type_example' # str | Restrict nationalID by type (optional) (optional)
include_remuneration = True # bool | Include remuneration in the earliest contract (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # List employees
        api_response = api_instance.get_employees(company_id=company_id, employee_number=employee_number, national_id=national_id, national_id_type=national_id_type, include_remuneration=include_remuneration, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| Only list employees for the given company. | [optional] 
 **employee_number** | **str**| List only employees by this employeeNumber. | [optional] 
 **national_id** | **str**| List only employees with this nationalID. | [optional] 
 **national_id_type** | **str**| Restrict nationalID by type (optional) | [optional] 
 **include_remuneration** | **bool**| Include remuneration in the earliest contract | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned employees |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_employee_pdf_password**
> InlineResponse2007 set_employee_pdf_password(employee_id, pdf_password)



Set PDF Password for employee

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
    api_instance = openapi_client.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | 
pdf_password = openapi_client.InlineObject3() # InlineObject3 | 

    try:
        api_response = api_instance.set_employee_pdf_password(employee_id, pdf_password)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->set_employee_pdf_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 
 **pdf_password** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password updated |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | Employee not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee**
> InlineResponse2007 update_employee(employee_id, employee)



Updates employee on id.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | 
employee = openapi_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

    try:
        api_response = api_instance.update_employee(employee_id, employee)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->update_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 
 **employee** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated employee |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**404** | Employee not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

