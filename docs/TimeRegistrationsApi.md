# openapi_client.TimeRegistrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coarse_time_registration**](TimeRegistrationsApi.md#create_coarse_time_registration) | **POST** /v2/coarseTimeRegistrations | Create Coarse Time Registration
[**create_time_registration**](TimeRegistrationsApi.md#create_time_registration) | **POST** /v2/timeRegistrations | Create Time Registration
[**delete_coarse_time_registration**](TimeRegistrationsApi.md#delete_coarse_time_registration) | **DELETE** /v2/coarseTimeRegistrations/{id} | Delete Coarse Time Registration
[**delete_time_registration**](TimeRegistrationsApi.md#delete_time_registration) | **DELETE** /v2/timeRegistrations/{id} | Delete Time Registration
[**get_coarse_time_registrations**](TimeRegistrationsApi.md#get_coarse_time_registrations) | **GET** /v2/coarseTimeRegistrations | List Coarse Time Registrations
[**get_time_registrations**](TimeRegistrationsApi.md#get_time_registrations) | **GET** /v2/timeRegistrations | List Time Registrations
[**update_coarse_time_registration**](TimeRegistrationsApi.md#update_coarse_time_registration) | **PUT** /v2/coarseTimeRegistrations/{id} | Update Coarse Time Registration
[**update_time_registration**](TimeRegistrationsApi.md#update_time_registration) | **PUT** /v2/timeRegistrations/{id} | Update Time Registration


# **create_coarse_time_registration**
> InlineResponse2002 create_coarse_time_registration(coarse_time_registration)

Create Coarse Time Registration

Create a coarse time registration for a period.

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    coarse_time_registration = openapi_client.CoarseTimeRegistration() # CoarseTimeRegistration | 

    try:
        # Create Coarse Time Registration
        api_response = api_instance.create_coarse_time_registration(coarse_time_registration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->create_coarse_time_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coarse_time_registration** | [**CoarseTimeRegistration**](CoarseTimeRegistration.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The coarse time registrations was created |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_registration**
> InlineResponse20018 create_time_registration(time_registration)

Create Time Registration

Creates a new time registration for an employee.

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    time_registration = openapi_client.TimeRegistration() # TimeRegistration | The new time registration to create.

    try:
        # Create Time Registration
        api_response = api_instance.create_time_registration(time_registration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->create_time_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_registration** | [**TimeRegistration**](TimeRegistration.md)| The new time registration to create. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time registrations was created |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coarse_time_registration**
> delete_coarse_time_registration(id)

Delete Coarse Time Registration

Delete an existing coarse time registration

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    id = 'id_example' # str | The ID of the coarse time registration to delete.

    try:
        # Delete Coarse Time Registration
        api_instance.delete_coarse_time_registration(id)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->delete_coarse_time_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the coarse time registration to delete. | 

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
**204** | The coarse time registration was deleted |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_registration**
> delete_time_registration(id)

Delete Time Registration

Delete a single, existing time registration.

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    id = 'id_example' # str | The ID of the time registration to delete.

    try:
        # Delete Time Registration
        api_instance.delete_time_registration(id)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->delete_time_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the time registration to delete. | 

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
**204** | The time registrations was deleted |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coarse_time_registrations**
> InlineResponse2001 get_coarse_time_registrations(pay_roll_id=pay_roll_id, employee_id=employee_id, salary_period_id=salary_period_id, company_id=company_id, limit=limit, offset=offset)

List Coarse Time Registrations

Get all coarse time registrations with the requested filter. You must provide one of the following sets of parameters:  * `employeeID` * `payRollID` * `salaryPeriodID`, `companyID` 

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    pay_roll_id = 'pay_roll_id_example' # str | The pay roll to list coarse time registrations for. (optional)
employee_id = 'employee_id_example' # str | The employee to list coarse time registrations for. (optional)
salary_period_id = 'salary_period_id_example' # str | The salary period to list coarse time registrations for. (optional)
company_id = 'company_id_example' # str | The company to list coarse time registrations for. (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # List Coarse Time Registrations
        api_response = api_instance.get_coarse_time_registrations(pay_roll_id=pay_roll_id, employee_id=employee_id, salary_period_id=salary_period_id, company_id=company_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->get_coarse_time_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_roll_id** | [**str**](.md)| The pay roll to list coarse time registrations for. | [optional] 
 **employee_id** | [**str**](.md)| The employee to list coarse time registrations for. | [optional] 
 **salary_period_id** | [**str**](.md)| The salary period to list coarse time registrations for. | [optional] 
 **company_id** | [**str**](.md)| The company to list coarse time registrations for. | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The coarse time registrations |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_registrations**
> InlineResponse20017 get_time_registrations(employee_id=employee_id, company_id=company_id, pay_roll_id=pay_roll_id, _from=_from, to=to, state_filter=state_filter, limit=limit, offset=offset)

List Time Registrations

Get all time registrations, filtered by companyID, employeeID, payRollID and/or time period. You must provide one of the following sets of parameters:  * `companyID`, `from`, `to` * `employeeID`, `from`, `to` * `payRollID` 

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    employee_id = 'employee_id_example' # str | The employee to list time registrations for. (optional)
company_id = 'company_id_example' # str | The company to list time registrations for. (optional)
pay_roll_id = 'pay_roll_id_example' # str | The pay roll to list time registrations for. (optional)
_from = '2013-10-20' # date | The earliest date to filter returned time registrations. (optional)
to = '2013-10-20' # date | The latest date to filter returned time registrations. (optional)
state_filter = 'state_filter_example' # str | Only return those that match this `state`. (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # List Time Registrations
        api_response = api_instance.get_time_registrations(employee_id=employee_id, company_id=company_id, pay_roll_id=pay_roll_id, _from=_from, to=to, state_filter=state_filter, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->get_time_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)| The employee to list time registrations for. | [optional] 
 **company_id** | [**str**](.md)| The company to list time registrations for. | [optional] 
 **pay_roll_id** | [**str**](.md)| The pay roll to list time registrations for. | [optional] 
 **_from** | **date**| The earliest date to filter returned time registrations. | [optional] 
 **to** | **date**| The latest date to filter returned time registrations. | [optional] 
 **state_filter** | **str**| Only return those that match this &#x60;state&#x60;. | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time registrations |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coarse_time_registration**
> InlineResponse2002 update_coarse_time_registration(id, coarse_time_registration)

Update Coarse Time Registration

Update an existing coarse time registration

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    id = 'id_example' # str | The ID of the coarse time registration to update.
coarse_time_registration = openapi_client.CoarseTimeRegistration() # CoarseTimeRegistration | 

    try:
        # Update Coarse Time Registration
        api_response = api_instance.update_coarse_time_registration(id, coarse_time_registration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->update_coarse_time_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the coarse time registration to update. | 
 **coarse_time_registration** | [**CoarseTimeRegistration**](CoarseTimeRegistration.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The coarse time registrations was updated |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_registration**
> InlineResponse20018 update_time_registration(id, time_registration)

Update Time Registration

Update a single, existing time registration.

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
    api_instance = openapi_client.TimeRegistrationsApi(api_client)
    id = 'id_example' # str | The ID of the time registration to update
time_registration = openapi_client.TimeRegistration() # TimeRegistration | 

    try:
        # Update Time Registration
        api_response = api_instance.update_time_registration(id, time_registration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeRegistrationsApi->update_time_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the time registration to update | 
 **time_registration** | [**TimeRegistration**](TimeRegistration.md)|  | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time registrations was updated |  -  |
**401** | Wrong credentials |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

