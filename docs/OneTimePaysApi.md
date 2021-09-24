# salarydk.OneTimePaysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_one_time_pay**](OneTimePaysApi.md#create_one_time_pay) | **POST** /v2/oneTimePays | 
[**delete_one_time_pay**](OneTimePaysApi.md#delete_one_time_pay) | **DELETE** /v2/oneTimePays/{id} | 
[**get_one_time_pays**](OneTimePaysApi.md#get_one_time_pays) | **GET** /v2/oneTimePays | 
[**update_one_time_pay**](OneTimePaysApi.md#update_one_time_pay) | **PUT** /v2/oneTimePays/{id} | 


# **create_one_time_pay**
> InlineResponse20058 create_one_time_pay(one_time_pay)



Create a new one time pay

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
api_instance = salarydk.OneTimePaysApi(salarydk.ApiClient(configuration))
one_time_pay = salarydk.OneTimePay() # OneTimePay | 

try:
    api_response = api_instance.create_one_time_pay(one_time_pay)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneTimePaysApi->create_one_time_pay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **one_time_pay** | [**OneTimePay**](OneTimePay.md)|  | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_time_pay**
> delete_one_time_pay(id)



delete the one time pay

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
api_instance = salarydk.OneTimePaysApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_one_time_pay(id)
except ApiException as e:
    print("Exception when calling OneTimePaysApi->delete_one_time_pay: %s\n" % e)
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

# **get_one_time_pays**
> InlineResponse20057 get_one_time_pays(employee_id=employee_id, company_id=company_id)



Gets all one time pays, filtered by employeeID or companyID

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
api_instance = salarydk.OneTimePaysApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_one_time_pays(employee_id=employee_id, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneTimePaysApi->get_one_time_pays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_time_pay**
> InlineResponse20058 update_one_time_pay(id, one_time_pay)



update the one time pay

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
api_instance = salarydk.OneTimePaysApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
one_time_pay = salarydk.OneTimePay() # OneTimePay | 

try:
    api_response = api_instance.update_one_time_pay(id, one_time_pay)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneTimePaysApi->update_one_time_pay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **one_time_pay** | [**OneTimePay**](OneTimePay.md)|  | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

