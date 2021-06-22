"""Low-level programming interface example
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import nanosurf

# We parse the  LogicalUnit_Shard file to have access to all the constants.
# Here we use the default version on the Q: server.
# make sure that the .h file is for the software version that you are currently
# using.
print("Connecting to Nanosurf Control software...")
spm = nanosurf.USPM("LogicalUnit_InterfaceShared.h")
spm.application.Visible = True

ll = spm.lowlevel

# After that we can read and write to LU attributes and triggers by name
lu_scan = ll.Scan()
print("Scan speed: " + str(lu_scan.time_per_line.value))

# change tip Voltage
tip_voltage_ramp = ll.RampGenerator(ll.RampGenerator.Instance.TIPVOLTAGE)

if tip_voltage_ramp.current_value.unit != 'V':
    print("The tip voltage ramp generator should output a voltage !")
    exit()

tip_voltage_ramp.current_value.value = 0.1       # 0.1[V]
tip_voltage_ramp.end_value_absolute.value = 5.0  # 5[V]
tip_voltage_ramp.moving_time.value = 2.0         # 2[s]

print("Start Tip Voltage ramp")
tip_voltage_ramp.start()

# wait until the ramp is done
while tip_voltage_ramp.is_moving:
    pass

# All objects decleared here have global scope. This means they continue to
# exist after the end of this program.
# The advantage of this is that they remain avaliable for executing commands
# with them in the Python Console/command line.
# A disadvantage is that the COM connection to the SPM control software is
# kept. This keeps the software running, possibly invisibly in the background.
# This in turn prevents (a new instance of) the control software to connect to
# the controller.
#
# The connetion can be cut in several ways, in order from bad to worse:
# 1.  Use `del()` to explicitly delete all the objects that use the COM
#     connection to the SPM control software
# 2.  Reset the Python kernel.
# 3.  Stop the control software using the Task manager.
#
# You can prevent putting objects in global scope by including your program in
# a function.
# In this case, the objects should be deleted when the function exits, and the
# connection to the control software is released.
print("End of demo")
