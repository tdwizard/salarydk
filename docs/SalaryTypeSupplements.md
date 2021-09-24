# SalaryTypeSupplements

A rule for automatically adding a supplement depending on the time worked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **float** | The number of minutes since Monday 00:00 this interval starts | 
**fixed_supplement** | **float** | The supplement to add for each whole hour worked in the interval | [optional] 
**is_holiday** | **bool** | If true, the &#x60;start&#x60; and &#x60;end&#x60; are relative to a holiday instead of a Monday. | 
**percentage_supplement** | **float** | The supplement to add as a percentage of the base hourly rate for each hour worked in the interval. | [optional] 
**start** | **float** | The number of minutes since Monday 00:00 this interval starts | 
**title** | **str** | The name of the supplement. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


