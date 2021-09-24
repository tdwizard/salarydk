# salarydk.ContractBookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_book_callback**](ContractBookApi.md#contract_book_callback) | **POST** /v2/companies/{companyID}/contractBookCallback | ContractBook callback handler
[**create_contract_book_draft**](ContractBookApi.md#create_contract_book_draft) | **POST** /v2/companies/{companyID}/contractBookDrafts | Create ContractBook draft
[**delete_contract_book_integration**](ContractBookApi.md#delete_contract_book_integration) | **DELETE** /v2/companies/{companyID}/contractBook | Remove a ContractBook integration
[**get_contract_book_contracts**](ContractBookApi.md#get_contract_book_contracts) | **GET** /v2/companies/{companyID}/contractBookContracts | List signed ContractBook contracts
[**get_contract_book_integration**](ContractBookApi.md#get_contract_book_integration) | **GET** /v2/companies/{companyID}/contractBook | Get ContractBook Integration
[**get_contract_book_templates**](ContractBookApi.md#get_contract_book_templates) | **GET** /v2/companies/{companyID}/contractBookTemplates | List ContractBook templates
[**update_contract_book_integration**](ContractBookApi.md#update_contract_book_integration) | **PUT** /v2/companies/{companyID}/contractBook | Update ContractBook Integration


# **contract_book_callback**
> contract_book_callback(company_id, token, param_callback=param_callback)

ContractBook callback handler

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.ContractBookApi()
company_id = 'company_id_example' # str | The company to set the integration for
token = 'token_example' # str | 
param_callback = salarydk.ContractBookCallback() # ContractBookCallback |  (optional)

try:
    # ContractBook callback handler
    api_instance.contract_book_callback(company_id, token, param_callback=param_callback)
except ApiException as e:
    print("Exception when calling ContractBookApi->contract_book_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to set the integration for | 
 **token** | [**str**](.md)|  | 
 **param_callback** | [**ContractBookCallback**](ContractBookCallback.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contract_book_draft**
> InlineResponse20024 create_contract_book_draft(company_id, draft=draft)

Create ContractBook draft

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
api_instance = salarydk.ContractBookApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get the templates for
draft = salarydk.InlineObject2() # InlineObject2 |  (optional)

try:
    # Create ContractBook draft
    api_response = api_instance.create_contract_book_draft(company_id, draft=draft)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractBookApi->create_contract_book_draft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get the templates for | 
 **draft** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract_book_integration**
> InlineResponse20022 delete_contract_book_integration(company_id)

Remove a ContractBook integration

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
api_instance = salarydk.ContractBookApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to set the integration for

try:
    # Remove a ContractBook integration
    api_response = api_instance.delete_contract_book_integration(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractBookApi->delete_contract_book_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to set the integration for | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_book_contracts**
> InlineResponse20023 get_contract_book_contracts(company_id)

List signed ContractBook contracts

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
api_instance = salarydk.ContractBookApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get the signed contracts for

try:
    # List signed ContractBook contracts
    api_response = api_instance.get_contract_book_contracts(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractBookApi->get_contract_book_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get the signed contracts for | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_book_integration**
> InlineResponse20022 get_contract_book_integration(company_id)

Get ContractBook Integration

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
api_instance = salarydk.ContractBookApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get the integration for

try:
    # Get ContractBook Integration
    api_response = api_instance.get_contract_book_integration(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractBookApi->get_contract_book_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get the integration for | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_book_templates**
> InlineResponse20025 get_contract_book_templates(company_id)

List ContractBook templates

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
api_instance = salarydk.ContractBookApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get the templates for

try:
    # List ContractBook templates
    api_response = api_instance.get_contract_book_templates(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractBookApi->get_contract_book_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get the templates for | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract_book_integration**
> InlineResponse20022 update_contract_book_integration(company_id, contract_book)

Update ContractBook Integration

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
api_instance = salarydk.ContractBookApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to set the integration for
contract_book = salarydk.ContractBookIntegration() # ContractBookIntegration | 

try:
    # Update ContractBook Integration
    api_response = api_instance.update_contract_book_integration(company_id, contract_book)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractBookApi->update_contract_book_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to set the integration for | 
 **contract_book** | [**ContractBookIntegration**](ContractBookIntegration.md)|  | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

