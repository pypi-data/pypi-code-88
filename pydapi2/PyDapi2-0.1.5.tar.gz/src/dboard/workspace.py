'''
Created on 15 mars 2021

@author: fv
'''
import dboard


class BaseWorkspace(dboard.BaseBoardItem):
    '''Base class for board's Workspace.
    
    :param BaseBoard board: The board.
    :param str name: The workspace name.
    :param int par: The workspace number = PAR value used to activate the workspace
    :param int pcr: The configuartion code  
    '''
        
    def __init__(self, board, name=None, par=None, pcr=None):
        super().__init__(board, name)
        self.par = par
        self._pcr = pcr
        #TODO: self._wca = MemoryWCA(self)        

    def __str__(self):
        return self.name
    
    def isFunctional(self):
        '''Check if workspace is functional.
        
        :return: True, if workspace is functional ; False otherwise.
        :rtype bool
        '''
        if self.board.regs.ctr.isUndefined():
            self.board.getRegisters('ctr')
        return self.board.regs.ctr.value != 0x0000       

    @property
    def standby(self):
        return False
    @property
    def active(self):
        return self is self._board.getWorkspace()      
    @property
    def pcr(self):
        return self._pcr
    @property
    def wca(self):
        return self._wca
    
class Workspace(BaseWorkspace):
    '''Class for a functional Workspace.
    
    :param BaseBoard board: The board. 
    :param str name: The workspace name.
    :param int par: The workspace number = PAR value used to activate the workspace
    :param int pcr: The configuartion code      
    '''
    
    def __init__(self, board, name=None, par=None, pcr=None):
        super().__init__(board, name, par, pcr)
        self.log.debug('PAR={0:d}, PCR={1:04x}'.format(par, pcr.value))
        self.cfg = [0]*4

        

            
        #TODO: for i in range(board.wcaCount): 
            # self.wca.append( MemoryWC(i, self.wca)  )
            #self.eeprom.wca_list.append(self.wca)        
            
            
        

    
#     def set_captor_mode(self, mode):
#         self._pcr['CAPTOR'].set(mode.value)
        #
    # def get_captor_mode(self):
        # return dboard.Sensors(self._pcr['CAPTOR'].value)
        #
#     def set_reference_mode(self, mode):
#         self._pcr['REFERENCE'].set(mode.value)
        
    # def get_reference_mode(self):
        # return dboard.SpeedRequestMode(self._pcr['REFERENCE'].value)
    
    def get_temp_running(self):
        return self._pcr['TMP_RUN'].value
    def get_temp_idle(self):
        return self._pcr['TMP_IDLE'].value
        

    @property
    def ppa(self):
        return self._pcr.value & 0x000f
     
    @property
    def rdt(self):
        return (self._pcr.value & 0x0f00) >> 8
    
    @property
    def idt(self):
        return (self._pcr.value & 0xf000) >> 12
    
    @property
    def description(self):
        return 'Workspace #{par:d}\nIdle temperature multiplicator: {idt:d}\nRun temperature multiplicator: {rdt:d}'.format(par=self.par,idt=self.idt, rdt=self.rdt)

    
         
class StandbyWorkspace(BaseWorkspace):
    '''Class for the *standby" workspace
    
    :param BaseBoard board: The board. 
    '''        
     
    def __init__(self, board):
        super().__init__(board, 'Standby', 0, None)
        self.log.debug('Construct')

    def isFunctional(self):
        '''Alwayse return False. This workspace is never functional.'''
        return False
     
    @property
    def standby(self):
        return True
    @property
    def description(self):
        return 'Standby'    
    
class WorkspacesContainer(dboard.BaseBoardItem):
    def __init__(self, board, name=None):
        super().__init__(board, name)
        self._items = []
        
    def __getitem__(self, index):
        self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def getByPAR(self, par):
        for w in self._items:
            if w.par == par:
                return w
    
    def clear(self):
        self._items.clear()
    
    def append(self, item):
        self._items.append(item)
        
    @property
    def count(self):
        return len(self._items)



        
        