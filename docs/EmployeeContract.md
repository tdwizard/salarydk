# EmployeeContract

A contract describes the salary, benefits, etc that an employee is getting as part of his employment. Over time, the contract might change within the same employment, but there can never be two active contacts at the same time within a single employment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_salary_amount** | **float** | The amount to show as salary next to each employee. Is calculated from the salary definitions of the remuneration | [optional] 
**car_allowance_rate** | **float** | Override of the default car allowance rate. | [optional] 
**car_allowance_registration_method_type** | **str** | The method used when registering car allowance in the frontend for this employee. | [optional] [default to 'Detailed']
**company_id** | **str** | The ID of the company. | [optional] [readonly] 
**contract_template_id** | **str** | The template that created this contract | [optional] 
**day_laborer** | **str** | Determines whether the employee is a day laborer or not. If the employee is a day laborer, it also determines how vacation days are calculated. | [optional] 
**employee_id** | **str** | The ID of the employee. | [optional] [readonly] 
**employment_id** | **str** | The ID of the employment. | 
**employment_position_id** | **str** | The ID of the standard employment position the employee has in the company. | [optional] 
**employment_type** | **str** | The employment type. | [optional] [default to 'Ordinary']
**extra_tax_percentage** | **int** | Extra tax percentage to deduct from salary. | [optional] 
**family_leave_fund** | **str** | The choice of family leave fund. If not set Barsel.dk is used. | [optional] [default to 'DK Barsel.dk']
**id** | **str** | The ID of the contract. | [optional] [readonly] 
**manual_vacation_fund** | **bool** | Determines whether or not the vacation fund CVR is manual or not. | [optional] 
**period_work_hours** | **float** | Override of the number of work hours to report for each period. | [optional] 
**position** | **str** | A description of the position the employee has in the company. | [optional] 
**production_unit_id** | **str** | The ID of the production unit this employee is working at.  IDs for production units can be obtained through [GetCompanies](#operation/GetCompanies). | 
**remuneration** | [**Remuneration**](Remuneration.md) |  | [optional] 
**remuneration_type** | **str** | The remuneration type of the contract. Is calculated from the salary definitions of the remuneration | [optional] 
**salary_cycle_id** | **str** | The ID of the salary cycle this contract follows. | 
**time_registration_method_type** | **str** | The method used when registering hours in the frontend for this employee. | 
**vacation_fund_cvr** | **str** | Override the CVR number of the vacation fund. | [optional] 
**valid_from** | **date** | The start of the validity period of this contract. | 
**valid_to** | **date** | The end of the validity period of this contract, if any. | [optional] [readonly] 
**weekly_hours** | **float** | The number of hours the employee is at work in a normal week. | 
**weekly_work_days** | **float** | The number of days the employee is at work in a normal week. | [optional] 
**work_schedule** | **str** | The strategy to use for default hours set in new periods for hourly employees. | [optional] [default to 'None']
**work_week** | **list[str]** | Defines the work week for the given employee. It is a list of week days. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


