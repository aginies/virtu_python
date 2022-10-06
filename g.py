#!/usr/bin/env python3
# aginies@suse.com
#
import sys
import parsexml
import pprint

dir(parsexml)
xml = parsexml.GuestInfo.name_uuid("sle15sp34.xml")

for info in xml:
    print(info)

