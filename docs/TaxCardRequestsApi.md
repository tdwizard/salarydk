# salarydk.TaxCardRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_card_request**](TaxCardRequestsApi.md#create_tax_card_request) | **POST** /v2/taxCardRequests | 
[**get_tax_card_requests**](TaxCardRequestsApi.md#get_tax_card_requests) | **GET** /v2/taxCardRequests | 


# **create_tax_card_request**
> InlineResponse20085 create_tax_card_request(tax_card_request=tax_card_request)



Requests an updated tax card from the authorities

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
api_instance = salarydk.TaxCardRequestsApi(salarydk.ApiClient(configuration))
tax_card_request = salarydk.InlineObject37() # InlineObject37 |  (optional)

try:
    api_response = api_instance.create_tax_card_request(tax_card_request=tax_card_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxCardRequestsApi->create_tax_card_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_card_request** | [**InlineObject37**](InlineObject37.md)|  | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_card_requests**
> InlineResponse20084 get_tax_card_requests(employee_id=employee_id)



Get all tax card requests, filtered by employeeID

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
api_instance = salarydk.TaxCardRequestsApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)

try:
    api_response = api_instance.get_tax_card_requests(employee_id=employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxCardRequestsApi->get_tax_card_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

