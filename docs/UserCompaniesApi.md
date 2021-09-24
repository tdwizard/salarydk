# salarydk.UserCompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_companies**](UserCompaniesApi.md#get_user_companies) | **GET** /v2/userCompanies | 
[**get_user_company**](UserCompaniesApi.md#get_user_company) | **GET** /v2/userCompanies/{companyID} | 
[**update_user_company**](UserCompaniesApi.md#update_user_company) | **PUT** /v2/userCompanies/{companyID} | 


# **get_user_companies**
> InlineResponse20031 get_user_companies()



Get all user companies

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
api_instance = salarydk.UserCompaniesApi(salarydk.ApiClient(configuration))

try:
    api_response = api_instance.get_user_companies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserCompaniesApi->get_user_companies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_company**
> InlineResponse20093 get_user_company(company_id)



Get user company settings for specific company

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
api_instance = salarydk.UserCompaniesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_user_company(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserCompaniesApi->get_user_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_company**
> InlineResponse20093 update_user_company(company_id, user_company)



Update user company settings

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
api_instance = salarydk.UserCompaniesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
user_company = salarydk.UserCompany() # UserCompany | 

try:
    api_response = api_instance.update_user_company(company_id, user_company)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserCompaniesApi->update_user_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **user_company** | [**UserCompany**](UserCompany.md)|  | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

