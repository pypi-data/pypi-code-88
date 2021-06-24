# TODO: coords units and other meta-data all represented here

# TODO: namedtuple / dataclass?
# TODO: Vx full names
param_attributes = {
    # Sphere params
    'N(O2)': {
        'long_name': 'O2 number density',
        'units': 'cm-3'},
    'N(N2)': {
        'long_name': 'N2 number density',
        'units': 'cm-3'},
    'N(O)': {
        'long_name': 'O number density',
        'units': 'cm-3'},
    'N(NO)': {
        'long_name': 'NO number density',
        'units': 'cm-3'},
    'N(N)': {
        'long_name': 'N number density',
        'units': 'cm-3'},
    'N(XY+)': {
        'long_name': 'Total positive molecular ion number density',
        'units': 'cm-3'},
    'Tn': {
        'long_name': 'Neutral temperature',
        'units': 'K'},
    'Ti': {
        'long_name': 'Ion temperature',
        'units': 'K'},
    'Te': {
        'long_name': 'Electron temperature',
        'units': 'K'},
    'Vr': {
        'long_name': '',
        'units': 'K'},
    'Vt': {
        'long_name': '',
        'units': 'cm/s'},
    'Vd': {
        'long_name': '',
        'units': 'cm/s'},
    'q(O2+)': {
        'long_name': 'O2+ ion production rate',
        'units': 'cm-3/s'},
    'q(N2+)': {
        'long_name': 'N2+ ion production rate',
        'units': 'cm-3/s'},
    'q(NO+)': {
        'long_name': 'NO+ ion production rate',
        'units': 'cm-3/s'},
    'q(O+)': {
        'long_name': 'O+ ion production rate',
        'units': 'cm-3/s'},
    # pot params
    'pot': {
        'long_name': 'Electric potential',
        'units': 'V'}, # TODO: verify this
    # params of tube interpolated to sphere 
    #   (Te is shared by sphere params)
    'N(O+)': {
        'long_name': 'O+ number density',
        'units': 'cm-3'},
    'Vr(O+)': {
        'long_name': '',
        'units': 'cm/s'},
    'Vt(O+)': {
        'long_name': '',
        'units': 'cm/s'},
    'Vd(O+)': {
        'long_name': '',
        'units': 'cm/s'},
    
    # tube params
    # ...
    } 