# CoarseTimeRegistration

A coarse time registration describes the total number of hours and days worked for a period.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | If approved, this registration is included in the pay roll. | [optional] [readonly] 
**company_id** | **str** | The ID of the company for the coarse time registration. | [optional] [readonly] 
**days** | **float** | The total number of different days work were performed. | 
**employee_id** | **str** | The ID of the employee for the coarse time registration. | 
**hours** | **float** | The total number of hours registered for the period. | 
**id** | **str** | The ID of the coarse time registration. | [optional] [readonly] 
**immutable** | **bool** | If true, this coarse time registration can not be changed anylonger, since the pay roll it was included in has completed. | [optional] [readonly] 
**salary_period_id** | **str** | The ID of the salary period for the coarse time registration | 
**salary_type** | **str** | Deprecated. Use salaryTypeID instead. The type of the hours registered. You can get a list of valid salary types from [GetSalaryTypes](#operation/GetSalaryTypes). | 
**salary_type_id** | **str** | The type of the hours registered. You can get a list of valid salary types from [GetSalaryTypes](#operation/GetSalaryTypes). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


