# Employee

An employee
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_employment** | [**Employment**](Employment.md) |  | [optional] 
**address** | **str** | The address of the employee.  Required if &#x60;onboardingState&#x60; &#x3D; &#x60;Final&#x60;. | [optional] 
**affiliation_type** | **str** | The affiliation type of the employee to the company. | 
**bank_account_number** | **str** | The bank account number of the employee, restricted to 10 characters for &#x60;DK Account&#x60;. | [optional] 
**bank_registration_number** | **str** | The bank registration number of the employee, restricted to 4 characters for &#x60;DK Account&#x60;. | [optional] 
**birth_date** | **date** | The birth date of the employee. Used when &#x60;nationalIDType&#x60; &#x3D; &#x60;DK Foreign&#x60; for tax reporting. | [optional] 
**calendar_feed_key** | **str** | A key to a vacation calendar feed for this employee. | [optional] 
**city** | **str** | The city of the employee.  Required if &#x60;onboardingState&#x60; &#x3D; &#x60;Final&#x60;. | [optional] 
**company_id** | **str** | The ID of the company for this employee. | [optional] 
**country** | **str** | The ISO-3166 code for the country of where the employee lives.  If not provided, it will default to &#x60;DK&#x60;.  Used when &#x60;nationalIDType&#x60; &#x3D; &#x60;DK Foreign&#x60; for tax reporting.  | [optional] [default to 'DK']
**department_id** | **str** | The ID of the department of the employee | [optional] 
**earliest_mutable_contract** | [**EmployeeContract**](EmployeeContract.md) |  | [optional] 
**email** | **str** | The e-mail of the employee. | [optional] 
**employment_status** | **str** | The current status of the employment for this employee. | [optional] [readonly] 
**gender** | **str** | The gender of the employee. Used when &#x60;nationalIDType&#x60; &#x3D; &#x60;DK Foreign&#x60; for tax reporting. | [optional] 
**has_pdf_password** | **bool** | Whether this employee has a custom PDF Password | [optional] [readonly] 
**has_swipe** | **bool** | Determines wether or not this employee has access to swipe. | [optional] 
**has_user** | **bool** | Shows whether this employee has a login user for the employee app. | [optional] [readonly] 
**id** | **str** | The ID of the employee | [optional] [readonly] 
**immutable_end_date** | **date** | The contract can not be edited before this date. | [optional] [readonly] 
**language** | **str** | The preferred language of the employee, for the purpose of pay slips and other documents sent to the employee, only Danish and English are supported. | 
**locked_end_date** | **date** | The contract is locked up to this date. An edit before this date will recalcuate any pay rolls locking this contract. | [optional] [readonly] 
**name** | **str** | The full name of the employee.  Required if &#x60;onboardingState&#x60; &#x3D; &#x60;Final&#x60;. | [optional] 
**national_id** | **str** | National Identification Number.  See &#x60;nationalIDType&#x60; to change its meaning. | [optional] 
**national_id_type** | **str** | The type of the National Identification Number.  * &#x60;DK CPR&#x60;: Is someone living in Denmark with a Danish CPR. * &#x60;DK CVR&#x60;: Is a company in Denmark with a Danish CVR. * &#x60;DK Foreign&#x60;: Is someone living abroad, but with a Danish CPR. * &#x60;DK No CPR&#x60;: Someone without a Danish CPR.  For &#x60;DK CPR&#x60;, &#x60;DK CVR&#x60; or &#x60;DK Foreign&#x60;, the field &#x60;nationalID&#x60; must be supplied. For &#x60;DK Foreign&#x60;, the fields &#x60;gender&#x60;, &#x60;country&#x60; and &#x60;birthDate&#x60; must also be supplied. For &#x60;DK No CPR&#x60;, &#x60;nationalID&#x60; should remain empty.  | [optional] [default to 'DK CPR']
**onboarding_state** | **str** | When using self-onboarding, an employee is in state &#39;Draft&#39; until the employee has entered all information.  This requires the onboarding feature for the company to be active, otherwise setting it to &#x60;Draft&#x60; will result in an error.  | [optional] [default to 'Final']
**paid_out_this_year** | **float** | Total salary amount paid out this year to date (i.e. after taxes) | [optional] [readonly] 
**pay_slip_transport_e_mail** | **bool** | Send payslip to employee via email. | [optional] 
**pay_slip_transport_national_inbox** | **bool** | Send payslip to employee via national solution (eboks). | [optional] 
**pay_slip_transport_sms** | **bool** | Send payslip information via SMS. | [optional] 
**phone_number** | **str** | The phone number without country code for the employee. | [optional] 
**phone_number_country_code** | **str** | The country code of the phone number of the employee. | [optional] 
**postal_code** | **str** | The postal code of the employee.  Required if &#x60;onboardingState&#x60; &#x3D; &#x60;Final&#x60;. | [optional] 
**profile_image_url** | **str** | URL to a profile image of the employee | [optional] [readonly] 
**transfer_destination_type** | **str** | The type of the destination for the salary pay out for this employee. | [optional] [default to 'None']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


