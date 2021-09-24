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


class AccountingIntegrationSetup(object):
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
        'account_mapping': 'list[AccountConfiguration]',
        'api_id': 'str',
        'api_key': 'str',
        'api_secret': 'str',
        'auth_parameters': 'list[AccountingIntegrationSetupAuthParameters]',
        'daybook_id': 'str',
        'dimension_id': 'str',
        'next': 'str',
        'organization_id': 'str',
        'password': 'str',
        'use_dimensions': 'str',
        'username': 'str'
    }

    attribute_map = {
        'account_mapping': 'accountMapping',
        'api_id': 'apiID',
        'api_key': 'apiKey',
        'api_secret': 'apiSecret',
        'auth_parameters': 'authParameters',
        'daybook_id': 'daybookID',
        'dimension_id': 'dimensionID',
        'next': 'next',
        'organization_id': 'organizationID',
        'password': 'password',
        'use_dimensions': 'useDimensions',
        'username': 'username'
    }

    def __init__(self, account_mapping=None, api_id=None, api_key=None, api_secret=None, auth_parameters=None, daybook_id=None, dimension_id=None, next=None, organization_id=None, password=None, use_dimensions=None, username=None, local_vars_configuration=None):  # noqa: E501
        """AccountingIntegrationSetup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_mapping = None
        self._api_id = None
        self._api_key = None
        self._api_secret = None
        self._auth_parameters = None
        self._daybook_id = None
        self._dimension_id = None
        self._next = None
        self._organization_id = None
        self._password = None
        self._use_dimensions = None
        self._username = None
        self.discriminator = None

        if account_mapping is not None:
            self.account_mapping = account_mapping
        self.api_id = api_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.auth_parameters = auth_parameters
        self.daybook_id = daybook_id
        self.dimension_id = dimension_id
        self.next = next
        self.organization_id = organization_id
        self.password = password
        self.use_dimensions = use_dimensions
        self.username = username

    @property
    def account_mapping(self):
        """Gets the account_mapping of this AccountingIntegrationSetup.  # noqa: E501


        :return: The account_mapping of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: list[AccountConfiguration]
        """
        return self._account_mapping

    @account_mapping.setter
    def account_mapping(self, account_mapping):
        """Sets the account_mapping of this AccountingIntegrationSetup.


        :param account_mapping: The account_mapping of this AccountingIntegrationSetup.  # noqa: E501
        :type: list[AccountConfiguration]
        """

        self._account_mapping = account_mapping

    @property
    def api_id(self):
        """Gets the api_id of this AccountingIntegrationSetup.  # noqa: E501


        :return: The api_id of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this AccountingIntegrationSetup.


        :param api_id: The api_id of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._api_id = api_id

    @property
    def api_key(self):
        """Gets the api_key of this AccountingIntegrationSetup.  # noqa: E501


        :return: The api_key of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this AccountingIntegrationSetup.


        :param api_key: The api_key of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def api_secret(self):
        """Gets the api_secret of this AccountingIntegrationSetup.  # noqa: E501


        :return: The api_secret of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this AccountingIntegrationSetup.


        :param api_secret: The api_secret of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._api_secret = api_secret

    @property
    def auth_parameters(self):
        """Gets the auth_parameters of this AccountingIntegrationSetup.  # noqa: E501


        :return: The auth_parameters of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: list[AccountingIntegrationSetupAuthParameters]
        """
        return self._auth_parameters

    @auth_parameters.setter
    def auth_parameters(self, auth_parameters):
        """Sets the auth_parameters of this AccountingIntegrationSetup.


        :param auth_parameters: The auth_parameters of this AccountingIntegrationSetup.  # noqa: E501
        :type: list[AccountingIntegrationSetupAuthParameters]
        """

        self._auth_parameters = auth_parameters

    @property
    def daybook_id(self):
        """Gets the daybook_id of this AccountingIntegrationSetup.  # noqa: E501


        :return: The daybook_id of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._daybook_id

    @daybook_id.setter
    def daybook_id(self, daybook_id):
        """Sets the daybook_id of this AccountingIntegrationSetup.


        :param daybook_id: The daybook_id of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._daybook_id = daybook_id

    @property
    def dimension_id(self):
        """Gets the dimension_id of this AccountingIntegrationSetup.  # noqa: E501


        :return: The dimension_id of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        """Sets the dimension_id of this AccountingIntegrationSetup.


        :param dimension_id: The dimension_id of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._dimension_id = dimension_id

    @property
    def next(self):
        """Gets the next of this AccountingIntegrationSetup.  # noqa: E501

        Force a new step and then do other actions accordingly (can only go back, not skip steps)  # noqa: E501

        :return: The next of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this AccountingIntegrationSetup.

        Force a new step and then do other actions accordingly (can only go back, not skip steps)  # noqa: E501

        :param next: The next of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"NeedKey", "NeedAuth", "ChooseOrganization", "ChooseDaybook", "ChooseDimension", "ChooseToUseDimensions", "MapAccounts", "Done"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and next not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `next` ({0}), must be one of {1}"  # noqa: E501
                .format(next, allowed_values)
            )

        self._next = next

    @property
    def organization_id(self):
        """Gets the organization_id of this AccountingIntegrationSetup.  # noqa: E501


        :return: The organization_id of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this AccountingIntegrationSetup.


        :param organization_id: The organization_id of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def password(self):
        """Gets the password of this AccountingIntegrationSetup.  # noqa: E501


        :return: The password of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AccountingIntegrationSetup.


        :param password: The password of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def use_dimensions(self):
        """Gets the use_dimensions of this AccountingIntegrationSetup.  # noqa: E501

        Whether to use dimensions, and if so, whether to be mapped to departments or cost centers  # noqa: E501

        :return: The use_dimensions of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._use_dimensions

    @use_dimensions.setter
    def use_dimensions(self, use_dimensions):
        """Sets the use_dimensions of this AccountingIntegrationSetup.

        Whether to use dimensions, and if so, whether to be mapped to departments or cost centers  # noqa: E501

        :param use_dimensions: The use_dimensions of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"No", "Departments", "CostCenters"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and use_dimensions not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `use_dimensions` ({0}), must be one of {1}"  # noqa: E501
                .format(use_dimensions, allowed_values)
            )

        self._use_dimensions = use_dimensions

    @property
    def username(self):
        """Gets the username of this AccountingIntegrationSetup.  # noqa: E501


        :return: The username of this AccountingIntegrationSetup.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AccountingIntegrationSetup.


        :param username: The username of this AccountingIntegrationSetup.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, AccountingIntegrationSetup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountingIntegrationSetup):
            return True

        return self.to_dict() != other.to_dict()