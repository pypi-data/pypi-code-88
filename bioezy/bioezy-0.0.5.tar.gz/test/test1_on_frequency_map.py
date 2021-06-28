from bioezy import bzy

test = bzy.frequency_map("ATAGTGCTCAGA", 3)

print(test)

""" 
Ubuntu Terminal Output: 
(venv-bioezy-test) bash 5.0.17 at /home/sururkhan ~/Python Code(wsl)/bioezypkg/test
>>> py test1_on_frequency_map.py
{'ATA': 1, 'TAG': 1, 'AGT': 1, 'GTG': 1, 'TGC': 1, 'GCT': 1, 'CTC': 1, 'TCA': 1, 'CAG': 1, 'AGA': 1}
"""

# Utilizing only the modules found in bioezy_requirements.txt
