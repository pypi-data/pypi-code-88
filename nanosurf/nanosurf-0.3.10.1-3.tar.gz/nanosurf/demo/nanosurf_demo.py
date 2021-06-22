"""High-level programming interface example
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import matplotlib.pyplot as plt
import nanosurf

print("Connecting to Nanosurf Control software...")
spm = nanosurf.SPM() # Depending on the software version, this could be nanosurf.C3000(), or nanosurf.CoreAFM(), etc.

# make a shortcut to the application object, to make subsequent code shorter:
application = spm.application
application.Visible = True

spec = application.Spec
spec.Start()
while spec.IsMeasuring:
    pass

# TODO: define these constants in the library, this would make the demo much
# shorter, and still easy to understand:
FORWARD_SPEC = 0
BACKWARD_SPEC = 1
DEFLECTION_CHANNEL = 0
RAW_DATA = 0
PHYSICAL_VALUES = 1

# plot the result of the measurement:
plt.plot(spec.GetLine2(
    FORWARD_SPEC, DEFLECTION_CHANNEL, 0, RAW_DATA, PHYSICAL_VALUES), 'k')
plt.plot(spec.GetLine2(
    BACKWARD_SPEC, DEFLECTION_CHANNEL, 0, RAW_DATA, PHYSICAL_VALUES), 'k:')
