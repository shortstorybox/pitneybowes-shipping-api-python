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


class CrossBorderQuotesRequestItemDimension(object):
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
        'length': 'int',
        'height': 'float',
        'width': 'int',
        'unit_of_measurement': 'str'
    }

    attribute_map = {
        'length': 'length',
        'height': 'height',
        'width': 'width',
        'unit_of_measurement': 'unitOfMeasurement'
    }

    def __init__(self, length=None, height=None, width=None, unit_of_measurement=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesRequestItemDimension - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._length = None
        self._height = None
        self._width = None
        self._unit_of_measurement = None
        self.discriminator = None

        if length is not None:
            self.length = length
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if unit_of_measurement is not None:
            self.unit_of_measurement = unit_of_measurement

    @property
    def length(self):
        """Gets the length of this CrossBorderQuotesRequestItemDimension.  # noqa: E501


        :return: The length of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CrossBorderQuotesRequestItemDimension.


        :param length: The length of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def height(self):
        """Gets the height of this CrossBorderQuotesRequestItemDimension.  # noqa: E501


        :return: The height of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CrossBorderQuotesRequestItemDimension.


        :param height: The height of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this CrossBorderQuotesRequestItemDimension.  # noqa: E501


        :return: The width of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CrossBorderQuotesRequestItemDimension.


        :param width: The width of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this CrossBorderQuotesRequestItemDimension.  # noqa: E501


        :return: The unit_of_measurement of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this CrossBorderQuotesRequestItemDimension.


        :param unit_of_measurement: The unit_of_measurement of this CrossBorderQuotesRequestItemDimension.  # noqa: E501
        :type: str
        """

        self._unit_of_measurement = unit_of_measurement

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
        if not isinstance(other, CrossBorderQuotesRequestItemDimension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesRequestItemDimension):
            return True

        return self.to_dict() != other.to_dict()