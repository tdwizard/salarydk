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


class InlineObject29(object):
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
        'document_category_id': 'str',
        'employee_id': 'str',
        'file_id': 'str',
        'name': 'str',
        'visible_for_employee': 'bool'
    }

    attribute_map = {
        'document_category_id': 'documentCategoryID',
        'employee_id': 'employeeID',
        'file_id': 'fileID',
        'name': 'name',
        'visible_for_employee': 'visibleForEmployee'
    }

    def __init__(self, document_category_id=None, employee_id=None, file_id=None, name=None, visible_for_employee=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject29 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document_category_id = None
        self._employee_id = None
        self._file_id = None
        self._name = None
        self._visible_for_employee = None
        self.discriminator = None

        self.document_category_id = document_category_id
        self.employee_id = employee_id
        self.file_id = file_id
        self.name = name
        self.visible_for_employee = visible_for_employee

    @property
    def document_category_id(self):
        """Gets the document_category_id of this InlineObject29.  # noqa: E501


        :return: The document_category_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._document_category_id

    @document_category_id.setter
    def document_category_id(self, document_category_id):
        """Sets the document_category_id of this InlineObject29.


        :param document_category_id: The document_category_id of this InlineObject29.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_category_id is None:  # noqa: E501
            raise ValueError("Invalid value for `document_category_id`, must not be `None`")  # noqa: E501

        self._document_category_id = document_category_id

    @property
    def employee_id(self):
        """Gets the employee_id of this InlineObject29.  # noqa: E501


        :return: The employee_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this InlineObject29.


        :param employee_id: The employee_id of this InlineObject29.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and employee_id is None:  # noqa: E501
            raise ValueError("Invalid value for `employee_id`, must not be `None`")  # noqa: E501

        self._employee_id = employee_id

    @property
    def file_id(self):
        """Gets the file_id of this InlineObject29.  # noqa: E501

        ID of the uploaded file to use  # noqa: E501

        :return: The file_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this InlineObject29.

        ID of the uploaded file to use  # noqa: E501

        :param file_id: The file_id of this InlineObject29.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def name(self):
        """Gets the name of this InlineObject29.  # noqa: E501


        :return: The name of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject29.


        :param name: The name of this InlineObject29.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def visible_for_employee(self):
        """Gets the visible_for_employee of this InlineObject29.  # noqa: E501


        :return: The visible_for_employee of this InlineObject29.  # noqa: E501
        :rtype: bool
        """
        return self._visible_for_employee

    @visible_for_employee.setter
    def visible_for_employee(self, visible_for_employee):
        """Sets the visible_for_employee of this InlineObject29.


        :param visible_for_employee: The visible_for_employee of this InlineObject29.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and visible_for_employee is None:  # noqa: E501
            raise ValueError("Invalid value for `visible_for_employee`, must not be `None`")  # noqa: E501

        self._visible_for_employee = visible_for_employee

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
        if not isinstance(other, InlineObject29):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject29):
            return True

        return self.to_dict() != other.to_dict()
