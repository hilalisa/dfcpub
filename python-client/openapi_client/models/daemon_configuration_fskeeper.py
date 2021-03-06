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


class DaemonConfigurationFskeeper(object):
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
        'fs_check_time': 'str',
        'offline_fs_check_time': 'str',
        'fskeeper_enabled': 'bool'
    }

    attribute_map = {
        'fs_check_time': 'fs_check_time',
        'offline_fs_check_time': 'offline_fs_check_time',
        'fskeeper_enabled': 'fskeeper_enabled'
    }

    def __init__(self, fs_check_time=None, offline_fs_check_time=None, fskeeper_enabled=None):  # noqa: E501
        """DaemonConfigurationFskeeper - a model defined in OpenAPI"""  # noqa: E501

        self._fs_check_time = None
        self._offline_fs_check_time = None
        self._fskeeper_enabled = None
        self.discriminator = None

        if fs_check_time is not None:
            self.fs_check_time = fs_check_time
        if offline_fs_check_time is not None:
            self.offline_fs_check_time = offline_fs_check_time
        if fskeeper_enabled is not None:
            self.fskeeper_enabled = fskeeper_enabled

    @property
    def fs_check_time(self):
        """Gets the fs_check_time of this DaemonConfigurationFskeeper.  # noqa: E501


        :return: The fs_check_time of this DaemonConfigurationFskeeper.  # noqa: E501
        :rtype: str
        """
        return self._fs_check_time

    @fs_check_time.setter
    def fs_check_time(self, fs_check_time):
        """Sets the fs_check_time of this DaemonConfigurationFskeeper.


        :param fs_check_time: The fs_check_time of this DaemonConfigurationFskeeper.  # noqa: E501
        :type: str
        """

        self._fs_check_time = fs_check_time

    @property
    def offline_fs_check_time(self):
        """Gets the offline_fs_check_time of this DaemonConfigurationFskeeper.  # noqa: E501


        :return: The offline_fs_check_time of this DaemonConfigurationFskeeper.  # noqa: E501
        :rtype: str
        """
        return self._offline_fs_check_time

    @offline_fs_check_time.setter
    def offline_fs_check_time(self, offline_fs_check_time):
        """Sets the offline_fs_check_time of this DaemonConfigurationFskeeper.


        :param offline_fs_check_time: The offline_fs_check_time of this DaemonConfigurationFskeeper.  # noqa: E501
        :type: str
        """

        self._offline_fs_check_time = offline_fs_check_time

    @property
    def fskeeper_enabled(self):
        """Gets the fskeeper_enabled of this DaemonConfigurationFskeeper.  # noqa: E501


        :return: The fskeeper_enabled of this DaemonConfigurationFskeeper.  # noqa: E501
        :rtype: bool
        """
        return self._fskeeper_enabled

    @fskeeper_enabled.setter
    def fskeeper_enabled(self, fskeeper_enabled):
        """Sets the fskeeper_enabled of this DaemonConfigurationFskeeper.


        :param fskeeper_enabled: The fskeeper_enabled of this DaemonConfigurationFskeeper.  # noqa: E501
        :type: bool
        """

        self._fskeeper_enabled = fskeeper_enabled

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
        if not isinstance(other, DaemonConfigurationFskeeper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
