# -*- coding: utf-8 -*-
#
# Copyright (c) 2019-2021 Kevin De Bruycker and Tim Krappitz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from __future__ import absolute_import
from collections import Counter
import itertools
import pymacroms
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from operator import itemgetter, attrgetter
import re
import sys
import progressbar

# todo: remove dependency on self.isobaricSpecies as the same info is now available under self.macromolecules directly as 'isobaricCompositions'

class Polymer:

    @staticmethod
    def getRUCombinations(monomersAmount: int,
                          minRepeatingUnits: list = None, minSumRepeatingUnits: int = None,
                          maxRepeatingUnits: list = None, maxSumRepeatingUnits: int = None):
        #process inputs
        if minRepeatingUnits is None and minSumRepeatingUnits is None:
            raise ValueError('Either minRepeatingUnits or minSumRepeatingUnits must not be None')
        elif minRepeatingUnits is None:
            minRepeatingUnits = minSumRepeatingUnits
        elif minSumRepeatingUnits is None:
            minSumRepeatingUnits = sum(minRepeatingUnits) if type(minRepeatingUnits) == list else minRepeatingUnits
        if maxRepeatingUnits is None and maxSumRepeatingUnits is None:
            raise ValueError('Either maxRepeatingUnits or maxSumRepeatingUnits must not be None')
        elif maxRepeatingUnits is None:
            maxRepeatingUnits = maxSumRepeatingUnits
        elif maxSumRepeatingUnits is None:
            maxSumRepeatingUnits = sum(maxRepeatingUnits) if type(maxRepeatingUnits) == list else maxRepeatingUnits

        assert maxSumRepeatingUnits >= minSumRepeatingUnits, "With the current parameters, minSumRepeatingUnits is higher than maxSumRepeatingUnits, this can't be correct..."
        # if lists are passed as either min or maxRepeatingUnits, their length must match the amount of monomers
        if type(minRepeatingUnits) == list and type(maxRepeatingUnits) == list:
            assert sum(maxRepeatingUnits) >= sum(minRepeatingUnits), "The sum of minRepeatingUnits is higher than the sum of maxRepeatingUnits, this can't be correct..."
            assert len(minRepeatingUnits) == monomersAmount, "The length of minRepeatingUnits does not match the amount of monomers!"
            assert len(maxRepeatingUnits) == monomersAmount, "The length of maxRepeatingUnits does not match the amount of monomers!"
        else:
            if type(minRepeatingUnits) == list:
                assert maxRepeatingUnits >= sum(minRepeatingUnits), "The sum of minRepeatingUnits is higher than maxRepeatingUnits, this can't be correct..."
                assert len(minRepeatingUnits) == monomersAmount, "The length of minRepeatingUnits does not match the amount of monomers!"
            if type(maxRepeatingUnits) == list:
                assert sum(maxRepeatingUnits) >= minRepeatingUnits, "minRepeatingUnits is higher than the sum of maxRepeatingUnits, this can't be correct..."
                assert len(maxRepeatingUnits) == monomersAmount, "The length of maxRepeatingUnits does not match the amount of monomers!"
            else:
                assert maxRepeatingUnits >= minRepeatingUnits, "minRepeatingUnits is higher than maxRepeatingUnits, this can't be correct..."

        # Now assemble the matrix
        if type(minRepeatingUnits) == list:
            if type(maxRepeatingUnits) == list:
                RUCombinations = [(a,) for a in range(minRepeatingUnits[0], maxRepeatingUnits[0] + 1)]
                for i in range(1, monomersAmount):
                    RUCombinations = [(*a, b) for a in RUCombinations for b in
                                      range(minRepeatingUnits[i], maxRepeatingUnits[i] + 1)
                                      if sum(a) + b <= maxSumRepeatingUnits]
                return None if len(RUCombinations) == 0 else RUCombinations
            elif type(maxRepeatingUnits) == int:
                RUCombinations = [(a,) for a in range(minRepeatingUnits[0], maxRepeatingUnits + 1)]
                for i in range(1, monomersAmount):
                    RUCombinations = [(*a, b) for a in RUCombinations for b in
                                      range(minRepeatingUnits[i], maxRepeatingUnits + 1 - sum(a))]
                return None if len(RUCombinations) == 0 else RUCombinations
            else:
                raise ValueError("maxRepeatingUnits must be either int or list.")
        elif type(minRepeatingUnits) == int:
            # in this case, only a global minimum is given, so all combinations have to be made from 0
            # the ones with a sum smaller than minSumRepeatingUnits will be filtered later
            if type(maxRepeatingUnits) == list:
                RUCombinations = [(a,) for a in range(maxRepeatingUnits[0] + 1)]
                for i in range(1, monomersAmount):
                    RUCombinations = [(*a, b) for a in RUCombinations
                                      for b in range(maxRepeatingUnits[i] + 1)
                                      if sum(a) + b <= maxSumRepeatingUnits]
                RUCombinations = [RUCombination for RUCombination in RUCombinations if
                                  sum(RUCombination) >= minSumRepeatingUnits]
                return None if len(RUCombinations) == 0 else RUCombinations
            elif type(maxRepeatingUnits) == int:
                # most simple case: every monomer from 0 to the maxRepeatingUnits minus what's already there from previous iterations
                RUCombinations = [(a,) for a in range(maxRepeatingUnits + 1)]
                for i in range(1, monomersAmount):
                    RUCombinations = [(*a, b) for a in RUCombinations for b in range(maxRepeatingUnits + 1 - sum(a))]
                RUCombinations = [RUCombination for RUCombination in RUCombinations if
                                  sum(RUCombination) >= minSumRepeatingUnits]
                return None if len(RUCombinations) == 0 else RUCombinations
            else:
                raise ValueError("maxRepeatingUnits must be either int or list.")
        else:
            raise ValueError("minRepeatingUnits must be either int or list.")

    def __init__(self,
                 endgroupPairs,
                 monomers,
                 adductIon = "H+",
                 charge = 1,
                 minRelAbundance = 0.01,
                 minRepeatingUnits = None,
                 minSumRepeatingUnits=None,
                 maxRepeatingUnits = None,
                 maxSumRepeatingUnits=None,
                 mzRange = None,
                 compositions = None,
                 customEndgroupsDatabase = None,
                 customMonomersDatabase = None,
                 firstMonomerMajor: bool = False,
                 comonomersToFirstMaxRatio: float = 1,
                 lastMonomerMinor: bool = False):
        """

        :type endgroupPairs: list
        :type monomers: list
        :type adductIon: str
        :type charge: int
        :type minRelAbundance: float
        :type minRepeatingUnits: list
        :type minSumRepeatingUnits: int
        :type maxRepeatingUnits: list
        :type maxSumRepeatingUnits: int
        :type mzRange: list
        :type compositions: list
        :type customEndgroupsDatabase: dict
        :type customMonomersDatabase: dict
        """

        # Internal formulas of endgroups and monomers should be (lists of) Counters for processing
        # Their self.attr counterpart is then the counter printed as str for easy external readout.
        #todo Maybe allow to enter chemical formulas directly, but then the code should first check whether the string is found in the database and if not transform it using the getCounterFromFormula function. Not urgent

        # input processing
        if customEndgroupsDatabase is not None:
            self.customEndgroupsDatabase = customEndgroupsDatabase
        else:
            self.customEndgroupsDatabase = dict()
        if customMonomersDatabase is not None:
            self.customMonomersDatabase = customMonomersDatabase
        else:
            self.customMonomersDatabase = dict()
        print("Simulating polymer...")
        if type(endgroupPairs) != list:
            endgroupPairs = [endgroupPairs]
        self.endgroupPairs = []
        for index, endgroupPair in enumerate(endgroupPairs):
            if type(endgroupPair) == str: # lookup the entry in the endgroups list in the database
                self.endgroupPairs.append(endgroupPair)
                if endgroupPair in self.customEndgroupsDatabase:
                    endgroupPairs[index] = self.customEndgroupsDatabase[endgroupPair][0] + self.customEndgroupsDatabase[endgroupPair][1]
                elif endgroupPair in pymacroms.database.endgroups:
                    endgroupPairs[index] = pymacroms.database.endgroups[endgroupPair][0] + pymacroms.database.endgroups[endgroupPair][1]
                else:
                    sys.exit("endgroupPair " + endgroupPair + " not found in either custom or built-in database!")
            elif type(endgroupPair) == list: # entry in the endgroups list is a list --> both endgroups are separate so should be combined first
                endgroupPairs[index] = endgroupPair[0] + endgroupPair[1]
                self.endgroupPairs.append(pymacroms.getFormulaStrFromCounter(endgroupPairs[index]))
            else: # entry is a counter, 1 counter for the 2 endgroups of the polymer
                self.endgroupPairs.append(pymacroms.getFormulaStrFromCounter(endgroupPair))
        if type(monomers) != list:
            monomers = [monomers]
        self.monomers = []
        for index, monomer in enumerate(monomers):
            if type(monomer) == str:
                self.monomers.append(monomer)
                if monomer in self.customMonomersDatabase:
                    monomers[index] = self.customMonomersDatabase[monomer]
                elif monomer in pymacroms.database.monomers:
                    monomers[index] = pymacroms.database.monomers[monomer]
                else:
                    sys.exit("Monomer " + monomer + " not found in either custom or built-in database!")
            else:
                self.monomers.append(pymacroms.getFormulaStrFromCounter(monomer))

        self.adductIon = adductIon
        self.charge = charge
        try:
            adductIon = pymacroms.database.ionising_species[adductIon]  # [formula: Counter, charge: int, mass_correction: float]
        except:
            sys.exit("adductIon not found in database!")
        self.amountAdductIons = abs(int(charge / adductIon[1]))
        if compositions is None:
            # macromolecules will be generated with a defined minimum and maximum (total) number of repeating units
            # These boundaries can be given as arguments, but can also be estimated from an mzRange and
            # the molecular weights of the smallest (maxRU) and biggest (minRU) monomer:
            # But first compatibility with old code:
            if minSumRepeatingUnits is None and type(minRepeatingUnits) == int:
                minSumRepeatingUnits = minRepeatingUnits
            if maxSumRepeatingUnits is None and type(maxRepeatingUnits) == int:
                maxSumRepeatingUnits = maxRepeatingUnits
            if maxRepeatingUnits is None and maxSumRepeatingUnits is None and mzRange is None:
                # it will be impossible to estimate the range of repeating units
                sys.exit("I'm struggling to build a matrix of possible combinations of monomers based on \nthe provided combination of mzRange, min(Sum)RepeatingUnits and max(Sum)RepeatingUnits.\nPlease check the parameters.")
            elif maxSumRepeatingUnits is None and mzRange is not None:
                if minSumRepeatingUnits is None:
                    minSumRepeatingUnits = max(int((mzRange[0] * abs(charge) - max(list(pymacroms.getMonoIsotopicMass(endgroupPair) for endgroupPair in endgroupPairs)) - abs(int(charge / adductIon[1])) * pymacroms.getMonoIsotopicMass(adductIon[0])) / max(list(pymacroms.getMonoIsotopicMass(monomer) for monomer in monomers))), 0)
                    print("--> minimum sum of repeating units: %i (estimated based on the provided mzRange and the masses of the components)" % minSumRepeatingUnits)
                maxSumRepeatingUnits = int((mzRange[1] * abs(charge) - min(list(pymacroms.getMonoIsotopicMass(endgroupPair) for endgroupPair in endgroupPairs)) - abs(int(charge / adductIon[1])) * pymacroms.getMonoIsotopicMass(adductIon[0])) / min(list(pymacroms.getMonoIsotopicMass(monomer) for monomer in monomers))) + 1
                print("--> maximum sum of repeating units: %i (estimated based on the provided mzRange and the masses of the components)" % maxSumRepeatingUnits)
            elif minSumRepeatingUnits is None:
                if mzRange is not None:
                    minSumRepeatingUnits = max(int((mzRange[0] * abs(charge) - max(list(pymacroms.getMonoIsotopicMass(endgroupPair) for endgroupPair in endgroupPairs)) - abs(int(charge / adductIon[1])) * pymacroms.getMonoIsotopicMass(adductIon[0])) / max(list(pymacroms.getMonoIsotopicMass(monomer) for monomer in monomers))), 0)
                    print("--> minimum sum of repeating units: %i (estimated based on the provided mzRange and the masses of the components)" % minSumRepeatingUnits)
                else:
                    minSumRepeatingUnits = 0
                    print("--> minimum sum of repeating units set to 0 since it cannot be estimated")
            # Now build all the combinations of repeating units within the limits of the given (or estimated) parameters
            RUCombinations = self.getRUCombinations(len(monomers),
                                                    minRepeatingUnits=minRepeatingUnits,
                                                    minSumRepeatingUnits=minSumRepeatingUnits,
                                                    maxRepeatingUnits=maxRepeatingUnits,
                                                    maxSumRepeatingUnits=maxSumRepeatingUnits)
            if RUCombinations is None:
                sys.exit("Failed to build a matrix of possible combinations of monomers based on \nthe provided combination of mzRange, min(Sum)RepeatingUnits and max(Sum)RepeatingUnits.\nPlease check the parameters.")
            # Finally, combine the combinations of repeating units with the different indices of the different end groups
            compositions = itertools.product(range(len(endgroupPairs)), RUCombinations)
            # Dropped the conversion from itertools.product to list as this gave a serious computational penalty and later it doesn't matter for the iteration
            # itertools doesn't have a length attribute though so output had to be adjusted as well
            # print("--> Possible combinations of repeating units/end groups based on given parameters: " + str(len(compositions)))
            print("--> Possible combinations of repeating units/end groups determined")
        print("--> Filtering and calculating the isotopic patterns...")

        formulaDatabase = [[], []]
        macromolecules = []
        isobaricSpecies = False
        numberCompositions = 0
        bar = progressbar.ProgressBar(widgets=[progressbar.Counter(), ' - ', progressbar.Timer()], max_value=progressbar.UnknownLength, prefix='Number of macromolecules assessed: ')
        for EGPairIndex, RUCombination in compositions:
            numberCompositions += 1
            sumRUCombination = sum(RUCombination)
            # should be redundant as this is now handled by the getRUCombinations function
            # if sumRUCombination < minRepeatingUnits or sumRUCombination > maxRepeatingUnits: # kick out the monomer combinations that result in a total amount of repeating units outside the defined range
            #     continue
            if firstMonomerMajor and RUCombination[0] < (sumRUCombination - RUCombination[0])/comonomersToFirstMaxRatio:
                continue
            lenRUCombination = len(RUCombination)
            if lastMonomerMinor and lenRUCombination > 2 and RUCombination[lenRUCombination-1] > sumRUCombination - RUCombination[0] - RUCombination[lenRUCombination-1]: #
                # only makes sense when there are 3 or more different monomers
                # will still include the combination that has the same amount of last monomer as the sum of others
                # RUCombination[len(RUCombination)-1] > min(RUCombination) is bad plan
                continue
            formulaCounter = Counter()
            for index, numberRU in enumerate(RUCombination):
                formulaCounter += Counter({element:amount*numberRU for element,amount in monomers[index].items()})
            formulaCounter = endgroupPairs[EGPairIndex] + formulaCounter
            if formulaCounter in formulaDatabase[0]:
                formulaDatabase[1][formulaDatabase[0].index(formulaCounter)].append([RUCombination, EGPairIndex])
                macromolecules[formulaDatabase[0].index(formulaCounter)]["isobaricCompositions"].append([EGPairIndex, RUCombination])
                isobaricSpecies = True
            else:
                if mzRange is not None:
                    # Don't even calculate the molecule if its monoisotopic mass is +- 10 outside the defined mass range
                    if not mzRange[0] - 10 <= pymacroms.getMonoIsotopicMass(formulaCounter + pymacroms.getCounterFromFormula(self.adductIon)) <= mzRange[1] + 10:
                        continue
                    else:
                        tempMolecule = pymacroms.Molecule(formulaCounter, self.adductIon, charge, minRelAbundance)
                    # kick out the molecule if it's outside the defined mass range
                    if not tempMolecule.inMassRange(mzRange, False):
                        continue
                else:
                    tempMolecule = pymacroms.Molecule(formulaCounter, self.adductIon, charge, minRelAbundance)
                macromolecules.append({#"id": numberCompositions - 1,
                                       "repUnitsTotal": sum(RUCombination),
                                       "repUnitsCombination": RUCombination,
                                       "endgroupPairIndex": EGPairIndex,
                                       "isobaricCompositions": [[EGPairIndex, RUCombination]],
                                       "moleculeData": tempMolecule})
                formulaDatabase[0].append(formulaCounter)
                formulaDatabase[1].append([[RUCombination, EGPairIndex]])
            bar.update(numberCompositions)
        bar.update(numberCompositions)
        bar.finish()
        if isobaricSpecies:
            self.isobaricSpecies = []
            for index, [counter, data] in enumerate(zip(formulaDatabase[0], formulaDatabase[1])):
                if len(data) > 1:
                    self.isobaricSpecies.append({"repUnitsCombinations": list(zip(*data))[0],
                                                 "endgroupPairIndices": list(zip(*data))[1],
                                                 "moleculeData": macromolecules[index]["moleculeData"],
                                                 # "macromoleculeID": macromolecules[index]["id"]
                                                 })
        else:
            self.isobaricSpecies = None
        print("--> Based on the restrictions, {} (non-isobaric) macromolecules were retained \n    of the {} combinations of repeating units/end groups...".format(len(macromolecules), numberCompositions))
        self.macromolecules = sorted(macromolecules, key=itemgetter("repUnitsTotal"))
        self.isotopicDist = self.getIsotopicDist()
        self.mzRange = [self.isotopicDist[0][0], self.isotopicDist[len(self.isotopicDist) - 1][0]]
        print("--> Done\n")

    def aggregateIsotopes(self, resolution: float):
        print("--> Combining isotopologues within resolution limits for all %i macromolecules" % len(self.macromolecules))
        sys.stdout.flush()
        if hasattr(self.macromolecules[0]["moleculeData"], "resolution"):
            if self.macromolecules[0]["moleculeData"].resolution == resolution:
                print("--> Isotopologues have already been aggregated with this resolution")
                return
        for macromolecule in progressbar.progressbar(self.macromolecules, 0, len(self.macromolecules)):
            macromolecule["moleculeData"].aggregateIsotopicDist(resolution)
        '''
        for macromolecule in progressbar.progressbar(self.macromolecules, 0, len(self.macromolecules)):
            macromolecule["moleculeData"].resolution = resolution
            macromolecule["moleculeData"].isotopicDist_resolution = pymacroms.combineIsotopes(macromolecule["moleculeData"].isotopicDist, resolution)
            macromolecule["moleculeData"].massMostAbundant = sorted(macromolecule["moleculeData"].isotopicDist_resolution, key=itemgetter(1), reverse=True)[0][0]
        '''

    def getIsotopicDist(self, resolution: float = None):
        if resolution is not None:
            self.aggregateIsotopes(resolution)
        isotopicDist = np.concatenate([np.array(macromolecule["moleculeData"].isotopicDist) for macromolecule in
                                       self.macromolecules]) if resolution is None else np.concatenate(
            [np.array(macromolecule["moleculeData"].isotopicDist_resolution) for macromolecule in self.macromolecules])
        isotopicDist = isotopicDist[isotopicDist[:, 0].argsort()]
        return [(mass, normAbund) for mass, normAbund in isotopicDist]

    def getIsotopicDist_indexed(self, resolution: float = None):
        try:
            return self.isotopicDist_indexed[resolution]
        except:
            if not hasattr(self, "isotopicDist_indexed"):
                self.isotopicDist_indexed = dict()
            if resolution is None:
                self.isotopicDist_indexed[resolution] = np.concatenate(([np.append(np.full((len(macromolecule["moleculeData"].isotopicDist), 1), index), np.array(macromolecule["moleculeData"].isotopicDist), axis=1) for index, macromolecule in enumerate(self.macromolecules)]))
            else:
                try:
                    self.isotopicDist_indexed[resolution] = np.concatenate(([np.append(np.full((len(macromolecule["moleculeData"].isotopicDist_resolution), 1), index), np.array(macromolecule["moleculeData"].isotopicDist_resolution) if macromolecule["moleculeData"].resolution == resolution else np.array(macromolecule["moleculeData"].aggregateIsotopicDist(resolution)), axis=1) for index, macromolecule in enumerate(self.macromolecules)]))
                except:
                    self.isotopicDist_indexed[resolution] = np.concatenate(([np.append(np.full((len(macromolecule["moleculeData"].aggregateIsotopicDist(resolution)), 1), index), np.array(macromolecule["moleculeData"].aggregateIsotopicDist(resolution)), axis=1) for index, macromolecule in enumerate(self.macromolecules)]))
            return self.isotopicDist_indexed[resolution]

    def getMoleculeList_old(self, experimentalMass: float = None, ppmDev: float = 5, resolution: float = None):
        isotopesNearMass = None
        moleculeList = []
        for index, macromolecule in enumerate(self.macromolecules):
            if experimentalMass is not None:
                isotopesNearMass = macromolecule["moleculeData"].getIsotopesNearMass(experimentalMass, ppmDev, resolution)
                if isotopesNearMass is None:
                    continue
            moleculeList.append([index, list(macromolecule["repUnitsCombination"]), isotopesNearMass])
        # return sorted(moleculeList, key=itemgetter(2))
        if len(moleculeList) > 0:
            return sorted(moleculeList, key=itemgetter(1))
        else:
            return None

    def getMoleculeList(self, experimentalMass: float = None, ppmDev: float = 5, resolution: float = None):
        if experimentalMass is None:
            return [[index, list(macromolecule["repUnitsCombination"]), None] for index, macromolecule in enumerate(self.macromolecules)]
        moleculeList = []
        isotopicDist = self.getIsotopicDist_indexed(resolution)
        deviation = abs((experimentalMass - isotopicDist[:, 1]) / isotopicDist[:, 1] * 1e6)
        in_limit = np.where(deviation <= ppmDev)
        isotopicDist = np.append(isotopicDist[in_limit], np.reshape(deviation, (-1, 1))[in_limit], axis=1)
        for index in np.unique(isotopicDist[:, 0]):
            moleculeList.append([int(index),
                                 list(self.macromolecules[int(index)]["repUnitsCombination"]),
                                 [(isotopeMass, normAbundance, deviation) for index, isotopeMass, normAbundance, deviation in isotopicDist[np.where(isotopicDist[:, 0] == index)]]])
        if len(moleculeList) > 0:
            return sorted(moleculeList, key=itemgetter(1))
        else:
            return None

    # def printMoleculeList(self, experimentalMass: float = None, ppmDev: float = 5):
    #     print("Monomer combination\tFormula (ion)\tMost abundant mass")
    #     # print("\t" + str(self.monomers))
    #     for macromoleculeIndex, repUnitsCombination, formula_ion, massMostAbundant in self.getMoleculeList(experimentalMass, ppmDev):
    #         print(str(repUnitsCombination) + "\t" + formula_ion + "\t" + str(massMostAbundant))

    def printMoleculeList(self, experimentalMass: float = None, ppmDev: float = 5, resolution: float = None):
        moleculeList = self.getMoleculeList(experimentalMass, ppmDev, resolution)
        if moleculeList is not None:
            print("Experimental mass: " + str(experimentalMass))
            print("Monomer combination\tEnd-groups\tFormula (ion)\tMost abundant mass\tMatched isotope(s) (m/z, dev. (ppm))")
            # print(str(self.monomers) + "\t\t\t(m/z, norm. abundance, dev (ppm))")
            for macromoleculeIndex, repUnitsCombination, isotopesNearMass in moleculeList:
                if isotopesNearMass is not None:
                    print(str(repUnitsCombination) + "\t" + self.endgroupPairs[self.macromolecules[macromoleculeIndex]["endgroupPairIndex"]] + "\t" + self.macromolecules[macromoleculeIndex]["moleculeData"].formula_ion + "\t" + str(self.macromolecules[macromoleculeIndex]["moleculeData"].massMostAbundant) + "\t" + str(list((mz, round(abs(dev), 2)) for mz, normAbund, dev in isotopesNearMass)))
                else:
                    print(str(repUnitsCombination) + "\t" + self.endgroupPairs[
                        self.macromolecules[macromoleculeIndex]["endgroupPairIndex"]] + "\t" +
                          self.macromolecules[macromoleculeIndex]["moleculeData"].formula_ion + "\t" + str(
                        self.macromolecules[macromoleculeIndex]["moleculeData"].massMostAbundant) + "\tN/A")
        else:
            print("No matching molecules found...")

    def saveMoleculeList(self, filename: str, experimentalMass: float = None, ppmDev: float = 5, resolution: float = None):
        moleculeList = self.getMoleculeList(experimentalMass, ppmDev, resolution)
        if moleculeList is not None:
            output = []
            for macromoleculeIndex, repUnitsCombination, isotopesNearMass in moleculeList:
                if isotopesNearMass is not None:
                    output.append([str(repUnitsCombination), self.endgroupPairs[self.macromolecules[macromoleculeIndex]["endgroupPairIndex"]], self.macromolecules[macromoleculeIndex]["moleculeData"].formula_ion, str(self.macromolecules[macromoleculeIndex]["moleculeData"].massMostAbundant), str(list((mz, round(abs(dev), 2)) for mz, normAbund, dev in isotopesNearMass))])
                else:
                    output.append([str(repUnitsCombination), self.endgroupPairs[self.macromolecules[macromoleculeIndex]["endgroupPairIndex"]], self.macromolecules[macromoleculeIndex]["moleculeData"].formula_ion, str(self.macromolecules[macromoleculeIndex]["moleculeData"].massMostAbundant), "N/A"])
            export = pd.DataFrame(output,
                                  columns=["Monomer combination", "End-groups", "Formula (ion)", "Most abundant mass",
                                           "Matched isotope(s) (m/z, dev. (ppm))"])
        else:
            export = pd.DataFrame(columns=["No matching molecules found..."])
        export.to_csv(filename + ".csv", index=False)

    def printFullInfo(self):
        print("Total number of repeating units\tMonomer combination\tEnd-groups\tFormula (ion)\tm/z\tRel. Abundance")
        print("\t" + str(self.monomers))
        for macromolecule in self.macromolecules:
            i = 1
            for mass, relAbund in pymacroms.toRelativeAbundance(macromolecule["moleculeData"].isotopicDist):
                if i == 1:
                    print(str(macromolecule["repUnitsTotal"]) + "\t" + str(list(macromolecule["repUnitsCombination"])) + "\t" + self.endgroupPairs[macromolecule["endgroupPairIndex"]] + "\t" + macromolecule["moleculeData"].formula_ion + "\t" + str(mass) + "\t" + str(relAbund))
                else:
                    print("\t\t\t\t" + str(mass) + "\t" + str(relAbund))
                i += 1

    def printIsotopicDist(self, resolution: float = None):
        print("Mass\tRel. Abundance")
        print("\t" + str(self.monomers))
        if resolution is not None:
            if not hasattr(self, "isotopicDist_resolution"):
                self.isotopicDist_resolution = self.getIsotopicDist(resolution)
            isotopicDist_rel = pymacroms.toRelativeAbundance(self.isotopicDist_resolution)
        else:
            isotopicDist_rel = pymacroms.toRelativeAbundance(self.isotopicDist)
        for mass, relAbund in isotopicDist_rel:
            print(str(mass) + "\t" + str(relAbund))

    def plotIsotopicDist(self, color = "black", mzRange: list = None):
        mz_axis = []
        relAbund_axis = []
        for mz, relAbund in pymacroms.toRelativeAbundance(self.isotopicDist):
            mz_axis += list([mz - 1e-10, mz, mz + 1e-10])
            relAbund_axis += list([-0.1, relAbund, -0.1])
        plt.plot(mz_axis, relAbund_axis, color=color)
        plt.title(r"Isotopic distribution ({}{} adducts) of a (co)polymer of".format(self.amountAdductIons, re.sub("([0-9]+)", "$_{\\1}$", re.sub("([+-]+)", "$^{\\1}$", self.adductIon))) + "\n" +
                  "{} with end-group(s): {}".format(re.sub("([0-9]+)", "$_{\\1}$", str(self.monomers)), re.sub("([0-9]+)", "$_{\\1}$", str(self.endgroupPairs))))
        plt.xlabel("m/z")
        plt.ylabel("Rel. abundance")
        if mzRange is not None:
            plt.xlim(mz for mz in mzRange)
        plt.ylim(0, 1.05)
        plt.show()

    def getIsobaricSpecies(self):
        if self.isobaricSpecies is None:
            return None
        else:
            isobaricSpecies = []
            for macromolecule in self.isobaricSpecies:
                isobaricSpecies.append([macromolecule["moleculeData"].formula_ion, macromolecule["moleculeData"].massMostAbundant, list([str(list(repUnitsCombination)), self.endgroupPairs[endgroupPair]] for repUnitsCombination, endgroupPair in zip(macromolecule["repUnitsCombinations"],macromolecule["endgroupPairIndices"]))])
            return sorted(isobaricSpecies, key=itemgetter(1))

    def printIsobaricSpecies(self):
        isobaricSpecies = self.getIsobaricSpecies()
        if isobaricSpecies is not None:
            print("Formula (ion)\tMost abundant mass\tMonomer combinations\tEnd-groups")
            print("\t" + str(self.monomers))
            for macromolecule in isobaricSpecies:
                i = 1
                for repUnitsCombination, endgroupPair in macromolecule[2]:
                    if i == 1:
                        print(macromolecule[0] + "\t" + "%.4f" % round(macromolecule[1], 4) + "\t" + repUnitsCombination + "\t" + endgroupPair)
                    else:
                        print("\t\t" + repUnitsCombination + "\t" + endgroupPair)
                    i += 1
        else:
            print("No isobaric macromolecules in the simulation...")
