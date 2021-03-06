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


class Transfer(object):
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
        'amount': 'float',
        'approved': 'bool',
        'automated': 'bool',
        'completed': 'bool',
        'deadline_change_automation': 'datetime',
        'employee_id': 'str',
        'id': 'str',
        'pay_roll_id': 'str',
        'payment_date': 'date',
        'payment_method': 'str',
        'recipient': 'str',
        'state': 'str',
        'transfer_destination_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'approved': 'approved',
        'automated': 'automated',
        'completed': 'completed',
        'deadline_change_automation': 'deadlineChangeAutomation',
        'employee_id': 'employeeID',
        'id': 'id',
        'pay_roll_id': 'payRollID',
        'payment_date': 'paymentDate',
        'payment_method': 'paymentMethod',
        'recipient': 'recipient',
        'state': 'state',
        'transfer_destination_type': 'transferDestinationType',
        'type': 'type'
    }

    def __init__(self, amount=None, approved=None, automated=None, completed=None, deadline_change_automation=None, employee_id=None, id=None, pay_roll_id=None, payment_date=None, payment_method=None, recipient=None, state=None, transfer_destination_type=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Transfer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._approved = None
        self._automated = None
        self._completed = None
        self._deadline_change_automation = None
        self._employee_id = None
        self._id = None
        self._pay_roll_id = None
        self._payment_date = None
        self._payment_method = None
        self._recipient = None
        self._state = None
        self._transfer_destination_type = None
        self._type = None
        self.discriminator = None

        self.amount = amount
        self.approved = approved
        if automated is not None:
            self.automated = automated
        if completed is not None:
            self.completed = completed
        self.deadline_change_automation = deadline_change_automation
        if employee_id is not None:
            self.employee_id = employee_id
        self.id = id
        self.pay_roll_id = pay_roll_id
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.recipient = recipient
        self.state = state
        if transfer_destination_type is not None:
            self.transfer_destination_type = transfer_destination_type
        self.type = type

    @property
    def amount(self):
        """Gets the amount of this Transfer.  # noqa: E501


        :return: The amount of this Transfer.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transfer.


        :param amount: The amount of this Transfer.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def approved(self):
        """Gets the approved of this Transfer.  # noqa: E501


        :return: The approved of this Transfer.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this Transfer.


        :param approved: The approved of this Transfer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and approved is None:  # noqa: E501
            raise ValueError("Invalid value for `approved`, must not be `None`")  # noqa: E501

        self._approved = approved

    @property
    def automated(self):
        """Gets the automated of this Transfer.  # noqa: E501

        Deprecated.  Old way to represent `paymentMethod` `true` => NETS/Stripe, `false` => Manual  # noqa: E501

        :return: The automated of this Transfer.  # noqa: E501
        :rtype: bool
        """
        return self._automated

    @automated.setter
    def automated(self, automated):
        """Sets the automated of this Transfer.

        Deprecated.  Old way to represent `paymentMethod` `true` => NETS/Stripe, `false` => Manual  # noqa: E501

        :param automated: The automated of this Transfer.  # noqa: E501
        :type: bool
        """

        self._automated = automated

    @property
    def completed(self):
        """Gets the completed of this Transfer.  # noqa: E501

        Deprecated.  Old way to represent `state`; `true` => Completed, `false` => Pending/Failed  # noqa: E501

        :return: The completed of this Transfer.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this Transfer.

        Deprecated.  Old way to represent `state`; `true` => Completed, `false` => Pending/Failed  # noqa: E501

        :param completed: The completed of this Transfer.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def deadline_change_automation(self):
        """Gets the deadline_change_automation of this Transfer.  # noqa: E501

        The latest time the automation of this transfer may be changed. If null, it is unchangeable.  # noqa: E501

        :return: The deadline_change_automation of this Transfer.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline_change_automation

    @deadline_change_automation.setter
    def deadline_change_automation(self, deadline_change_automation):
        """Sets the deadline_change_automation of this Transfer.

        The latest time the automation of this transfer may be changed. If null, it is unchangeable.  # noqa: E501

        :param deadline_change_automation: The deadline_change_automation of this Transfer.  # noqa: E501
        :type: datetime
        """

        self._deadline_change_automation = deadline_change_automation

    @property
    def employee_id(self):
        """Gets the employee_id of this Transfer.  # noqa: E501

        The employee the transfer is related to  # noqa: E501

        :return: The employee_id of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Transfer.

        The employee the transfer is related to  # noqa: E501

        :param employee_id: The employee_id of this Transfer.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def id(self):
        """Gets the id of this Transfer.  # noqa: E501


        :return: The id of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transfer.


        :param id: The id of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def pay_roll_id(self):
        """Gets the pay_roll_id of this Transfer.  # noqa: E501


        :return: The pay_roll_id of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._pay_roll_id

    @pay_roll_id.setter
    def pay_roll_id(self, pay_roll_id):
        """Sets the pay_roll_id of this Transfer.


        :param pay_roll_id: The pay_roll_id of this Transfer.  # noqa: E501
        :type: str
        """

        self._pay_roll_id = pay_roll_id

    @property
    def payment_date(self):
        """Gets the payment_date of this Transfer.  # noqa: E501

        The latest payment date for the transfer  # noqa: E501

        :return: The payment_date of this Transfer.  # noqa: E501
        :rtype: date
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this Transfer.

        The latest payment date for the transfer  # noqa: E501

        :param payment_date: The payment_date of this Transfer.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def payment_method(self):
        """Gets the payment_method of this Transfer.  # noqa: E501


        :return: The payment_method of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Transfer.


        :param payment_method: The payment_method of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payment_method is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501
        allowed_values = ["Manual", "NETS", "Stripe"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and payment_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def recipient(self):
        """Gets the recipient of this Transfer.  # noqa: E501

        The recipient of the transfer  # noqa: E501

        :return: The recipient of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Transfer.

        The recipient of the transfer  # noqa: E501

        :param recipient: The recipient of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and recipient is None:  # noqa: E501
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def state(self):
        """Gets the state of this Transfer.  # noqa: E501


        :return: The state of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Transfer.


        :param state: The state of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["Pending", "Completed", "Failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def transfer_destination_type(self):
        """Gets the transfer_destination_type of this Transfer.  # noqa: E501


        :return: The transfer_destination_type of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._transfer_destination_type

    @transfer_destination_type.setter
    def transfer_destination_type(self, transfer_destination_type):
        """Sets the transfer_destination_type of this Transfer.


        :param transfer_destination_type: The transfer_destination_type of this Transfer.  # noqa: E501
        :type: str
        """
        allowed_values = ["DK Account", "DK NemKonto", "DK NemKonto CVR", "Foreign Account", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and transfer_destination_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `transfer_destination_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transfer_destination_type, allowed_values)
            )

        self._transfer_destination_type = transfer_destination_type

    @property
    def type(self):
        """Gets the type of this Transfer.  # noqa: E501

        The type of transfer  # noqa: E501

        :return: The type of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transfer.

        The type of transfer  # noqa: E501

        :param type: The type of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, Transfer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transfer):
            return True

        return self.to_dict() != other.to_dict()
