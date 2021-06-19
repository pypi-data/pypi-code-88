#===============
# SETUP
#===============

from helipad import Helipad, MultiLevel, Agent
from math import floor
from random import uniform, choice

heli = Helipad()
heli.name = 'Illicit Supply Chains'
heli.order = 'random'

heli.addPrimitive('firm', MultiLevel, dflt=20, priority=1)
heli.removePrimitive('agent')
mapPlot = heli.spatial(x=5, y=1, wrap=False)
mapPlot.config({
	'patchProperty': 'x',
	'patchAspect': 2
})

#Initialize submodels
@heli.hook
def firmInit(firm, model):
	firm.param('num_agent', 20)

def firmsize(self): return len(self.agents['agent'])*5
MultiLevel.size = property(firmsize)
mapPlot.config('agentSize', 'size')

#===============
# BEHAVIOR
#===============

heli.param('num_firm', 20)

@heli.hook
def firmStep(firm, model, stage):
	if len(firm.agents['agent']):
		choice(firm.agents['agent']).transfer(choice(list(firm.patch.agentsOn))) #One agent moves to a random firm on the same patch

@heli.hook
def modelPostSetup(model):
	for n,a in enumerate(model.agents['firm']):
		stage = floor(n/4)
		a.moveTo(uniform(stage-0.4, stage+0.4), uniform(-0.5, 0.5))
	
	#Create links after all firms have been assigned to a stage
	for f in model.agents['firm']:
		if f.patch.x > 0: f.newEdge(choice(list(f.patch.left.agentsOn)))

#===============
# DATA AND VISUALIZATION
#===============


#===============
# LAUNCH THE GUI
#===============

heli.launchCpanel()