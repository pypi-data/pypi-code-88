import pytz,pandas as pd
from dorianUtils.templateDashD import TemplateDashTagsUnit

class ScreenBuildingDash(TemplateDashTagsUnit):
    # ==========================================================================
    #                       INIT FUNCTIONS
    # ==========================================================================

    def __init__(self,cfg,baseNameUrl='/monitoringBuilding/',title='Monitoring buildings',port=45103):
        super().__init__(cfg,baseNameUrl=baseNameUrl,title=title,
                            port=port,cacheRedis=False)
