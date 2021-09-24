# salarydk.CompanyBankAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_company_bank_account**](CompanyBankAccountsApi.md#set_company_bank_account) | **POST** /v2/companyBankAccounts/{companyID} | 


# **set_company_bank_account**
> set_company_bank_account(company_id, bank_account=bank_account)



Set the company bank account for paying salary. The contact information must be a person with power of attorney. If they are blank, the contact information for the logged in user will be used instead.

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
api_instance = salarydk.CompanyBankAccountsApi(salarydk.ApiClient(configuration))
company_id = 'company_id_example' # str | 
bank_account = salarydk.InlineObject4() # InlineObject4 |  (optional)

try:
    api_instance.set_company_bank_account(company_id, bank_account=bank_account)
except ApiException as e:
    print("Exception when calling CompanyBankAccountsApi->set_company_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **bank_account** | [**InlineObject4**](InlineObject4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authorizedUser](../README.md#authorizedUser)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

