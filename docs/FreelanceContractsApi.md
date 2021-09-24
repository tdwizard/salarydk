# salarydk.FreelanceContractsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_freelance_contract**](FreelanceContractsApi.md#create_freelance_contract) | **POST** /v2/freelanceContracts | 
[**delete_freelance_contract**](FreelanceContractsApi.md#delete_freelance_contract) | **DELETE** /v2/freelanceContracts/{id} | 
[**get_freelance_contract**](FreelanceContractsApi.md#get_freelance_contract) | **GET** /v2/freelanceContracts/{id} | 
[**get_freelance_contracts**](FreelanceContractsApi.md#get_freelance_contracts) | **GET** /v2/freelanceContracts | 
[**terminate_freelance_contract**](FreelanceContractsApi.md#terminate_freelance_contract) | **PATCH** /v2/freelanceContracts/{id} | 
[**update_freelance_contract**](FreelanceContractsApi.md#update_freelance_contract) | **PUT** /v2/freelanceContracts/{id} | 


# **create_freelance_contract**
> InlineResponse20049 create_freelance_contract(freelance_contract=freelance_contract)



Create new freelance contract.

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
api_instance = salarydk.FreelanceContractsApi(salarydk.ApiClient(configuration))
freelance_contract = salarydk.InlineObject22() # InlineObject22 |  (optional)

try:
    api_response = api_instance.create_freelance_contract(freelance_contract=freelance_contract)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreelanceContractsApi->create_freelance_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **freelance_contract** | [**InlineObject22**](InlineObject22.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_freelance_contract**
> delete_freelance_contract(id)



Delete freelance contract on id.

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
api_instance = salarydk.FreelanceContractsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_freelance_contract(id)
except ApiException as e:
    print("Exception when calling FreelanceContractsApi->delete_freelance_contract: %s\n" % e)
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

# **get_freelance_contract**
> InlineResponse20049 get_freelance_contract(id)



Get freelance contract by id

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
api_instance = salarydk.FreelanceContractsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_freelance_contract(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreelanceContractsApi->get_freelance_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_freelance_contracts**
> InlineResponse20048 get_freelance_contracts(employee_id=employee_id, company_id=company_id)



Get all freelance contracts filtered by employeeID or companyID

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
api_instance = salarydk.FreelanceContractsApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_freelance_contracts(employee_id=employee_id, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreelanceContractsApi->get_freelance_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_freelance_contract**
> InlineResponse20049 terminate_freelance_contract(id, freelance_contract=freelance_contract)



Terminate freelance contract on id.

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
api_instance = salarydk.FreelanceContractsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
freelance_contract = salarydk.InlineObject24() # InlineObject24 |  (optional)

try:
    api_response = api_instance.terminate_freelance_contract(id, freelance_contract=freelance_contract)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreelanceContractsApi->terminate_freelance_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **freelance_contract** | [**InlineObject24**](InlineObject24.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_freelance_contract**
> InlineResponse20049 update_freelance_contract(id, freelance_contract=freelance_contract)



Updates freelance contract on id.

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
api_instance = salarydk.FreelanceContractsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
freelance_contract = salarydk.InlineObject23() # InlineObject23 |  (optional)

try:
    api_response = api_instance.update_freelance_contract(id, freelance_contract=freelance_contract)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreelanceContractsApi->update_freelance_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **freelance_contract** | [**InlineObject23**](InlineObject23.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

