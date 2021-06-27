import logging
from .Constants import *
from .SelfRegistering import SelfRegistering
from .Serializable import Serializable

#A Datum is a base class for any datum type that you would like to find trends between.
#This class is intended to be derived from and added to.
#The members of this class are helpful labels along with the ability to invalidate a datum.
class Datum(SelfRegistering, Serializable):

    #Don't worry about this.
    #If you really want to know, look at SelfRegistering.
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name=INVALID_NAME, number=0):
        # logging.debug("init Datum")

        self.number = number
        self.name = name
        self.colorId = "" #a unique color to help identify trends

        #A unique id states that any 2 Data with the same id are, in fact, the same, regardless of what else might vary.
        #This should be a time-based value, etc.
        #For example, if you measure some chemical species that elutes off a column at a given rate, it won't matter how much eluate is present between different runs of the experiment, the time taken to observe the substance uniquely identifies that species.
        #Unique, time-based ids are especially valuable when there are multiple candidates vying for the same name (per names based on known time-based values). This underlies the bestMatch system, below.
        self.uniqueID = 0

        #Storing validity as a member makes it easy to generate bad return values (i.e. instead of checking for None) as well as manipulate data (e.g. each analysis step invalidates some data and all invalid data are discarded at the end of analysis).
        self.valid = True 

        #Children of *this might have similar characteristics to one another (e.g. if there is contamination in the sample)
        #Because of that, children are permitted to know about each other only in terms of whether or not they are the best of their classification
        #Using this is optional, so it defaults to True.
        #See IsBetterMatchThan, below, for more info.
        self.bestMatch = True

        #The nameMatchDiscrepancy is the difference between the known and experimental values.
        #This is useful when trying to determine bestMatch through comparison with other children.
        #We can then account for noisy data by how off a child is to what we expect.
        self.nameMatchDiscrepancy = 0

    #RETURNS: valid
    #Override this if you have your own validity checks.
    def IsValid(self):
        return self.valid == True

    #Sets valid to true
    #Override this if you have members you need to handle with care.
    def MakeValid(self):
        self.valid = True

    #Sets valid to false.
    def Invalidate(self):
        self.valid = False

    #RETURNS: bestMatch
    def IsBestMatch(self):
        return self.bestMatch == True

    def SetBestMatch(self, newValue):
        self.bestMatch = newValue

    #Use a formula to pick out which children are the best fits for their names.
    #RETURNS: a boolean favoring self (true) or compare (false)
    #The caller can use this information to set self.bestMatch.
    #Basically, this says that stronger signals and more accurate signals are both equally valid metrics in determining the correct label for a children. These metrics obviously vary with each data set (some data are more precise and have large signals, causing this function to weight strength more heavily than accuracy, and vice versa). However, this rough calculation should serve for most data. Plus, hey, it's Python. Hack this!
    def IsBetterMatchThan(self, compare, attribute):
        try:
            selfValue = getattr(self, attribute)
            compareValue = getattr(compare, attribute)
            if(self.nameMatchDiscrepancy != 0):
                selfValue /= abs(self.nameMatchDiscrepancy)
            if(compare.nameMatchDiscrepancy != 0):
                compareValue /= abs(compare.nameMatchDiscrepancy)
        except Exception as e:
            logging.error(f"Error comparing {self.name} and {compare.name}: {e.message}")
            return False;

        return selfValue > compareValue
