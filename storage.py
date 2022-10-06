#!/usr/bin/env python3
import sys
import libvirt
import connection
import pprint

stgvol_xml = """
<volume>
  <name>sparse.img</name>
  <allocation>0</allocation>
  <capacity unit="G">2</capacity>
  <target>
    <path>/var/lib/virt/images/sparse.img</path>
    <permissions>
      <owner>107</owner>
      <group>107</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>"""

poolname = 'default'

conn = connection.LibVirtConnect.local()

pool = conn.storagePoolLookupByName(poolname)
if pool == None:
    print('Failed to locate any StoragePool objects.', file=sys.stderr)
    exit(1)
print('Pool \n' +pool.XMLDesc())

stgvol = pool.createXML(stgvol_xml, 0)
if stgvol == None:
    print('Failed to create a  StorageVol objects.', file=sys.stderr)
    exit(1)
print('Volume Storage: \n' +stgvol.XMLDesc())
#:print('  Storage vol: '+vars(stgvol.name))

sp = conn.storagePoolLookupByName(poolname)
if sp == None:
    print('Failed to find storage pool '+poolname, file=sys.stderr)
    exit(1)

stgvols = sp.listVolumes()
for stgvollist in stgvols :
    print('  Storage vol: '+stgvollist)


# remove the storage volume
# physically remove the storage volume from the underlying disk media
stgvol.wipe(0)
# logically remove the storage volume from the storage pool
stgvol.delete(0)

stgvols = sp.listVolumes()
print('Storage pool: '+poolname, file=sys.stderr)
for stgvollist in stgvols :
    print('  Storage vol: '+stgvollist)
    try:
        print('  Storage vol: '+stgvollist.__dict__.keys())
    except AttributeError:
        print("There is no such attribute")


conn.close()
exit(0)
