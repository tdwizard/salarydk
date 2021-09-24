# salarydk.CompanyFeaturesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_company_feature**](CompanyFeaturesApi.md#activate_company_feature) | **POST** /v2/companyFeatures | 
[**deactivate_company_feature**](CompanyFeaturesApi.md#deactivate_company_feature) | **DELETE** /v2/companyFeatures | 
[**get_company_features**](CompanyFeaturesApi.md#get_company_features) | **GET** /v2/companyFeatures | 


# **activate_company_feature**
> activate_company_feature(feature=feature)



Activate feature for company, requires admin.

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
api_instance = salarydk.CompanyFeaturesApi(salarydk.ApiClient(configuration))
feature = salarydk.InlineObject5() # InlineObject5 |  (optional)

try:
    api_instance.activate_company_feature(feature=feature)
except ApiException as e:
    print("Exception when calling CompanyFeaturesApi->activate_company_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | [**InlineObject5**](InlineObject5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_company_feature**
> deactivate_company_feature(company_id, feature_type)



Deactivate feature for company, requires admin.

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
api_instance = salarydk.CompanyFeaturesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
feature_type = 'feature_type_example' # str | 

try:
    api_instance.deactivate_company_feature(company_id, feature_type)
except ApiException as e:
    print("Exception when calling CompanyFeaturesApi->deactivate_company_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **feature_type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_features**
> InlineResponse20028 get_company_features(company_id)



Get a list of active features for a company.

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
api_instance = salarydk.CompanyFeaturesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_company_features(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyFeaturesApi->get_company_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

