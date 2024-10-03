import asyncio
from dbus_next.aio import MessageBus
from dbus_next import (Variant, BusType)

# Function to get SSIDs of available wireless networks
async def get_available_networks():
    # Connect to the session/system bus
    bus = await MessageBus(bus_type=BusType.SYSTEM).connect()

    # Get a proxy object for the NetworkManager
    network_manager = await bus.introspect('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager')
    proxy_object = bus.get_proxy_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager', network_manager)

    # Get the "org.freedesktop.NetworkManager" interface
    nm_interface = proxy_object.get_interface('org.freedesktop.NetworkManager')

    # Get the list of available devices
    devices = await nm_interface.call_get_devices()

    ssids = []
    
    # Iterate over each device
    for device_path in devices:
        device = await bus.introspect('org.freedesktop.NetworkManager', device_path)
        device_proxy = bus.get_proxy_object('org.freedesktop.NetworkManager', device_path, device)
        device_interface = device_proxy.get_interface('org.freedesktop.NetworkManager.Device')

        # Check if the device type is WiFi (type 2)
        device_type = await device_interface.get_device_type()
        if device_type == 2:  # 2 is the type for WiFi devices
            # Get the WiFi interface for this device
            wifi_interface = device_proxy.get_interface('org.freedesktop.NetworkManager.Device.Wireless')

            # Get the list of available access points
            access_points = await wifi_interface.call_get_access_points()

            for ap_path in access_points:
                ap = await bus.introspect('org.freedesktop.NetworkManager', ap_path)
                ap_proxy = bus.get_proxy_object('org.freedesktop.NetworkManager', ap_path, ap)
                ap_interface = ap_proxy.get_interface('org.freedesktop.NetworkManager.AccessPoint')

                # Get the SSID from the access point
                ssid_variant = await ap_interface.get_ssid()
                ssid = ''.join([chr(byte) for byte in ssid_variant])
                ssids.append(ssid)

    return ssids

# Run the async function
if __name__ == '__main__':
    networks = asyncio.run(get_available_networks())
    for network in networks:
        print(f"SSID: {network}")
