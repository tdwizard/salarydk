# openapi-client
This is the public API for Salary.dk.

# General

Our API is a JSON-based, REST-like API. Our webapp uses the exact same API, so everything you can do in our
webapp, you can do through our API. However, we are slowly opening up the API, so not all endpoints are documented
here yet. Only the endpoints documented here are stable. If there is some functionality you would like to
access through our API, please contact us.

The API is located at https://api.salary.dk.
All requests must use TLS.

In order to use the API on behalf of other users than yourself, you need to register as an API client. You do
this by sending an e-mail to dev@salary.dk with the name and purpose of your client.

API-keys for each account can be obtained once logged in to Salary, under the settings for the Company.

All endpoints are documented to be able to return the 500 error code. We strive to not return this error code,
so if you do encounter this error code, it might mean there is an error on our side. In this case, do not
hesitate to contact us.

# Versioning, upgrade and deprecation policy
Our API might change over time. In order to ensure a stable API, we follow these rules when changing the API.

New fields might be added at any time to any response or as non-required parameters to any input. When adding
input fields, we ensure the default behaviour when not supplying the field is the same as the previous version.
In these cases, the version of an endpoint is not increased, since it is backwards compatible. Since we might
add new fields to responses, be sure to use a JSON parser in your implementation. This ensures that any extra
fields added are ignored by your implementation.

We might add entirely new endpoints at any time. If we need to change an existing endpoint without being able to
make it backwards compatible, we will add a new version of the endpoint, and mark the old as deprecated but still
functional. We will then contact any users of the deprecated endpoint and ensure an upgrade is performed. Once all
consumers have moved to the new endpoint version, the old one will be removed.

We will not at any point change the meaning of any existing field, nor will we remove any field or endpoint without
following the above deprecated procedure. However, we might add new types to existing enums at any time.

# Cross-Origin Resource Sharing
This API features Cross-Origin Resource Sharing (CORS) implemented in compliance
with [W3C spec](https://www.w3.org/TR/cors/) - and that allows cross-domain communication from the browser.
All responses have a wildcard same-origin which makes them completely public and accessible to everyone,
including any code on any site, as long as the proper access token is passed.

# Authentication
All request require an access token. There are two ways to obtain an access token:
* Logging in as a user. (this endpoint is not yet publicly available).
* Using an API-key: [endpoint](#operation/APIClientLogin)

Using one of these methods, you will obtain an access token. In all subsequest requests, this access token should
be passed in the Authorization header. The access token is valid for around one hour, after which a new token
should be obtained.

You do not need to dispose of access tokens once created. They have a limited lifetime, and Salary.dk will
automatically expire old ones.

For some endpoints, the authorizedUserQuery security definition is used. This allows for passing the
access token as a query parameter where it is not possible to pass it as a header. In particular, this is
used for downloading files.

<!-- ReDoc-Inject: <security-definitions> -->


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompaniesApi* | [**get_companies**](docs/CompaniesApi.md#get_companies) | **GET** /v2/companies | List companies
*EmployeeContractsApi* | [**create_employee_contract**](docs/EmployeeContractsApi.md#create_employee_contract) | **POST** /v2/employeeContracts | 
*EmployeeContractsApi* | [**create_leave_for_employee**](docs/EmployeeContractsApi.md#create_leave_for_employee) | **POST** /v2/employees/{employeeID}/leave | 
*EmployeeContractsApi* | [**delete_employee_contract**](docs/EmployeeContractsApi.md#delete_employee_contract) | **DELETE** /v2/employeeContracts/{employeeContractID} | 
*EmployeeContractsApi* | [**get_employee_contract**](docs/EmployeeContractsApi.md#get_employee_contract) | **GET** /v2/employeeContracts/{employeeContractID} | 
*EmployeeContractsApi* | [**get_employee_contracts**](docs/EmployeeContractsApi.md#get_employee_contracts) | **GET** /v2/employeeContracts | 
*EmployeeContractsApi* | [**remove_leave_for_employee_contract**](docs/EmployeeContractsApi.md#remove_leave_for_employee_contract) | **DELETE** /v2/employeeContracts/{employeeContractID}/leave | 
*EmployeesApi* | [**create_employee**](docs/EmployeesApi.md#create_employee) | **POST** /v2/employees | 
*EmployeesApi* | [**delete_employee**](docs/EmployeesApi.md#delete_employee) | **DELETE** /v2/employees/{employeeID} | 
*EmployeesApi* | [**get_employee**](docs/EmployeesApi.md#get_employee) | **GET** /v2/employees/{employeeID} | 
*EmployeesApi* | [**get_employees**](docs/EmployeesApi.md#get_employees) | **GET** /v2/employees | List employees
*EmployeesApi* | [**set_employee_pdf_password**](docs/EmployeesApi.md#set_employee_pdf_password) | **POST** /v2/employees/{employeeID}/pdfPassword | 
*EmployeesApi* | [**update_employee**](docs/EmployeesApi.md#update_employee) | **PUT** /v2/employees/{employeeID} | 
*EmploymentsApi* | [**create_employment**](docs/EmploymentsApi.md#create_employment) | **POST** /v2/employments | 
*EmploymentsApi* | [**delete_employment**](docs/EmploymentsApi.md#delete_employment) | **DELETE** /v2/employments/{employmentID} | 
*EmploymentsApi* | [**get_employment**](docs/EmploymentsApi.md#get_employment) | **GET** /v2/employments/{employmentID} | 
*EmploymentsApi* | [**get_employments**](docs/EmploymentsApi.md#get_employments) | **GET** /v2/employments | 
*EmploymentsApi* | [**rehire_employee**](docs/EmploymentsApi.md#rehire_employee) | **POST** /v2/employees/{employeeID}/rehire | 
*EmploymentsApi* | [**remove_termination_for_employment**](docs/EmploymentsApi.md#remove_termination_for_employment) | **PATCH** /v2/employments/{employmentID}/removeTermination | 
*EmploymentsApi* | [**terminate_employment**](docs/EmploymentsApi.md#terminate_employment) | **PATCH** /v2/employments/{employmentID}/terminate | 
*LeaveTypesApi* | [**get_leave_types**](docs/LeaveTypesApi.md#get_leave_types) | **GET** /v2/leaveTypes | List Leave Types
*LoginApi* | [**a_pi_client_login**](docs/LoginApi.md#a_pi_client_login) | **POST** /v2/auth | Log in with API client
*PaySlipsApi* | [**get_pay_slip**](docs/PaySlipsApi.md#get_pay_slip) | **GET** /v2/paySlips/{id} | Get Pay Slip
*PaySlipsApi* | [**get_pay_slip_pdf**](docs/PaySlipsApi.md#get_pay_slip_pdf) | **GET** /v2/paySlipsPDF/{id} | Get Pay Slip as PDF
*PaySlipsApi* | [**get_pay_slips**](docs/PaySlipsApi.md#get_pay_slips) | **GET** /v2/paySlips | Get Pay Slips
*PaySlipsApi* | [**get_pay_slips_pdf**](docs/PaySlipsApi.md#get_pay_slips_pdf) | **GET** /v2/paySlipsPDF | Get Pay Slips as PDF
*PaySlipsApi* | [**get_pay_slips_zip**](docs/PaySlipsApi.md#get_pay_slips_zip) | **GET** /v2/paySlipsZip | Get Pay Slips as .zip
*ReportsApi* | [**get_report_csv**](docs/ReportsApi.md#get_report_csv) | **GET** /v2/reportCSV | 
*ReportsApi* | [**get_report_excel**](docs/ReportsApi.md#get_report_excel) | **GET** /v2/reportExcel | 
*SalaryCyclesApi* | [**get_salary_cycles**](docs/SalaryCyclesApi.md#get_salary_cycles) | **GET** /v2/salaryCycles | List Salary Cycles
*SalaryPeriodsApi* | [**get_salary_periods**](docs/SalaryPeriodsApi.md#get_salary_periods) | **GET** /v2/salaryPeriods | List Salary Periods
*SalaryTypesApi* | [**get_salary_types**](docs/SalaryTypesApi.md#get_salary_types) | **GET** /v2/salaryTypes | 
*TimeRegistrationsApi* | [**create_coarse_time_registration**](docs/TimeRegistrationsApi.md#create_coarse_time_registration) | **POST** /v2/coarseTimeRegistrations | Create Coarse Time Registration
*TimeRegistrationsApi* | [**create_time_registration**](docs/TimeRegistrationsApi.md#create_time_registration) | **POST** /v2/timeRegistrations | Create Time Registration
*TimeRegistrationsApi* | [**delete_coarse_time_registration**](docs/TimeRegistrationsApi.md#delete_coarse_time_registration) | **DELETE** /v2/coarseTimeRegistrations/{id} | Delete Coarse Time Registration
*TimeRegistrationsApi* | [**delete_time_registration**](docs/TimeRegistrationsApi.md#delete_time_registration) | **DELETE** /v2/timeRegistrations/{id} | Delete Time Registration
*TimeRegistrationsApi* | [**get_coarse_time_registrations**](docs/TimeRegistrationsApi.md#get_coarse_time_registrations) | **GET** /v2/coarseTimeRegistrations | List Coarse Time Registrations
*TimeRegistrationsApi* | [**get_time_registrations**](docs/TimeRegistrationsApi.md#get_time_registrations) | **GET** /v2/timeRegistrations | List Time Registrations
*TimeRegistrationsApi* | [**update_coarse_time_registration**](docs/TimeRegistrationsApi.md#update_coarse_time_registration) | **PUT** /v2/coarseTimeRegistrations/{id} | Update Coarse Time Registration
*TimeRegistrationsApi* | [**update_time_registration**](docs/TimeRegistrationsApi.md#update_time_registration) | **PUT** /v2/timeRegistrations/{id} | Update Time Registration


## Documentation For Models

 - [AccessToken](docs/AccessToken.md)
 - [CoarseTimeRegistration](docs/CoarseTimeRegistration.md)
 - [Company](docs/Company.md)
 - [CompanyDkSpecific](docs/CompanyDkSpecific.md)
 - [CompanySettingBoolean](docs/CompanySettingBoolean.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardPayRolls](docs/DashboardPayRolls.md)
 - [Employee](docs/Employee.md)
 - [EmployeeContract](docs/EmployeeContract.md)
 - [Employment](docs/Employment.md)
 - [Error](docs/Error.md)
 - [ErrorError](docs/ErrorError.md)
 - [IncomeType](docs/IncomeType.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Data](docs/InlineResponse2008Data.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [LeaveType](docs/LeaveType.md)
 - [Pagination](docs/Pagination.md)
 - [PaySlip](docs/PaySlip.md)
 - [PaySlipAggregates](docs/PaySlipAggregates.md)
 - [PaySlipCalculations](docs/PaySlipCalculations.md)
 - [PaySlipFields](docs/PaySlipFields.md)
 - [PaySlipRows](docs/PaySlipRows.md)
 - [ProductionUnit](docs/ProductionUnit.md)
 - [Remuneration](docs/Remuneration.md)
 - [RemunerationBenefits](docs/RemunerationBenefits.md)
 - [RemunerationLeave](docs/RemunerationLeave.md)
 - [RemunerationPension](docs/RemunerationPension.md)
 - [RemunerationSupplements](docs/RemunerationSupplements.md)
 - [SalaryCycle](docs/SalaryCycle.md)
 - [SalaryDefinition](docs/SalaryDefinition.md)
 - [SalaryPeriod](docs/SalaryPeriod.md)
 - [SalaryType](docs/SalaryType.md)
 - [SalaryTypeSupplements](docs/SalaryTypeSupplements.md)
 - [SupplementType](docs/SupplementType.md)
 - [TimeRegistration](docs/TimeRegistration.md)
 - [User](docs/User.md)
 - [UserPermission](docs/UserPermission.md)
 - [VacationCalendar](docs/VacationCalendar.md)
 - [VacationDay](docs/VacationDay.md)


## Documentation For Authorization


## authorizedUser

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## authorizedUserQuery

- **Type**: API key
- **API key parameter name**: apiKey
- **Location**: URL query string


## Author

dev@salary.dk


