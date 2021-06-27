import logging
import operator
from .Constants import *
from .Datum import Datum

#A DataContainer allows Data to be analyzed.
#This class is intended to be derived from and added to.
#Each DataContainer is comprised of multiple Data (see Datum.py for more).
#This class has a lot of helpful methods for manipulating Data.
#For details on each of these methods, please see the function definition below.
#NOTE: DataContainers are, themselves Data. Thus, you can nest your child classes however you would like.
class DataContainer(Datum):
    def __init__(self, name=INVALID_NAME):
        super().__init__(name)
        self.data = []

    #RETURNS: an empty, invalid Datum.
    def InvalidDatum(self):
        ret = Datum()
        ret.Invalidate()
        return ret

    #If your Data use a time-based unique id, then sorting by id will sort the Data in *this into chronological order.
    def SortData(self, by='uniqueID'):
        self.data.sort(key=operator.attrgetter(by))

    #Adds a Datum to *this
    def AddDatum(self, datum):
        self.data.append(datum)

    #RETURNS: a Datum with datumAttribute equal to match, an invalid Datum if none found.
    def GetDatumBy(self, datumAttribute, match, bestMatch=True):
        for d in self.data:
            try: #within for loop cause maybe the issue is only with 1 Datum and the rest are fine.
                if (getattr(d, datumAttribute) == match):
                    if (bestMatch and not d.bestMatch):
                        continue
                    return d
            except Exception as e:
                logging.error(f"{self.name} - {e.message}")
                continue
        return self.InvalidDatum()

    #RETURNS: a Datum of the given name, an invalid Datum if none found.
    def GetDatum(self, name, bestMatch=True):
        return self.GetDatumBy('name', name, bestMatch)

    #Removes all Data in toRem from *this.
    #RETURNS: the Data removed
    def RemoveData(self, toRem):
        self.data = [d for d in self.data if d not in toRem]
        return toRem

    #Removes all Data in *this except toKeep.
    #RETURNS: the Data removed
    def KeepOnlyData(self, toKeep):
        toRem = [d for d in self.data if d not in toKeep]
        return self.RemoveData(toRem)

    #Removes all Data with the name "INVALID NAME"
    #RETURNS: the removed Data
    def RemoveAllUnlabeledData(self):
        toRem = []
        for d in self.data:
            if (d.name =="INVALID NAME"):
                toRem.append(d)
        return self.RemoveData(toRem)

    #Removes all invalid Data
    #RETURNS: the removed Data
    def RemoveAllInvalidData(self):
        toRem = []
        for d in self.data:
            if (not d.IsValid()):
                toRem.append(d)
        return self.RemoveData(toRem)

    #Removes all Data that are not the bestMatch for their names
    #RETURNS: the removed Data
    def KeepOnlyBestMatchingData(self):
        toRem = []
        for d in self.data:
            if (not d.bestMatch):
                toRem.append(d)
        return self.RemoveData(toRem)

    #Removes all Data that have an attribute value relative to target.
    #The given relation can be things like operator.le (i.e. <=)
    #   See https://docs.python.org/3/library/operator.html for more info.
    #If ignoreNames is specified, any Data of those names will be ignored.
    #RETURNS: the Data removed
    def RemoveDataRelativeToTarget(self, datumAttribute, relation, target, ignoreNames = []):
        try:
            toRem = []
            for d in self.data:
                if (ignoreNames and d.name in ignoreNames):
                    continue
                if (relation(getattr(d, datumAttribute), target)):
                    toRem.append(d)
            return self.RemoveData(toRem)
        except Exception as e:
            logging.error(f"{self.name} - {e.message}")
            return []

    #Adds all Data from otherDataContainer to *this.
    #If there are duplicate Data they are removed here.
    #RETURNS: the Data removed
    def ImportDataFrom(self, otherDataContainer):
        self.data.extend(otherDataContainer.data);
        toRem = [] #list of Data
        alreadyProcessed = [] #list of unique ids.
        for d1 in self.data:
            skip = False
            for dp in alreadyProcessed:
                if (d1.uniqueID == dp):
                    skip = True
                    break
            if (skip):
                continue
            for d2 in self.data:
                if (d1 is not d2 and d1.uniqueID == d2.uniqueID):
                    logging.info(f"Removing duplicate Datum {d2} with unique id {d2.uniqueID}")
                    toRem.append(d2)
                    alreadyProcessed.append(d1.uniqueID)
        return self.RemoveData(toRem)

    #RETURNS: the sum of datumAttribute for all data
    #If bestMatch is True, only Data with bestMatch of True will be summed.
    #If ignoreNames is specified, any Data of those names will be ignored.
    def GetDatumTotal(self, datumAttribute, bestMatch = False, ignoreNames = []):
        try:
            ret = 0
            for d in self.data:
                if (bestMatch and not d.bestMatch):
                    continue
                if (ignoreNames and d.name in ignoreNames):
                    continue
                ret += getattr(d, datumAttribute)
            return ret
        except Exception as e:
            logging.error(f"{self.name} - {e.message}")
            return 0

    #RETURNS: the Data with an absolute maximum (or minimum) of the given attribute.
    #For useful relations, see https://docs.python.org/3/library/operator.html.
    def GetDatumOfExtremeRelation(self, datumAttribute, relation):
        try:
            ret = None
            toBeat = 0 #FIXME: Possible bugs here if looking for a maximum of negative values, etc.
            for d in self.data:
                if (relation(getattr(d, datumAttribute), toBeat)):
                    toBeat = getattr(d, datumAttribute)
                    ret = d
            return d
        except Exception as e:
            logging.error(f"{self.name} - {e.message}")
            return self.InvalidDatum()

    #RETURNS: the smallest gap between unique ids in data
    def GetSmallestGapOfUniqueIds(self, shouldSort=True):
        if (shouldSort):
            self.SortData()

        gap = 1000000 #too big #FIXME: Arbitrary value.
        for i in range(len(self.data)):
            if (i == len(self.data)-1):
                break #we look at i and i+1, so break before last i
            dUI = abs(self.data[i].uniqueID - self.data[i+1].uniqueID)
            if (dUI < gap):
                gap = dUI
        return gap

    #RETURNS: the Data past the starting id, which has an attribute that is of the given relation to both Data next to it.
    #RETURNS: InvalidDatum() if the requested value does not exist
    #startingId will be adjusted to the first valid id that is >= to startingId
    def GetNextLocalExtremity(self, startingId, datumAttribute, relation, shouldSort=True):
        if (shouldSort):
            self.SortData()

        #check corner cases first
        if (startingId >= self.data[-1].uniqueID): #startingId is too high.
            return self.InvalidDatum()

        try:
            for i in range(len(self.data)):
                if (self.data[i].uniqueID < startingId):
                    continue
                if (not self.data[i].IsValid()):
                    continue
                if (i == 0):
                    if (relation(getattr(self.data[i], datumAttribute), getattr(self.data[i+1], datumAttribute))):
                        return self.data[i]
                    else:
                        continue
                if (i == len(self.data)-1):
                    if (relation(getattr(self.data[i], datumAttribute), getattr(self.data[i-1], datumAttribute))):
                        return self.data[i]
                    else:
                        return self.InvalidDatum()
                if (relation(getattr(self.data[i], datumAttribute), getattr(self.data[i+1], datumAttribute)) and relation(getattr(self.data[i], datumAttribute), getattr(self.data[i-1], datumAttribute))):
                    return self.data[i]
        except Exception as e:
            logging.error(f"{self.name} - {e.message}")
            return self.InvalidDatum()


    #RETURNS: a list of all Data in *this that are local extremities of the given relation.
    def GetAllLocalExtremities(self, datumAttribute, relation, shouldSort=True):
        if (shouldSort):
            self.SortData()

        startingId = self.data[0].uniqueID
        ret = DataContainer()
        while (True):
            tempData = self.GetNextLocalExtremity(startingId, datumAttribute, relation, False)
            startingId = tempData.uniqueID
            if (tempData.IsValid()):
                ret.AddDatum(tempData)
            else:
                return ret

    #Uses a standard to translate raw data into a usable ratio.
    #Basically, this gives someDatum.datumAttribute / standard.datumAttribute * self.stdAttribute / self.selfAttribute, for each Data in *this. This value is stored in each Data under datumAttributeToSet.
    #REQUIREMENTS:
    #   1. all Data have been labeled
    #   2. all Data have a valid, numeric datumAttribute
    #   3. the stdName provided matches a Datum within *this
    #   4. stdAttribute and selfAttribute are defined and are valid numbers in *this
    #EXAMPLE:
    #   *this, a DataContainer, contains data from a gas chromatograph, which includes a known standard, with name given by stdName. Each Datum in *this, an individual fatty acid methyl ester, would be an instance of a FAME class, which would be a child of Datum containing a peak area. Thus, the datumAttribute would be something like "peakArea", the member variable of our FAME class. By comparing peak areas, the known mass of the standard can be used to calculate the known mass of each other Datum in *this. Thus, stdAttribute would be something like "mgStd", meaning self.mgStd would return a valid number for *this. We then calculate the attributeFraction by comparing the stdAttribute with the corresponding selfAttribute, in this case the mass of our sample, something like "mgDryWeight". The resulting value is stored in the FAME instance for each Datum, perhaps as a member by name of "percentFA".
    #   This gives us a way to translate raw data into real-world, relevant information, which can be compared between samples.
    #   To recap, we use:
    #       stdName = the name of our standard (e.g. "C:17")
    #       datumAttribute = peak area (e.g. "peakArea")
    #       datumAttributeToSet = mg/mg fatty acid ratio (e.g. "percentFA")
    #       stdAttribute = mg standard in sample (e.g. "mgStd")
    #       selfAttribute = mg sample used (e.g. "mgDryWeight")
    #   and we get:
    #       A mg / mg ratio of each fatty acid species to dry weight of sample.
    #   This is given by:
    #       {datum.peak area} / {std.peak area} * {std.mass} / {sample.mass}
    #NOTE: The reason stdAttribute is a member of a DataContainer child and not a Datum child is that calculating the stdAttribute for all Data is almost always meaningless until those values are normalized to how much of each Datum was used in the experiment. Thus, instead of eating up more RAM and CPU time sorting through extra values that won't be used, stdAttribute is only stored once, within *this.
    def CalculateAttributePercent(self, stdName, datumAttribute, datumAttributeToSet, stdAttribute, selfAttribute):
        std = self.GetDatum(stdName)
        if (not std.IsValid()):
            logging.info(f"{self.name} - Percent of {selfAttribute} not calculated: no valid {stdName} found.")
            return
        try:
            fractionDenominator = getattr(self, selfAttribute)
            if (fractionDenominator == 0):
                logging.info(f"Invalid {selfAttribute} in {self.name}")
                return
            
            fractionNumerator = getattr(self, stdAttribute)
            if (fractionNumerator == 0):
                logging.info(f"Invalid {stdAttribute} in {self.name}")
                return

            stdComparator = getattr(std, datumAttribute)
            if (stdComparator == 0):
                logging.info(f"Invalid {datumAttribute} of standard {std.name} in {self.name}")
                return

            attributeFraction = fractionNumerator / fractionDenominator
            for d in self.data:
                if (not d.IsValid()):
                    continue
                if (d.name == "INVALID NAME" or not d.bestMatch):
                    continue
                if (d.name == std.name):
                    continue
                setattr(d, datumAttributeToSet, getattr(d, datumAttribute) /stdComparator * attributeFraction)
        except Exception as e:
            logging.error(f"{self.name} - Error calculating percent {selfAttribute}: {e.message}")
            return

    #Changes name of each Data to be that of the labeledData with the closest unique id.
    def ApplyNamesWithClosestMatchFrom(self, labeledData, shouldSort=True):
        if (shouldSort):
            self.SortData()

        acceptableGapLow = 1 #BIG but not too big.. #FIXME: calculate this?
        for i in range(len(labeledData)):
            if (i != len(labeledData)-1):
                acceptableGapHigh = abs(labeledData[i+1].uniqueId - labeledData[i].uniqueId) / 2
                # logging.info("Next acceptable gap is", acceptableGapHigh, "making range", labeledData[i].uniqueId - acceptableGapLow,"to", labeledData[i].uniqueId + acceptableGapHigh)
            else:
                acceptableGapHigh = 0
            for d in self.data:
                if (d.uniqueId > labeledData[i].uniqueId - acceptableGapLow and d.uniqueId <= labeledData[i].uniqueId + acceptableGapHigh):
                    d.name = labeledData[i].name
                    d.nameMatchDiscrepancy = d.uniqueId - labeledData[i].uniqueId
            acceptableGapLow = acceptableGapHigh

    #Once Data have names, this method may be called to find which one "best" matches its label.
    #This is useful iff 2+ Data have the same label, but not the same id.
    #This method relies on IsBetterMatchThan(...) to determine what a "best" match is.
    def FindBestMatchingData(self, datumAttribute):
        currentName = ""
        matchToBeat = Datum()
        matchToBeat.Invalidate()
        for d in self.data:
            #find local min for nameMatchDiscrepancy
            if (d.name != currentName):
                currentName = d.name
                matchToBeat = d
                d.bestMatch = True
            elif (not matchToBeat.IsValid() or d.IsBetterMatchThan(matchToBeat, datumAttribute)):
                matchToBeat.bestMatch = False
                matchToBeat = d;
                d.bestMatch = True
