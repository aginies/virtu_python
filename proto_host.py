#!/usr/bin/env python3
# Authors: Antoine Ginies <aginies@suse.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
Host side
create some XML files
"""

import uuid
#import os
from string import Template
import template


def create_net_xml(file, net_data):
    """
    Create a libvirt XML for the network bridge
    """
    xml_template = template.NETWORK_TEMPLATE
    xml_info = {
        'uuid': str(uuid.uuid4()),
        'network_name': net_data['network_name'],
        'bridge': net_data['bridge'],
        'ip': net_data['ip'],
        'dhcp_start': '.'.join(net_data['ip'].split('.')[0:3]+[net_data['dhcp_start']]),
        'dhcp_end': '.'.join(net_data['ip'].split('.')[0:3]+[net_data['dhcp_end']]),
    }

    xml = Template(xml_template).substitute(xml_info)
    with open(file, 'w') as file_h:
        file_h.write(xml)

def create_storage_vol_xml(file, storage_data):
    """
    create storage vol xml
    """
    xml_template = template.STORAGE_TEMPLATE
    xml_info = {
        'uuid': str(uuid.uuid4()),
        'name': storage_data['name'],
        'allocation': storage_data['allocation'],
        'unit': storage_data['unit'],
        'capacity': storage_data['capacity'],
        'path': storage_data['path'],
        'owner': storage_data['owner'],
        'group': storage_data['group'],
        'mode': storage_data['mode'],
        'label': storage_data['label'],
        }

    xml = Template(xml_template).substitute(xml_info)
    with open(file, 'w') as file_h:
        file_h.write(xml)

# Storage
STORAGE_DATA = {
    'name': 'name',
    'allocation': '0',
    'unit': 'G',
    'capacity': '3000',
    'path': '/var/lib/libvirt/images/',
    'owner': '107',
    'group': '107',
    'mode': '0744',
    'label': 'storage_label',
}
create_storage_vol_xml("storage.xml", STORAGE_DATA)

# Net data
NET_DATA = {
    'network_name': "plop",
    'bridge': "br0",
    'ip': "19.12.12.1",
    'dhcp_start': "30",
    'dhcp_end': "254",
}
create_net_xml("test.xml", NET_DATA)
