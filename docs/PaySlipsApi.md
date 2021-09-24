# openapi_client.PaySlipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pay_slip**](PaySlipsApi.md#get_pay_slip) | **GET** /v2/paySlips/{id} | Get Pay Slip
[**get_pay_slip_pdf**](PaySlipsApi.md#get_pay_slip_pdf) | **GET** /v2/paySlipsPDF/{id} | Get Pay Slip as PDF
[**get_pay_slips**](PaySlipsApi.md#get_pay_slips) | **GET** /v2/paySlips | Get Pay Slips
[**get_pay_slips_pdf**](PaySlipsApi.md#get_pay_slips_pdf) | **GET** /v2/paySlipsPDF | Get Pay Slips as PDF
[**get_pay_slips_zip**](PaySlipsApi.md#get_pay_slips_zip) | **GET** /v2/paySlipsZip | Get Pay Slips as .zip


# **get_pay_slip**
> InlineResponse20013 get_pay_slip(id)

Get Pay Slip

Gets data for a single pay slip.

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
    api_instance = openapi_client.PaySlipsApi(api_client)
    id = 'id_example' # str | The ID of the pay slip to get.

    try:
        # Get Pay Slip
        api_response = api_instance.get_pay_slip(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaySlipsApi->get_pay_slip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the pay slip to get. | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returned payslip |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slip_pdf**
> file get_pay_slip_pdf(id, disposition=disposition)

Get Pay Slip as PDF

Get a pay slip as PDF.  Note that this endpoints takes authorization as a query parameter instead of a header. [Details](#section/Authentication/authorizedUser) 

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
    api_instance = openapi_client.PaySlipsApi(api_client)
    id = 'id_example' # str | The ID of the pay slip to get.
disposition = 'disposition_example' # str | How to return the payslip. Directly affects the `Content-Disposition` header in the response. Can be used to direct a browser to either download or display the file directly. (optional)

    try:
        # Get Pay Slip as PDF
        api_response = api_instance.get_pay_slip_pdf(id, disposition=disposition)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaySlipsApi->get_pay_slip_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the pay slip to get. | 
 **disposition** | **str**| How to return the payslip. Directly affects the &#x60;Content-Disposition&#x60; header in the response. Can be used to direct a browser to either download or display the file directly. | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned pay slip as binary PDF. |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slips**
> InlineResponse20012 get_pay_slips(employee_id=employee_id, pay_roll_id=pay_roll_id, limit=limit, offset=offset)

Get Pay Slips

Gets a list of pay slips for either an employee or a pay roll.

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
    api_instance = openapi_client.PaySlipsApi(api_client)
    employee_id = 'employee_id_example' # str | The employee to get a list of pay slips for. (optional)
pay_roll_id = 'pay_roll_id_example' # str | The pay roll to get a list of pay slips for. (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # Get Pay Slips
        api_response = api_instance.get_pay_slips(employee_id=employee_id, pay_roll_id=pay_roll_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaySlipsApi->get_pay_slips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)| The employee to get a list of pay slips for. | [optional] 
 **pay_roll_id** | [**str**](.md)| The pay roll to get a list of pay slips for. | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned pay slips. |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slips_pdf**
> file get_pay_slips_pdf(employee_id=employee_id, pay_roll_id=pay_roll_id, disposition=disposition)

Get Pay Slips as PDF

Gets all payslips as one long PDF. Either `employeeID` or `payRollID` is required.  Note that this endpoints takes authorization as a query parameter instead of a header. [Details](#section/Authentication/authorizedUser) 

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
    api_instance = openapi_client.PaySlipsApi(api_client)
    employee_id = 'employee_id_example' # str | The employee to obtain pay slips for. (optional)
pay_roll_id = 'pay_roll_id_example' # str | The pay roll to obtain pay slips for. (optional)
disposition = 'disposition_example' # str | How to return the file. Directly affects the `Content-Disposition` header in the response. Can be used to direct a browser to either download or display the file directly. (optional)

    try:
        # Get Pay Slips as PDF
        api_response = api_instance.get_pay_slips_pdf(employee_id=employee_id, pay_roll_id=pay_roll_id, disposition=disposition)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaySlipsApi->get_pay_slips_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)| The employee to obtain pay slips for. | [optional] 
 **pay_roll_id** | [**str**](.md)| The pay roll to obtain pay slips for. | [optional] 
 **disposition** | **str**| How to return the file. Directly affects the &#x60;Content-Disposition&#x60; header in the response. Can be used to direct a browser to either download or display the file directly. | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned pay slips as a single PDF |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slips_zip**
> file get_pay_slips_zip(employee_id=employee_id, pay_roll_id=pay_roll_id, disposition=disposition)

Get Pay Slips as .zip

Gets all payslips in one zip-file. Either `employeeID` or `payRollID` is required.  Note that this endpoints takes authorization as a query parameter instead of a header. [Details](#section/Authentication/authorizedUser) 

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
    api_instance = openapi_client.PaySlipsApi(api_client)
    employee_id = 'employee_id_example' # str | The employee to obtain pay slips for. (optional)
pay_roll_id = 'pay_roll_id_example' # str | The pay roll to obtain pay slips for. (optional)
disposition = 'disposition_example' # str | How to return the file. Directly affects the `Content-Disposition` header in the response. Can be used to direct a browser to either download or display the file directly. (optional)

    try:
        # Get Pay Slips as .zip
        api_response = api_instance.get_pay_slips_zip(employee_id=employee_id, pay_roll_id=pay_roll_id, disposition=disposition)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaySlipsApi->get_pay_slips_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)| The employee to obtain pay slips for. | [optional] 
 **pay_roll_id** | [**str**](.md)| The pay roll to obtain pay slips for. | [optional] 
 **disposition** | **str**| How to return the file. Directly affects the &#x60;Content-Disposition&#x60; header in the response. Can be used to direct a browser to either download or display the file directly. | [optional] 

### Return type

**file**

### Authorization

[authorizedUserQuery](../README.md#authorizedUserQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned pay slips as PDFs in a .zip file. |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

