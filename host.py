#!/usr/bin/env python3
# aginies@suse.com
#
import sys
import libvirt
import connection

conn = connection.LibVirtConnect.local()
# only SSH for now
# conn = connection.LibVirtConnect.remote('qemu+ssh', '10.0.1.73')
ver = conn.getVersion()
print('Version: '+str(ver))
caps = conn.getCapabilities()
print("Capabilities:\n" + caps)

host = conn.getHostname()
print('Hostname:'+host)
print('Connection is encrypted: '+str(conn.isEncrypted()))
vcpus = conn.getMaxVcpus(None)
print('Maximum support virtual CPUs: '+str(vcpus))

nodeinfo = conn.getInfo()
print('Model: '+str(nodeinfo[0]))
print('Memory size: '+str(nodeinfo[1])+'MB')
print('Number of CPUs: '+str(nodeinfo[2]))
print('MHz of CPUs: '+str(nodeinfo[3]))
print('Number of NUMA nodes: '+str(nodeinfo[4]))
print('Number of CPU sockets: '+str(nodeinfo[5]))
print('Number of CPU cores per socket: '+str(nodeinfo[6]))
print('Number of CPU threads per core: '+str(nodeinfo[7]))

xml = '<cpu mode="custom" match="exact">' + \
        '<model fallback="forbid">kvm64</model>' + \
      '</cpu>'
retc = conn.compareCPU(xml)
if retc == libvirt.VIR_CPU_COMPARE_ERROR:
    print("CPUs are not the same or ther was error.")
elif retc == libvirt.VIR_CPU_COMPARE_INCOMPATIBLE:
    print("CPUs are incompatible.")
elif retc == libvirt.VIR_CPU_COMPARE_IDENTICAL:
    print("CPUs are identical.")
elif retc == libvirt.VIR_CPU_COMPARE_SUPERSET:
    print("The host CPU is better than the one specified.")
else:
    print("An Unknown return code was emitted.")

conn.close()
exit(0)
