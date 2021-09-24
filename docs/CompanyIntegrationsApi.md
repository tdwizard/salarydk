# salarydk.CompanyIntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company_integration**](CompanyIntegrationsApi.md#create_company_integration) | **POST** /v2/companies/{companyID}/integrations | Create Company Integration
[**delete_company_integration**](CompanyIntegrationsApi.md#delete_company_integration) | **DELETE** /v2/companies/{companyID}/integrations/{companyIntegrationID} | Delete Company Integration
[**get_company_integration**](CompanyIntegrationsApi.md#get_company_integration) | **GET** /v2/companies/{companyID}/integrations/{companyIntegrationID} | Get Company Integration
[**get_company_integrations**](CompanyIntegrationsApi.md#get_company_integrations) | **GET** /v2/companies/{companyID}/integrations | Get Company Integrations


# **create_company_integration**
> InlineResponse20027 create_company_integration(company_id, company_integration)

Create Company Integration

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
api_instance = salarydk.CompanyIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to set the integration for
company_integration = salarydk.CompanyIntegration() # CompanyIntegration | 

try:
    # Create Company Integration
    api_response = api_instance.create_company_integration(company_id, company_integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyIntegrationsApi->create_company_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to set the integration for | 
 **company_integration** | [**CompanyIntegration**](CompanyIntegration.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_integration**
> delete_company_integration(company_id, company_integration_id)

Delete Company Integration

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
api_instance = salarydk.CompanyIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to set the integration for
company_integration_id = 'company_integration_id_example' # str | The company integration ID

try:
    # Delete Company Integration
    api_instance.delete_company_integration(company_id, company_integration_id)
except ApiException as e:
    print("Exception when calling CompanyIntegrationsApi->delete_company_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to set the integration for | 
 **company_integration_id** | [**str**](.md)| The company integration ID | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_integration**
> InlineResponse20027 get_company_integration(company_id, company_integration_id)

Get Company Integration

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
api_instance = salarydk.CompanyIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get the integration for
company_integration_id = 'company_integration_id_example' # str | The company integration ID

try:
    # Get Company Integration
    api_response = api_instance.get_company_integration(company_id, company_integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyIntegrationsApi->get_company_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get the integration for | 
 **company_integration_id** | [**str**](.md)| The company integration ID | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_integrations**
> InlineResponse20026 get_company_integrations(company_id)

Get Company Integrations

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
api_instance = salarydk.CompanyIntegrationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get the integrations for

try:
    # Get Company Integrations
    api_response = api_instance.get_company_integrations(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyIntegrationsApi->get_company_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get the integrations for | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

