#!/usr/bin/env python3
# aginies@suse.com
#
import sys
import libvirt

class LibVirtConnect:
        """Connection method to libvirt"""
        def __init__(self,connector,dst):
            self.connector = connector
            self.dst = dst
            print(connector +" "+ dst)
            conn = None

        def local():
            conn = None
            try:
                conn = libvirt.open("qemu:///system")
                ver = conn.getVersion()
                #print('Connected \nVersion: '+str(ver))
                return conn
            except libvirt.libvirtError as e:
                print(repr(e), file=sys.stderr)
                exit(1)

        def remote(connector, dst):
            dst_conn = None
            print(connector+'://'+dst+'/system')
            try:
                dst_conn = libvirt.open(connector+'://'+dst+'/system')
                ver = dst_conn.getVersion()
                #print('Connected \nVersion: '+str(ver))
                return dst_conn
            except libvirt.libvirtError as e:
                print(repr(e), file=sys.stderr)
                exit(1)
