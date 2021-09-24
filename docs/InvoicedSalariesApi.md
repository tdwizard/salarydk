# salarydk.InvoicedSalariesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoiced_salary**](InvoicedSalariesApi.md#create_invoiced_salary) | **POST** /v2/invoicedSalary | 
[**delete_invoiced_salary**](InvoicedSalariesApi.md#delete_invoiced_salary) | **DELETE** /v2/invoicedSalary/{id} | 
[**get_invoiced_salaries**](InvoicedSalariesApi.md#get_invoiced_salaries) | **GET** /v2/invoicedSalary | 
[**update_invoiced_salary**](InvoicedSalariesApi.md#update_invoiced_salary) | **PUT** /v2/invoicedSalary/{id} | 


# **create_invoiced_salary**
> InlineResponse20052 create_invoiced_salary(invoiced_salary)



Create a new invoiced salary

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
api_instance = salarydk.InvoicedSalariesApi(salarydk.ApiClient(configuration))
invoiced_salary = salarydk.InvoicedSalary() # InvoicedSalary | 

try:
    api_response = api_instance.create_invoiced_salary(invoiced_salary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicedSalariesApi->create_invoiced_salary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoiced_salary** | [**InvoicedSalary**](InvoicedSalary.md)|  | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoiced_salary**
> delete_invoiced_salary(id)



delete the invoiced salary

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
api_instance = salarydk.InvoicedSalariesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_invoiced_salary(id)
except ApiException as e:
    print("Exception when calling InvoicedSalariesApi->delete_invoiced_salary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoiced_salaries**
> InlineResponse20051 get_invoiced_salaries(employee_id)



Gets all invoiced salaries, filtered by employeeID

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
api_instance = salarydk.InvoicedSalariesApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str | 

try:
    api_response = api_instance.get_invoiced_salaries(employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicedSalariesApi->get_invoiced_salaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoiced_salary**
> InlineResponse20052 update_invoiced_salary(id, invoiced_salary)



update the invoiced salary

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
api_instance = salarydk.InvoicedSalariesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
invoiced_salary = salarydk.InvoicedSalary() # InvoicedSalary | 

try:
    api_response = api_instance.update_invoiced_salary(id, invoiced_salary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicedSalariesApi->update_invoiced_salary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **invoiced_salary** | [**InvoicedSalary**](InvoicedSalary.md)|  | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

