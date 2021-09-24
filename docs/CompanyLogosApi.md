# salarydk.CompanyLogosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_logo**](CompanyLogosApi.md#delete_company_logo) | **DELETE** /v2/companyLogos/{companyID} | 
[**get_company_logo**](CompanyLogosApi.md#get_company_logo) | **GET** /v2/companyLogos/{companyID} | 
[**set_company_logo**](CompanyLogosApi.md#set_company_logo) | **PUT** /v2/companyLogos/{companyID} | 


# **delete_company_logo**
> delete_company_logo(company_id)



Delete the company payslip logo

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
api_instance = salarydk.CompanyLogosApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_instance.delete_company_logo(company_id)
except ApiException as e:
    print("Exception when calling CompanyLogosApi->delete_company_logo: %s\n" % e)
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

# **get_company_logo**
> InlineResponse20029 get_company_logo(company_id)



Get the company payslip logo, if any.

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
api_instance = salarydk.CompanyLogosApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_company_logo(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLogosApi->get_company_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_company_logo**
> InlineResponse20029 set_company_logo(company_id, logo=logo)



Set the company payslip logo.

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
api_instance = salarydk.CompanyLogosApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
logo = salarydk.InlineObject6() # InlineObject6 |  (optional)

try:
    api_response = api_instance.set_company_logo(company_id, logo=logo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLogosApi->set_company_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **logo** | [**InlineObject6**](InlineObject6.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

