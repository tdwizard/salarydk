# salarydk.VouchersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounting**](VouchersApi.md#get_accounting) | **GET** /v2/vouchers | 
[**rebook_voucher**](VouchersApi.md#rebook_voucher) | **PATCH** /v2/vouchers/{id} | 


# **get_accounting**
> InlineResponse20097 get_accounting(pay_roll_id=pay_roll_id, company_id=company_id)



Gets all voucher rows, filtered by payRollID or companyID

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
api_instance = salarydk.VouchersApi(salarydk.ApiClient(configuration))
pay_roll_id = 'pay_roll_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)

try:
    api_response = api_instance.get_accounting(pay_roll_id=pay_roll_id, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->get_accounting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_roll_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebook_voucher**
> InlineResponse20098 rebook_voucher(id)



Rebooks a failed voucher. The voucher must have state = `Booking Failed`. The accounts for the voucher will be remapped with the current accounting configuration of the company, and queued for booking.

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
api_instance = salarydk.VouchersApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.rebook_voucher(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->rebook_voucher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

