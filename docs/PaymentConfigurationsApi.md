# salarydk.PaymentConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_configuration**](PaymentConfigurationsApi.md#create_payment_configuration) | **POST** /v2/paymentConfigurations | 
[**get_payment_configuration**](PaymentConfigurationsApi.md#get_payment_configuration) | **GET** /v2/paymentConfigurations | 
[**update_payment_transfer_settings**](PaymentConfigurationsApi.md#update_payment_transfer_settings) | **PATCH** /v2/paymentConfigurations/{companyID} | 


# **create_payment_configuration**
> create_payment_configuration(payment_configuration=payment_configuration)



Creates a payment configuration file for testing purposes

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
api_instance = salarydk.PaymentConfigurationsApi(salarydk.ApiClient(configuration))
payment_configuration = salarydk.InlineObject31() # InlineObject31 |  (optional)

try:
    api_instance.create_payment_configuration(payment_configuration=payment_configuration)
except ApiException as e:
    print("Exception when calling PaymentConfigurationsApi->create_payment_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_configuration** | [**InlineObject31**](InlineObject31.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_configuration**
> InlineResponse20065 get_payment_configuration(company_id)



Gets the payment configurations, filtered by companyID

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
api_instance = salarydk.PaymentConfigurationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 

try:
    api_response = api_instance.get_payment_configuration(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentConfigurationsApi->get_payment_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_transfer_settings**
> InlineResponse20065 update_payment_transfer_settings(company_id, transfer_settings)



Update the payment transfer settings

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
api_instance = salarydk.PaymentConfigurationsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
transfer_settings = NULL # list[TransferSetting] | 

try:
    api_response = api_instance.update_payment_transfer_settings(company_id, transfer_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentConfigurationsApi->update_payment_transfer_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **transfer_settings** | [**list[TransferSetting]**](list.md)|  | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

