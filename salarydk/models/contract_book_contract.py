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


class ContractBookContract(object):
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
        'affiliation_type': 'str',
        'bank_account_number': 'str',
        'bank_registration_number': 'str',
        'city': 'str',
        'contract_book_id': 'str',
        'contract_id': 'str',
        'contract_name': 'str',
        'contract_valid_from': 'datetime',
        'email': 'str',
        'employee_number': 'str',
        'employment_start_date': 'datetime',
        'fields': 'list[AccountingIntegrationSetupAuthParameters]',
        'language': 'str',
        'national_id': 'str',
        'phone_number': 'str',
        'phone_number_country_code': 'str',
        'position': 'str',
        'postal_code': 'str',
        'remuneration': 'Remuneration',
        'signee_name': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'address': 'address',
        'affiliation_type': 'affiliationType',
        'bank_account_number': 'bankAccountNumber',
        'bank_registration_number': 'bankRegistrationNumber',
        'city': 'city',
        'contract_book_id': 'contractBookID',
        'contract_id': 'contractID',
        'contract_name': 'contractName',
        'contract_valid_from': 'contractValidFrom',
        'email': 'email',
        'employee_number': 'employeeNumber',
        'employment_start_date': 'employmentStartDate',
        'fields': 'fields',
        'language': 'language',
        'national_id': 'nationalID',
        'phone_number': 'phoneNumber',
        'phone_number_country_code': 'phoneNumberCountryCode',
        'position': 'position',
        'postal_code': 'postalCode',
        'remuneration': 'remuneration',
        'signee_name': 'signeeName',
        'updated_at': 'updatedAt'
    }

    def __init__(self, address=None, affiliation_type=None, bank_account_number=None, bank_registration_number=None, city=None, contract_book_id=None, contract_id=None, contract_name=None, contract_valid_from=None, email=None, employee_number=None, employment_start_date=None, fields=None, language=None, national_id=None, phone_number=None, phone_number_country_code=None, position=None, postal_code=None, remuneration=None, signee_name=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """ContractBookContract - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._affiliation_type = None
        self._bank_account_number = None
        self._bank_registration_number = None
        self._city = None
        self._contract_book_id = None
        self._contract_id = None
        self._contract_name = None
        self._contract_valid_from = None
        self._email = None
        self._employee_number = None
        self._employment_start_date = None
        self._fields = None
        self._language = None
        self._national_id = None
        self._phone_number = None
        self._phone_number_country_code = None
        self._position = None
        self._postal_code = None
        self._remuneration = None
        self._signee_name = None
        self._updated_at = None
        self.discriminator = None

        self.address = address
        self.affiliation_type = affiliation_type
        self.bank_account_number = bank_account_number
        self.bank_registration_number = bank_registration_number
        self.city = city
        if contract_book_id is not None:
            self.contract_book_id = contract_book_id
        self.contract_id = contract_id
        self.contract_name = contract_name
        self.contract_valid_from = contract_valid_from
        self.email = email
        self.employee_number = employee_number
        self.employment_start_date = employment_start_date
        self.fields = fields
        self.language = language
        self.national_id = national_id
        self.phone_number = phone_number
        self.phone_number_country_code = phone_number_country_code
        self.position = position
        self.postal_code = postal_code
        if remuneration is not None:
            self.remuneration = remuneration
        self.signee_name = signee_name
        self.updated_at = updated_at

    @property
    def address(self):
        """Gets the address of this ContractBookContract.  # noqa: E501


        :return: The address of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ContractBookContract.


        :param address: The address of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def affiliation_type(self):
        """Gets the affiliation_type of this ContractBookContract.  # noqa: E501


        :return: The affiliation_type of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_type

    @affiliation_type.setter
    def affiliation_type(self, affiliation_type):
        """Sets the affiliation_type of this ContractBookContract.


        :param affiliation_type: The affiliation_type of this ContractBookContract.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"Standard", "Director", "Freelancer"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and affiliation_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `affiliation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(affiliation_type, allowed_values)
            )

        self._affiliation_type = affiliation_type

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this ContractBookContract.  # noqa: E501


        :return: The bank_account_number of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this ContractBookContract.


        :param bank_account_number: The bank_account_number of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def bank_registration_number(self):
        """Gets the bank_registration_number of this ContractBookContract.  # noqa: E501


        :return: The bank_registration_number of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._bank_registration_number

    @bank_registration_number.setter
    def bank_registration_number(self, bank_registration_number):
        """Sets the bank_registration_number of this ContractBookContract.


        :param bank_registration_number: The bank_registration_number of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._bank_registration_number = bank_registration_number

    @property
    def city(self):
        """Gets the city of this ContractBookContract.  # noqa: E501


        :return: The city of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContractBookContract.


        :param city: The city of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def contract_book_id(self):
        """Gets the contract_book_id of this ContractBookContract.  # noqa: E501

        The internal contract book integration, this one is associated with (useful when having more than one)  # noqa: E501

        :return: The contract_book_id of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_book_id

    @contract_book_id.setter
    def contract_book_id(self, contract_book_id):
        """Sets the contract_book_id of this ContractBookContract.

        The internal contract book integration, this one is associated with (useful when having more than one)  # noqa: E501

        :param contract_book_id: The contract_book_id of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._contract_book_id = contract_book_id

    @property
    def contract_id(self):
        """Gets the contract_id of this ContractBookContract.  # noqa: E501


        :return: The contract_id of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this ContractBookContract.


        :param contract_id: The contract_id of this ContractBookContract.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contract_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def contract_name(self):
        """Gets the contract_name of this ContractBookContract.  # noqa: E501


        :return: The contract_name of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_name

    @contract_name.setter
    def contract_name(self, contract_name):
        """Sets the contract_name of this ContractBookContract.


        :param contract_name: The contract_name of this ContractBookContract.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contract_name is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_name`, must not be `None`")  # noqa: E501

        self._contract_name = contract_name

    @property
    def contract_valid_from(self):
        """Gets the contract_valid_from of this ContractBookContract.  # noqa: E501


        :return: The contract_valid_from of this ContractBookContract.  # noqa: E501
        :rtype: datetime
        """
        return self._contract_valid_from

    @contract_valid_from.setter
    def contract_valid_from(self, contract_valid_from):
        """Sets the contract_valid_from of this ContractBookContract.


        :param contract_valid_from: The contract_valid_from of this ContractBookContract.  # noqa: E501
        :type: datetime
        """

        self._contract_valid_from = contract_valid_from

    @property
    def email(self):
        """Gets the email of this ContractBookContract.  # noqa: E501


        :return: The email of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContractBookContract.


        :param email: The email of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def employee_number(self):
        """Gets the employee_number of this ContractBookContract.  # noqa: E501


        :return: The employee_number of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this ContractBookContract.


        :param employee_number: The employee_number of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._employee_number = employee_number

    @property
    def employment_start_date(self):
        """Gets the employment_start_date of this ContractBookContract.  # noqa: E501


        :return: The employment_start_date of this ContractBookContract.  # noqa: E501
        :rtype: datetime
        """
        return self._employment_start_date

    @employment_start_date.setter
    def employment_start_date(self, employment_start_date):
        """Sets the employment_start_date of this ContractBookContract.


        :param employment_start_date: The employment_start_date of this ContractBookContract.  # noqa: E501
        :type: datetime
        """

        self._employment_start_date = employment_start_date

    @property
    def fields(self):
        """Gets the fields of this ContractBookContract.  # noqa: E501


        :return: The fields of this ContractBookContract.  # noqa: E501
        :rtype: list[AccountingIntegrationSetupAuthParameters]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ContractBookContract.


        :param fields: The fields of this ContractBookContract.  # noqa: E501
        :type: list[AccountingIntegrationSetupAuthParameters]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def language(self):
        """Gets the language of this ContractBookContract.  # noqa: E501


        :return: The language of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ContractBookContract.


        :param language: The language of this ContractBookContract.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"da", "en"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def national_id(self):
        """Gets the national_id of this ContractBookContract.  # noqa: E501


        :return: The national_id of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        """Sets the national_id of this ContractBookContract.


        :param national_id: The national_id of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._national_id = national_id

    @property
    def phone_number(self):
        """Gets the phone_number of this ContractBookContract.  # noqa: E501


        :return: The phone_number of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ContractBookContract.


        :param phone_number: The phone_number of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_country_code(self):
        """Gets the phone_number_country_code of this ContractBookContract.  # noqa: E501


        :return: The phone_number_country_code of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_country_code

    @phone_number_country_code.setter
    def phone_number_country_code(self, phone_number_country_code):
        """Sets the phone_number_country_code of this ContractBookContract.


        :param phone_number_country_code: The phone_number_country_code of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._phone_number_country_code = phone_number_country_code

    @property
    def position(self):
        """Gets the position of this ContractBookContract.  # noqa: E501


        :return: The position of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ContractBookContract.


        :param position: The position of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def postal_code(self):
        """Gets the postal_code of this ContractBookContract.  # noqa: E501


        :return: The postal_code of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ContractBookContract.


        :param postal_code: The postal_code of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def remuneration(self):
        """Gets the remuneration of this ContractBookContract.  # noqa: E501


        :return: The remuneration of this ContractBookContract.  # noqa: E501
        :rtype: Remuneration
        """
        return self._remuneration

    @remuneration.setter
    def remuneration(self, remuneration):
        """Sets the remuneration of this ContractBookContract.


        :param remuneration: The remuneration of this ContractBookContract.  # noqa: E501
        :type: Remuneration
        """

        self._remuneration = remuneration

    @property
    def signee_name(self):
        """Gets the signee_name of this ContractBookContract.  # noqa: E501


        :return: The signee_name of this ContractBookContract.  # noqa: E501
        :rtype: str
        """
        return self._signee_name

    @signee_name.setter
    def signee_name(self, signee_name):
        """Sets the signee_name of this ContractBookContract.


        :param signee_name: The signee_name of this ContractBookContract.  # noqa: E501
        :type: str
        """

        self._signee_name = signee_name

    @property
    def updated_at(self):
        """Gets the updated_at of this ContractBookContract.  # noqa: E501


        :return: The updated_at of this ContractBookContract.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ContractBookContract.


        :param updated_at: The updated_at of this ContractBookContract.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, ContractBookContract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContractBookContract):
            return True

        return self.to_dict() != other.to_dict()