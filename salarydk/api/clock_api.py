# coding: utf-8

"""
    Salary.dk API

    This is the public API for Salary.dk.  # General  Our API is a JSON-based, REST-like API. Our webapp uses the exact same API, so everything you can do in our webapp, you can do through our API. However, we are slowly opening up the API, so not all endpoints are documented here yet. Only the endpoints documented here are stable. If there is some functionality you would like to access through our API, please contact us.  The API is located at https://api.salary.dk. All requests must use TLS.  In order to use the API on behalf of other users than yourself, you need to register as an API client. You do this by sending an e-mail to dev@salary.dk with the name and purpose of your client.  API-keys for each account can be obtained once logged in to Salary, under the settings for the Company.  All endpoints are documented to be able to return the 500 error code. We strive to not return this error code, so if you do encounter this error code, it might mean there is an error on our side. In this case, do not hesitate to contact us.  # Versioning, upgrade and deprecation policy Our API might change over time. In order to ensure a stable API, we follow these rules when changing the API.  New fields might be added at any time to any response or as non-required parameters to any input. When adding input fields, we ensure the default behaviour when not supplying the field is the same as the previous version. In these cases, the version of an endpoint is not increased, since it is backwards compatible. Since we might add new fields to responses, be sure to use a JSON parser in your implementation. This ensures that any extra fields added are ignored by your implementation.  We might add entirely new endpoints at any time. If we need to change an existing endpoint without being able to make it backwards compatible, we will add a new version of the endpoint, and mark the old as deprecated but still functional. We will then contact any users of the deprecated endpoint and ensure an upgrade is performed. Once all consumers have moved to the new endpoint version, the old one will be removed.  We will not at any point change the meaning of any existing field, nor will we remove any field or endpoint without following the above deprecated procedure. However, we might add new types to existing enums at any time.  # Cross-Origin Resource Sharing This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/) - and that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site, as long as the proper access token is passed.  # Authentication All request require an access token. There are two ways to obtain an access token: * Logging in as a user. (this endpoint is not yet publicly available). * Using an API-key: [endpoint](#operation/APIClientLogin)  Using one of these methods, you will obtain an access token. In all subsequest requests, this access token should be passed in the Authorization header. The access token is valid for around one hour, after which a new token should be obtained.  You do not need to dispose of access tokens once created. They have a limited lifetime, and Salary.dk will automatically expire old ones.  For some endpoints, the authorizedUserQuery security definition is used. This allows for passing the access token as a query parameter where it is not possible to pass it as a header. In particular, this is used for downloading files.  <!-- ReDoc-Inject: <security-definitions> -->   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@salary.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from salarydk.api_client import ApiClient
from salarydk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ClockApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rebase_clock(self, rebase_ts, **kwargs):  # noqa: E501
        """rebase_clock  # noqa: E501

        rebase the clock, sets the current time on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rebase_clock(rebase_ts, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime rebase_ts: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.rebase_clock_with_http_info(rebase_ts, **kwargs)  # noqa: E501

    def rebase_clock_with_http_info(self, rebase_ts, **kwargs):  # noqa: E501
        """rebase_clock  # noqa: E501

        rebase the clock, sets the current time on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rebase_clock_with_http_info(rebase_ts, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime rebase_ts: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20030, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rebase_ts'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rebase_clock" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rebase_ts' is set
        if self.api_client.client_side_validation and ('rebase_ts' not in local_var_params or  # noqa: E501
                                                        local_var_params['rebase_ts'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rebase_ts` when calling `rebase_clock`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rebase_ts' in local_var_params and local_var_params['rebase_ts'] is not None:  # noqa: E501
            query_params.append(('rebaseTs', local_var_params['rebase_ts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authorizedUser']  # noqa: E501

        return self.api_client.call_api(
            '/v2/clock', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20030',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def time_now(self, **kwargs):  # noqa: E501
        """time_now  # noqa: E501

        get the current time on server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.time_now(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.time_now_with_http_info(**kwargs)  # noqa: E501

    def time_now_with_http_info(self, **kwargs):  # noqa: E501
        """time_now  # noqa: E501

        get the current time on server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.time_now_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20030, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method time_now" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/clock', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20030',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
