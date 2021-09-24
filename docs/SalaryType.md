# SalaryType

A type of salary. This is used when registering hours, since an employee might have several different hourly rates. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the salary type is available for new employees. | 
**_class** | **str** | The type of the salary type. Only salary types with &#x60;Hourly&#x60; can be used for registering hours. | 
**company_id** | **str** | The company this salary type is valid for. Different companies might have different valid types. | [optional] [readonly] 
**id** | **str** | The ID of the salary type. | [optional] [readonly] 
**name** | **str** | The internal name of the salary type. This is used when registering hours for an employee. | [optional] [readonly] 
**supplements** | [**list[SalaryTypeSupplements]**](SalaryTypeSupplements.md) |  | [optional] 
**title** | **str** | The display name of the salary type. This is used when selecting a salary type from a list. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


