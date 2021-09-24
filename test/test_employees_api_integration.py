# coding: utf-8

"""
    Salary.dk API

    This is the public API for Salary.dk.  # General  Our API is a JSON-based, REST-like API. Our webapp uses the exact same API, so everything you can do in our webapp, you can do through our API. However, we are slowly opening up the API, so not all endpoints are documented here yet. Only the endpoints documented here are stable. If there is some functionality you would like to access through our API, please contact us.  The API is located at https://api.salary.dk. All requests must use TLS.  In order to use the API on behalf of other users than yourself, you need to register as an API client. You do this by sending an e-mail to dev@salary.dk with the name and purpose of your client.  API-keys for each account can be obtained once logged in to Salary, under the settings for the Company.  All endpoints are documented to be able to return the 500 error code. We strive to not return this error code, so if you do encounter this error code, it might mean there is an error on our side. In this case, do not hesitate to contact us.  # Cross-Origin Resource Sharing This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/) - and that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site, as long as the proper access token is passed.  # Authentication All request require an access token. There are two ways to obtain an access token: * Logging in as a user. (this endpoint is not yet publicly available). * Using an API-key: [endpoint](#operation/APIClientLogin)  Using one of these methods, you will obtain an access token. In all subsequest requests, this access token should be passed in the Authorization header. The access token is valid for around one hour, after which a new token should be obtained.  You do not need to dispose of access tokens once created. They have a limited lifetime, and Salary.dk will automatically expire old ones.  For some endpoints, the authorizedUserQuery security definition is used. This allows for passing the access token as a query parameter where it is not possible to pass it as a header. In particular, this is used for downloading files.  <!-- ReDoc-Inject: <security-definitions> -->   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dev@salary.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import json
import random
import string
import unittest
from random import randrange
from datetime import date

import requests

import salarydk
from salarydk.api.employees_api import EmployeesApi  # noqa: E501
from salarydk.rest import ApiException
from salarydk.api_client import ApiClient


coefs = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
start_date = datetime.datetime(1900, 1, 1)
end_date = datetime.datetime(2000, 12, 31)


def generate_cpr():
    while True:
        delta = end_date - start_date
        random_delta = randrange(delta.days)

        birth_date = start_date + datetime.timedelta(days=random_delta)

        series = str(randrange(999)).zfill(3)

        cpr = birth_date.strftime('%y%m%d') + series

        partial_sum = 0
        for i, digit in enumerate(cpr):
            partial_sum += coefs[i] * int(digit)

        check_digit = 11 - (partial_sum % 11)
        cpr += str(check_digit)

        if len(cpr) == 10:
            break

    return cpr


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class TestRegistrationFlow(unittest.TestCase):
    """RegistrationFlow integration test"""

    def setUp(self):
        self.company_id = "582c9956-bebc-4588-4189-480dfaf15d76"
        configuration = salarydk.Configuration()
        configuration.host = "https://api-staging.sallysalary.dk"
        configuration.client_side_validation = False

        client_id = '1609ffd5-954e-4542-b64d-673681583fe8'
        client_secret = "L1hxffJrYX54pvHldl3lgPLQBmixd52tqHjszveoVm7qC90jpcAFjtJmIj7P1nIILr5jEjyzidPCGJ7OgHf" + \
            "ssj9SQbm976zDRA5FEtoYGIX2KQ2h0nSXJHeX9VUieChLE4Fdq3UAzqEeVXR8oTCrrUgtWnK" + \
            "JBUmhNj0Af3uUIq8fNVaOnCGwiGBLkKeKwOhRBfM2BmjumPpLJ09jLGKNjG7u1paIkIdiZpdvC" + \
            "v6YarKAN8jn3CCodYO1bt1oU405"
        api_key = "fa2e40daf2fd28167e4e9f8fc88273896565f8cc66777d2e2f6a6f304fe06e1f366b436522ee31fa" + \
            "21bbcbbca7a066c2179718e988ba96745e1d3d42402dd86bde5d725857b289e3b75f7875b3a2ebf27d06f30" + \
            "8005a3f5851d35dd699290c63e11f1716158cf65f189e500f746b30c195b9f803e4db2235130783d83306862f"

        login_url = configuration.host + "/v2/auth"
        data = json.dumps(
            {'apiClientID': client_id, 'apiClientSecret': client_secret, "apiKey": api_key}
        )
        headers = {'content-type': 'application/json'}

        r = requests.post(login_url, data, headers=headers)
        access_token = r.json()['data']['accessToken']
        configuration.api_key['Authorization'] = access_token
        api_client = ApiClient(configuration=configuration)

        self.api = salarydk.api.employees_api.EmployeesApi(api_client)  # noqa: E501
        self.employment_api = salarydk.api.employments_api.EmploymentsApi(api_client)
        self.employment_positions_id_of_arkivar = "57cf8192-04ed-57e1-5228-5dd16e6611ec"
        self.leave_types_api = salarydk.api.leave_types_api.LeaveTypesApi(api_client)
        self.salary_types_api = salarydk.api.salary_types_api.SalaryTypesApi(api_client)
        self.contracts_api = salarydk.api.employee_contracts_api.EmployeeContractsApi(api_client)
        self.time_registrations_api = salarydk.api.time_registrations_api.TimeRegistrationsApi(api_client)
        companies = salarydk.api.companies_api.CompaniesApi(api_client).get_companies()
        salary_cycles = salarydk.api.salary_cycles_api.SalaryCyclesApi(api_client).get_salary_cycles(include_salary_periods=True, limit=100)
        self.production_unit_uuid = companies.data[0].production_units[0].id
        self.salary_id_uuid = '2c28f6ab-40ec-5c2b-6460-a1365de18e4e'  # salary cycle id
        self.salary_type_id = '66d888a6-17a5-4ad5-7506-24a59e3db1a6'
        self.salary_type_id_150 = 'ff769eba-9b23-4af2-7156-7e9fc5b329d1'
        self.employee_id = 'eabdbec8-dc5b-4d35-6b96-c2f7d6d5e3d3'

    def tearDown(self):
        pass

    # @unittest.skip
    def test_create_salary_type(self):
        salary_type = {
            "class": "Hourly",
            "companyID": self.company_id,
            "includeInPensionBasis": False,
            "includeInVacationBasis": False,
            "title": "Ackro 170"
        }
        data = self.salary_types_api.create_salary_type(salary_type=salary_type)
        self.assertIsNotNone(data)

    def test_get_salary_types(self):

        data = self.salary_types_api.get_salary_types(self.company_id)
        self.assertIsNotNone(data)

    def test_create_employee(self):
        """Test case for create_employee

        """

        employee = {
                'address': 'Kungsgatan 2000',
                'affiliationType': 'Standard',
                'bankAccountNumber': '7180982',
                'bankRegistrationNumber': '5479',
                'city': 'Copenhagen',
                'companyID': self.company_id,
                'email': "{}@example.com".format(randomword(6)),
                'language': 'da',
                'name': "{}".format(randomword(6)),
                'nationalID':  generate_cpr(),
                'phoneNumber': '4542422325',
                'postalCode': '2000',
                'sendLogin': False
        }
        employee = self.api.create_employee(employee=employee)
        self.assertIsNotNone(employee.data)
        self.employee_id = employee.data.id

    # @unittest.skip
    def test_get_employees(self):
        """Test case for get_employees

        List employees  # noqa: E501
        """
        employees = self.api.get_employees(company_id="582c9956-bebc-4588-4189-480dfaf15d76")
        self.assertIsNotNone(employees.data)

    @unittest.skip
    def test_delete_employees(self):
        """Test case for get_employees

        List employees  # noqa: E501
        """
        employees = self.api.get_employees(company_id="582c9956-bebc-4588-4189-480dfaf15d76")
        self.assertIsNotNone(employees.data)
        # for emp in employees.data:
        #     self.api.delete_employee(emp.id)

    def test_create_employment(self):
        """Test case for create employment.

        Create employement  # noqa: E501
        """
        employee = {
                'address': 'Kungsgatan 2000',
                'affiliationType': 'Standard',
                'bankAccountNumber': '7180982',
                'bankRegistrationNumber': '5479',
                'city': 'Copenhagen',
                'companyID': self.company_id,
                'email': "{}@example.com".format(randomword(6)),
                'language': 'da',
                'name': "Jan {}".format(randomword(6)),
                # 'name': 'Jan Kowalski',
                'nationalID':  generate_cpr(),
                'phoneNumber': '4542422325',
                'postalCode': '2000',
                'sendLogin': False
        }
        employee = self.api.create_employee(employee=employee)

        employment = {
            "employeeID": employee.data.id,
            "employeeNumber": "meplosa-{}".format(randomword(6)),
            "preferredTaxCardType": "Primary",
            "startDate": "2018-12-15",
            "endDate": "2018-12-31"
        }
        employment = self.employment_api.create_employment(employment=employment)
        self.assertIsNotNone(employment.data)

    def test_create_employment_contract(self):
        """Test case for create contract.

        Create contract  # noqa: E501
        """
        employee = {
                'address': 'Kungsgatan 2000',
                'affiliationType': 'Standard',  # use value 'Director' and will start working
                'bankAccountNumber': '7180982',
                'bankRegistrationNumber': '5479',
                'city': 'Copenhagen',
                'companyID': self.company_id,
                'email': "{}@example.com".format(randomword(6)),
                'language': 'da',
                # 'name': "{}".format(randomword(6)),
                'name': 'Tomasz Kowalski',
                'nationalID':  generate_cpr(),
                'phoneNumber': '4542422325',
                'postalCode': '2000',
                'sendLogin': False
        }
        employee = self.api.create_employee(employee=employee)

        employment = {
            "employeeID": employee.data.id,
            "employeeNumber": "meplosa-{}".format(randomword(6)),
            "preferredTaxCardType": "Primary",
            "startDate": "2018-12-15",
            "endDate": "2022-12-31"
        }
        employment = self.employment_api.create_employment(employment=employment)
        self.assertIsNotNone(employment.data)

        leave_types = self.leave_types_api.get_leave_types(self.company_id)
        leave_type_id = [lt.id for lt in leave_types.data if lt.name == 'DenmarkVacationFund'][0]

        employee_contract = {
            "carAllowanceRegistrationMethodType": "Coarse",
            "employmentID": employment.data.id,
            "employmentPositionID": self.employment_positions_id_of_arkivar,
            "employmentType": "Ordinary",
            "position": "string",
            "manualVacationFund": False,
            "productionUnitID": self.production_unit_uuid,
            "remuneration": {
                "salary": [
                    {
                        "rate": 120,
                        "title": "example title",
                        "salaryTypeID": self.salary_type_id,
                        "type": 'Hourly'
                    },
                    {
                        "rate": 150,
                        "title": "Ackro 150",
                        "salaryTypeID": self.salary_type_id_150,
                        "type": 'Hourly'
                    }
                ],
                "benefits": [],
                "leave": [
                    {
                        'days': 25,
                        'typeID': leave_type_id,
                    }
                ],
                "pension": [],
                "supplements": []
            },
            "remunerationType": "Hourly",
            "salaryCycleID": self.salary_id_uuid,
            "timeRegistrationMethodType": "Detailed",
            "validFrom": "2021-08-30",
            # "validTo": "2021-12-22",
            "varyingWorkplace": True,
            "weeklyHours": 35,
            "weeklyWorkDays": 5,
        }

        contract = self.contracts_api.create_employee_contract(
            employee_contract=employee_contract)
        self.assertIsNotNone(contract.data)
    
    def test_contract_update(self):
        contract_id = '97f31e36-0deb-40c6-74ff-44819a804d29'
        contract = self.contracts_api.get_employee_contract(employee_contract_id=contract_id)
        # contract.data.productionUnitID = self.production_unit_uuid
        self.contracts_api.update_employee_contract(
            employee_contract_id=contract.data.id,
            employee_contract=contract.data
        )

    def get_active_contract(self, employee_id):
        contracts = self.contracts_api.get_employee_contracts(employee_id=employee_id).data
        for contract in contracts:
            if (contract.valid_from <= date.today() and contract.valid_to is None) or (contract.valid_from <= date.today() and contract.valid_to >= date.today()):
                return contract
        return None

    def test_contract_update_with_pension(self):
        employee_id = '1b2d368d-6d80-48ee-6923-67e906117f97'
        contract = self.get_active_contract(employee_id)
        self.assertIsNotNone(contract)
        employee_contract = self._build_contract_data(contract)
        # contract = self.contracts_api.create_employee_contract(
        #     employee_contract=employee_contract)

    def _build_contract_data(self, sal_contract, salary_types=[], update_on_salary_change_only=True):

        leave_types = self.leave_types_api.get_leave_types(self.company_id)
        leave_type_id = [lt.id for lt in leave_types.data if lt.name == 'DenmarkVacationFund'][0]
        salary_list = []
        for sal in sal_contract.remuneration.salary:
            salary_list.append(
                {
                        "rate": sal.rate,
                        "title": sal.title,
                        "salaryTypeID": sal.salary_type_id,
                        "type": 'Hourly'
                }
            )
        salary_types_ids = map(lambda d: d['salaryTypeID'], salary_list)
        for salary_type in salary_types:
            if salary_type.sal_id in salary_types_ids:
                continue
            salary_list.append(
                {
                        "rate": salary_type.hourly_rate,
                        "title": salary_type.title,
                        "salaryTypeID": salary_type.sal_id,
                        "type": 'Hourly'
                }
            )

        pension_list = []
        for pension in sal_contract.remuneration.pension:
            pension_list.append(
                {
                    'title': pension.title,
                    'scheme': pension.scheme,
                    'destinationType': pension.destination_type,
                    'pensionCustomerID': pension.pension_customer_id,
                    'pensionCompanyID': pension.pension_company_id,
                    'percentage': pension.percentage
                }
            )

        supplement_list = []
        for sup in sal_contract.remuneration.supplements:
            supplement_list.append(
                {
                    'compensationRate': sup.compensation_rate,
                    'typeID': sup.type_id,
                    'type': {
                        'compensationType': sup.type.compensation_type,
                        'cycle': sup.type.cycle,
                        'cycleStart': int(sup.type.cycle_start),
                        'includeInPensionBasis': sup.type.include_in_pension_basis,
                        'payoutOnExpiration': sup.type.payout_on_expiration,
                        'payoutOnTermination': sup.type.payout_on_termination,
                        'title': sup.type.title,
                        'vesting': sup.type.vesting
                    }
                }
            )

        employee_contract = {
            "carAllowanceRegistrationMethodType": "Coarse",
            "employmentID": sal_contract.employment_id,
            "employmentPositionID": self.employment_positions_id_of_arkivar,
            "employmentType": "Ordinary",
            "position": "string",
            "manualVacationFund": False,
            "productionUnitID": sal_contract.production_unit_id,
            "remuneration": {
                "salary": salary_list,
                "benefits": [],
                "leave": [
                    {
                        'days': 25,
                        'typeID': leave_type_id,
                    }
                ],
                "pension": pension_list,
                "supplements": supplement_list
            },
            "remunerationType": "Hourly",
            "salaryCycleID": sal_contract.salary_cycle_id,
            "timeRegistrationMethodType": "Detailed",
            "validFrom": sal_contract.valid_from,
            # "validTo": "2021-12-22",
            "varyingWorkplace": True,
            "weeklyHours": sal_contract.weekly_hours,
            "weeklyWorkDays": 5,
        }
        return employee_contract

    def test_time_registration(self):
        time_registration = {
            "class": "Hours",
            "date": "2021-09-14",
            "employeeID": self.employee_id,
            "hours": 4,
            # "salaryTypeID": '0ba2b6dd-8718-45cd-668c-67b2ad307361',
            "typeName": '0ba2b6dd-8718-45cd-668c-67b2ad307361'
        }

        data = self.time_registrations_api.create_time_registration(
            time_registration=time_registration
        )

        time_registration = {
            "class": "Hours",
            "date": "2021-09-14",
            "employeeID": self.employee_id,
            "hours": 3.5,
            # "salaryTypeID": 'ed97cef8-c443-457e-58ee-109a8b3d5212',
            "typeName": 'ed97cef8-c443-457e-58ee-109a8b3d5212'

        }

        data = self.time_registrations_api.create_time_registration(
            time_registration=time_registration
        )
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
