# salarydk.BanksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bank_logo_image**](BanksApi.md#get_bank_logo_image) | **GET** /v2/bankImages/{id} | 
[**get_banks**](BanksApi.md#get_banks) | **GET** /v2/banks | 


# **get_bank_logo_image**
> file get_bank_logo_image(id)



Gets a bank logo image

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.BanksApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_bank_logo_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->get_bank_logo_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_banks**
> InlineResponse20011 get_banks(country, sort_code=sort_code)



Get all banks

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
api_instance = salarydk.BanksApi(salarydk.ApiClient(configuration))
country = 'country_example' # str | 
sort_code = 'sort_code_example' # str |  (optional)

try:
    api_response = api_instance.get_banks(country, sort_code=sort_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->get_banks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **sort_code** | **str**|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

