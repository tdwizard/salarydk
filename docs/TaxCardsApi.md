# salarydk.TaxCardsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_card**](TaxCardsApi.md#create_tax_card) | **POST** /v2/taxCards | 
[**get_tax_cards**](TaxCardsApi.md#get_tax_cards) | **GET** /v2/taxCards | 


# **create_tax_card**
> create_tax_card(tax_card)



Create new tax card for testing purposes

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
api_instance = salarydk.TaxCardsApi(salarydk.ApiClient(configuration))
tax_card = salarydk.TaxCard() # TaxCard | 

try:
    api_instance.create_tax_card(tax_card)
except ApiException as e:
    print("Exception when calling TaxCardsApi->create_tax_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_card** | [**TaxCard**](TaxCard.md)|  | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_cards**
> InlineResponse20086 get_tax_cards(employee_id=employee_id, company_id=company_id)



Gets the tax cards, filtered by employeeID or companyID

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
api_instance = salarydk.TaxCardsApi(salarydk.ApiClient(configuration))
employee_id = 'employee_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_tax_cards(employee_id=employee_id, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxCardsApi->get_tax_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

