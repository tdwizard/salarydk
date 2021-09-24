# salarydk.SupplementTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supplement_types**](SupplementTypesApi.md#get_supplement_types) | **GET** /v2/supplementTypes | 
[**update_supplement_payout**](SupplementTypesApi.md#update_supplement_payout) | **PATCH** /v2/supplementTypes/{companyID} | 


# **get_supplement_types**
> InlineResponse20081 get_supplement_types(company_id)



Gets supplement types, filtered by companyID

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
api_instance = salarydk.SupplementTypesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_supplement_types(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplementTypesApi->get_supplement_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplement_payout**
> InlineResponse20082 update_supplement_payout(company_id, supplement_type=supplement_type)



update payout on termination or expiration company-wide

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
api_instance = salarydk.SupplementTypesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
supplement_type = salarydk.InlineObject35() # InlineObject35 |  (optional)

try:
    api_response = api_instance.update_supplement_payout(company_id, supplement_type=supplement_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplementTypesApi->update_supplement_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **supplement_type** | [**InlineObject35**](InlineObject35.md)|  | [optional] 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

