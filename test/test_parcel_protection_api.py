# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pbshipping
from pbshipping.api.parcel_protection_api import ParcelProtectionApi  # noqa: E501
from pbshipping.rest import ApiException


class TestParcelProtectionApi(unittest.TestCase):
    """ParcelProtectionApi unit test stubs"""

    def setUp(self):
        self.api = pbshipping.api.parcel_protection_api.ParcelProtectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_parcel_protection(self):
        """Test case for cancel_parcel_protection

        Parcel Protection Coverage  # noqa: E501
        """
        pass

    def test_get_parcel_protection_coverage(self):
        """Test case for get_parcel_protection_coverage

        Parcel Protection Coverage  # noqa: E501
        """
        pass

    def test_get_parcel_protection_quote(self):
        """Test case for get_parcel_protection_quote

        Parcel Protection Quote  # noqa: E501
        """
        pass

    def test_get_parcel_protection_reports(self):
        """Test case for get_parcel_protection_reports

        Parcel Protection Reports  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()