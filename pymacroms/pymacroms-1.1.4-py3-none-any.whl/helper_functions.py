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
from math import exp, log, sqrt
from collections import Counter
import itertools
import pymacroms
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from operator import itemgetter, attrgetter
import re
import sys
import time
import PySimpleGUI as sg
# from numba import jit

def getMonoIsotopicMass(formula: Counter):
    return sum(list(sorted(pymacroms.database.isotopic_abundances[element], key=itemgetter(1), reverse=True)[0][0]*amount for element, amount in formula.items()))
    # totalMass = 0
    # for element, amount in formula.items():
    #     totalMass += pymacroms.database.isotopic_abundances[element][0][0] * amount
    # return totalMass

def getMolecularWeight(formula: Counter):
    return sum(list(pymacroms.database.atomic_weights[element]*amount for element, amount in formula.items()))


def getCounterFromFormula(formula: str):
    return Counter({element: int(amount) for element, amount in re.findall("([A-Z][a-z]*)([0-9]+)", re.sub(" ", "", re.sub("  ", " 1 ", re.sub("([A-Z][a-z]*)([0-9]*)", "\\1 \\2 ", re.sub(" ","", formula)))))})
    #first removes all spaces, then replace all elements with optional number by element-space-amount-space
    #because an absent number will result in a double space, the double spaces are then replaced by space-1-space
    #by removing the spaces again, the formula is then guaranteed to have an amount for every element (C9H18NO --> C9H18N1O1)
    #finally, transform in a list and then Counter by matching the element-amount pairs

    '''
    return Counter({element: int(amount) for element, amount in re.findall("([A-Z][a-z]*)([0-9]*)", re.sub("([A-Z][a-z]*)([A-Z]|\Z)", "\g<1>1\g<2>", formula))})
    Is more simple but gives an error on for example C9H18NO because in the first substitution, NO is replaced by N1O, and because O is already matched, it is not replaced by O1
    This results in an O: '' in the library and thus an error when converting to int 
    '''

def getFormulaStrFromCounter(formula: Counter):
    tempFormula = ""
    for element, amount in formula.items():  # sorted(dict) does not influence the calculations, while leaving it out typically gives more OK formulas for the OCDd chemist
        tempFormula += element + str(amount)
    return tempFormula

def toRelativeAbundance(peaklist: list):
    maxAbund = max(list(zip(*peaklist))[1])
    return sorted(list((mass, normAbund/maxAbund) for mass, normAbund in peaklist))

# @jit(nopython=True)
def combineIsotopes_old(peaklist: list, resolution: float):
    # returns a list of peaks [(mz, normAbundance)]
    if type(peaklist) == list:
        peaklist_df = pd.DataFrame(peaklist, columns=["mz", "abundance"])
        columns_temp = ["mz", "abundance"]
    else:
        columns_temp = peaklist.columns
        peaklist_df = peaklist.copy(deep=True)
        peaklist_df.columns = ["mz", "abundance"]

    peaklist_df.sort_values(by=['abundance'], ascending=False, inplace=True, ignore_index=True)
    result = []
    while len(peaklist_df) > 0:
        mz = peaklist_df.mz.iloc[0]
        dmz = mz / (2 * resolution)
        indices = peaklist_df.loc[(peaklist_df.mz >= mz - dmz) & (peaklist_df.mz <= mz + dmz)].index
        extract = peaklist_df.loc[indices]
        peaklist_df.drop(indices, inplace=True)
        if len(extract) > 1:
            result.append(np.average(extract.mz, weights=extract.abundance, returned=True))
        else:
            result.append(list(extract.itertuples(index=False, name=None))[0])
    result = sorted(result, key=itemgetter(0))

    if type(peaklist) == list:
        return result
    else:
        return pd.DataFrame(result, columns=columns_temp)

# @jit(nopython=True)
def combineIsotopes(peaklist: list, resolution: float):
    # returns a list of peaks [(mz, normAbundance)]
    if type(peaklist) == list:
        list_out = True
        peaklist = np.array(peaklist)
    else:
        list_out = False

    # sort in descending peak height
    peaklist = peaklist[peaklist[:, 1].argsort()[::-1]]
    result = np.array([])
    while len(peaklist) > 0:
        mz = peaklist[0, 0]
        dmz = 1.4 * mz / resolution # was mz / (2 * resolution) in previous versions
        # FWHM: dm = m/R --> peak = m +- m/(2R); 10% valley (95% normal): dm approx 2m/R --> peak = m +- m/R; 99.5% normal: dm approx 3m/R --> peak = m +- 1.5m/R
        # factor 1.4 estimated from simulations in Xcalibur with regard to centroiding and resolution
        indices = np.where(np.logical_and(peaklist[:, 0] >= mz - dmz, peaklist[:, 0] <= mz + dmz))
        extract = peaklist[indices]
        result = np.append(result, np.average(extract[:, 0], weights=extract[:, 1], returned=True))
        peaklist = np.delete(peaklist, indices, axis=0)

    result = np.reshape(result, (-1, 2))
    result = result[result[:, 0].argsort()] # sort mz
    return [(mz, abund) for mz, abund in result] if list_out else result

def gui():
    ThermoRawFrame = [
        [
            sg.Text("MS Scan filter:"),
            sg.DropDown([], size=(40, 1), key="-SCANFILTER-"),
        ],
        [
            sg.Checkbox("Filter charges", key="-CHARGEFILTER CHECK-"),
            sg.InputText(size=(7, 1), key="-CHARGEFILTER-", disabled=True)
        ],
        [
            sg.Radio('Average over scans', 'RadioThermoRaw1', default=True, key="-AVERAGESCANS-"),
        ],
        [
            sg.Text("    "),
            sg.Radio("Scan range:", 'RadioThermoRaw2', default=True, key="-AVERAGERANGE-"),
            sg.InputText(size=(7, 1), key="-SCANRANGE 1-"),
            sg.Text("to"),
            sg.InputText(size=(7, 1), key="-SCANRANGE 2-"),
        ],
        [
            sg.Text("    "),
            sg.Radio("Retention times:", 'RadioThermoRaw2', key="-AVERAGETIMES-"),
            sg.InputText(size=(7, 1), key="-RT 1-"),
            sg.Text("to"),
            sg.InputText(size=(7, 1), key="-RT 2-"),
        ],
        [
            sg.Radio('Select active scan', 'RadioThermoRaw1', key="-SINGLESCAN-"),
        ],
        [
            sg.Text("    "),
            sg.Text("Active scan:"),
            sg.InputText(size=(7, 1), key="-ACTIVESCAN-"),
        ],
    ]

    MSParametersFrame = [
        [
            sg.Text("Minimum relative abundance:"),
            sg.InputText(0.01, size=(7, 1), key="-MINRELABUNDANCE-")
        ],
        [
            sg.Text("m/z range:"),
            sg.InputText(size=(7, 1), key="-MZRANGE 1-"),
            sg.Text("to"),
            sg.InputText(size=(7, 1), key="-MZRANGE 2-"),
        ],
        [
            sg.Text("Maximum ppm deviation:"),
            sg.InputText(5, size=(7, 1), key="-PPMDEV-"),
        ],
        [
            sg.Text("Resolution:"),
            sg.InputText(20000, size=(7, 1), key="-RESOLUTION-"),
        ],
        [
            sg.Text("m/z offset:"),
            sg.InputText(0, size=(7, 1), key="-MZOFFSET-"),
        ],
    ]

    MSFileColumn = [
        [
            sg.Text("MS File:"),
            sg.InputText(size=(35, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(file_types=(("CSV Files", "*.csv"), ("Thermo RAW Files", "*.raw"),)),
        ],
        [
            sg.Frame("Thermo RAW file parameters:", ThermoRawFrame, visible=False, key="-ThermoRawFrame-")
        ],
        [
            sg.Frame("MS parameters:", MSParametersFrame)
        ],

        # [
        #     sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"),
        # ],
    ]

    MonomersFrame = [
        [
            sg.Listbox(list(pymacroms.database.monomers), size=(30, 6), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                       key="-MONOMERS-")
        ]
    ]

    EndgroupFrame = [
        [
            sg.Listbox(list(pymacroms.database.endgroups), size=(30, 6), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                       key="-ENDGROUPS-")
        ]
    ]

    SimulationColumn = [
        [
            sg.Text("Charge:"),
            sg.InputText(1, size=(7, 1), key="-CHARGE-")
        ],
        [
            sg.Text("Adduct Ion:"),
            sg.DropDown(list(pymacroms.database.ionising_species), size=(7, 1), key="-ADDUCTION-")
        ],
        [
            sg.Frame("Monomers", MonomersFrame)
        ],
        [
            sg.Frame("Endgroups", EndgroupFrame)
        ]
    ]

    OutputColumn = [
        [
            sg.Text("Minimum matched isotope fraction:"),
            sg.InputText(0.1, size=(7, 1), key="-MINISOFRACTION-"),
        ],
        [
            sg.Text("Minimum quantified amount:"),
            sg.InputText(0, size=(7, 1), key="-MINAMOUNT-"),
        ],
        [
            sg.Text(""),
        ],
        [
            sg.Checkbox("Plot overview matched peaks", key="-plotMatchPeaksOverview-", default=True)
        ],
        [
            sg.Checkbox("Print composition", key="-printComposition-", default=True)
        ],
        [
            sg.Checkbox("Print isobaric species", key="-printIsobaricSpecies-", default=False)
        ],
        [
            sg.Checkbox("Save composition (CSV)", key="-saveComposition-", default=False)
        ],
        [
            sg.Checkbox("Plot comparison spectrum", key="-plotComparisonSpectrum-", default=False)
        ],
        [
            sg.Checkbox("Save report (PDF)", key="-saveReport-", default=False)
        ],
        [
            sg.Text('')
        ],
        [
            sg.Submit(),
            sg.Button('Continue after showing plot')
        ],
    ]

    layout = [
        [
            sg.Column(MSFileColumn),
            sg.VSeperator(),
            sg.Column(SimulationColumn),
            sg.VSeperator(),
            sg.Column(OutputColumn),
        ],
        [
            sg.Output(size=(160, 10)),
        ],
    ]

    window = sg.Window("PyMacroMS v" + pymacroms.version, layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-FILE-":
            folder = values["-FILE-"]
            MSData = pymacroms.MSData(values["-FILE-"])
            if MSData.extension == "raw":
                window["-ThermoRawFrame-"].update(visible=True)
                window["-SCANRANGE 1-"].update(list(MSData.scanRange)[0])
                window["-SCANRANGE 2-"].update(list(MSData.scanRange)[len(MSData.scanRange) - 1])
                window["-SCANFILTER-"].update(MSData.MSScanFilters[0])
                window["-SCANFILTER-"].update(values=MSData.MSScanFilters)
        if event == 'Submit':
            t0 = time.time()
            polymerSimulation = pymacroms.Polymer(
                endgroupPairs=values["-ENDGROUPS-"],
                monomers=values["-MONOMERS-"],
                adductIon=values["-ADDUCTION-"],
                charge=int(values["-CHARGE-"]),
                minRelAbundance=float(values["-MINRELABUNDANCE-"]),
                mzRange=[float(values["-MZRANGE 1-"]), float(values["-MZRANGE 2-"])],
                # customEndgroupsDatabase=customEndgroupsDatabase,
                # customMonomersDatabase=customMonomersDatabase,
            )

            filterCharge = None
            averageOverScanRange = None
            averageOverRetentionTime = None
            if values["-CHARGEFILTER CHECK-"]:
                filterCharge = [0, int(values["-CHARGE-"])]
            if values["-AVERAGESCANS-"] and values["-AVERAGERANGE-"]:
                averageOverScanRange = [int(values["-SCANRANGE 1-"]), int(values["-SCANRANGE 2-"])]
            if values["-AVERAGESCANS-"] and values["-AVERAGETIMES-"]:
                averageOverRetentionTime = [float(values["-RT 1-"]), float(values["-RT 2-"])]
            MSData = pymacroms.MSData(
                values["-FILE-"],
                filterCharge=filterCharge,
                averageOverScanRange=averageOverScanRange,
                averageOverRetentionTime=averageOverRetentionTime,
                MSScanFilter=values["-SCANFILTER-"],
                mzOffset=float(values["-MZOFFSET-"]),
            )

            spectrumExperimental = pymacroms.Spectrum(
                MSData=MSData,
                mzRange=[float(values["-MZRANGE 1-"]), float(values["-MZRANGE 2-"])],
                minRelAbundance=float(values["-MINRELABUNDANCE-"]),
                ppmDev=float(values["-PPMDEV-"]),
                resolution=float(values["-RESOLUTION-"]),
                activeScan=values["-ACTIVESCAN-"],
                # customMonomersDatabase=customMonomersDatabase,
            )
            spectrumExperimental.matchPeaks(polymerSimulation)
            spectrumExperimental.calcComposition(
                minimumIsotopeFraction=float(values["-MINISOFRACTION-"]),
                minimumAmount=float(values["-MINAMOUNT-"]),
            )
            print("")
            print("All calculations finished in %f seconds." % (time.time() - t0))
            print("")
            if values["-plotMatchPeaksOverview-"]:
                spectrumExperimental.plotMatchPeaksOverview()
            if values["-printComposition-"]:
                spectrumExperimental.printComposition()
            if values["-printIsobaricSpecies-"]:
                polymerSimulation.printIsobaricSpecies()
            if values["-saveComposition-"]:
                spectrumExperimental.saveComposition()
            if values["-plotComparisonSpectrum-"]:
                spectrumExperimental.plotComparisonSpectrum(
                    resolution=float(values["-RESOLUTION-"]),
                    color="darkblue",
                    # savePlotAs="pdf"
                )
            if values["-saveReport-"]:
                spectrumExperimental.saveReport()

            print("")
            print("Script finished in %f seconds." % (time.time() - t0))

        if event == 'Continue after showing plot':
            # plt.close()
            pass

    window.close()



