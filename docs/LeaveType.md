# LeaveType

A leave type is a type of leave an employee can register. This includes days off, vacation, sick days, etc. Most of the fields for a leave type is used when calculating the amount of leave available, and whether to pay out unused days, etc. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignable** | **bool** | If true, this type can be used in contracts. If false, all employees can use this leave type. | [optional] 
**_class** | **str** |  | [optional] 
**company_id** | **str** | The company this leave type is valid for. Each company can have their own leave types. | [optional] [readonly] 
**cycle** | **str** |  | [optional] 
**cycle_start** | **float** |  | [optional] 
**employee_selectable** | **bool** | If true, an employee can select to register leave on. | [optional] 
**excess_type** | **str** |  | [optional] 
**expiry_type** | **str** |  | [optional] 
**id** | **str** | The ID of the leave type. | [optional] [readonly] 
**include_in_pension_basis** | **bool** |  | [optional] 
**max_days** | **float** |  | [optional] 
**min_days** | **float** |  | [optional] 
**name** | **str** | The internal name of this leave type. This is used when registering a leave for an employee. | [optional] [readonly] 
**payout_destination** | **str** |  | [optional] 
**payout_on_termination** | **bool** |  | [optional] 
**payout_type** | **str** |  | [optional] 
**title** | **str** | This is the display name of this leave type. Used when selecting a leave type from a list. | [optional] 
**unit** | **str** |  | [optional] 
**vesting** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


