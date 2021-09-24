# salarydk.CompanyPricingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_pricings**](CompanyPricingsApi.md#get_company_pricings) | **GET** /v2/companyPricings/{companyID} | 
[**update_company_pricings**](CompanyPricingsApi.md#update_company_pricings) | **PUT** /v2/companyPricings/{companyID} | 


# **get_company_pricings**
> InlineResponse20030 get_company_pricings(company_id)



Gets a list of pricing points for a company

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
api_instance = salarydk.CompanyPricingsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_company_pricings(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyPricingsApi->get_company_pricings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_pricings**
> update_company_pricings(company_id, pricings)



Overwrites the pricing points for a company, requries admin.

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
api_instance = salarydk.CompanyPricingsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
pricings = NULL # list[CompanyPricing] | 

try:
    api_instance.update_company_pricings(company_id, pricings)
except ApiException as e:
    print("Exception when calling CompanyPricingsApi->update_company_pricings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **pricings** | [**list[CompanyPricing]**](list.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

