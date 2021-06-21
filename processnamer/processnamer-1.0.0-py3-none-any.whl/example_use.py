import sys
from time import sleep

#Import the lib:
from processnamer import processGame
#Create object:
prg = processGame()

#Display information (stdout or print will cause brokenpipe error):
sys.stderr.write("I am " + prg.prcname + ", and i have pid " + str(prg.pid) + "\n")

#Gather information:                  #Gets the name, but it can do this foe any pid
info = prg.getName(prg.pid)           #Get info for pid of this process
#Display information:
sys.stderr.write("I am " + info + ", and i have pid " + str(prg.pid) + "\n")


if prg.prcname == "python":           #If this is the original process

    #Restart this as process imcool:
    prg.nameStart("imcool",prg.script)
    sleep(2)
    prg.nameStop("imcool")            #Stop the second process

else:
    sleep(10)                         #Second process waits so that it can be stopped
