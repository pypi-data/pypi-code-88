import pandas as pd

state_dictionary = {'01': ['Alabama', 'AL'],
                    '02': ['Alaska', 'AK'],
                    '60': ['American Samoa', 'AS'],
                    '04': ['Arizona', 'AZ'],
                    '05': ['Arkanas', 'AR'],
                    '06': ['Califorinia', 'CA'],
                    '08': ['Colorado', 'CO'],
                    '69': ['Commonwealth of the Northern Marinara Islands', 'MP'],
                    '09': ['Connecticut', 'CT'],
                    '10': ['Delaware', 'DE'],
                    '11': ['Disctrict of Columbia', 'DC'],
                    '12': ['Florida', 'FL'],
                    '13': ['Georgia', 'GA'],
                    '66': ['Guam', 'GU'],
                    '15': ['Hawaii', 'HI'],
                    '16': ['Idaho', 'ID'],
                    '17': ['Illiois', 'IL'],
                    '18': ['Indiana', 'IN'],
                    '19': ['Iowa', 'IA'],
                    '20': ['Kansas', 'KS'],
                    '21': ['Kentucky', 'KY'],
                    '22': ['Louisiana', 'LA'],
                    '23': ['Maine', 'ME'],
                    '24': ['Maryland', 'MD'],
                    '25': ['Massachusetts', 'MA'],
                    '26': ['Michigan', 'MI'],
                    '27': ['Minnesota', 'MN'],
                    '28': ['Mississippi', 'MS'],
                    '29': ['Missouri', 'MO'],
                    '30': ['Montana', 'MT'],
                    '31': ['Nebraska', 'NE'],
                    '32': ['Nevada', 'NV'],
                    '33': ['New Hampshire', 'NH'],
                    '34': ['New Jersey', 'NJ'],
                    '35': ['New Mexico', 'NM'],
                    '36': ['New York', 'NY'],
                    '37': ['North Carolina', 'NC'],
                    '38': ['North Dakota', 'ND'],
                    '39': ['Ohio', 'OH'],
                    '40': ['Oklahoma', 'OK'],
                    '41': ['Oregon', 'OR'],
                    '42': ['Pennsylvania', 'PA'],
                    '72': ['Puerto Rico', 'PR'],
                    '44': ['Rhode Island', 'RI'],
                    '45': ['South Carolina', 'SC'],
                    '46': ['South Dakota', 'SD'],
                    '47': ['Tennessee', 'TN'],
                    '48': ['Texas', 'TX'],
                    '74': ['US Minor Outlying Islands', 'UM'],
                    '78': ['US Virgin Islands', 'VI'],
                    '49': ['Utah', 'UT'],
                    '50': ['Vermont', 'VT'],
                    '51': ['Virginia', 'VA'],
                    '53': ['Washington', 'WA'],
                    '54': ['West Virginia', 'WV'],
                    '55': ['Wisconsin', 'WI'],
                    '56': ['Wyoming', 'WY']}
census_tracts_OCONUS = ['02','15','60','66','69','72','74','78']

def states(string):
    for key in state_dictionary:
        if string.startswith(key):
            return state_dictionary[key][0]

def state_column(data_frame: pd.DataFrame(), tractcode_column: str):
    data_frame['State'] = data_frame[tractcode_column].apply(states)
    return data_frame

def state_abbrev(string):
    for key in state_dictionary:
        if string.startswith(key):
            return state_dictionary[key][1]

def state_abb_column(data_frame: pd.DataFrame(), tractcode_column: str):
    data_frame['State abbreviation'] = data_frame[tractcode_column].apply(state_abbrev)
    return data_frame

def conus_only(data_frame: pd.DataFrame(), tractcode_column: str):
    for census_tract in census_tracts_OCONUS:
        data_frame = data_frame[~data_frame[tractcode_column].astype(str).str.startswith(census_tract)]
    return data_frame

def oconus(data_frame: pd.DataFrame(), tractcode_column: str):
    data_frame2 = pd.DataFrame()
    for census_tract in census_tracts_OCONUS:
        data_frame2 = data_frame2.append(data_frame[data_frame[tractcode_column].astype(str).str.startswith(census_tract)])
    return data_frame2

def geoid_to_tract(data_frame: pd.DataFrame(), geoid_column: str):
    data_frame['tractcode'] = data_frame[geoid_column].str.replace(r'^1400000US', '')
    return data_frame
