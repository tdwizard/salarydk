# salarydk.PayRollsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pay_roll**](PayRollsApi.md#get_pay_roll) | **GET** /v2/payRolls/{id} | 
[**get_pay_rolls**](PayRollsApi.md#get_pay_rolls) | **GET** /v2/payRolls | 
[**patch_pay_roll**](PayRollsApi.md#patch_pay_roll) | **PATCH** /v2/payRolls/{id} | 
[**start_pay_roll**](PayRollsApi.md#start_pay_roll) | **POST** /v2/payRolls | 


# **get_pay_roll**
> InlineResponse20062 get_pay_roll(id)



Get a pay roll by id

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
api_instance = salarydk.PayRollsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_pay_roll(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayRollsApi->get_pay_roll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_rolls**
> InlineResponse20061 get_pay_rolls(company_id, _from, to)



Get a all pay rolls, filtered

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
api_instance = salarydk.PayRollsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
_from = '2013-10-20' # date | 
to = '2013-10-20' # date | 

try:
    api_response = api_instance.get_pay_rolls(company_id, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayRollsApi->get_pay_rolls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **_from** | **date**|  | 
 **to** | **date**|  | 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pay_roll**
> patch_pay_roll(id, operation=operation)



Performs an operation on a pay roll

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
api_instance = salarydk.PayRollsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
operation = salarydk.InlineObject30() # InlineObject30 |  (optional)

try:
    api_instance.patch_pay_roll(id, operation=operation)
except ApiException as e:
    print("Exception when calling PayRollsApi->patch_pay_roll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **operation** | [**InlineObject30**](InlineObject30.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_pay_roll**
> InlineResponse20062 start_pay_roll(pay_roll)



Manually start a payroll for a company for a salary period.

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
api_instance = salarydk.PayRollsApi(salarydk.ApiClient(configuration))
pay_roll = salarydk.StartPayRoll() # StartPayRoll | 

try:
    api_response = api_instance.start_pay_roll(pay_roll)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayRollsApi->start_pay_roll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_roll** | [**StartPayRoll**](StartPayRoll.md)|  | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

