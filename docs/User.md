# User

Describes a user of Salary.dk.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the user. Also used as user name when logging in. | 
**email_verified_at** | **datetime** | Timestamp for when email was last verified. | [optional] 
**id** | **str** | The ID of the user | [optional] [readonly] 
**language** | **str** | Preferred language of the user. | 
**mfa_channel** | **str** | Preferred MFA channel of the user. | 
**name** | **str** | The full name of the user. | [optional] 
**password** | **str** | The password of the user. Can only be set, will never be returned in calls. | 
**phone_number** | **str** | The phone number of the user, without country code. | [optional] 
**phone_number_country_code** | **str** | The country code of the phone number of the user. | [optional] 
**profile_image_url** | **str** | An URL for the profile image of the user. | [optional] 
**user_type** | **str** | Type of user | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


