# Employment

An employment describes a relation between a company and an employee.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_book_contract_id** | **str** | If employment is created based on a ContractBook contract, give the ID to link here. | [optional] 
**employee_id** | **str** | The ID of the employee. | [optional] 
**employee_number** | **str** | The employee number of the employee | 
**end_date** | **date** | The end date of the employment. If &#x60;null&#x60;, there is no end date. | [optional] 
**id** | **str** | The ID of the employment | [optional] [readonly] 
**income_type** | **str** | Income type (Danish: \&quot;Indkomsttyper\&quot;) for the employee, as it relates to for which field to report income.  * &#x60;DKSalaryIncome&#x60;: Reported to field 00. * &#x60;DKBIncome&#x60;: Reported to field 05. * &#x60;DKResearchIncome&#x60;: Reported to field 08. * &#x60;DKContributionFree&#x60;: Reported to field 09. * &#x60;DKContributionFreeAM&#x60;: Reported to field 09, but includes AM contribution.  See [SKATs page about \&quot;indkomsttyper\&quot;](https://skat.dk/SKAT.aspx?oid&#x3D;2045876) for more information.  | [optional] [default to 'DKSalaryIncome']
**preferred_tax_card_type** | **str** | The preferred tax card type to use when requesting a tax card from the tax authorities. | 
**settled** | **bool** | Whether the employment has been completely terminated. | [optional] [readonly] 
**start_date** | **date** | The start date of the employment | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


