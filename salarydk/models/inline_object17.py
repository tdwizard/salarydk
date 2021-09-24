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


class InlineObject17(object):
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
        'bank_account_number': 'str',
        'bank_registration_number': 'str',
        'contact_email': 'str',
        'contact_name': 'str',
        'contact_phone': 'str'
    }

    attribute_map = {
        'bank_account_number': 'bankAccountNumber',
        'bank_registration_number': 'bankRegistrationNumber',
        'contact_email': 'contactEmail',
        'contact_name': 'contactName',
        'contact_phone': 'contactPhone'
    }

    def __init__(self, bank_account_number=None, bank_registration_number=None, contact_email=None, contact_name=None, contact_phone=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject17 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bank_account_number = None
        self._bank_registration_number = None
        self._contact_email = None
        self._contact_name = None
        self._contact_phone = None
        self.discriminator = None

        self.bank_account_number = bank_account_number
        self.bank_registration_number = bank_registration_number
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_phone = contact_phone

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this InlineObject17.  # noqa: E501


        :return: The bank_account_number of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this InlineObject17.


        :param bank_account_number: The bank_account_number of this InlineObject17.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bank_account_number is None:  # noqa: E501
            raise ValueError("Invalid value for `bank_account_number`, must not be `None`")  # noqa: E501

        self._bank_account_number = bank_account_number

    @property
    def bank_registration_number(self):
        """Gets the bank_registration_number of this InlineObject17.  # noqa: E501


        :return: The bank_registration_number of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._bank_registration_number

    @bank_registration_number.setter
    def bank_registration_number(self, bank_registration_number):
        """Sets the bank_registration_number of this InlineObject17.


        :param bank_registration_number: The bank_registration_number of this InlineObject17.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bank_registration_number is None:  # noqa: E501
            raise ValueError("Invalid value for `bank_registration_number`, must not be `None`")  # noqa: E501

        self._bank_registration_number = bank_registration_number

    @property
    def contact_email(self):
        """Gets the contact_email of this InlineObject17.  # noqa: E501


        :return: The contact_email of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this InlineObject17.


        :param contact_email: The contact_email of this InlineObject17.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def contact_name(self):
        """Gets the contact_name of this InlineObject17.  # noqa: E501


        :return: The contact_name of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this InlineObject17.


        :param contact_name: The contact_name of this InlineObject17.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this InlineObject17.  # noqa: E501


        :return: The contact_phone of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this InlineObject17.


        :param contact_phone: The contact_phone of this InlineObject17.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

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
        if not isinstance(other, InlineObject17):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject17):
            return True

        return self.to_dict() != other.to_dict()
