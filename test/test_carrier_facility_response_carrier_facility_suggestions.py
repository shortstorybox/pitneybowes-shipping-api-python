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
from pbshipping.models.carrier_facility_response_carrier_facility_suggestions import CarrierFacilityResponseCarrierFacilitySuggestions  # noqa: E501
from pbshipping.rest import ApiException

class TestCarrierFacilityResponseCarrierFacilitySuggestions(unittest.TestCase):
    """CarrierFacilityResponseCarrierFacilitySuggestions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CarrierFacilityResponseCarrierFacilitySuggestions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.carrier_facility_response_carrier_facility_suggestions.CarrierFacilityResponseCarrierFacilitySuggestions()  # noqa: E501
        if include_optional :
            return CarrierFacilityResponseCarrierFacilitySuggestions(
                address = pbshipping.models.address.Address(
                    address_lines = [
                        '0'
                        ], 
                    carrier_route = '0', 
                    city_town = '0', 
                    company = '0', 
                    country_code = '0', 
                    delivery_point = '0', 
                    email = '0', 
                    name = '0', 
                    phone = '0', 
                    postal_code = '0', 
                    residential = True, 
                    state_province = '0', 
                    status = 'PARSED', 
                    tax_id = '0', 
                    tax_id_type = 'EIN', ), 
                carrier_facility_attributes = [
                    pbshipping.models.carrier_facility_response_carrier_facility_options.CarrierFacilityResponse_carrierFacilityOptions(
                        name = '0', 
                        value = '0', )
                    ], 
                facility_hours = [
                    pbshipping.models.carrier_facility_response_facility_hours.CarrierFacilityResponse_facilityHours(
                        day = '0', 
                        facility_timings = [
                            pbshipping.models.carrier_facility_response_facility_timings.CarrierFacilityResponse_facilityTimings(
                                closes_at = '0', 
                                opens_at = '0', )
                            ], )
                    ], 
                facility_parking = '0'
            )
        else :
            return CarrierFacilityResponseCarrierFacilitySuggestions(
        )

    def testCarrierFacilityResponseCarrierFacilitySuggestions(self):
        """Test CarrierFacilityResponseCarrierFacilitySuggestions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()