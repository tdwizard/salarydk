# coding: utf-8

# flake8: noqa
"""
    Salary.dk API

    This is the public API for Salary.dk.  # General  Our API is a JSON-based, REST-like API. Our webapp uses the exact same API, so everything you can do in our webapp, you can do through our API. However, we are slowly opening up the API, so not all endpoints are documented here yet. Only the endpoints documented here are stable. If there is some functionality you would like to access through our API, please contact us.  The API is located at https://api.salary.dk. All requests must use TLS.  In order to use the API on behalf of other users than yourself, you need to register as an API client. You do this by sending an e-mail to dev@salary.dk with the name and purpose of your client.  API-keys for each account can be obtained once logged in to Salary, under the settings for the Company.  All endpoints are documented to be able to return the 500 error code. We strive to not return this error code, so if you do encounter this error code, it might mean there is an error on our side. In this case, do not hesitate to contact us.  # Versioning, upgrade and deprecation policy Our API might change over time. In order to ensure a stable API, we follow these rules when changing the API.  New fields might be added at any time to any response or as non-required parameters to any input. When adding input fields, we ensure the default behaviour when not supplying the field is the same as the previous version. In these cases, the version of an endpoint is not increased, since it is backwards compatible. Since we might add new fields to responses, be sure to use a JSON parser in your implementation. This ensures that any extra fields added are ignored by your implementation.  We might add entirely new endpoints at any time. If we need to change an existing endpoint without being able to make it backwards compatible, we will add a new version of the endpoint, and mark the old as deprecated but still functional. We will then contact any users of the deprecated endpoint and ensure an upgrade is performed. Once all consumers have moved to the new endpoint version, the old one will be removed.  We will not at any point change the meaning of any existing field, nor will we remove any field or endpoint without following the above deprecated procedure. However, we might add new types to existing enums at any time.  # Cross-Origin Resource Sharing This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/) - and that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site, as long as the proper access token is passed.  # Authentication All request require an access token. There are two ways to obtain an access token: * Logging in as a user. (this endpoint is not yet publicly available). * Using an API-key: [endpoint](#operation/APIClientLogin)  Using one of these methods, you will obtain an access token. In all subsequest requests, this access token should be passed in the Authorization header. The access token is valid for around one hour, after which a new token should be obtained.  You do not need to dispose of access tokens once created. They have a limited lifetime, and Salary.dk will automatically expire old ones.  For some endpoints, the authorizedUserQuery security definition is used. This allows for passing the access token as a query parameter where it is not possible to pass it as a header. In particular, this is used for downloading files.  <!-- ReDoc-Inject: <security-definitions> -->   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@salary.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from salarydk.models.access_token import AccessToken
from salarydk.models.account_configuration import AccountConfiguration
from salarydk.models.account_plan import AccountPlan
from salarydk.models.account_plan_mapping import AccountPlanMapping
from salarydk.models.accounting_account import AccountingAccount
from salarydk.models.accounting_integration import AccountingIntegration
from salarydk.models.accounting_integration_account_mapping import AccountingIntegrationAccountMapping
from salarydk.models.accounting_integration_configurations import AccountingIntegrationConfigurations
from salarydk.models.accounting_integration_setup import AccountingIntegrationSetup
from salarydk.models.accounting_integration_setup_auth_parameters import AccountingIntegrationSetupAuthParameters
from salarydk.models.accounting_integration_setup_status import AccountingIntegrationSetupStatus
from salarydk.models.accounting_integration_setup_status_daybooks import AccountingIntegrationSetupStatusDaybooks
from salarydk.models.accounting_integration_setup_status_dimension_values import AccountingIntegrationSetupStatusDimensionValues
from salarydk.models.accounting_integration_setup_status_dimensions import AccountingIntegrationSetupStatusDimensions
from salarydk.models.accounting_integration_setup_status_organizations import AccountingIntegrationSetupStatusOrganizations
from salarydk.models.agreement import Agreement
from salarydk.models.api_client import ApiClient
from salarydk.models.api_key import ApiKey
from salarydk.models.approvable import Approvable
from salarydk.models.approver import Approver
from salarydk.models.asset import Asset
from salarydk.models.asset_category import AssetCategory
from salarydk.models.audit_log import AuditLog
from salarydk.models.audit_log_lines import AuditLogLines
from salarydk.models.available_accounting_integration import AvailableAccountingIntegration
from salarydk.models.available_accounting_integration_parameters import AvailableAccountingIntegrationParameters
from salarydk.models.available_time_registration_integration import AvailableTimeRegistrationIntegration
from salarydk.models.bank import Bank
from salarydk.models.book import Book
from salarydk.models.book_chapter import BookChapter
from salarydk.models.book_version import BookVersion
from salarydk.models.car_allowance import CarAllowance
from salarydk.models.coarse_car_allowance import CoarseCarAllowance
from salarydk.models.coarse_salary_registration import CoarseSalaryRegistration
from salarydk.models.coarse_time_registration import CoarseTimeRegistration
from salarydk.models.company import Company
from salarydk.models.company_deletion import CompanyDeletion
from salarydk.models.company_deviation_configuration import CompanyDeviationConfiguration
from salarydk.models.company_dk_specific import CompanyDkSpecific
from salarydk.models.company_feature import CompanyFeature
from salarydk.models.company_group import CompanyGroup
from salarydk.models.company_group_user import CompanyGroupUser
from salarydk.models.company_integration import CompanyIntegration
from salarydk.models.company_payment_integration import CompanyPaymentIntegration
from salarydk.models.company_pricing import CompanyPricing
from salarydk.models.company_pricing_package import CompanyPricingPackage
from salarydk.models.company_setting_boolean import CompanySettingBoolean
from salarydk.models.contract_book_callback import ContractBookCallback
from salarydk.models.contract_book_callback_contract import ContractBookCallbackContract
from salarydk.models.contract_book_contract import ContractBookContract
from salarydk.models.contract_book_integration import ContractBookIntegration
from salarydk.models.contract_book_template import ContractBookTemplate
from salarydk.models.contract_template import ContractTemplate
from salarydk.models.contract_template_contract import ContractTemplateContract
from salarydk.models.cost_center import CostCenter
from salarydk.models.dashboard import Dashboard
from salarydk.models.dashboard_pay_rolls import DashboardPayRolls
from salarydk.models.department import Department
from salarydk.models.device_token import DeviceToken
from salarydk.models.document import Document
from salarydk.models.document_category import DocumentCategory
from salarydk.models.employee import Employee
from salarydk.models.employee_batch_result import EmployeeBatchResult
from salarydk.models.employee_contract import EmployeeContract
from salarydk.models.employee_emergency_contact import EmployeeEmergencyContact
from salarydk.models.employee_swipe_status import EmployeeSwipeStatus
from salarydk.models.employees_import import EmployeesImport
from salarydk.models.employees_import_bank import EmployeesImportBank
from salarydk.models.employees_import_employees import EmployeesImportEmployees
from salarydk.models.employees_import_errors import EmployeesImportErrors
from salarydk.models.employees_import_salary_types import EmployeesImportSalaryTypes
from salarydk.models.employment import Employment
from salarydk.models.employment_position import EmploymentPosition
from salarydk.models.error import Error
from salarydk.models.error_error import ErrorError
from salarydk.models.expense_category import ExpenseCategory
from salarydk.models.harvest_information import HarvestInformation
from salarydk.models.income_tax_report import IncomeTaxReport
from salarydk.models.income_tax_report_employees import IncomeTaxReportEmployees
from salarydk.models.income_tax_report_salary_lines import IncomeTaxReportSalaryLines
from salarydk.models.income_tax_report_terminations import IncomeTaxReportTerminations
from salarydk.models.income_type import IncomeType
from salarydk.models.inline_object import InlineObject
from salarydk.models.inline_object1 import InlineObject1
from salarydk.models.inline_object10 import InlineObject10
from salarydk.models.inline_object11 import InlineObject11
from salarydk.models.inline_object12 import InlineObject12
from salarydk.models.inline_object13 import InlineObject13
from salarydk.models.inline_object14 import InlineObject14
from salarydk.models.inline_object15 import InlineObject15
from salarydk.models.inline_object16 import InlineObject16
from salarydk.models.inline_object17 import InlineObject17
from salarydk.models.inline_object18 import InlineObject18
from salarydk.models.inline_object19 import InlineObject19
from salarydk.models.inline_object2 import InlineObject2
from salarydk.models.inline_object20 import InlineObject20
from salarydk.models.inline_object21 import InlineObject21
from salarydk.models.inline_object22 import InlineObject22
from salarydk.models.inline_object23 import InlineObject23
from salarydk.models.inline_object24 import InlineObject24
from salarydk.models.inline_object25 import InlineObject25
from salarydk.models.inline_object26 import InlineObject26
from salarydk.models.inline_object27 import InlineObject27
from salarydk.models.inline_object28 import InlineObject28
from salarydk.models.inline_object29 import InlineObject29
from salarydk.models.inline_object3 import InlineObject3
from salarydk.models.inline_object30 import InlineObject30
from salarydk.models.inline_object31 import InlineObject31
from salarydk.models.inline_object32 import InlineObject32
from salarydk.models.inline_object33 import InlineObject33
from salarydk.models.inline_object34 import InlineObject34
from salarydk.models.inline_object35 import InlineObject35
from salarydk.models.inline_object36 import InlineObject36
from salarydk.models.inline_object37 import InlineObject37
from salarydk.models.inline_object38 import InlineObject38
from salarydk.models.inline_object39 import InlineObject39
from salarydk.models.inline_object4 import InlineObject4
from salarydk.models.inline_object40 import InlineObject40
from salarydk.models.inline_object41 import InlineObject41
from salarydk.models.inline_object42 import InlineObject42
from salarydk.models.inline_object43 import InlineObject43
from salarydk.models.inline_object44 import InlineObject44
from salarydk.models.inline_object45 import InlineObject45
from salarydk.models.inline_object46 import InlineObject46
from salarydk.models.inline_object47 import InlineObject47
from salarydk.models.inline_object48 import InlineObject48
from salarydk.models.inline_object49 import InlineObject49
from salarydk.models.inline_object5 import InlineObject5
from salarydk.models.inline_object50 import InlineObject50
from salarydk.models.inline_object51 import InlineObject51
from salarydk.models.inline_object52 import InlineObject52
from salarydk.models.inline_object53 import InlineObject53
from salarydk.models.inline_object54 import InlineObject54
from salarydk.models.inline_object55 import InlineObject55
from salarydk.models.inline_object56 import InlineObject56
from salarydk.models.inline_object57 import InlineObject57
from salarydk.models.inline_object58 import InlineObject58
from salarydk.models.inline_object59 import InlineObject59
from salarydk.models.inline_object6 import InlineObject6
from salarydk.models.inline_object60 import InlineObject60
from salarydk.models.inline_object61 import InlineObject61
from salarydk.models.inline_object62 import InlineObject62
from salarydk.models.inline_object63 import InlineObject63
from salarydk.models.inline_object64 import InlineObject64
from salarydk.models.inline_object65 import InlineObject65
from salarydk.models.inline_object66 import InlineObject66
from salarydk.models.inline_object67 import InlineObject67
from salarydk.models.inline_object68 import InlineObject68
from salarydk.models.inline_object69 import InlineObject69
from salarydk.models.inline_object7 import InlineObject7
from salarydk.models.inline_object70 import InlineObject70
from salarydk.models.inline_object71 import InlineObject71
from salarydk.models.inline_object72 import InlineObject72
from salarydk.models.inline_object73 import InlineObject73
from salarydk.models.inline_object74 import InlineObject74
from salarydk.models.inline_object75 import InlineObject75
from salarydk.models.inline_object76 import InlineObject76
from salarydk.models.inline_object77 import InlineObject77
from salarydk.models.inline_object78 import InlineObject78
from salarydk.models.inline_object79 import InlineObject79
from salarydk.models.inline_object8 import InlineObject8
from salarydk.models.inline_object80 import InlineObject80
from salarydk.models.inline_object81 import InlineObject81
from salarydk.models.inline_object82 import InlineObject82
from salarydk.models.inline_object83 import InlineObject83
from salarydk.models.inline_object84 import InlineObject84
from salarydk.models.inline_object9 import InlineObject9
from salarydk.models.inline_response200 import InlineResponse200
from salarydk.models.inline_response2001 import InlineResponse2001
from salarydk.models.inline_response20010 import InlineResponse20010
from salarydk.models.inline_response200100 import InlineResponse200100
from salarydk.models.inline_response200101 import InlineResponse200101
from salarydk.models.inline_response200102 import InlineResponse200102
from salarydk.models.inline_response200103 import InlineResponse200103
from salarydk.models.inline_response200104 import InlineResponse200104
from salarydk.models.inline_response200105 import InlineResponse200105
from salarydk.models.inline_response200105_data import InlineResponse200105Data
from salarydk.models.inline_response200106 import InlineResponse200106
from salarydk.models.inline_response200107 import InlineResponse200107
from salarydk.models.inline_response200108 import InlineResponse200108
from salarydk.models.inline_response200109 import InlineResponse200109
from salarydk.models.inline_response20011 import InlineResponse20011
from salarydk.models.inline_response200110 import InlineResponse200110
from salarydk.models.inline_response200111 import InlineResponse200111
from salarydk.models.inline_response200112 import InlineResponse200112
from salarydk.models.inline_response200113 import InlineResponse200113
from salarydk.models.inline_response200114 import InlineResponse200114
from salarydk.models.inline_response200115 import InlineResponse200115
from salarydk.models.inline_response200116 import InlineResponse200116
from salarydk.models.inline_response200117 import InlineResponse200117
from salarydk.models.inline_response200118 import InlineResponse200118
from salarydk.models.inline_response200119 import InlineResponse200119
from salarydk.models.inline_response200119_data import InlineResponse200119Data
from salarydk.models.inline_response20012 import InlineResponse20012
from salarydk.models.inline_response200120 import InlineResponse200120
from salarydk.models.inline_response200120_data import InlineResponse200120Data
from salarydk.models.inline_response200121 import InlineResponse200121
from salarydk.models.inline_response200122 import InlineResponse200122
from salarydk.models.inline_response200123 import InlineResponse200123
from salarydk.models.inline_response200124 import InlineResponse200124
from salarydk.models.inline_response200125 import InlineResponse200125
from salarydk.models.inline_response200126 import InlineResponse200126
from salarydk.models.inline_response200127 import InlineResponse200127
from salarydk.models.inline_response200128 import InlineResponse200128
from salarydk.models.inline_response200129 import InlineResponse200129
from salarydk.models.inline_response20013 import InlineResponse20013
from salarydk.models.inline_response200130 import InlineResponse200130
from salarydk.models.inline_response200131 import InlineResponse200131
from salarydk.models.inline_response200132 import InlineResponse200132
from salarydk.models.inline_response200133 import InlineResponse200133
from salarydk.models.inline_response200134 import InlineResponse200134
from salarydk.models.inline_response200135 import InlineResponse200135
from salarydk.models.inline_response200136 import InlineResponse200136
from salarydk.models.inline_response200136_data import InlineResponse200136Data
from salarydk.models.inline_response200137 import InlineResponse200137
from salarydk.models.inline_response200138 import InlineResponse200138
from salarydk.models.inline_response200138_data import InlineResponse200138Data
from salarydk.models.inline_response200139 import InlineResponse200139
from salarydk.models.inline_response20014 import InlineResponse20014
from salarydk.models.inline_response200140 import InlineResponse200140
from salarydk.models.inline_response200141 import InlineResponse200141
from salarydk.models.inline_response200142 import InlineResponse200142
from salarydk.models.inline_response200143 import InlineResponse200143
from salarydk.models.inline_response200144 import InlineResponse200144
from salarydk.models.inline_response200144_data import InlineResponse200144Data
from salarydk.models.inline_response200145 import InlineResponse200145
from salarydk.models.inline_response200146 import InlineResponse200146
from salarydk.models.inline_response200147 import InlineResponse200147
from salarydk.models.inline_response200148 import InlineResponse200148
from salarydk.models.inline_response200149 import InlineResponse200149
from salarydk.models.inline_response20015 import InlineResponse20015
from salarydk.models.inline_response200150 import InlineResponse200150
from salarydk.models.inline_response200151 import InlineResponse200151
from salarydk.models.inline_response200152 import InlineResponse200152
from salarydk.models.inline_response200153 import InlineResponse200153
from salarydk.models.inline_response200154 import InlineResponse200154
from salarydk.models.inline_response200155 import InlineResponse200155
from salarydk.models.inline_response200156 import InlineResponse200156
from salarydk.models.inline_response200157 import InlineResponse200157
from salarydk.models.inline_response200158 import InlineResponse200158
from salarydk.models.inline_response200159 import InlineResponse200159
from salarydk.models.inline_response200159_data import InlineResponse200159Data
from salarydk.models.inline_response20016 import InlineResponse20016
from salarydk.models.inline_response200160 import InlineResponse200160
from salarydk.models.inline_response200161 import InlineResponse200161
from salarydk.models.inline_response200162 import InlineResponse200162
from salarydk.models.inline_response200163 import InlineResponse200163
from salarydk.models.inline_response200164 import InlineResponse200164
from salarydk.models.inline_response200165 import InlineResponse200165
from salarydk.models.inline_response200166 import InlineResponse200166
from salarydk.models.inline_response200167 import InlineResponse200167
from salarydk.models.inline_response200168 import InlineResponse200168
from salarydk.models.inline_response200169 import InlineResponse200169
from salarydk.models.inline_response20017 import InlineResponse20017
from salarydk.models.inline_response200170 import InlineResponse200170
from salarydk.models.inline_response200171 import InlineResponse200171
from salarydk.models.inline_response200172 import InlineResponse200172
from salarydk.models.inline_response20018 import InlineResponse20018
from salarydk.models.inline_response20019 import InlineResponse20019
from salarydk.models.inline_response2002 import InlineResponse2002
from salarydk.models.inline_response20020 import InlineResponse20020
from salarydk.models.inline_response20021 import InlineResponse20021
from salarydk.models.inline_response20022 import InlineResponse20022
from salarydk.models.inline_response20023 import InlineResponse20023
from salarydk.models.inline_response20024 import InlineResponse20024
from salarydk.models.inline_response20025 import InlineResponse20025
from salarydk.models.inline_response20026 import InlineResponse20026
from salarydk.models.inline_response20027 import InlineResponse20027
from salarydk.models.inline_response20027_data import InlineResponse20027Data
from salarydk.models.inline_response20028 import InlineResponse20028
from salarydk.models.inline_response20028_data import InlineResponse20028Data
from salarydk.models.inline_response20029 import InlineResponse20029
from salarydk.models.inline_response2003 import InlineResponse2003
from salarydk.models.inline_response20030 import InlineResponse20030
from salarydk.models.inline_response20030_data import InlineResponse20030Data
from salarydk.models.inline_response20031 import InlineResponse20031
from salarydk.models.inline_response20032 import InlineResponse20032
from salarydk.models.inline_response20033 import InlineResponse20033
from salarydk.models.inline_response20034 import InlineResponse20034
from salarydk.models.inline_response20035 import InlineResponse20035
from salarydk.models.inline_response20036 import InlineResponse20036
from salarydk.models.inline_response20037 import InlineResponse20037
from salarydk.models.inline_response20038 import InlineResponse20038
from salarydk.models.inline_response20039 import InlineResponse20039
from salarydk.models.inline_response2004 import InlineResponse2004
from salarydk.models.inline_response20040 import InlineResponse20040
from salarydk.models.inline_response20041 import InlineResponse20041
from salarydk.models.inline_response20041_data import InlineResponse20041Data
from salarydk.models.inline_response20042 import InlineResponse20042
from salarydk.models.inline_response20043 import InlineResponse20043
from salarydk.models.inline_response20044 import InlineResponse20044
from salarydk.models.inline_response20045 import InlineResponse20045
from salarydk.models.inline_response20045_data import InlineResponse20045Data
from salarydk.models.inline_response20046 import InlineResponse20046
from salarydk.models.inline_response20047 import InlineResponse20047
from salarydk.models.inline_response20048 import InlineResponse20048
from salarydk.models.inline_response20049 import InlineResponse20049
from salarydk.models.inline_response20049_data import InlineResponse20049Data
from salarydk.models.inline_response2005 import InlineResponse2005
from salarydk.models.inline_response20050 import InlineResponse20050
from salarydk.models.inline_response20051 import InlineResponse20051
from salarydk.models.inline_response20052 import InlineResponse20052
from salarydk.models.inline_response20053 import InlineResponse20053
from salarydk.models.inline_response20054 import InlineResponse20054
from salarydk.models.inline_response20055 import InlineResponse20055
from salarydk.models.inline_response20056 import InlineResponse20056
from salarydk.models.inline_response20057 import InlineResponse20057
from salarydk.models.inline_response20058 import InlineResponse20058
from salarydk.models.inline_response20059 import InlineResponse20059
from salarydk.models.inline_response2006 import InlineResponse2006
from salarydk.models.inline_response20060 import InlineResponse20060
from salarydk.models.inline_response20061 import InlineResponse20061
from salarydk.models.inline_response20062 import InlineResponse20062
from salarydk.models.inline_response20063 import InlineResponse20063
from salarydk.models.inline_response20064 import InlineResponse20064
from salarydk.models.inline_response20065 import InlineResponse20065
from salarydk.models.inline_response20066 import InlineResponse20066
from salarydk.models.inline_response20067 import InlineResponse20067
from salarydk.models.inline_response20068 import InlineResponse20068
from salarydk.models.inline_response20069 import InlineResponse20069
from salarydk.models.inline_response2007 import InlineResponse2007
from salarydk.models.inline_response20070 import InlineResponse20070
from salarydk.models.inline_response20071 import InlineResponse20071
from salarydk.models.inline_response20072 import InlineResponse20072
from salarydk.models.inline_response20073 import InlineResponse20073
from salarydk.models.inline_response20073_data import InlineResponse20073Data
from salarydk.models.inline_response20074 import InlineResponse20074
from salarydk.models.inline_response20075 import InlineResponse20075
from salarydk.models.inline_response20076 import InlineResponse20076
from salarydk.models.inline_response20077 import InlineResponse20077
from salarydk.models.inline_response20078 import InlineResponse20078
from salarydk.models.inline_response20079 import InlineResponse20079
from salarydk.models.inline_response2008 import InlineResponse2008
from salarydk.models.inline_response20080 import InlineResponse20080
from salarydk.models.inline_response20081 import InlineResponse20081
from salarydk.models.inline_response20082 import InlineResponse20082
from salarydk.models.inline_response20083 import InlineResponse20083
from salarydk.models.inline_response20084 import InlineResponse20084
from salarydk.models.inline_response20085 import InlineResponse20085
from salarydk.models.inline_response20086 import InlineResponse20086
from salarydk.models.inline_response20086_data import InlineResponse20086Data
from salarydk.models.inline_response20087 import InlineResponse20087
from salarydk.models.inline_response20088 import InlineResponse20088
from salarydk.models.inline_response20089 import InlineResponse20089
from salarydk.models.inline_response2009 import InlineResponse2009
from salarydk.models.inline_response20090 import InlineResponse20090
from salarydk.models.inline_response20090_data import InlineResponse20090Data
from salarydk.models.inline_response20091 import InlineResponse20091
from salarydk.models.inline_response20091_data import InlineResponse20091Data
from salarydk.models.inline_response20091_dk_specific import InlineResponse20091DkSpecific
from salarydk.models.inline_response20092 import InlineResponse20092
from salarydk.models.inline_response20092_data import InlineResponse20092Data
from salarydk.models.inline_response20093 import InlineResponse20093
from salarydk.models.inline_response20094 import InlineResponse20094
from salarydk.models.inline_response20095 import InlineResponse20095
from salarydk.models.inline_response20096 import InlineResponse20096
from salarydk.models.inline_response20097 import InlineResponse20097
from salarydk.models.inline_response20098 import InlineResponse20098
from salarydk.models.inline_response20099 import InlineResponse20099
from salarydk.models.inline_response201 import InlineResponse201
from salarydk.models.inline_response401 import InlineResponse401
from salarydk.models.inline_response403 import InlineResponse403
from salarydk.models.invoice import Invoice
from salarydk.models.invoice_lines import InvoiceLines
from salarydk.models.leave_adjustment import LeaveAdjustment
from salarydk.models.leave_balance import LeaveBalance
from salarydk.models.leave_type import LeaveType
from salarydk.models.meta_data import MetaData
from salarydk.models.meta_data_immutable_period import MetaDataImmutablePeriod
from salarydk.models.mfa import Mfa
from salarydk.models.nets_message import NetsMessage
from salarydk.models.one_time_pay import OneTimePay
from salarydk.models.one_time_pay_pension import OneTimePayPension
from salarydk.models.outgoing_lead import OutgoingLead
from salarydk.models.pagination import Pagination
from salarydk.models.pay_roll import PayRoll
from salarydk.models.pay_roll_deviation import PayRollDeviation
from salarydk.models.pay_roll_tasks import PayRollTasks
from salarydk.models.pay_slip import PaySlip
from salarydk.models.pay_slip_aggregates import PaySlipAggregates
from salarydk.models.pay_slip_calculations import PaySlipCalculations
from salarydk.models.pay_slip_fields import PaySlipFields
from salarydk.models.pay_slip_rows import PaySlipRows
from salarydk.models.payment_configuration import PaymentConfiguration
from salarydk.models.pension_company import PensionCompany
from salarydk.models.pricing_package import PricingPackage
from salarydk.models.production_unit import ProductionUnit
from salarydk.models.reimbursement_voucher import ReimbursementVoucher
from salarydk.models.remote_upload import RemoteUpload
from salarydk.models.remuneration import Remuneration
from salarydk.models.remuneration_benefits import RemunerationBenefits
from salarydk.models.remuneration_leave import RemunerationLeave
from salarydk.models.remuneration_pension import RemunerationPension
from salarydk.models.remuneration_supplements import RemunerationSupplements
from salarydk.models.salary_cycle import SalaryCycle
from salarydk.models.salary_definition import SalaryDefinition
from salarydk.models.salary_period import SalaryPeriod
from salarydk.models.salary_type import SalaryType
from salarydk.models.salary_type_supplements import SalaryTypeSupplements
from salarydk.models.shipment import Shipment
from salarydk.models.shipment_notifications import ShipmentNotifications
from salarydk.models.shipment_replies import ShipmentReplies
from salarydk.models.staged_import import StagedImport
from salarydk.models.staged_import_companies import StagedImportCompanies
from salarydk.models.staged_import_dk_specific import StagedImportDkSpecific
from salarydk.models.staged_import_employees import StagedImportEmployees
from salarydk.models.staged_import_error import StagedImportError
from salarydk.models.standard_profile_image import StandardProfileImage
from salarydk.models.start_balance import StartBalance
from salarydk.models.start_balance_dk_specific import StartBalanceDkSpecific
from salarydk.models.start_balance_dk_specific_car_allowance import StartBalanceDkSpecificCarAllowance
from salarydk.models.start_balance_dk_specific_extra_vacation_accrual import StartBalanceDkSpecificExtraVacationAccrual
from salarydk.models.start_balance_dk_specific_personal_time_accrual import StartBalanceDkSpecificPersonalTimeAccrual
from salarydk.models.start_balance_dk_specific_vacation_accrual import StartBalanceDkSpecificVacationAccrual
from salarydk.models.start_balance_dk_specific_vacation_fund import StartBalanceDkSpecificVacationFund
from salarydk.models.start_balance_dk_specific_vacation_no_pay import StartBalanceDkSpecificVacationNoPay
from salarydk.models.start_balance_dk_specific_vacation_optional import StartBalanceDkSpecificVacationOptional
from salarydk.models.start_balance_dk_specific_vacation_paid import StartBalanceDkSpecificVacationPaid
from salarydk.models.start_balance_dk_specific_vacation_paid_additional import StartBalanceDkSpecificVacationPaidAdditional
from salarydk.models.start_balance_dk_specific_vacation_personal_days import StartBalanceDkSpecificVacationPersonalDays
from salarydk.models.start_pay_roll import StartPayRoll
from salarydk.models.supplement_adjustment import SupplementAdjustment
from salarydk.models.supplement_balance import SupplementBalance
from salarydk.models.supplement_type import SupplementType
from salarydk.models.swipe import Swipe
from salarydk.models.tax_card import TaxCard
from salarydk.models.tax_card_request import TaxCardRequest
from salarydk.models.time_registration import TimeRegistration
from salarydk.models.time_registration_import import TimeRegistrationImport
from salarydk.models.time_registration_import_employees import TimeRegistrationImportEmployees
from salarydk.models.time_registration_import_errors import TimeRegistrationImportErrors
from salarydk.models.time_registration_import_registrations import TimeRegistrationImportRegistrations
from salarydk.models.time_registration_import_salary_types import TimeRegistrationImportSalaryTypes
from salarydk.models.time_registration_integration import TimeRegistrationIntegration
from salarydk.models.time_registration_integration_setup import TimeRegistrationIntegrationSetup
from salarydk.models.time_registration_integration_setup_status import TimeRegistrationIntegrationSetupStatus
from salarydk.models.time_registration_integration_setup_status_salary_types import TimeRegistrationIntegrationSetupStatusSalaryTypes
from salarydk.models.transaction import Transaction
from salarydk.models.transfer import Transfer
from salarydk.models.transfer_setting import TransferSetting
from salarydk.models.user import User
from salarydk.models.user_company import UserCompany
from salarydk.models.user_company_permissions import UserCompanyPermissions
from salarydk.models.user_department import UserDepartment
from salarydk.models.user_department_response import UserDepartmentResponse
from salarydk.models.user_employee import UserEmployee
from salarydk.models.user_invite import UserInvite
from salarydk.models.user_permission import UserPermission
from salarydk.models.v2_balance_transfer_leave_transfers import V2BalanceTransferLeaveTransfers
from salarydk.models.v2_books_draft_chapters import V2BooksDraftChapters
from salarydk.models.v2_salary_types_supplements import V2SalaryTypesSupplements
from salarydk.models.v2_time_registration_integrations_employees_employees import V2TimeRegistrationIntegrationsEmployeesEmployees
from salarydk.models.v2_time_registration_integrations_employees_salary_types import V2TimeRegistrationIntegrationsEmployeesSalaryTypes
from salarydk.models.v2_time_registration_integrations_registrations_employees import V2TimeRegistrationIntegrationsRegistrationsEmployees
from salarydk.models.v2_time_registration_integrations_registrations_registrations import V2TimeRegistrationIntegrationsRegistrationsRegistrations
from salarydk.models.v2_time_registration_integrations_registrations_salary_types import V2TimeRegistrationIntegrationsRegistrationsSalaryTypes
from salarydk.models.v2_user_invites_departments import V2UserInvitesDepartments
from salarydk.models.vacation_calendar import VacationCalendar
from salarydk.models.vacation_day import VacationDay
from salarydk.models.voucher import Voucher
from salarydk.models.voucher_lines import VoucherLines
from salarydk.models.warning import Warning
