# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pbshipping.configuration import Configuration


class TrackingResponse(object):
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
        'package_count': 'int',
        'carrier': 'str',
        'service_name': 'str',
        'tracking_number': 'str',
        'reference_number': 'str',
        'status': 'str',
        'updated_date': 'date',
        'updated_time': 'str',
        'ship_date': 'date',
        'ship_time': 'str',
        'ship_time_offset': 'str',
        'estimated_delivery_date': 'date',
        'estimated_delivery_time': 'str',
        'estimated_delivery_time_offset': 'str',
        'delivery_date': 'date',
        'delivery_time': 'str',
        'delivery_time_offset': 'str',
        'delivery_location': 'str',
        'delivery_location_description': 'str',
        'signed_by': 'str',
        'weight': 'float',
        'weight_oum': 'str',
        'reattempt_date': 'date',
        'reattempt_time': 'str',
        'destination_address': 'TrackingAddress',
        'sender_address': 'TrackingAddress',
        'scan_details_list': 'list[TrackingResponseScanDetailsList]',
        'current_status': 'TrackingResponseScanDetailsList',
        'last_package_status_location': 'str'
    }

    attribute_map = {
        'package_count': 'packageCount',
        'carrier': 'carrier',
        'service_name': 'serviceName',
        'tracking_number': 'trackingNumber',
        'reference_number': 'referenceNumber',
        'status': 'status',
        'updated_date': 'updatedDate',
        'updated_time': 'updatedTime',
        'ship_date': 'shipDate',
        'ship_time': 'shipTime',
        'ship_time_offset': 'shipTimeOffset',
        'estimated_delivery_date': 'estimatedDeliveryDate',
        'estimated_delivery_time': 'estimatedDeliveryTime',
        'estimated_delivery_time_offset': 'estimatedDeliveryTimeOffset',
        'delivery_date': 'deliveryDate',
        'delivery_time': 'deliveryTime',
        'delivery_time_offset': 'deliveryTimeOffset',
        'delivery_location': 'deliveryLocation',
        'delivery_location_description': 'deliveryLocationDescription',
        'signed_by': 'signedBy',
        'weight': 'weight',
        'weight_oum': 'weightOUM',
        'reattempt_date': 'reattemptDate',
        'reattempt_time': 'reattemptTime',
        'destination_address': 'destinationAddress',
        'sender_address': 'senderAddress',
        'scan_details_list': 'scanDetailsList',
        'current_status': 'currentStatus',
        'last_package_status_location': 'lastPackageStatusLocation'
    }

    def __init__(self, 
            package_count=None, 
            carrier=None, 
            service_name=None,
            tracking_number=None, 
            reference_number=None, 
            status=None, 
            updated_date=None, 
            updated_time=None, 
            ship_date=None, 
            ship_time=None,
            ship_time_offset=None,
            estimated_delivery_date=None, 
            estimated_delivery_time=None, 
            estimated_delivery_time_offset=None, 
            delivery_date=None, 
            delivery_time=None, 
            delivery_time_offset=None, 
            delivery_location=None,
            delivery_location_description=None,
            signed_by=None,
            weight=None,
            weight_oum=None,
            reattempt_date=None, 
            reattempt_time=None, 
            destination_address=None, 
            sender_address=None, 
            scan_details_list=None, 
            current_status=None,
            last_package_status_location=None,
            local_vars_configuration=None
        ):  # noqa: E501
        """TrackingResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._package_count = None
        self._carrier = None
        self._tracking_number = None
        self._reference_number = None
        self._status = None
        self._updated_date = None
        self._updated_time = None
        self._ship_date = None
        self._estimated_delivery_date = None
        self._estimated_delivery_time = None
        self._delivery_date = None
        self._delivery_time = None
        self._delivery_location = None
        self._delivery_location_description = None
        self._signed_by = None
        self._weight = None
        self._weight_oum = None
        self._reattempt_date = None
        self._reattempt_time = None
        self._destination_address = None
        self._sender_address = None
        self._scan_details_list = None
        self.discriminator = None
        self._service_name=None
        self._ship_time=None
        self._ship_time_offset=None
        self._estimated_delivery_time_offset=None
        self._delivery_time_offset=None
        self._current_status=None
        self._last_package_status_location=None


        if package_count is not None:
            self.package_count = package_count
        if carrier is not None:
            self.carrier = carrier
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if reference_number is not None:
            self.reference_number = reference_number
        if status is not None:
            self.status = status
        if updated_date is not None:
            self.updated_date = updated_date
        if updated_time is not None:
            self.updated_time = updated_time
        if ship_date is not None:
            self.ship_date = ship_date
        if estimated_delivery_date is not None:
            self.estimated_delivery_date = estimated_delivery_date
        if estimated_delivery_time is not None:
            self.estimated_delivery_time = estimated_delivery_time
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if delivery_time is not None:
            self.delivery_time = delivery_time
        if delivery_location is not None:
            self.delivery_location = delivery_location
        if delivery_location_description is not None:
            self.delivery_location_description = delivery_location_description
        if signed_by is not None:
            self.signed_by = signed_by
        if weight is not None:
            self.weight = weight
        if weight_oum is not None:
            self.weight_oum = weight_oum
        if reattempt_date is not None:
            self.reattempt_date = reattempt_date
        if reattempt_time is not None:
            self.reattempt_time = reattempt_time
        if destination_address is not None:
            self.destination_address = destination_address
        if sender_address is not None:
            self.sender_address = sender_address
        if scan_details_list is not None:
            self.scan_details_list = scan_details_list

        if service_name is not None:
            self._service_name = service_name
        if ship_time is not None:
            self._ship_time=ship_time
        if ship_time_offset is not None:
            self._ship_time_offset=ship_time_offset,
        if estimated_delivery_time_offset is not None:
            self._estimated_delivery_time_offset=estimated_delivery_time_offset, 
        if delivery_time_offset is not None:
            self._delivery_time_offset=delivery_time_offset
        if current_status is not None:
            self._current_status=current_status
        if last_package_status_location is not None:
            self._last_package_status_location=last_package_status_location

    @property
    def package_count(self):
        """Gets the package_count of this TrackingResponse.  # noqa: E501


        :return: The package_count of this TrackingResponse.  # noqa: E501
        :rtype: int
        """
        return self._package_count

    @package_count.setter
    def package_count(self, package_count):
        """Sets the package_count of this TrackingResponse.


        :param package_count: The package_count of this TrackingResponse.  # noqa: E501
        :type: int
        """

        self._package_count = package_count

    @property
    def carrier(self):
        """Gets the carrier of this TrackingResponse.  # noqa: E501


        :return: The carrier of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this TrackingResponse.


        :param carrier: The carrier of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def service_name(self):
        """Gets the service_name of this TrackingResponse.  # noqa: E501


        :return: The service_name of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this TrackingResponse.


        :param service_name: The service_name of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def tracking_number(self):
        """Gets the tracking_number of this TrackingResponse.  # noqa: E501


        :return: The tracking_number of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this TrackingResponse.


        :param tracking_number: The tracking_number of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

    @property
    def reference_number(self):
        """Gets the reference_number of this TrackingResponse.  # noqa: E501


        :return: The reference_number of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this TrackingResponse.


        :param reference_number: The reference_number of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._reference_number = reference_number

    @property
    def status(self):
        """Gets the status of this TrackingResponse.  # noqa: E501


        :return: The status of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrackingResponse.


        :param status: The status of this TrackingResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["In Transit", "Delivered", "Manifest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_date(self):
        """Gets the updated_date of this TrackingResponse.  # noqa: E501


        :return: The updated_date of this TrackingResponse.  # noqa: E501
        :rtype: date
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this TrackingResponse.


        :param updated_date: The updated_date of this TrackingResponse.  # noqa: E501
        :type: date
        """

        self._updated_date = updated_date

    @property
    def updated_time(self):
        """Gets the updated_time of this TrackingResponse.  # noqa: E501


        :return: The updated_time of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this TrackingResponse.


        :param updated_time: The updated_time of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._updated_time = updated_time

    @property
    def ship_date(self):
        """Gets the ship_date of this TrackingResponse.  # noqa: E501


        :return: The ship_date of this TrackingResponse.  # noqa: E501
        :rtype: date
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this TrackingResponse.


        :param ship_date: The ship_date of this TrackingResponse.  # noqa: E501
        :type: date
        """

        self._ship_date = ship_date

    @property
    def estimated_delivery_date(self):
        """Gets the estimated_delivery_date of this TrackingResponse.  # noqa: E501


        :return: The estimated_delivery_date of this TrackingResponse.  # noqa: E501
        :rtype: date
        """
        return self._estimated_delivery_date

    @estimated_delivery_date.setter
    def estimated_delivery_date(self, estimated_delivery_date):
        """Sets the estimated_delivery_date of this TrackingResponse.


        :param estimated_delivery_date: The estimated_delivery_date of this TrackingResponse.  # noqa: E501
        :type: date
        """

        self._estimated_delivery_date = estimated_delivery_date

    @property
    def estimated_delivery_time(self):
        """Gets the estimated_delivery_time of this TrackingResponse.  # noqa: E501


        :return: The estimated_delivery_time of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._estimated_delivery_time

    @estimated_delivery_time.setter
    def estimated_delivery_time(self, estimated_delivery_time):
        """Sets the estimated_delivery_time of this TrackingResponse.


        :param estimated_delivery_time: The estimated_delivery_time of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._estimated_delivery_time = estimated_delivery_time

    @property
    def delivery_date(self):
        """Gets the delivery_date of this TrackingResponse.  # noqa: E501


        :return: The delivery_date of this TrackingResponse.  # noqa: E501
        :rtype: date
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this TrackingResponse.


        :param delivery_date: The delivery_date of this TrackingResponse.  # noqa: E501
        :type: date
        """

        self._delivery_date = delivery_date

    @property
    def delivery_time(self):
        """Gets the delivery_time of this TrackingResponse.  # noqa: E501


        :return: The delivery_time of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, delivery_time):
        """Sets the delivery_time of this TrackingResponse.


        :param delivery_time: The delivery_time of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._delivery_time = delivery_time

    @property
    def delivery_location(self):
        """Gets the delivery_location of this TrackingResponse.  # noqa: E501


        :return: The delivery_location of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._delivery_location

    @delivery_location.setter
    def delivery_location(self, delivery_location):
        """Sets the delivery_location of this TrackingResponse.


        :param delivery_location: The delivery_location of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._delivery_location = delivery_location

    @property
    def delivery_location_description(self):
        """Gets the delivery_location_description of this TrackingResponse.  # noqa: E501


        :return: The delivery_location_description of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._delivery_location_description

    @delivery_location_description.setter
    def delivery_location_description(self, delivery_location_description):
        """Sets the delivery_location_description of this TrackingResponse.


        :param delivery_location_description: The delivery_location_description of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._delivery_location_description = delivery_location_description

    @property
    def signed_by(self):
        """Gets the signed_by of this TrackingResponse.  # noqa: E501


        :return: The signed_by of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._signed_by

    @signed_by.setter
    def signed_by(self, signed_by):
        """Sets the signed_by of this TrackingResponse.


        :param signed_by: The signed_by of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._signed_by = signed_by

    @property
    def weight(self):
        """Gets the weight of this TrackingResponse.  # noqa: E501


        :return: The weight of this TrackingResponse.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TrackingResponse.


        :param weight: The weight of this TrackingResponse.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def weight_oum(self):
        """Gets the weight_oum of this TrackingResponse.  # noqa: E501


        :return: The weight_oum of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._weight_oum

    @weight_oum.setter
    def weight_oum(self, weight_oum):
        """Sets the weight_oum of this TrackingResponse.


        :param weight_oum: The weight_oum of this TrackingResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["LBS", "KGS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and weight_oum not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `weight_oum` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_oum, allowed_values)
            )

        self._weight_oum = weight_oum

    @property
    def reattempt_date(self):
        """Gets the reattempt_date of this TrackingResponse.  # noqa: E501


        :return: The reattempt_date of this TrackingResponse.  # noqa: E501
        :rtype: date
        """
        return self._reattempt_date

    @reattempt_date.setter
    def reattempt_date(self, reattempt_date):
        """Sets the reattempt_date of this TrackingResponse.


        :param reattempt_date: The reattempt_date of this TrackingResponse.  # noqa: E501
        :type: date
        """

        self._reattempt_date = reattempt_date

    @property
    def reattempt_time(self):
        """Gets the reattempt_time of this TrackingResponse.  # noqa: E501


        :return: The reattempt_time of this TrackingResponse.  # noqa: E501
        :rtype: str
        """
        return self._reattempt_time

    @reattempt_time.setter
    def reattempt_time(self, reattempt_time):
        """Sets the reattempt_time of this TrackingResponse.


        :param reattempt_time: The reattempt_time of this TrackingResponse.  # noqa: E501
        :type: str
        """

        self._reattempt_time = reattempt_time

    @property
    def destination_address(self):
        """Gets the destination_address of this TrackingResponse.  # noqa: E501


        :return: The destination_address of this TrackingResponse.  # noqa: E501
        :rtype: TrackingAddress
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """Sets the destination_address of this TrackingResponse.


        :param destination_address: The destination_address of this TrackingResponse.  # noqa: E501
        :type: TrackingAddress
        """

        self._destination_address = destination_address

    @property
    def sender_address(self):
        """Gets the sender_address of this TrackingResponse.  # noqa: E501


        :return: The sender_address of this TrackingResponse.  # noqa: E501
        :rtype: TrackingAddress
        """
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address):
        """Sets the sender_address of this TrackingResponse.


        :param sender_address: The sender_address of this TrackingResponse.  # noqa: E501
        :type: TrackingAddress
        """

        self._sender_address = sender_address

    @property
    def scan_details_list(self):
        """Gets the scan_details_list of this TrackingResponse.  # noqa: E501


        :return: The scan_details_list of this TrackingResponse.  # noqa: E501
        :rtype: list[TrackingResponseScanDetailsList]
        """
        return self._scan_details_list

    @scan_details_list.setter
    def scan_details_list(self, scan_details_list):
        """Sets the scan_details_list of this TrackingResponse.


        :param scan_details_list: The scan_details_list of this TrackingResponse.  # noqa: E501
        :type: list[TrackingResponseScanDetailsList]
        """

        self._scan_details_list = scan_details_list

    @property
    def ship_time(self):
        """Gets the ship_time of this TrackingResponse.

        :return: The ship_time of this TrackingResponse.
        :rtype: datetime
        """
        return self._ship_time

    @ship_time.setter
    def ship_time(self, ship_time):
        """Sets the ship_time of this TrackingResponse.

        :param ship_time: The ship_time of this TrackingResponse.
        :type: datetime
        """
        self._ship_time = ship_time

    @property
    def ship_time_offset(self):
        """Gets the ship_time_offset of this TrackingResponse.

        :return: The ship_time_offset of this TrackingResponse.
        :rtype: int
        """
        return self._ship_time_offset

    @ship_time_offset.setter
    def ship_time_offset(self, ship_time_offset):
        """Sets the ship_time_offset of this TrackingResponse.

        :param ship_time_offset: The ship_time_offset of this TrackingResponse.
        :type: int
        """
        self._ship_time_offset = ship_time_offset

    @property
    def estimated_delivery_time_offset(self):
        """Gets the estimated_delivery_time_offset of this TrackingResponse.

        :return: The estimated_delivery_time_offset of this TrackingResponse.
        :rtype: int
        """
        return self._estimated_delivery_time_offset

    @estimated_delivery_time_offset.setter
    def estimated_delivery_time_offset(self, estimated_delivery_time_offset):
        """Sets the estimated_delivery_time_offset of this TrackingResponse.

        :param estimated_delivery_time_offset: The estimated_delivery_time_offset of this TrackingResponse.
        :type: int
        """
        self._estimated_delivery_time_offset = estimated_delivery_time_offset

    @property
    def delivery_time_offset(self):
        """Gets the delivery_time_offset of this TrackingResponse.

        :return: The delivery_time_offset of this TrackingResponse.
        :rtype: int
        """
        return self._delivery_time_offset

    @delivery_time_offset.setter
    def delivery_time_offset(self, delivery_time_offset):
        """Sets the delivery_time_offset of this TrackingResponse.

        :param delivery_time_offset: The delivery_time_offset of this TrackingResponse.
        :type: int
        """
        self._delivery_time_offset = delivery_time_offset

    @property
    def current_status(self):
        """Gets the current_status of this TrackingResponse.

        :return: The current_status of this TrackingResponse.
        :rtype: str
        """
        return self._current_status

    @current_status.setter
    def current_status(self, current_status):
        """Sets the current_status of this TrackingResponse.

        :param current_status: The current_status of this TrackingResponse.
        :type: str
        """
        self._current_status = current_status

    @property
    def last_package_status_location(self):
        """Gets the last_package_status_location of this TrackingResponse.

        :return: The last_package_status_location of this TrackingResponse.
        :rtype: str
        """
        return self._last_package_status_location

    @last_package_status_location.setter
    def last_package_status_location(self, last_package_status_location):
        """Sets the last_package_status_location of this TrackingResponse.

        :param last_package_status_location: The last_package_status_location of this TrackingResponse.
        :type: str
        """
        self._last_package_status_location = last_package_status_location

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
        if not isinstance(other, TrackingResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackingResponse):
            return True

        return self.to_dict() != other.to_dict()
