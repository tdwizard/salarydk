# salarydk.AgreementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agreements**](AgreementsApi.md#get_agreements) | **GET** /v2/agreements | 
[**sign_agreement**](AgreementsApi.md#sign_agreement) | **POST** /v2/agreements | 


# **get_agreements**
> InlineResponse2004 get_agreements(company_id=company_id)



Get agreements

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
api_instance = salarydk.AgreementsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_agreements(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->get_agreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_agreement**
> InlineResponse2005 sign_agreement(agreement)



Sign agreement

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
api_instance = salarydk.AgreementsApi(salarydk.ApiClient(configuration))
agreement = salarydk.Agreement() # Agreement | 

try:
    api_response = api_instance.sign_agreement(agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->sign_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement** | [**Agreement**](Agreement.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

