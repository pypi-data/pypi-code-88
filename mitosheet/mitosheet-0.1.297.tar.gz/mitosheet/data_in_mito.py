from enum import Enum
import pandas as pd


"""
    The DataTypeInMito enum is used to signify the type of data in Mito.
    It can be one of four types:

    1. NONE = no data is in Mito
    2. PROVIDED = any data that we provided through our docs, except the tutorial data which has a special designation
    3. TUTORIAL = the tutorial data provided through the docs
    4. PERSONAL = any data not provided by Mito

    NOTE: this should be the same as the enum in Mito.tsx with the same name
"""
class DataTypeInMito(Enum):
    NONE = 'none'
    PROVIDED = 'provided'
    TUTORIAL = 'tutorial'
    PERSONAL = 'personal'


# We keep track of the tutorial and provided data
TUTORIAL_FILE_NAMES = ['Airport-Pets.csv', 'Zipcode-Data.csv']
TUTORIAL_AIRPORT_PETS_COLUMNS = ['Zip', 'City', 'State', 'Division', 'Parking', 'Pets', 'Food', 'Lounge']
TUTORIAL_ZIPCODE_COLUMNS = ['Zip', 'Median_Income', 'Mean_Income', 'Pop']

PROVIDED_TICKET_OFFICE_COLUMNS = ['Zip', 'City', 'State', 'Ticket_Office']
PROVIDED_TICKET_ZIPCODE_COLUMNS = ['Zip', 'Median_Income', 'Median_Income', 'Mean_Income', 'Pop']


def get_data_type_in_mito(*args) -> DataTypeInMito:
    """
    Returns the DataTypeInMito based on the args to the function.

    If this function is called by the simple import condition of the handle_edit_event,
    then the args are the names of the files that are imported

    If this function is called from the mitosheet.sheet() call then its either a string or dataframe object
    """
    args = list(args)
    tutorial_data_found = False

    if len(args) <= 0:
        return DataTypeInMito.NONE

    for arg in args:
        # If the arg is a string, its either the path to a file which we then assume is personal data or
        # it is the name of the file imported during a simple import. 
        if isinstance(arg, str):
            # If the arg is a string, check if its a tutorial file name.
            # If its not tutorial data, then its personal data
            if arg not in TUTORIAL_FILE_NAMES:
                return DataTypeInMito.PERSONAL
            else:
                # We mark that we came across tutorial data because if we don't end up finding personal data
                # then we want to be able to return that we found tutorial data
                tutorial_data_found = True

        # If the arg is a dataframe, then check if the columns are either from the tutorial or provided data. 
        if isinstance(arg, pd.DataFrame):
            # If the user passed a dataframe with headers the same as the tutorial data, then return DataTypeInMito.TUTORIAL
            if (
                arg.columns.tolist() == TUTORIAL_AIRPORT_PETS_COLUMNS or 
                arg.columns.tolist() == TUTORIAL_ZIPCODE_COLUMNS 
            ): 
                return DataTypeInMito.TUTORIAL

            # If the user passed a dataframe with headers the same as the provided data, then return DataTypeInMito.PROVIDED
            if (
                arg.columns.tolist() == PROVIDED_TICKET_OFFICE_COLUMNS or 
                arg.columns.tolist() == PROVIDED_TICKET_ZIPCODE_COLUMNS
            ):
                return DataTypeInMito.PROVIDED

    # If we came across tutorial data and have not yet returned Personal data, then return Tutorial Data
    # otherwise, the data is personal data
    return DataTypeInMito.TUTORIAL if tutorial_data_found else DataTypeInMito.PERSONAL
