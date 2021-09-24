# openapi_client.CompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_companies**](CompaniesApi.md#get_companies) | **GET** /v2/companies | List companies


# **get_companies**
> InlineResponse2003 get_companies(limit=limit, offset=offset)

List companies

Gets a list of all companies.

### Example

* Api Key Authentication (authorizedUser):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authorizedUser
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompaniesApi(api_client)
    limit = 1000 # int | For pagination, the requested number of entries to return. (optional) (default to 1000)
offset = 0 # int | For pagination, the offset to start listing entries. (optional) (default to 0)

    try:
        # List companies
        api_response = api_instance.get_companies(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompaniesApi->get_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| For pagination, the requested number of entries to return. | [optional] [default to 1000]
 **offset** | **int**| For pagination, the offset to start listing entries. | [optional] [default to 0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned companies |  -  |
**400** | Bad request |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

