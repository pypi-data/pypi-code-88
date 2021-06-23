import pyvisa
from time import sleep

class ESP300:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.esp = self.rm.open_resource('ASRL/dev/ttyUSB1::INSTR')
        self.esp.baud_rate = 19200

    def moveAbs(self,axis, position):
        '''Position given in mm'''
        self.esp.write(f'{axis} PA {position}')
        
    def moveRel(self,axis,step):
        self.esp.write(f'{axis} PR {step}')
        
    def Home(self, axis):
        self.esp.write(f'{axis}OR')
        
    def Enable(self,axis):
        self.esp.write(f'{axis}MO')
        
    def GetPos(self, axis):
        return self.esp.query(f'{axis}TP')
        
    def GetVel(self, axis):
        return self.esp.query(f'{axis}TV')
        
    #Set stuff
    def SetVel(self, axis, velocity):
        return self.esp.write(f'{axis}TP{velocity}')
        
    def SetAcc(self, axis, acceleration):
         return self.esp.write(f'{axis}AC{acceleration}')


if __name__=='__main__':
    ESP300 = ESP300()

    
