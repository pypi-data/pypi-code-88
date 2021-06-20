##
#  File:           PharosTargetActivityProvider.py
#  Date:           17-Jun-2021 jdw
#
#  Updated:
#
##
"""
Accessors for Pharos target activity data.

"""

import datetime
import logging
import os.path
import time

from rcsb.utils.io.FileUtil import FileUtil
from rcsb.utils.io.MarshalUtil import MarshalUtil
from rcsb.utils.io.StashableBase import StashableBase


logger = logging.getLogger(__name__)


class PharosTargetActivityProvider(StashableBase):
    """Accessors for Pharos target activity data."""

    def __init__(self, cachePath, useCache):
        #
        self.__cachePath = cachePath
        self.__dirName = "Pharos-target-activity"
        super(PharosTargetActivityProvider, self).__init__(self.__cachePath, [self.__dirName])
        self.__dirPath = os.path.join(self.__cachePath, self.__dirName)
        self.__mU = MarshalUtil(workPath=self.__cachePath)
        #
        baseVersion = "6"
        self.__version = baseVersion
        self.__aD = self.__reload(self.__dirPath, useCache)

    def testCache(self, minCount=0):
        if minCount == 0:
            return True
        if self.__aD and (len(self.__aD) > minCount):
            logger.info("Activity data for (%d) targets", len(self.__aD))
            return True
        return False

    def getAssignmentVersion(self):
        return self.__version

    def getTargetActivityDataPath(self):
        return os.path.join(self.__dirPath, "pharos-target-activity-data.json")

    def __reload(self, dirPath, useCache):
        startTime = time.time()
        aD = {}
        fU = FileUtil()
        fU.mkdir(dirPath)
        targetActivityFilePath = self.getTargetActivityDataPath()
        #
        if useCache and fU.exists(targetActivityFilePath):
            logger.info("useCache %r using %r", useCache, targetActivityFilePath)
            qD = self.__mU.doImport(targetActivityFilePath, fmt="json")
            aD = qD["activity"] if "activity" in qD else {}
        #
        logger.info("Completed reload of (%d) at %s (%.4f seconds)", len(aD), time.strftime("%Y %m %d %H:%M:%S", time.localtime()), time.time() - startTime)
        #
        return aD

    def getTargetActivity(self, pharosTargetId):
        try:
            return self.__aD[pharosTargetId] if pharosTargetId in self.__aD else []
        except Exception:
            return []

    def hasTargetActivity(self, pharosTargetId):
        try:
            return pharosTargetId in self.__aD
        except Exception:
            return False

    def fetchTargetActivityData(self):
        targetD = {}
        cofactorFilePath = os.path.join(self.__dirPath, "drug_activity.tdd")
        cfDL = self.__mU.doImport(cofactorFilePath, fmt="tdd", rowFormat="dict")
        targetD = self.__extactCofactorData(cfDL)
        #
        cofactorFilePath = os.path.join(self.__dirPath, "cmpd_activity.tdd")
        cfDL = self.__mU.doImport(cofactorFilePath, fmt="tdd", rowFormat="dict")
        targetD.update(self.__extactCofactorData(cfDL))
        #
        tS = datetime.datetime.now().isoformat()
        vS = datetime.datetime.now().strftime("%Y-%m-%d")
        ok = self.__mU.doExport(self.getTargetActivityDataPath(), {"version": vS, "created": tS, "activity": targetD}, fmt="json", indent=3)
        return ok

    def __extactCofactorData(self, cfDL):
        """Extract ids, activity and moa data for drugs and cofactors from the Pharos schema dump files.

        Args:
            cfDL (list): list of dictionaries of containing pharos exported db data.

        Returns:
            dict: dictionary of extracted cofactor data
        """
        try:
            qD = {}
            targetD = {}
            for cfD in cfDL:
                tId = cfD["target_id"]
                qD = {}
                qD["smiles"] = cfD["smiles"] if "smiles" in cfD and cfD["smiles"] not in ["N", "NULL"] else None
                qD["chemblId"] = cfD["cmpd_chemblid"] if "cmpd_chemblid" in cfD else None
                qD["chemblId"] = cfD["cmpd_id_in_src"] if "catype" in cfD and cfD["catype"].upper() == "CHEMBL" else qD["chemblId"]
                qD["chemblId"] = qD["chemblId"] if qD["chemblId"] not in ["N", "NULL"] else None
                qD["pubChemId"] = cfD["cmpd_pubchem_cid"] if "cmpd_pubchem_cid" in cfD and cfD["cmpd_pubchem_cid"] not in ["NULL"] else None
                #
                qD["activity"] = cfD["act_value"] if "act_value" in cfD and cfD["act_value"] != "NULL" else None
                qD["activityType"] = cfD["act_type"] if "act_type" in cfD and cfD["act_type"] != "NULL" else None
                if qD["activity"] is not None:
                    qD["activity"] = float(qD["activity"])
                    qD["activityUnits"] = "nM"
                #
                qD["moa"] = cfD["action"] if "action" in cfD and cfD["moa"] == "1" else None
                tS = cfD["drug"] if "drug" in cfD else None
                tS = cfD["cmpd_name_in_src"] if "cmpd_name_in_src" in cfD and cfD["cmpd_name_in_src"] != "NULL" else tS
                #
                if tS and tS.startswith("US"):
                    tS = tS.split(",")[0].strip()
                    qD["patent"] = tS
                else:
                    qD["name"] = tS
                #
                pmId = None
                tS = cfD["reference"] if "reference" in cfD else None
                if tS and "pubmed" in tS:
                    pmId = tS.split("/")[-1]
                tS = cfD["pubmed_ids"].split(",")[0] if "pubmed_ids" in cfD and cfD["pubmed_ids"] else pmId
                qD["pubmedId"] = tS if tS and tS not in ["NULL"] else None
                #
                if qD["activity"] and qD["chemblId"]:
                    targetD.setdefault(tId, []).append({ky: qD[ky] for ky in qD if qD[ky] is not None})

            #
        except Exception as e:
            logger.exception("Failing with %r %s", qD, str(e))
        return targetD
