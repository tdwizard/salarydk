# salarydk.CarAllowancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_car_allowances**](CarAllowancesApi.md#approve_car_allowances) | **PATCH** /v2/carAllowances | 
[**create_car_allowance**](CarAllowancesApi.md#create_car_allowance) | **POST** /v2/carAllowances | 
[**create_car_allowance21**](CarAllowancesApi.md#create_car_allowance21) | **POST** /v2.1/carAllowances | 
[**create_car_allowance22**](CarAllowancesApi.md#create_car_allowance22) | **POST** /v2.2/carAllowances | 
[**create_coarse_car_allowance**](CarAllowancesApi.md#create_coarse_car_allowance) | **POST** /v2/coarseCarAllowances | 
[**delete_car_allowance**](CarAllowancesApi.md#delete_car_allowance) | **DELETE** /v2/carAllowances/{id} | 
[**delete_coarse_car_allowance**](CarAllowancesApi.md#delete_coarse_car_allowance) | **DELETE** /v2/coarseCarAllowances/{id} | 
[**get_car_allowances**](CarAllowancesApi.md#get_car_allowances) | **GET** /v2/carAllowances | 
[**get_coarse_car_allowances**](CarAllowancesApi.md#get_coarse_car_allowances) | **GET** /v2/coarseCarAllowances | 
[**update_car_allowance**](CarAllowancesApi.md#update_car_allowance) | **PUT** /v2/carAllowances/{id} | 
[**update_coarse_car_allowance**](CarAllowancesApi.md#update_coarse_car_allowance) | **PUT** /v2/coarseCarAllowances/{id} | 


# **approve_car_allowances**
> InlineResponse200 approve_car_allowances(car_allowances)



Bulk approval of car allowances

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
car_allowances = NULL # list[str] | 

try:
    api_response = api_instance.approve_car_allowances(car_allowances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->approve_car_allowances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_allowances** | [**list[str]**](list.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_car_allowance**
> InlineResponse20013 create_car_allowance(car_allowance)



Create new car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
car_allowance = salarydk.CarAllowance() # CarAllowance | 

try:
    api_response = api_instance.create_car_allowance(car_allowance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->create_car_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_allowance** | [**CarAllowance**](CarAllowance.md)|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_car_allowance21**
> InlineResponse200 create_car_allowance21(car_allowance)



Create new car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
car_allowance = salarydk.CarAllowance() # CarAllowance | 

try:
    api_response = api_instance.create_car_allowance21(car_allowance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->create_car_allowance21: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_allowance** | [**CarAllowance**](CarAllowance.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_car_allowance22**
> InlineResponse200 create_car_allowance22(car_allowance)



Create new car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
car_allowance = NULL # list[CarAllowance] | 

try:
    api_response = api_instance.create_car_allowance22(car_allowance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->create_car_allowance22: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_allowance** | [**list[CarAllowance]**](list.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coarse_car_allowance**
> InlineResponse20016 create_coarse_car_allowance(coarse_car_allowance)



Create a coarse car allowance for a period

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
coarse_car_allowance = salarydk.CoarseCarAllowance() # CoarseCarAllowance | 

try:
    api_response = api_instance.create_coarse_car_allowance(coarse_car_allowance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->create_coarse_car_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coarse_car_allowance** | [**CoarseCarAllowance**](CoarseCarAllowance.md)|  | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_car_allowance**
> delete_car_allowance(id)



Delete a car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_car_allowance(id)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->delete_car_allowance: %s\n" % e)
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

# **delete_coarse_car_allowance**
> delete_coarse_car_allowance(id)



Deletes the coarse car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_coarse_car_allowance(id)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->delete_coarse_car_allowance: %s\n" % e)
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

# **get_car_allowances**
> InlineResponse200 get_car_allowances(employee_id=employee_id, company_id=company_id, _from=_from, to=to)



Gets all car allowances filtered by employeeID or companyID and time period

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.get_car_allowances(employee_id=employee_id, company_id=company_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->get_car_allowances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coarse_car_allowances**
> InlineResponse20015 get_coarse_car_allowances(pay_roll_id=pay_roll_id, employee_id=employee_id, company_id=company_id, salary_period_id=salary_period_id)



Get all coarse car allowances for an employeeID, payRollID or companyID+salaryPeriodID

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
pay_roll_id = 'pay_roll_id_example' # str |  (optional)
employee_id = 'employee_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)
salary_period_id = 'salary_period_id_example' # str | Period to obtain registrations for. Separate multiple by comma. (optional)

try:
    api_response = api_instance.get_coarse_car_allowances(pay_roll_id=pay_roll_id, employee_id=employee_id, company_id=company_id, salary_period_id=salary_period_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->get_coarse_car_allowances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_roll_id** | [**str**](.md)|  | [optional] 
 **employee_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 
 **salary_period_id** | **str**| Period to obtain registrations for. Separate multiple by comma. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_car_allowance**
> InlineResponse20013 update_car_allowance(id, car_allowance)



Update a car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
car_allowance = salarydk.CarAllowance() # CarAllowance | 

try:
    api_response = api_instance.update_car_allowance(id, car_allowance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->update_car_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **car_allowance** | [**CarAllowance**](CarAllowance.md)|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coarse_car_allowance**
> InlineResponse20016 update_coarse_car_allowance(id, coarse_car_allowance)



Updates the coarse car allowance

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
api_instance = salarydk.CarAllowancesApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
coarse_car_allowance = salarydk.CoarseCarAllowance() # CoarseCarAllowance | 

try:
    api_response = api_instance.update_coarse_car_allowance(id, coarse_car_allowance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarAllowancesApi->update_coarse_car_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **coarse_car_allowance** | [**CoarseCarAllowance**](CoarseCarAllowance.md)|  | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

