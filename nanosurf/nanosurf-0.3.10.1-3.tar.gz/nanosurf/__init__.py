"""Package for scripting the Nansurf control software.
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import nanosurf._spm 

_known_spm_app_names = [ 'SPM', 
        'MobileS', 'SPM_S', 'Easyscan2', 'C3000', 'Naio', 'USPM',
        'CoreAFM', 'CX']

for _application_name in _known_spm_app_names:
    globals()[_application_name] = type(
        _application_name, (nanosurf._spm.Spm,),
        {'_class_id': (_application_name + ".Application")})
