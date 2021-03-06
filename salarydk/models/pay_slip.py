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


class PaySlip(object):
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
        'aggregates': 'list[PaySlipAggregates]',
        'calculations': 'list[PaySlipCalculations]',
        'department_id': 'str',
        'disposition_date': 'date',
        'employee_id': 'str',
        'fields': 'list[PaySlipFields]',
        'id': 'str',
        'pay_check': 'float',
        'pay_roll_id': 'str',
        'salary_period': 'SalaryPeriod',
        'salary_period_id': 'str',
        'settled': 'bool',
        'termination': 'bool'
    }

    attribute_map = {
        'aggregates': 'aggregates',
        'calculations': 'calculations',
        'department_id': 'departmentID',
        'disposition_date': 'dispositionDate',
        'employee_id': 'employeeID',
        'fields': 'fields',
        'id': 'id',
        'pay_check': 'payCheck',
        'pay_roll_id': 'payRollID',
        'salary_period': 'salaryPeriod',
        'salary_period_id': 'salaryPeriodID',
        'settled': 'settled',
        'termination': 'termination'
    }

    def __init__(self, aggregates=None, calculations=None, department_id=None, disposition_date=None, employee_id=None, fields=None, id=None, pay_check=None, pay_roll_id=None, salary_period=None, salary_period_id=None, settled=None, termination=None, local_vars_configuration=None):  # noqa: E501
        """PaySlip - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aggregates = None
        self._calculations = None
        self._department_id = None
        self._disposition_date = None
        self._employee_id = None
        self._fields = None
        self._id = None
        self._pay_check = None
        self._pay_roll_id = None
        self._salary_period = None
        self._salary_period_id = None
        self._settled = None
        self._termination = None
        self.discriminator = None

        if aggregates is not None:
            self.aggregates = aggregates
        if calculations is not None:
            self.calculations = calculations
        self.department_id = department_id
        if disposition_date is not None:
            self.disposition_date = disposition_date
        if employee_id is not None:
            self.employee_id = employee_id
        if fields is not None:
            self.fields = fields
        if id is not None:
            self.id = id
        if pay_check is not None:
            self.pay_check = pay_check
        self.pay_roll_id = pay_roll_id
        if salary_period is not None:
            self.salary_period = salary_period
        if salary_period_id is not None:
            self.salary_period_id = salary_period_id
        if settled is not None:
            self.settled = settled
        if termination is not None:
            self.termination = termination

    @property
    def aggregates(self):
        """Gets the aggregates of this PaySlip.  # noqa: E501

        The period aggregates to include on this pay slip.  # noqa: E501

        :return: The aggregates of this PaySlip.  # noqa: E501
        :rtype: list[PaySlipAggregates]
        """
        return self._aggregates

    @aggregates.setter
    def aggregates(self, aggregates):
        """Sets the aggregates of this PaySlip.

        The period aggregates to include on this pay slip.  # noqa: E501

        :param aggregates: The aggregates of this PaySlip.  # noqa: E501
        :type: list[PaySlipAggregates]
        """

        self._aggregates = aggregates

    @property
    def calculations(self):
        """Gets the calculations of this PaySlip.  # noqa: E501

        The detailed calculations of the pay slip, in a machine-readable format.  # noqa: E501

        :return: The calculations of this PaySlip.  # noqa: E501
        :rtype: list[PaySlipCalculations]
        """
        return self._calculations

    @calculations.setter
    def calculations(self, calculations):
        """Sets the calculations of this PaySlip.

        The detailed calculations of the pay slip, in a machine-readable format.  # noqa: E501

        :param calculations: The calculations of this PaySlip.  # noqa: E501
        :type: list[PaySlipCalculations]
        """

        self._calculations = calculations

    @property
    def department_id(self):
        """Gets the department_id of this PaySlip.  # noqa: E501

        The department this pay slip belongs to.  # noqa: E501

        :return: The department_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this PaySlip.

        The department this pay slip belongs to.  # noqa: E501

        :param department_id: The department_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def disposition_date(self):
        """Gets the disposition_date of this PaySlip.  # noqa: E501

        The date the net amount is paid out.  # noqa: E501

        :return: The disposition_date of this PaySlip.  # noqa: E501
        :rtype: date
        """
        return self._disposition_date

    @disposition_date.setter
    def disposition_date(self, disposition_date):
        """Sets the disposition_date of this PaySlip.

        The date the net amount is paid out.  # noqa: E501

        :param disposition_date: The disposition_date of this PaySlip.  # noqa: E501
        :type: date
        """

        self._disposition_date = disposition_date

    @property
    def employee_id(self):
        """Gets the employee_id of this PaySlip.  # noqa: E501

        The employee this pay slip belongs to.  # noqa: E501

        :return: The employee_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this PaySlip.

        The employee this pay slip belongs to.  # noqa: E501

        :param employee_id: The employee_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def fields(self):
        """Gets the fields of this PaySlip.  # noqa: E501

        A list of key-values included on the pay slip.  # noqa: E501

        :return: The fields of this PaySlip.  # noqa: E501
        :rtype: list[PaySlipFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this PaySlip.

        A list of key-values included on the pay slip.  # noqa: E501

        :param fields: The fields of this PaySlip.  # noqa: E501
        :type: list[PaySlipFields]
        """

        self._fields = fields

    @property
    def id(self):
        """Gets the id of this PaySlip.  # noqa: E501

        The ID of the pay slip  # noqa: E501

        :return: The id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaySlip.

        The ID of the pay slip  # noqa: E501

        :param id: The id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pay_check(self):
        """Gets the pay_check of this PaySlip.  # noqa: E501

        The net amount paid out to the employee for this pay slip.  # noqa: E501

        :return: The pay_check of this PaySlip.  # noqa: E501
        :rtype: float
        """
        return self._pay_check

    @pay_check.setter
    def pay_check(self, pay_check):
        """Sets the pay_check of this PaySlip.

        The net amount paid out to the employee for this pay slip.  # noqa: E501

        :param pay_check: The pay_check of this PaySlip.  # noqa: E501
        :type: float
        """

        self._pay_check = pay_check

    @property
    def pay_roll_id(self):
        """Gets the pay_roll_id of this PaySlip.  # noqa: E501

        The pay roll this pay slip belongs to.  # noqa: E501

        :return: The pay_roll_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._pay_roll_id

    @pay_roll_id.setter
    def pay_roll_id(self, pay_roll_id):
        """Sets the pay_roll_id of this PaySlip.

        The pay roll this pay slip belongs to.  # noqa: E501

        :param pay_roll_id: The pay_roll_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._pay_roll_id = pay_roll_id

    @property
    def salary_period(self):
        """Gets the salary_period of this PaySlip.  # noqa: E501


        :return: The salary_period of this PaySlip.  # noqa: E501
        :rtype: SalaryPeriod
        """
        return self._salary_period

    @salary_period.setter
    def salary_period(self, salary_period):
        """Sets the salary_period of this PaySlip.


        :param salary_period: The salary_period of this PaySlip.  # noqa: E501
        :type: SalaryPeriod
        """

        self._salary_period = salary_period

    @property
    def salary_period_id(self):
        """Gets the salary_period_id of this PaySlip.  # noqa: E501

        The ID of the period this pay slip belongs to  # noqa: E501

        :return: The salary_period_id of this PaySlip.  # noqa: E501
        :rtype: str
        """
        return self._salary_period_id

    @salary_period_id.setter
    def salary_period_id(self, salary_period_id):
        """Sets the salary_period_id of this PaySlip.

        The ID of the period this pay slip belongs to  # noqa: E501

        :param salary_period_id: The salary_period_id of this PaySlip.  # noqa: E501
        :type: str
        """

        self._salary_period_id = salary_period_id

    @property
    def settled(self):
        """Gets the settled of this PaySlip.  # noqa: E501

        Whether this pay slip has actually been run, false if the pay slip is a preview of a potential future pay slip.  # noqa: E501

        :return: The settled of this PaySlip.  # noqa: E501
        :rtype: bool
        """
        return self._settled

    @settled.setter
    def settled(self, settled):
        """Sets the settled of this PaySlip.

        Whether this pay slip has actually been run, false if the pay slip is a preview of a potential future pay slip.  # noqa: E501

        :param settled: The settled of this PaySlip.  # noqa: E501
        :type: bool
        """

        self._settled = settled

    @property
    def termination(self):
        """Gets the termination of this PaySlip.  # noqa: E501

        Whether this pay slip is the termination pay slip for the employee.  # noqa: E501

        :return: The termination of this PaySlip.  # noqa: E501
        :rtype: bool
        """
        return self._termination

    @termination.setter
    def termination(self, termination):
        """Sets the termination of this PaySlip.

        Whether this pay slip is the termination pay slip for the employee.  # noqa: E501

        :param termination: The termination of this PaySlip.  # noqa: E501
        :type: bool
        """

        self._termination = termination

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
        if not isinstance(other, PaySlip):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaySlip):
            return True

        return self.to_dict() != other.to_dict()
