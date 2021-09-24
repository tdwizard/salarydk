# salarydk.TransfersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfers**](TransfersApi.md#get_transfers) | **GET** /v2/transfers | 
[**patch_transfer**](TransfersApi.md#patch_transfer) | **PATCH** /v2/transfers/{id} | 


# **get_transfers**
> InlineResponse20090 get_transfers(pay_roll_id=pay_roll_id, company_id=company_id, include_details=include_details, _from=_from, to=to, limit=limit, offset=offset)



Gets all transfers, filtered by payRollID or companyID.

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
api_instance = salarydk.TransfersApi(salarydk.ApiClient(configuration))
pay_roll_id = 'pay_roll_id_example' # str |  (optional)
company_id = 'company_id_example' # str |  (optional)
include_details = NULL # object | For each returned transfer, include details such as which employee the transfer belongs to. Setting this to false improves performance. (optional)
_from = '2013-10-20' # date | When listing for a company, only return transfers with a payment date later than this date. (optional)
to = '2013-10-20' # date | When listing for a company, only return transfers with a payment date earlier than this date. (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

try:
    api_response = api_instance.get_transfers(pay_roll_id=pay_roll_id, company_id=company_id, include_details=include_details, _from=_from, to=to, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_roll_id** | [**str**](.md)|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 
 **include_details** | [**object**](.md)| For each returned transfer, include details such as which employee the transfer belongs to. Setting this to false improves performance. | [optional] 
 **_from** | **date**| When listing for a company, only return transfers with a payment date later than this date. | [optional] 
 **to** | **date**| When listing for a company, only return transfers with a payment date earlier than this date. | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_transfer**
> InlineResponse20091 patch_transfer(id, automation=automation)



Change the automation of a transfer

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
api_instance = salarydk.TransfersApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 
automation = salarydk.InlineObject39() # InlineObject39 |  (optional)

try:
    api_response = api_instance.patch_transfer(id, automation=automation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->patch_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **automation** | [**InlineObject39**](InlineObject39.md)|  | [optional] 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

