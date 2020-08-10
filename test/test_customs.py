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
from pbshipping.models.customs import Customs  # noqa: E501
from pbshipping.rest import ApiException

class TestCustoms(unittest.TestCase):
    """Customs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Customs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.customs.Customs()  # noqa: E501
        if include_optional :
            return Customs(
                customs_info = pbshipping.models.customs_info.CustomsInfo(
                    eelpfc = '0', 
                    blanket_end_date = '0', 
                    blanket_start_date = '0', 
                    certificate_number = '0', 
                    comments = '0', 
                    currency_code = '0', 
                    customs_declared_value = 1.337, 
                    declaration_statement = '0', 
                    freight_charge = 1.337, 
                    from_customs_reference = '0', 
                    handling_costs = 1.337, 
                    importer_customs_reference = '0', 
                    insured_amount = 1.337, 
                    insured_number = '0', 
                    invoice_number = '0', 
                    license_number = '0', 
                    other_charge = 1.337, 
                    other_description = '0', 
                    other_type = 'COMMISSIONS', 
                    packing_costs = 1.337, 
                    producer_specification = 'MULTIPLE_SPECIFIED', 
                    reason_for_export = 'GIFT', 
                    reason_for_export_explanation = '0', 
                    sdr_value = 1.337, 
                    shipping_document_type = 'NAFTA', 
                    signature_contact = pbshipping.models.address.Address(
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
                    terms_of_sale = '0', ), 
                customs_items = [
                    pbshipping.models.customs_item.CustomsItem(
                        description = '0', 
                        h_s_tariff_code = '0', 
                        net_cost_method = 'NO_NET_COST', 
                        origin_country_code = '0', 
                        origin_state_province = '0', 
                        preference_criterion = 'A', 
                        producer_address = pbshipping.models.address.Address(
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
                        producer_determination = 'NO_1', 
                        producer_id = '0', 
                        quantity = 56, 
                        quantity_uom = '0', 
                        unit_price = 1.337, 
                        unit_weight = pbshipping.models.parcel_weight.ParcelWeight(
                            weight = 1.337, 
                            unit_of_measurement = 'GM', ), )
                    ]
            )
        else :
            return Customs(
        )

    def testCustoms(self):
        """Test Customs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()