# Company

A company
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**da_union_code** | **float** | The DA Union code for this company. | [optional] 
**accounting_manual_payment_always_asset** | **bool** | Determines whether manual payments are from asset. | [optional] [default to True]
**accounting_vacation_liability** | **bool** | Determines whether or not accounting for vacation liability is enabled. | [optional] [default to False]
**active_employee_cap** | **float** | The limit to how many active employees this company can have, if null, then there is no limit | [optional] 
**address** | **str** | The address of the company | 
**allow_custom_pdf_passwords** | **bool** | Determines whether or not custom PDF Passwords can be set for employees. | [optional] [default to False]
**allow_empty_tax_card_mail** | **bool** | Determines whether or not a mail may be sent to employees when we receive an empty tax card. | [optional] [default to True]
**allow_pay_roll_review** | **bool** | Whether to allow pay rolls to be reviewed | [optional] 
**auto_approve_car_allowances** | **bool** | If true, all car allowances registered by employees are approved when registered. | [optional] [default to False]
**auto_approve_compensations** | **bool** | If true, all compensations sent for approval by employees are approved when sent for approval. | [optional] [default to False]
**auto_approve_reimbursement_vouchers** | **bool** | If true, all reimbursement vouchers sent for approval by employees are approved when sent for approval. | [optional] [default to False]
**auto_approve_time_registration_hours** | **bool** | If true, all hours registered by employees are approved when registered. | [optional] [default to False]
**bank_account_number** | **str** | The bank account number for paying salary | [optional] [readonly] 
**bank_registration_number** | **str** | The bank registration number for paying salary | [optional] [readonly] 
**city** | **str** | The city of the company | 
**cost_center_accounting** | **str** | Whether cost center accounting is active. | [optional] [readonly] 
**created_at** | **datetime** | Timestamp for creation of the company in Salary.dk | [optional] [readonly] 
**default_biweekly_cycle_id** | **str** | The default biweekly cycle to use for new biweekly employees. | [optional] 
**default_hourly_monthly_cycle_id** | **str** | The default monthly cycle to use for new hourly monthly employees. | [optional] 
**dk_specific** | [**CompanyDkSpecific**](CompanyDkSpecific.md) |  | [optional] 
**employee_count** | **int** | The number of employees in this company | [optional] 
**enable_absence_statistics** | **bool** | Determines whether or not automatic absence statistics reporting is enabled. | [optional] [default to False]
**enable_always_current_pay_roll_run** | **bool** | When offset periods have ended, but their disposition date have not yet been reached, the following pay roll run will not have started.  Enabling this will start one, so there is always a current (calendar date wise) pay roll run. | [optional] [default to False]
**enable_early_payments** | **bool** | Determines whether or not payments should be made as early as possible. | [optional] [default to False]
**enable_immediate_pay** | **bool** | Determines whether or not the immediate pay feature is enabled. | [optional] [default to False]
**enable_negating_pay_rolls** | **bool** | Determines whether or not the negating pay roll feature is enabled. | [optional] [default to False]
**enable_nem_konto_transfers** | **bool** | Determines whether or not the nem konto transfer feature is enabled. | [optional] [default to False]
**enable_otp_accounting_text** | **bool** | Determines whether or not the accounting text on one time pays feature is enabled. | [optional] [default to False]
**enable_quarterly_salary_statistics** | **bool** | Determines whether or not automatic quarterly salary statistics reporting is enabled. | [optional] [default to False]
**enable_swipe** | **bool** | Determines whether or not swipe is enabled. | [optional] [default to False]
**enable_yearly_salary_statistics** | **bool** | Determines whether or not automatic yearly salary statistics reporting is enabled. | [optional] [default to False]
**family_leave_fund** | **str** | The choice of family leave fund. If not set Barsel.dk is used. | [optional] [default to 'DK Barsel.dk']
**id** | **str** | The ID of the company. | [optional] [readonly] 
**limit_i_calendar_to_departments** | **str** | How much can the employee see when using the icalendar feed | [optional] 
**name** | **str** | The name of the company | 
**national_id** | **str** | National identification number. For Denmark, this is equivalent to CVR-number. | 
**next_available_employee_number** | **int** | The next available employee number. | [optional] [readonly] 
**number_of_basic_approvers** | **float** | The number of basic approvers is the number of required approvers for one time pays, time registrations and car allowances. Default is one. | [optional] 
**number_of_pay_roll_approvers** | **float** | The number of pay roll approvers is the number of required approvers for pay rolls to be approved. Default is one. | [optional] 
**number_of_pay_roll_reviewers** | **float** | The number of pay roll reviewers is the number of required reviewers for pay rolls to be approved. Default is zero. | [optional] 
**offset_disposition_bi_weekly** | **str** | Offset the disposition date for bi-weekly periods | [optional] [default to 'PeriodEnd']
**offset_disposition_weekly** | **str** | Offset the disposition date for weekly periods | [optional] [default to 'PeriodEnd']
**pay_slip_questions_link** | **str** | The URL of the link to show on pay slips, if visible. | [optional] 
**pay_slip_questions_visible** | **bool** | Whether to show a link on the pay slips for questions or not. | [optional] 
**pending_invite_count** | **int** | The number of pending invites for this company | [optional] 
**periodic_limit_for_immediate_pay_out** | **float** | The periodic limit for immediate pay out common for both Swipe and immediate pay (each employee has this limit regardless of period). | [optional] 
**postal_code** | **str** | The postal code of the company | 
**primary_color** | **str** | The primary color of the company, based on the company logo | [optional] 
**production_units** | [**list[ProductionUnit]**](ProductionUnit.md) | A list of production units for the company. | 
**rule_pay_roll_run_approval** | **str** | How to handle pay roll approval | 
**settings_enabled** | [**list[CompanySettingBoolean]**](CompanySettingBoolean.md) | List of enabled settings (disabled settings do not appear). | [optional] 
**state** | **str** | The state of the company. Only &#x60;active&#x60; companies can perform pay rolls. | [optional] 
**swipe_employee_types** | **list[str]** | When Swipe is enabled, the list of employee types it is enabled for. | [optional] 
**swipe_notification_at** | **float** | When one or more users have notification for Swipe enabled, at what hour during the day should it be sent. | [optional] 
**user_count** | **int** | The number of users with access to this company | [optional] 
**vacation_excess_limit** | **float** | Determines whether or not excess vacation is allowed and the limit. | [optional] 
**verified** | **bool** | (deprecated) Is the company verified, and may perform reporting through the system? | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


