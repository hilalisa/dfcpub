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


class DaemonConfigurationTestFspaths(object):
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
        'root': 'str',
        'count': 'int',
        'instance': 'int'
    }

    attribute_map = {
        'root': 'root',
        'count': 'count',
        'instance': 'instance'
    }

    def __init__(self, root=None, count=None, instance=None):  # noqa: E501
        """DaemonConfigurationTestFspaths - a model defined in OpenAPI"""  # noqa: E501

        self._root = None
        self._count = None
        self._instance = None
        self.discriminator = None

        if root is not None:
            self.root = root
        if count is not None:
            self.count = count
        if instance is not None:
            self.instance = instance

    @property
    def root(self):
        """Gets the root of this DaemonConfigurationTestFspaths.  # noqa: E501


        :return: The root of this DaemonConfigurationTestFspaths.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this DaemonConfigurationTestFspaths.


        :param root: The root of this DaemonConfigurationTestFspaths.  # noqa: E501
        :type: str
        """

        self._root = root

    @property
    def count(self):
        """Gets the count of this DaemonConfigurationTestFspaths.  # noqa: E501


        :return: The count of this DaemonConfigurationTestFspaths.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DaemonConfigurationTestFspaths.


        :param count: The count of this DaemonConfigurationTestFspaths.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def instance(self):
        """Gets the instance of this DaemonConfigurationTestFspaths.  # noqa: E501


        :return: The instance of this DaemonConfigurationTestFspaths.  # noqa: E501
        :rtype: int
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this DaemonConfigurationTestFspaths.


        :param instance: The instance of this DaemonConfigurationTestFspaths.  # noqa: E501
        :type: int
        """

        self._instance = instance

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
        if not isinstance(other, DaemonConfigurationTestFspaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other