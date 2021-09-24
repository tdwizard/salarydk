# TimeRegistration

Describes a single time registration for an employee. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the time registration. | [optional] 
**approved** | **bool** | Whether the time registration has been approved by the employer. Only approved registrations are included in the pay roll.  | [optional] [readonly] 
**category** | **str** | Optional category for the time registration | [optional] 
**_class** | **str** | The type of registration. | [optional] 
**cost_center_id** | **str** | The cost center this registration is attached to.  Only for &#x60;class &#x3D; \&quot;Hours&#x60;. | [optional] 
**date** | **date** | The date the time worked occured, or the date the leave happened. | 
**days** | **float** | For registrations of leave held (&#x60;class &#x3D; \&quot;Leave\&quot;&#x60;), this is the number of days held. Normally this is 1.0, but 0.25, 0.50 and 0.75 are also valid values. This can be used to take half a day off work.  | [optional] 
**employee_id** | **str** | The employee for the time registration. | 
**end** | **float** | For time registrations of work done (&#x60;class &#x3D; \&quot;Hours\&quot;&#x60;), this is the number of minutes since midnight (local time) this registration ends. For instance, if it ends at 18:00, this should be set to 1080. If the &#x60;start&#x60; + &#x60;hours&#x60; would be less than &#x60;end&#x60;, then the remaining time is assumed to be breaks. &#x60;end&#x60; cannot be a value so &#x60;start&#x60; + &#x60;hours&#x60; &gt; &#x60;end&#x60;.  | [optional] 
**hours** | **float** | For time registrations of work done (&#x60;class &#x3D; \&quot;Hours\&quot;&#x60;), this is the number of hours worked. | [optional] 
**immutable** | **bool** | Deprecated | [optional] [readonly] 
**leave_type_id** | **str** | For &#x60;class &#x3D; \&quot;Leave\&quot;&#x60;, this indicates the type of leave taken. You can get a list of valid IDs from [GetLeaveTypes](#operation/GetLeaveTypes).  | [optional] 
**minutes** | **float** | For registrations of flex time held (&#x60;class &#x3D; \&quot;Flex\&quot;&#x60;), this is the number of minutes held. This can be used to take a fraction of a day off work.  | [optional] 
**note** | **str** | Optional note the employee and employer can use. | [optional] 
**salary_type_id** | **str** | For &#x60;class &#x3D; \&quot;Hours\&quot;&#x60;, this indicates the type of hours worked. You can get a list of valid IDs from [GetSalaryTypes](#operation/GetSalaryTypes).  | [optional] 
**settled** | **bool** | Deprecated | [optional] [readonly] 
**start** | **float** | For time registrations of work done (&#x60;class &#x3D; \&quot;Hours\&quot;&#x60;), this is the number of minutes since midnight (local time) this registration starts. For instance, if it starts at 10:00, this should be set to 600.  | [optional] 
**state** | **str** | Only when &#x60;Pending&#x60; is the time registration still mutable. | [optional] [readonly] 
**type_name** | **str** | Deprecated. Use salaryTypeID instead. For &#x60;class &#x3D; \&quot;Hours\&quot;&#x60;, this indicates the type of hours worked. You can get a list of valid IDs from [GetSalaryTypes](#operation/GetSalaryTypes).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


