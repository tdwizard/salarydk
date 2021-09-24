# SalaryCycle

A salary cycle describes a frequency period for a pay roll. `BiWeekly` is 14 days.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disposition_date_rule** | **str** | For &#x60;PeriodEnd&#x60;, the disposition date is on the last banking day within the periods of the cycle. For &#x60;MonthEnd&#x60;, the disposition date is on the last banking day of the month where the end of the cycle is. For instance, if the cycle ends on 2018-09-15, the disposition date would be 2018-09-28.  | [optional] 
**frequency** | **str** | How long each period in the cycle is before the next period begins. | [optional] [readonly] 
**id** | **str** | The ID of the salary cycle. | [optional] [readonly] 
**offset** | **int** | If present, this number indicates an offset period. For instance, an offset of 10 for a cycle with &#x60;frequency&#x3D;Monthly&#x60; would cover the 10th in the month to the 9th of the next month, instead of from the 1st to the last of the month.  | [optional] 
**prepaid** | **bool** | If true, salary in this cycle is prepaid, meaning the disposition date is before the cycle starts. If false, salary is at the end of the cycle - often on the last banking day in the cycle.  | [optional] [readonly] 
**salary_periods** | [**list[SalaryPeriod]**](SalaryPeriod.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


