"""TORQUE_UTILS
    this module was developed by Victor Cossich (victor.cossich@gmail.com) and Conrado Torres (conradotl@gmail.com)
        to organize the main routines used in the lab. We are trying to make it usefull for the scientific comunity.
        Email us if you have any advice, reccomendation or want to talk about signals. ;)

"""
try:from torque_utils.sigproc import *
except: print('import -lab_utils.sigproc- has failed.\n'+
'Use help(lab_utils.sigproc) to see the requirements. dont worry,the other functions in this module is still working')


try:from torque_utils.statscalc import *
except: print('import -lab_utils.statscalc- has failed.\n'+
'Use help(lab_utils.statscalc) to see the requirements. dont worry,the other functions in this module is still working')


try:from torque_utils.vidproc import *
except: print('import -lab_utils.vidproc- has failed.\n'+
'Use help(lab_utils.vidproc) to see the requirements. dont worry,the other functions in this module is still working')

__version__ = "1.0.0"