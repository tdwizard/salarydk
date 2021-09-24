# PaySlip

A pay slip
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregates** | [**list[PaySlipAggregates]**](PaySlipAggregates.md) | The period aggregates to include on this pay slip. | [optional] 
**calculations** | [**list[PaySlipCalculations]**](PaySlipCalculations.md) | The detailed calculations of the pay slip, in a machine-readable format. | [optional] 
**department_id** | **str** | The department this pay slip belongs to. | [optional] 
**disposition_date** | **date** | The date the net amount is paid out. | [optional] 
**employee_id** | **str** | The employee this pay slip belongs to. | [optional] 
**fields** | [**list[PaySlipFields]**](PaySlipFields.md) | A list of key-values included on the pay slip. | [optional] 
**id** | **str** | The ID of the pay slip | [optional] [readonly] 
**pay_check** | **float** | The net amount paid out to the employee for this pay slip. | [optional] [readonly] 
**pay_roll_id** | **str** | The pay roll this pay slip belongs to. | [optional] 
**salary_period** | [**SalaryPeriod**](SalaryPeriod.md) |  | [optional] 
**salary_period_id** | **str** | The ID of the period this pay slip belongs to | [optional] [readonly] 
**settled** | **bool** | Whether this pay slip has actually been run, false if the pay slip is a preview of a potential future pay slip. | [optional] 
**termination** | **bool** | Whether this pay slip is the termination pay slip for the employee. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


