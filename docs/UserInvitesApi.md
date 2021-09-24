# salarydk.UserInvitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_invitation**](UserInvitesApi.md#delete_user_invitation) | **DELETE** /v2/userInvites | 
[**get_pending_invites**](UserInvitesApi.md#get_pending_invites) | **GET** /v2/userInvites | 
[**get_user_invite_token**](UserInvitesApi.md#get_user_invite_token) | **GET** /v2/userInvites/{token} | 
[**send_user_invite**](UserInvitesApi.md#send_user_invite) | **POST** /v2/userInvites | 
[**spend_user_invitation_token**](UserInvitesApi.md#spend_user_invitation_token) | **POST** /v2/userInvites/{token} | 


# **delete_user_invitation**
> delete_user_invitation(company_id, email)



Deletes a pending user invitation

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
api_instance = salarydk.UserInvitesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
email = 'email_example' # str | The pending email invite to delete

try:
    api_instance.delete_user_invitation(company_id, email)
except ApiException as e:
    print("Exception when calling UserInvitesApi->delete_user_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **email** | **str**| The pending email invite to delete | 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_invites**
> InlineResponse20094 get_pending_invites(company_id)



Get pending user invites for a company

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
api_instance = salarydk.UserInvitesApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | The company to get a list of pending user invites for.

try:
    api_response = api_instance.get_pending_invites(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitesApi->get_pending_invites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The company to get a list of pending user invites for. | 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_invite_token**
> InlineResponse20096 get_user_invite_token(token)



Get company information for user invitation token

### Example
```python
from __future__ import print_function
import time
import salarydk
from salarydk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = salarydk.UserInvitesApi()
token = 'token_example' # str | An user invitation token

try:
    api_response = api_instance.get_user_invite_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitesApi->get_user_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**str**](.md)| An user invitation token | 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_user_invite**
> InlineResponse20095 send_user_invite(user_invite=user_invite)



Send invitation information to a new user

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
api_instance = salarydk.UserInvitesApi(salarydk.ApiClient(configuration))
user_invite = salarydk.InlineObject44() # InlineObject44 |  (optional)

try:
    api_response = api_instance.send_user_invite(user_invite=user_invite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitesApi->send_user_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invite** | [**InlineObject44**](InlineObject44.md)|  | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spend_user_invitation_token**
> InlineResponse20093 spend_user_invitation_token(token)



Spends the user invitation token on the current user

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
api_instance = salarydk.UserInvitesApi(salarydk.ApiClient(configuration))
token = 'token_example' # str | An user invitation token

try:
    api_response = api_instance.spend_user_invitation_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitesApi->spend_user_invitation_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**str**](.md)| An user invitation token | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

