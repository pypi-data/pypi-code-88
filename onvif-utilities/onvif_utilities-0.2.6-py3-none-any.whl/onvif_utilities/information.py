import asyncio

from onvif_utilities.onvif import ONVIFCamera
from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
from urllib.parse import urlparse

class CameraDetail():
    def __init__(self,ip, port, username, password):
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port
        self.camera = ONVIFCamera(self.ip, self.port ,user=self.username, passwd=self.password, encrypt=False)
        self.media_service = self.camera.create_media_service()
        self.camera_device = self.camera.create_devicemgmt_service()
        
    async def get_mac_addr(self):
        network = await self.camera_device.GetNetworkInterfaces()
        mac_addr = network[0].Info.HwAddress
        return mac_addr

    async def get_camera_name(self):
        name = await self.camera_device.GetHostname()
        return name["Name"]

    async def get_camera_model(self):
        info = await  self.camera_device.GetDeviceInformation()
        return info.Model
    
    async def get_serial_number(self):
        info = await self.camera_device.GetDeviceInformation()
        return info.SerialNumber

    async def get_hardware_id(self):
        info = await self.camera_device.GetDeviceInformation()
        return info.HardwareId

    async def get_resolutions_available(self):
        self.media_service_profile = await self.media_service.GetProfiles()
        request = self.media_service.create_type('GetVideoEncoderConfigurationOptions')
        request.ProfileToken = self.media_service_profile[0].token
        config = await self.media_service.GetVideoEncoderConfigurationOptions(request)
        return [res.Height for res in config.H264.ResolutionsAvailable]
    
    async def get_rtsp(self):
        self.media_service_profile = await self.media_service.GetProfiles()
        req = self.media_service.create_type("GetStreamUri")
        req.ProfileToken = self.media_service_profile[0].token
        req.StreamSetup = {
            "Stream": "RTP-Unicast",
            "Transport": {"Protocol": "RTSP"},
        }
        # TODO should fix channels issu
        uri = await self.media_service.GetStreamUri(req)
        rtsp = uri.Uri
        if not "username" in rtsp:
            rtsp = rtsp.replace("rtsp://", f"rtsp://{self.username}:{self.password}@", 1).replace("?transportmode=unicast&profile=Profile_1", "")
        return rtsp

    async def camera_detail(self):
        camera_dict = {
            "ip": self.ip,
            "rtsp": await self.get_rtsp(),
            "name": await self.get_camera_name(),
            "model": await self.get_camera_model(),
            "mac_addr": await self.get_mac_addr(),
            "serial_number": await self.get_serial_number(),
            "hardware_id": await self.get_hardware_id(),
            "resolution": await self.get_resolutions_available()
        }
        return camera_dict

    def camera_list():
        wsd = WSDiscovery()
        wsd.start()
        founded_list = []
        found = wsd.searchServices()
        for service in found:
            url = urlparse(service.getXAddrs()[0])
            if "onvif" not in url.path:
               print(f"not an onvif service path:{url.path}")
            else:
                found = url
                founded_list.append([found.hostname, found.port or 80, found.netloc+found.path])
        wsd.stop()
        return founded_list

if __name__ == "__main__":
    cameras = CameraDetail.camera_list()
    print(cameras)
    for camera in cameras:
        print(camera[0])
        a = CameraDetail(ip=camera[0],
                port="80",
                username="admin", password="admin")
        async def run():
            await a.camera_detail()
            await a.camera.close()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())