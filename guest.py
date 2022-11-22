#!/usr/bin/env python3
# aginies@suse.com
#
import sys
import libvirt
import connection

conn = connection.LibVirtConnect.local()

domName = 'sle15sp4-2'
dom= None
try:
    dom = conn.lookupByName(domName)
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

id = dom.ID()
if id == -1:
    print('The domain '+domName + ' is not running so has no ID.')
    exit(1)
else:
    print('The ID of the domain is ' + str(id))

if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

vcpu= 4
state, maxmem, mem, cpus, cput = dom.info()
print ('Setting '+str(vcpu) +' Vcpu(s) ' +'to domain '+domName, file=sys.stderr)
dom.setVcpus(vcpu)
print('The number of cpus is ' + str(cpus))
print('OSType: '+dom.OSType(), file=sys.stderr)
print('The state is ' + str(state))
print('The max memory is ' + str(maxmem))
print('The memory is ' + str(mem))
print('The number of cpus is ' + str(cpus))
print('The cpu time is ' + str(cput))

conn.close()
exit(0)
