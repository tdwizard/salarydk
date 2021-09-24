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


class IncomeTaxReportEmployees(object):
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
        'cpr': 'str',
        'cvr': 'str',
        'disposition_date': 'date',
        'employee_number': 'str',
        'employment_end_date': 'date',
        'employment_start_date': 'date',
        'income_type': 'str',
        'paid_ahead': 'bool',
        'period_end': 'date',
        'period_start': 'date',
        'preferred_tax_card': 'str',
        'production_number': 'str',
        'salary_lines': 'list[IncomeTaxReportSalaryLines]',
        'terminations': 'list[IncomeTaxReportTerminations]'
    }

    attribute_map = {
        'cpr': 'cpr',
        'cvr': 'cvr',
        'disposition_date': 'dispositionDate',
        'employee_number': 'employeeNumber',
        'employment_end_date': 'employmentEndDate',
        'employment_start_date': 'employmentStartDate',
        'income_type': 'incomeType',
        'paid_ahead': 'paidAhead',
        'period_end': 'periodEnd',
        'period_start': 'periodStart',
        'preferred_tax_card': 'preferredTaxCard',
        'production_number': 'productionNumber',
        'salary_lines': 'salaryLines',
        'terminations': 'terminations'
    }

    def __init__(self, cpr=None, cvr=None, disposition_date=None, employee_number=None, employment_end_date=None, employment_start_date=None, income_type=None, paid_ahead=None, period_end=None, period_start=None, preferred_tax_card=None, production_number=None, salary_lines=None, terminations=None, local_vars_configuration=None):  # noqa: E501
        """IncomeTaxReportEmployees - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpr = None
        self._cvr = None
        self._disposition_date = None
        self._employee_number = None
        self._employment_end_date = None
        self._employment_start_date = None
        self._income_type = None
        self._paid_ahead = None
        self._period_end = None
        self._period_start = None
        self._preferred_tax_card = None
        self._production_number = None
        self._salary_lines = None
        self._terminations = None
        self.discriminator = None

        if cpr is not None:
            self.cpr = cpr
        if cvr is not None:
            self.cvr = cvr
        self.disposition_date = disposition_date
        self.employee_number = employee_number
        self.employment_end_date = employment_end_date
        self.employment_start_date = employment_start_date
        self.income_type = income_type
        self.paid_ahead = paid_ahead
        self.period_end = period_end
        self.period_start = period_start
        self.preferred_tax_card = preferred_tax_card
        self.production_number = production_number
        self.salary_lines = salary_lines
        self.terminations = terminations

    @property
    def cpr(self):
        """Gets the cpr of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The cpr of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._cpr

    @cpr.setter
    def cpr(self, cpr):
        """Sets the cpr of this IncomeTaxReportEmployees.


        :param cpr: The cpr of this IncomeTaxReportEmployees.  # noqa: E501
        :type: str
        """

        self._cpr = cpr

    @property
    def cvr(self):
        """Gets the cvr of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The cvr of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._cvr

    @cvr.setter
    def cvr(self, cvr):
        """Sets the cvr of this IncomeTaxReportEmployees.


        :param cvr: The cvr of this IncomeTaxReportEmployees.  # noqa: E501
        :type: str
        """

        self._cvr = cvr

    @property
    def disposition_date(self):
        """Gets the disposition_date of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The disposition_date of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: date
        """
        return self._disposition_date

    @disposition_date.setter
    def disposition_date(self, disposition_date):
        """Sets the disposition_date of this IncomeTaxReportEmployees.


        :param disposition_date: The disposition_date of this IncomeTaxReportEmployees.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and disposition_date is None:  # noqa: E501
            raise ValueError("Invalid value for `disposition_date`, must not be `None`")  # noqa: E501

        self._disposition_date = disposition_date

    @property
    def employee_number(self):
        """Gets the employee_number of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The employee_number of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this IncomeTaxReportEmployees.


        :param employee_number: The employee_number of this IncomeTaxReportEmployees.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and employee_number is None:  # noqa: E501
            raise ValueError("Invalid value for `employee_number`, must not be `None`")  # noqa: E501

        self._employee_number = employee_number

    @property
    def employment_end_date(self):
        """Gets the employment_end_date of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The employment_end_date of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: date
        """
        return self._employment_end_date

    @employment_end_date.setter
    def employment_end_date(self, employment_end_date):
        """Sets the employment_end_date of this IncomeTaxReportEmployees.


        :param employment_end_date: The employment_end_date of this IncomeTaxReportEmployees.  # noqa: E501
        :type: date
        """

        self._employment_end_date = employment_end_date

    @property
    def employment_start_date(self):
        """Gets the employment_start_date of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The employment_start_date of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: date
        """
        return self._employment_start_date

    @employment_start_date.setter
    def employment_start_date(self, employment_start_date):
        """Sets the employment_start_date of this IncomeTaxReportEmployees.


        :param employment_start_date: The employment_start_date of this IncomeTaxReportEmployees.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and employment_start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `employment_start_date`, must not be `None`")  # noqa: E501

        self._employment_start_date = employment_start_date

    @property
    def income_type(self):
        """Gets the income_type of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The income_type of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._income_type

    @income_type.setter
    def income_type(self, income_type):
        """Sets the income_type of this IncomeTaxReportEmployees.


        :param income_type: The income_type of this IncomeTaxReportEmployees.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and income_type is None:  # noqa: E501
            raise ValueError("Invalid value for `income_type`, must not be `None`")  # noqa: E501

        self._income_type = income_type

    @property
    def paid_ahead(self):
        """Gets the paid_ahead of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The paid_ahead of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: bool
        """
        return self._paid_ahead

    @paid_ahead.setter
    def paid_ahead(self, paid_ahead):
        """Sets the paid_ahead of this IncomeTaxReportEmployees.


        :param paid_ahead: The paid_ahead of this IncomeTaxReportEmployees.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and paid_ahead is None:  # noqa: E501
            raise ValueError("Invalid value for `paid_ahead`, must not be `None`")  # noqa: E501

        self._paid_ahead = paid_ahead

    @property
    def period_end(self):
        """Gets the period_end of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The period_end of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: date
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this IncomeTaxReportEmployees.


        :param period_end: The period_end of this IncomeTaxReportEmployees.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and period_end is None:  # noqa: E501
            raise ValueError("Invalid value for `period_end`, must not be `None`")  # noqa: E501

        self._period_end = period_end

    @property
    def period_start(self):
        """Gets the period_start of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The period_start of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: date
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this IncomeTaxReportEmployees.


        :param period_start: The period_start of this IncomeTaxReportEmployees.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and period_start is None:  # noqa: E501
            raise ValueError("Invalid value for `period_start`, must not be `None`")  # noqa: E501

        self._period_start = period_start

    @property
    def preferred_tax_card(self):
        """Gets the preferred_tax_card of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The preferred_tax_card of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._preferred_tax_card

    @preferred_tax_card.setter
    def preferred_tax_card(self, preferred_tax_card):
        """Sets the preferred_tax_card of this IncomeTaxReportEmployees.


        :param preferred_tax_card: The preferred_tax_card of this IncomeTaxReportEmployees.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and preferred_tax_card is None:  # noqa: E501
            raise ValueError("Invalid value for `preferred_tax_card`, must not be `None`")  # noqa: E501
        allowed_values = ["Primary", "Secondary"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and preferred_tax_card not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `preferred_tax_card` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_tax_card, allowed_values)
            )

        self._preferred_tax_card = preferred_tax_card

    @property
    def production_number(self):
        """Gets the production_number of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The production_number of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._production_number

    @production_number.setter
    def production_number(self, production_number):
        """Sets the production_number of this IncomeTaxReportEmployees.


        :param production_number: The production_number of this IncomeTaxReportEmployees.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and production_number is None:  # noqa: E501
            raise ValueError("Invalid value for `production_number`, must not be `None`")  # noqa: E501

        self._production_number = production_number

    @property
    def salary_lines(self):
        """Gets the salary_lines of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The salary_lines of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: list[IncomeTaxReportSalaryLines]
        """
        return self._salary_lines

    @salary_lines.setter
    def salary_lines(self, salary_lines):
        """Sets the salary_lines of this IncomeTaxReportEmployees.


        :param salary_lines: The salary_lines of this IncomeTaxReportEmployees.  # noqa: E501
        :type: list[IncomeTaxReportSalaryLines]
        """
        if self.local_vars_configuration.client_side_validation and salary_lines is None:  # noqa: E501
            raise ValueError("Invalid value for `salary_lines`, must not be `None`")  # noqa: E501

        self._salary_lines = salary_lines

    @property
    def terminations(self):
        """Gets the terminations of this IncomeTaxReportEmployees.  # noqa: E501


        :return: The terminations of this IncomeTaxReportEmployees.  # noqa: E501
        :rtype: list[IncomeTaxReportTerminations]
        """
        return self._terminations

    @terminations.setter
    def terminations(self, terminations):
        """Sets the terminations of this IncomeTaxReportEmployees.


        :param terminations: The terminations of this IncomeTaxReportEmployees.  # noqa: E501
        :type: list[IncomeTaxReportTerminations]
        """
        if self.local_vars_configuration.client_side_validation and terminations is None:  # noqa: E501
            raise ValueError("Invalid value for `terminations`, must not be `None`")  # noqa: E501

        self._terminations = terminations

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
        if not isinstance(other, IncomeTaxReportEmployees):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncomeTaxReportEmployees):
            return True

        return self.to_dict() != other.to_dict()
