async def recurcive_update(self, obj, config):
    for k, v in config.items():
        if isinstance(v, dict):
            v = await self.recurcive_update(getattr(obj, k), v)
        setattr(obj, k, v) 
    return obj

async def set_configuration(self, config={}):
    """
    Sample Config:
    {
        "token": enc_token,
        "Name": "last-test",
        "UseCount": 2,
        "Encoding": "H264",
        "Resolution":{
            "Width": 1920,
            "Height": 1080,
        },
        "Quality": 4.5,
        "RateControl":{
            "FrameRateLimit":12,
            "EncodingInterval":1,
            "BitrateLimit":1
        },
        "MPEG4": None,
        'H264': {
            'GovLength': 50,
            'H264Profile': 'Main'
        },
        'Multicast': {
            'Address': {
                'Type': 'IPv4',
                'IPv4Address': '0.0.0.0',
                'IPv6Address': None
            },
            'Port': 8860,
            'TTL': 128,
            'AutoStart': False,
        },
        "SessionTimeout": ''
    }
    """
    self.media_service.create_type('SetVideoEncoderConfiguration')
    media_service_profile = await self.media_service.GetProfiles()
    enc_token =  media_service_profile[0].VideoEncoderConfiguration.token
    new_config = await self.media_service.GetVideoEncoderConfiguration({'ConfigurationToken': enc_token,})
    new_config.token = enc_token
    new_config = await self.recurcive_update(new_config, config)
    config = await self.media_service.SetVideoEncoderConfiguration({'Configuration':new_config, 'ForcePersistence':True})
    new_config = await self.media_service.GetVideoEncoderConfiguration({'ConfigurationToken': enc_token,})
    await self.media_service.close()
    return new_config
