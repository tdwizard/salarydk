# openapi_client.LoginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_pi_client_login**](LoginApi.md#a_pi_client_login) | **POST** /v2/auth | Log in with API client


# **a_pi_client_login**
> InlineResponse200 a_pi_client_login(login)

Log in with API client

Obtains an access token on behalf of a company. The access token can be used for subsequent requests to the API.

### Example

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


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LoginApi(api_client)
    login = openapi_client.InlineObject() # InlineObject | 

    try:
        # Log in with API client
        api_response = api_instance.a_pi_client_login(login)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoginApi->a_pi_client_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization was successful, and an access token is returned. |  -  |
**401** | Wrong credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

