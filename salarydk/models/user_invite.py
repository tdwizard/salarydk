# coding: utf-8

"""
    Salary.dk API

    This is the public API for Salary.dk.  # General  Our API is a JSON-based, REST-like API. Our webapp uses the exact same API, so everything you can do in our webapp, you can do through our API. However, we are slowly opening up the API, so not all endpoints are documented here yet. Only the endpoints documented here are stable. If there is some functionality you would like to access through our API, please contact us.  The API is located at https://api.salary.dk. All requests must use TLS.  In order to use the API on behalf of other users than yourself, you need to register as an API client. You do this by sending an e-mail to dev@salary.dk with the name and purpose of your client.  API-keys for each account can be obtained once logged in to Salary, under the settings for the Company.  All endpoints are documented to be able to return the 500 error code. We strive to not return this error code, so if you do encounter this error code, it might mean there is an error on our side. In this case, do not hesitate to contact us.  # Versioning, upgrade and deprecation policy Our API might change over time. In order to ensure a stable API, we follow these rules when changing the API.  New fields might be added at any time to any response or as non-required parameters to any input. When adding input fields, we ensure the default behaviour when not supplying the field is the same as the previous version. In these cases, the version of an endpoint is not increased, since it is backwards compatible. Since we might add new fields to responses, be sure to use a JSON parser in your implementation. This ensures that any extra fields added are ignored by your implementation.  We might add entirely new endpoints at any time. If we need to change an existing endpoint without being able to make it backwards compatible, we will add a new version of the endpoint, and mark the old as deprecated but still functional. We will then contact any users of the deprecated endpoint and ensure an upgrade is performed. Once all consumers have moved to the new endpoint version, the old one will be removed.  We will not at any point change the meaning of any existing field, nor will we remove any field or endpoint without following the above deprecated procedure. However, we might add new types to existing enums at any time.  # Cross-Origin Resource Sharing This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/) - and that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site, as long as the proper access token is passed.  # Authentication All request require an access token. There are two ways to obtain an access token: * Logging in as a user. (this endpoint is not yet publicly available). * Using an API-key: [endpoint](#operation/APIClientLogin)  Using one of these methods, you will obtain an access token. In all subsequest requests, this access token should be passed in the Authorization header. The access token is valid for around one hour, after which a new token should be obtained.  You do not need to dispose of access tokens once created. They have a limited lifetime, and Salary.dk will automatically expire old ones.  For some endpoints, the authorizedUserQuery security definition is used. This allows for passing the access token as a query parameter where it is not possible to pass it as a header. In particular, this is used for downloading files.  <!-- ReDoc-Inject: <security-definitions> -->   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@salary.dk
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from salarydk.configuration import Configuration


class UserInvite(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'company_group_id': 'str',
        'company_id': 'str',
        'created_at': 'datetime',
        'departments': 'list[V2UserInvitesDepartments]',
        'email': 'str',
        'group_user_type': 'str',
        'permissions': 'list[str]',
        'user_type': 'str'
    }

    attribute_map = {
        'company_group_id': 'companyGroupID',
        'company_id': 'companyID',
        'created_at': 'createdAt',
        'departments': 'departments',
        'email': 'email',
        'group_user_type': 'groupUserType',
        'permissions': 'permissions',
        'user_type': 'userType'
    }

    def __init__(self, company_group_id=None, company_id=None, created_at=None, departments=None, email=None, group_user_type=None, permissions=None, user_type=None, local_vars_configuration=None):  # noqa: E501
        """UserInvite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company_group_id = None
        self._company_id = None
        self._created_at = None
        self._departments = None
        self._email = None
        self._group_user_type = None
        self._permissions = None
        self._user_type = None
        self.discriminator = None

        if company_group_id is not None:
            self.company_group_id = company_group_id
        if company_id is not None:
            self.company_id = company_id
        if created_at is not None:
            self.created_at = created_at
        if departments is not None:
            self.departments = departments
        if email is not None:
            self.email = email
        if group_user_type is not None:
            self.group_user_type = group_user_type
        if permissions is not None:
            self.permissions = permissions
        if user_type is not None:
            self.user_type = user_type

    @property
    def company_group_id(self):
        """Gets the company_group_id of this UserInvite.  # noqa: E501


        :return: The company_group_id of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._company_group_id

    @company_group_id.setter
    def company_group_id(self, company_group_id):
        """Sets the company_group_id of this UserInvite.


        :param company_group_id: The company_group_id of this UserInvite.  # noqa: E501
        :type: str
        """

        self._company_group_id = company_group_id

    @property
    def company_id(self):
        """Gets the company_id of this UserInvite.  # noqa: E501


        :return: The company_id of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this UserInvite.


        :param company_id: The company_id of this UserInvite.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def created_at(self):
        """Gets the created_at of this UserInvite.  # noqa: E501


        :return: The created_at of this UserInvite.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserInvite.


        :param created_at: The created_at of this UserInvite.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def departments(self):
        """Gets the departments of this UserInvite.  # noqa: E501

        This is a list of department ids and their corresponding permissions. This list is optional and not required.  # noqa: E501

        :return: The departments of this UserInvite.  # noqa: E501
        :rtype: list[V2UserInvitesDepartments]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this UserInvite.

        This is a list of department ids and their corresponding permissions. This list is optional and not required.  # noqa: E501

        :param departments: The departments of this UserInvite.  # noqa: E501
        :type: list[V2UserInvitesDepartments]
        """

        self._departments = departments

    @property
    def email(self):
        """Gets the email of this UserInvite.  # noqa: E501


        :return: The email of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInvite.


        :param email: The email of this UserInvite.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def group_user_type(self):
        """Gets the group_user_type of this UserInvite.  # noqa: E501

        The invited user type, if company group.  # noqa: E501

        :return: The group_user_type of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._group_user_type

    @group_user_type.setter
    def group_user_type(self, group_user_type):
        """Sets the group_user_type of this UserInvite.

        The invited user type, if company group.  # noqa: E501

        :param group_user_type: The group_user_type of this UserInvite.  # noqa: E501
        :type: str
        """
        allowed_values = ["Admin", "Regular"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and group_user_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `group_user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(group_user_type, allowed_values)
            )

        self._group_user_type = group_user_type

    @property
    def permissions(self):
        """Gets the permissions of this UserInvite.  # noqa: E501

        If no permissions are set, it is assumed to be Manager for company.  For company group, this permission list is for when they are added to companies.  # noqa: E501

        :return: The permissions of this UserInvite.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserInvite.

        If no permissions are set, it is assumed to be Manager for company.  For company group, this permission list is for when they are added to companies.  # noqa: E501

        :param permissions: The permissions of this UserInvite.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Admin", "Manager", "ApprovePayRoll", "ReviewPayRoll", "ReadOnly"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(permissions).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

    @property
    def user_type(self):
        """Gets the user_type of this UserInvite.  # noqa: E501

        The invited user type, if company.  # noqa: E501

        :return: The user_type of this UserInvite.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UserInvite.

        The invited user type, if company.  # noqa: E501

        :param user_type: The user_type of this UserInvite.  # noqa: E501
        :type: str
        """
        allowed_values = ["Business", "Accountant", "InternalSalaryAdministrator", "ExternalSalaryAdministrator", "BookKeeper"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and user_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInvite):
            return True

        return self.to_dict() != other.to_dict()
