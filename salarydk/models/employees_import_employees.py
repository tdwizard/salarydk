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


class EmployeesImportEmployees(object):
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
        'address': 'str',
        'bank': 'EmployeesImportBank',
        'can_import': 'bool',
        'city': 'str',
        'email': 'str',
        'employee_id': 'str',
        'employee_number': 'str',
        'errors': 'EmployeesImportErrors',
        'import_employee_id': 'str',
        'name': 'str',
        'national_id': 'str',
        'phone_number': 'str',
        'phone_number_cc': 'str',
        'position': 'str',
        'postal_code': 'str',
        'preferred_tax_card': 'str',
        'salary_types': 'list[EmployeesImportSalaryTypes]',
        'start_date': 'date'
    }

    attribute_map = {
        'address': 'address',
        'bank': 'bank',
        'can_import': 'canImport',
        'city': 'city',
        'email': 'email',
        'employee_id': 'employeeID',
        'employee_number': 'employeeNumber',
        'errors': 'errors',
        'import_employee_id': 'importEmployeeID',
        'name': 'name',
        'national_id': 'nationalID',
        'phone_number': 'phoneNumber',
        'phone_number_cc': 'phoneNumberCC',
        'position': 'position',
        'postal_code': 'postalCode',
        'preferred_tax_card': 'preferredTaxCard',
        'salary_types': 'salaryTypes',
        'start_date': 'startDate'
    }

    def __init__(self, address=None, bank=None, can_import=None, city=None, email=None, employee_id=None, employee_number=None, errors=None, import_employee_id=None, name=None, national_id=None, phone_number=None, phone_number_cc=None, position=None, postal_code=None, preferred_tax_card=None, salary_types=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """EmployeesImportEmployees - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._bank = None
        self._can_import = None
        self._city = None
        self._email = None
        self._employee_id = None
        self._employee_number = None
        self._errors = None
        self._import_employee_id = None
        self._name = None
        self._national_id = None
        self._phone_number = None
        self._phone_number_cc = None
        self._position = None
        self._postal_code = None
        self._preferred_tax_card = None
        self._salary_types = None
        self._start_date = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if bank is not None:
            self.bank = bank
        if can_import is not None:
            self.can_import = can_import
        if city is not None:
            self.city = city
        if email is not None:
            self.email = email
        self.employee_id = employee_id
        if employee_number is not None:
            self.employee_number = employee_number
        if errors is not None:
            self.errors = errors
        if import_employee_id is not None:
            self.import_employee_id = import_employee_id
        if name is not None:
            self.name = name
        if national_id is not None:
            self.national_id = national_id
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_number_cc is not None:
            self.phone_number_cc = phone_number_cc
        if position is not None:
            self.position = position
        if postal_code is not None:
            self.postal_code = postal_code
        if preferred_tax_card is not None:
            self.preferred_tax_card = preferred_tax_card
        if salary_types is not None:
            self.salary_types = salary_types
        if start_date is not None:
            self.start_date = start_date

    @property
    def address(self):
        """Gets the address of this EmployeesImportEmployees.  # noqa: E501


        :return: The address of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this EmployeesImportEmployees.


        :param address: The address of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def bank(self):
        """Gets the bank of this EmployeesImportEmployees.  # noqa: E501


        :return: The bank of this EmployeesImportEmployees.  # noqa: E501
        :rtype: EmployeesImportBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this EmployeesImportEmployees.


        :param bank: The bank of this EmployeesImportEmployees.  # noqa: E501
        :type: EmployeesImportBank
        """

        self._bank = bank

    @property
    def can_import(self):
        """Gets the can_import of this EmployeesImportEmployees.  # noqa: E501

        Whether this employee is ready for import.  # noqa: E501

        :return: The can_import of this EmployeesImportEmployees.  # noqa: E501
        :rtype: bool
        """
        return self._can_import

    @can_import.setter
    def can_import(self, can_import):
        """Sets the can_import of this EmployeesImportEmployees.

        Whether this employee is ready for import.  # noqa: E501

        :param can_import: The can_import of this EmployeesImportEmployees.  # noqa: E501
        :type: bool
        """

        self._can_import = can_import

    @property
    def city(self):
        """Gets the city of this EmployeesImportEmployees.  # noqa: E501


        :return: The city of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EmployeesImportEmployees.


        :param city: The city of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def email(self):
        """Gets the email of this EmployeesImportEmployees.  # noqa: E501


        :return: The email of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmployeesImportEmployees.


        :param email: The email of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def employee_id(self):
        """Gets the employee_id of this EmployeesImportEmployees.  # noqa: E501

        If we find a matching employee in Salary, this will be set.  But those will not be imported, and will remain unmodified  # noqa: E501

        :return: The employee_id of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this EmployeesImportEmployees.

        If we find a matching employee in Salary, this will be set.  But those will not be imported, and will remain unmodified  # noqa: E501

        :param employee_id: The employee_id of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def employee_number(self):
        """Gets the employee_number of this EmployeesImportEmployees.  # noqa: E501


        :return: The employee_number of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this EmployeesImportEmployees.


        :param employee_number: The employee_number of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._employee_number = employee_number

    @property
    def errors(self):
        """Gets the errors of this EmployeesImportEmployees.  # noqa: E501


        :return: The errors of this EmployeesImportEmployees.  # noqa: E501
        :rtype: EmployeesImportErrors
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this EmployeesImportEmployees.


        :param errors: The errors of this EmployeesImportEmployees.  # noqa: E501
        :type: EmployeesImportErrors
        """

        self._errors = errors

    @property
    def import_employee_id(self):
        """Gets the import_employee_id of this EmployeesImportEmployees.  # noqa: E501

        A temporary ID used when modifying the import  # noqa: E501

        :return: The import_employee_id of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._import_employee_id

    @import_employee_id.setter
    def import_employee_id(self, import_employee_id):
        """Sets the import_employee_id of this EmployeesImportEmployees.

        A temporary ID used when modifying the import  # noqa: E501

        :param import_employee_id: The import_employee_id of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._import_employee_id = import_employee_id

    @property
    def name(self):
        """Gets the name of this EmployeesImportEmployees.  # noqa: E501


        :return: The name of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmployeesImportEmployees.


        :param name: The name of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def national_id(self):
        """Gets the national_id of this EmployeesImportEmployees.  # noqa: E501


        :return: The national_id of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        """Sets the national_id of this EmployeesImportEmployees.


        :param national_id: The national_id of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._national_id = national_id

    @property
    def phone_number(self):
        """Gets the phone_number of this EmployeesImportEmployees.  # noqa: E501


        :return: The phone_number of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this EmployeesImportEmployees.


        :param phone_number: The phone_number of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_cc(self):
        """Gets the phone_number_cc of this EmployeesImportEmployees.  # noqa: E501


        :return: The phone_number_cc of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_cc

    @phone_number_cc.setter
    def phone_number_cc(self, phone_number_cc):
        """Sets the phone_number_cc of this EmployeesImportEmployees.


        :param phone_number_cc: The phone_number_cc of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._phone_number_cc = phone_number_cc

    @property
    def position(self):
        """Gets the position of this EmployeesImportEmployees.  # noqa: E501


        :return: The position of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this EmployeesImportEmployees.


        :param position: The position of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def postal_code(self):
        """Gets the postal_code of this EmployeesImportEmployees.  # noqa: E501


        :return: The postal_code of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EmployeesImportEmployees.


        :param postal_code: The postal_code of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def preferred_tax_card(self):
        """Gets the preferred_tax_card of this EmployeesImportEmployees.  # noqa: E501


        :return: The preferred_tax_card of this EmployeesImportEmployees.  # noqa: E501
        :rtype: str
        """
        return self._preferred_tax_card

    @preferred_tax_card.setter
    def preferred_tax_card(self, preferred_tax_card):
        """Sets the preferred_tax_card of this EmployeesImportEmployees.


        :param preferred_tax_card: The preferred_tax_card of this EmployeesImportEmployees.  # noqa: E501
        :type: str
        """
        allowed_values = ["Primary", "Secondary"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and preferred_tax_card not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `preferred_tax_card` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_tax_card, allowed_values)
            )

        self._preferred_tax_card = preferred_tax_card

    @property
    def salary_types(self):
        """Gets the salary_types of this EmployeesImportEmployees.  # noqa: E501

        Salary types suggested for this employee  # noqa: E501

        :return: The salary_types of this EmployeesImportEmployees.  # noqa: E501
        :rtype: list[EmployeesImportSalaryTypes]
        """
        return self._salary_types

    @salary_types.setter
    def salary_types(self, salary_types):
        """Sets the salary_types of this EmployeesImportEmployees.

        Salary types suggested for this employee  # noqa: E501

        :param salary_types: The salary_types of this EmployeesImportEmployees.  # noqa: E501
        :type: list[EmployeesImportSalaryTypes]
        """

        self._salary_types = salary_types

    @property
    def start_date(self):
        """Gets the start_date of this EmployeesImportEmployees.  # noqa: E501

        Start date for employee  # noqa: E501

        :return: The start_date of this EmployeesImportEmployees.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EmployeesImportEmployees.

        Start date for employee  # noqa: E501

        :param start_date: The start_date of this EmployeesImportEmployees.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

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
        if not isinstance(other, EmployeesImportEmployees):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmployeesImportEmployees):
            return True

        return self.to_dict() != other.to_dict()
