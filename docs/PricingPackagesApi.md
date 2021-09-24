# salarydk.PricingPackagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pricing_packages**](PricingPackagesApi.md#get_pricing_packages) | **GET** /v2/pricingPackages | 
[**update_company_pricing_package**](PricingPackagesApi.md#update_company_pricing_package) | **POST** /v2/companyPricingPackages/{companyID} | 


# **get_pricing_packages**
> InlineResponse20067 get_pricing_packages(include_pricing_package_id=include_pricing_package_id, include_all=include_all)



Gets pricing packages. By default, only selectable, active packages are returned.

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
api_instance = salarydk.PricingPackagesApi(salarydk.ApiClient(configuration))
include_pricing_package_id = 'include_pricing_package_id_example' # str | Include the given pricing package, which might not be selectable or active (optional)
include_all = True # bool | Includes all pricing packages, requires admin (optional)

try:
    api_response = api_instance.get_pricing_packages(include_pricing_package_id=include_pricing_package_id, include_all=include_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricingPackagesApi->get_pricing_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_pricing_package_id** | [**str**](.md)| Include the given pricing package, which might not be selectable or active | [optional] 
 **include_all** | **bool**| Includes all pricing packages, requires admin | [optional] 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_pricing_package**
> update_company_pricing_package(company_id, pricing_package=pricing_package)



Selects a new pricing package for a company

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
api_instance = salarydk.PricingPackagesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
pricing_package = salarydk.InlineObject7() # InlineObject7 |  (optional)

try:
    api_instance.update_company_pricing_package(company_id, pricing_package=pricing_package)
except ApiException as e:
    print("Exception when calling PricingPackagesApi->update_company_pricing_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **pricing_package** | [**InlineObject7**](InlineObject7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

