from .tofreedb import ToFreedb
from .fromfreedb import FreedbSource
from .freedbfilter import FreedbDocNotExistFilter
from .freedbdelete import FreedbDeleteDoc
from .freedbdoc import FreedbDocGet


to_freedb = ToFreedb
freedb = FreedbSource
freedb_doc_not_exist = FreedbDocNotExistFilter
freedb_delete = FreedbDeleteDoc
freedb_get_doc = FreedbDocGet
