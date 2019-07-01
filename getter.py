from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

passw = getpass()

xrdevice = dict(
username = 'aayy',
password = passw,
hostname = '10.11.165.172',
device_type = 'iosxr',
optional_args = {}
)

iosdevice = dict(
username = 'aayy',
password = passw,
hostname = '10.11.165.173',
device_type = 'ios',
optional_args = {}
)
devicelist = [xrdevice,iosdevice]
for item in devicelist:
        devtype = item.pop('device_type')
        driver = get_network_driver(devtype)
        instance = driver(**item)
        print ('connection to {} is open'.format(item.get('hostname')))
        instance.open()
        output = instance.get_facts()
        pprint(output)
        instance.close()
