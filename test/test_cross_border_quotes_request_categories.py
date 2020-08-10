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
import datetime

import pbshipping
from pbshipping.models.cross_border_quotes_request_categories import CrossBorderQuotesRequestCategories  # noqa: E501
from pbshipping.rest import ApiException

class TestCrossBorderQuotesRequestCategories(unittest.TestCase):
    """CrossBorderQuotesRequestCategories unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesRequestCategories
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.cross_border_quotes_request_categories.CrossBorderQuotesRequestCategories()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesRequestCategories(
                category_code = '0', 
                descriptions = [
                    pbshipping.models.cross_border_quotes_request_descriptions.CrossBorderQuotesRequest_descriptions(
                        locale = '0', 
                        name = '0', 
                        parents_names = [
                            '0'
                            ], )
                    ], 
                parent_category_code = '0', 
                url = '0'
            )
        else :
            return CrossBorderQuotesRequestCategories(
        )

    def testCrossBorderQuotesRequestCategories(self):
        """Test CrossBorderQuotesRequestCategories"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()