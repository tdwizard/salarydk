# salarydk.ShipmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shipment**](ShipmentsApi.md#get_shipment) | **GET** /v2/shipments/{id} | 
[**get_shipment_content**](ShipmentsApi.md#get_shipment_content) | **GET** /v2/shipmentsContent/{id} | 
[**get_shipment_reply_content**](ShipmentsApi.md#get_shipment_reply_content) | **GET** /v2/shipmentRepliesContent/{id} | 
[**get_shipments**](ShipmentsApi.md#get_shipments) | **GET** /v2/shipments | 


# **get_shipment**
> InlineResponse20076 get_shipment(id)



Gets shipment

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
api_instance = salarydk.ShipmentsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_shipment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->get_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_content**
> InlineResponse20074 get_shipment_content(id)



Gets the content of a shipment

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
api_instance = salarydk.ShipmentsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_shipment_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->get_shipment_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_reply_content**
> InlineResponse20074 get_shipment_reply_content(id)



Gets the content of a shipment reply

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
api_instance = salarydk.ShipmentsApi(salarydk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_shipment_reply_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->get_shipment_reply_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipments**
> InlineResponse20075 get_shipments(workflow_id=workflow_id, limit=limit, offset=offset)



Gets shipments

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
api_instance = salarydk.ShipmentsApi(salarydk.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str |  (optional)
limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

try:
    api_response = api_instance.get_shipments(workflow_id=workflow_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->get_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | [**str**](.md)|  | [optional] 
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

