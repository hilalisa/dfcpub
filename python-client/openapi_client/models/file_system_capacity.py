# coding: utf-8

"""
    DFC

    DFC is a scalable object-storage based caching system with Amazon and Google Cloud backends.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: dfcdev@exchange.nvidia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FileSystemCapacity(object):
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
        'used': 'int',
        'avail': 'int',
        'usedpct': 'int'
    }

    attribute_map = {
        'used': 'used',
        'avail': 'avail',
        'usedpct': 'usedpct'
    }

    def __init__(self, used=None, avail=None, usedpct=None):  # noqa: E501
        """FileSystemCapacity - a model defined in OpenAPI"""  # noqa: E501

        self._used = None
        self._avail = None
        self._usedpct = None
        self.discriminator = None

        if used is not None:
            self.used = used
        if avail is not None:
            self.avail = avail
        if usedpct is not None:
            self.usedpct = usedpct

    @property
    def used(self):
        """Gets the used of this FileSystemCapacity.  # noqa: E501


        :return: The used of this FileSystemCapacity.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this FileSystemCapacity.


        :param used: The used of this FileSystemCapacity.  # noqa: E501
        :type: int
        """

        self._used = used

    @property
    def avail(self):
        """Gets the avail of this FileSystemCapacity.  # noqa: E501


        :return: The avail of this FileSystemCapacity.  # noqa: E501
        :rtype: int
        """
        return self._avail

    @avail.setter
    def avail(self, avail):
        """Sets the avail of this FileSystemCapacity.


        :param avail: The avail of this FileSystemCapacity.  # noqa: E501
        :type: int
        """

        self._avail = avail

    @property
    def usedpct(self):
        """Gets the usedpct of this FileSystemCapacity.  # noqa: E501


        :return: The usedpct of this FileSystemCapacity.  # noqa: E501
        :rtype: int
        """
        return self._usedpct

    @usedpct.setter
    def usedpct(self, usedpct):
        """Sets the usedpct of this FileSystemCapacity.


        :param usedpct: The usedpct of this FileSystemCapacity.  # noqa: E501
        :type: int
        """

        self._usedpct = usedpct

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
        if not isinstance(other, FileSystemCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
