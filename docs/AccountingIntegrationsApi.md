# salarydk.AccountingIntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_accounting_integration**](AccountingIntegrationsApi.md#delete_accounting_integration) | **DELETE** /v2/accountingIntegrations | 
[**get_account_plan**](AccountingIntegrationsApi.md#get_account_plan) | **GET** /v2/accountPlans | 
[**get_accounting_integration**](AccountingIntegrationsApi.md#get_accounting_integration) | **GET** /v2/accountingIntegrations | 
[**update_accounting_integration**](AccountingIntegrationsApi.md#update_accounting_integration) | **PUT** /v2/accountingIntegrations | 


# **delete_accounting_integration**
> delete_accounting_integration(company_id)



Deletes the accounting integration for a company

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
api_instance = salarydk.AccountingIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_instance.delete_accounting_integration(company_id)
except ApiException as e:
    print("Exception when calling AccountingIntegrationsApi->delete_accounting_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_plan**
> InlineResponse2002 get_account_plan(company_id, integration_type, api_key=api_key, username=username, password=password, organization_id=organization_id, daybook_id=daybook_id)



Gets the accounting plan from a 3rd party accounting system. This operation does not perform any database changes.

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
api_instance = salarydk.AccountingIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
integration_type = 'integration_type_example' # str | 
api_key = 'api_key_example' # str |  (optional)
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)
organization_id = 'organization_id_example' # str |  (optional)
daybook_id = 'daybook_id_example' # str |  (optional)

try:
    api_response = api_instance.get_account_plan(company_id, integration_type, api_key=api_key, username=username, password=password, organization_id=organization_id, daybook_id=daybook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingIntegrationsApi->get_account_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **integration_type** | **str**|  | 
 **api_key** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **organization_id** | **str**|  | [optional] 
 **daybook_id** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_integration**
> InlineResponse2003 get_accounting_integration(company_id)



Gets the accounting integration for a company

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
api_instance = salarydk.AccountingIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_accounting_integration(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingIntegrationsApi->get_accounting_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accounting_integration**
> InlineResponse2003 update_accounting_integration(company_id, accounting_integration)



Updates the accounting integration for a company

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
api_instance = salarydk.AccountingIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
accounting_integration = salarydk.AccountingIntegration() # AccountingIntegration | 

try:
    api_response = api_instance.update_accounting_integration(company_id, accounting_integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingIntegrationsApi->update_accounting_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **accounting_integration** | [**AccountingIntegration**](AccountingIntegration.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

