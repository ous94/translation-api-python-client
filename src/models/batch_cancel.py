#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


class BatchCancel(object):
    """
    NOTE: This class is auto generated by the systran code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Systran model

        :param dict systran_types: The key is attribute name and the value is attribute type.
        :param dict attribute_map: The key is attribute name and the value is json key in definition.
        """
        self.systran_types = {
            'status': 'str',
            'error': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'error': 'error'
        }
        
        # Result of the request
        self.status = None  # str
        
        # Error of the request
        self.error = None  # str
        

    def __repr__(self):
        properties = []
        for p in self.__dict__:
            if p != 'systran_types' and p != 'attribute_map':
                properties.append('{prop}={val!r}'.format(prop=p, val=self.__dict__[p]))

        return '<{name} {props}>'.format(name=__name__, props=' '.join(properties))


