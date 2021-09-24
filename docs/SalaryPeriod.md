# SalaryPeriod

A salary period describes a single period to perform a salary payout for. A period has a start date, an end date and a disposition date. Within the same cycle, the periods fully cover all days without any overlap. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disposition_date** | **date** | The date the salary should be at disposition for the recipient. | [optional] 
**end** | **date** | The end date of the period | 
**id** | **str** | The ID of the salary period | [optional] [readonly] 
**latest_start_time** | **datetime** | The latest time to start a pay roll run for this period in order to still make it before the deadline. | [optional] 
**start** | **date** | The start date of the period | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


