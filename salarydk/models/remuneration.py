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


class Remuneration(object):
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
        'benefits': 'list[RemunerationBenefits]',
        'id': 'str',
        'leave': 'list[RemunerationLeave]',
        'pension': 'list[RemunerationPension]',
        'salary': 'list[SalaryDefinition]',
        'supplements': 'list[RemunerationSupplements]'
    }

    attribute_map = {
        'benefits': 'benefits',
        'id': 'id',
        'leave': 'leave',
        'pension': 'pension',
        'salary': 'salary',
        'supplements': 'supplements'
    }

    def __init__(self, benefits=None, id=None, leave=None, pension=None, salary=None, supplements=None, local_vars_configuration=None):  # noqa: E501
        """Remuneration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._benefits = None
        self._id = None
        self._leave = None
        self._pension = None
        self._salary = None
        self._supplements = None
        self.discriminator = None

        self.benefits = benefits
        if id is not None:
            self.id = id
        self.leave = leave
        self.pension = pension
        self.salary = salary
        self.supplements = supplements

    @property
    def benefits(self):
        """Gets the benefits of this Remuneration.  # noqa: E501

        A list of all the benefits.  # noqa: E501

        :return: The benefits of this Remuneration.  # noqa: E501
        :rtype: list[RemunerationBenefits]
        """
        return self._benefits

    @benefits.setter
    def benefits(self, benefits):
        """Sets the benefits of this Remuneration.

        A list of all the benefits.  # noqa: E501

        :param benefits: The benefits of this Remuneration.  # noqa: E501
        :type: list[RemunerationBenefits]
        """
        if self.local_vars_configuration.client_side_validation and benefits is None:  # noqa: E501
            raise ValueError("Invalid value for `benefits`, must not be `None`")  # noqa: E501

        self._benefits = benefits

    @property
    def id(self):
        """Gets the id of this Remuneration.  # noqa: E501

        The ID of the remuneration.  # noqa: E501

        :return: The id of this Remuneration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Remuneration.

        The ID of the remuneration.  # noqa: E501

        :param id: The id of this Remuneration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def leave(self):
        """Gets the leave of this Remuneration.  # noqa: E501

        A list of all leave types.  # noqa: E501

        :return: The leave of this Remuneration.  # noqa: E501
        :rtype: list[RemunerationLeave]
        """
        return self._leave

    @leave.setter
    def leave(self, leave):
        """Sets the leave of this Remuneration.

        A list of all leave types.  # noqa: E501

        :param leave: The leave of this Remuneration.  # noqa: E501
        :type: list[RemunerationLeave]
        """
        if self.local_vars_configuration.client_side_validation and leave is None:  # noqa: E501
            raise ValueError("Invalid value for `leave`, must not be `None`")  # noqa: E501

        self._leave = leave

    @property
    def pension(self):
        """Gets the pension of this Remuneration.  # noqa: E501

        A list of pensions.  # noqa: E501

        :return: The pension of this Remuneration.  # noqa: E501
        :rtype: list[RemunerationPension]
        """
        return self._pension

    @pension.setter
    def pension(self, pension):
        """Sets the pension of this Remuneration.

        A list of pensions.  # noqa: E501

        :param pension: The pension of this Remuneration.  # noqa: E501
        :type: list[RemunerationPension]
        """
        if self.local_vars_configuration.client_side_validation and pension is None:  # noqa: E501
            raise ValueError("Invalid value for `pension`, must not be `None`")  # noqa: E501

        self._pension = pension

    @property
    def salary(self):
        """Gets the salary of this Remuneration.  # noqa: E501

        A list of all the salary rows.  # noqa: E501

        :return: The salary of this Remuneration.  # noqa: E501
        :rtype: list[SalaryDefinition]
        """
        return self._salary

    @salary.setter
    def salary(self, salary):
        """Sets the salary of this Remuneration.

        A list of all the salary rows.  # noqa: E501

        :param salary: The salary of this Remuneration.  # noqa: E501
        :type: list[SalaryDefinition]
        """
        if self.local_vars_configuration.client_side_validation and salary is None:  # noqa: E501
            raise ValueError("Invalid value for `salary`, must not be `None`")  # noqa: E501

        self._salary = salary

    @property
    def supplements(self):
        """Gets the supplements of this Remuneration.  # noqa: E501

        A list of all the supplements.  # noqa: E501

        :return: The supplements of this Remuneration.  # noqa: E501
        :rtype: list[RemunerationSupplements]
        """
        return self._supplements

    @supplements.setter
    def supplements(self, supplements):
        """Sets the supplements of this Remuneration.

        A list of all the supplements.  # noqa: E501

        :param supplements: The supplements of this Remuneration.  # noqa: E501
        :type: list[RemunerationSupplements]
        """
        if self.local_vars_configuration.client_side_validation and supplements is None:  # noqa: E501
            raise ValueError("Invalid value for `supplements`, must not be `None`")  # noqa: E501

        self._supplements = supplements

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
        if not isinstance(other, Remuneration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Remuneration):
            return True

        return self.to_dict() != other.to_dict()
