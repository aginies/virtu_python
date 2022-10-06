#!/usr/bin/env python3
# aginies@suse.com
#
# parse VM xml file
#
import sys
import xml.etree.ElementTree as ET

#Element.iter(‘tag’) -Iterates over all the child elements(Sub-tree elements)
#Element.findall(‘tag’) -Finds only elements with a tag which are direct children of the current element.
#Element.find(‘tag’) -Finds the first Child with the particular tag.
#Element.get(‘tag’) -Accesses the elements attributes.
#Element.text -Gives the text of the element.
#Element.attrib-returns all the attributes present.
#Element.tag-returns the element name.
# Modify
#Element.set(‘attrname’, ‘value’) – Modifying element attributes.
#Element.SubElement(parent, new_childtag) -creates a new child tag under the parent.
#Element.write(‘filename.xml’)-creates the tree of xml into another file.
#Element.pop() -delete a particular attribute.
#Element.remove() -to delete a complete tag.

class GuestInfo:
    def __init__(self):
        print('Here')

    def parse_file(xml):
        tree = ET.parse(xml)
        root = tree.getroot()
        return root

    def name_uuid(xml):
        root = GuestInfo.parse_file(xml)
        name = root.find('name').text
        uuid = root.find('uuid').text
        print('Name: ' +name)
        print('uuid: ' +uuid)
        return(name, uuid)

