# -*- coding: utf-8 -*-
#
#  
import logging

from langutil import C_OK, C_FAIL, C_ERROR, C_FILE_NOT_FOUND, LogStatus
from langutil.File import File

from pypos3d.pftk.PoserBasic import PoserToken, PoserConst, index, LowerLangName, LowerChanTypes
from pypos3d.pftk.StructuredAttribut import ValueOpDelta
from pypos3d.wftk.PoserFileParser import ParsingErrorException
#           exc_type, exc_value, exc_tb = sys.exc_info()
#           traceback.print_exception(exc_type, exc_value, exc_tb)



def parseOrNull(s):
  return float(s) if s else 0.0 

def nextWord(s):
  if not s:
    return None, None
  s = s.strip()
  i = 0
  while i<len(s) and (s[i].isalnum() or s[i]==':' or s[i]=='.'):
    i+=1
    
  return s[:i], s[i:].strip() if i<len(s) else ''



class FigurePart(LogStatus):
  ''' Parameter Class used to describe a part of a mechanical figure to create (for PyPos3dLO interface).
  Represent the data columns:
  Level  Name  Print Name  Geom File  Geom Group  Op  Translation  Rotation  Orientation  Center  Hidden  AddToMenu
  '''
  def __init__(self, partType='', level=-1, name=None, printName=None, geom=None, geomGroup=None, oplst=None, \
               trans=None, rot=None, orient=None, center=None, hidden=False, addToMenu=True):
    
    super(FigurePart, self).__init__() 

    self.partType = partType
    self.level = level
    self.name = name
    self.printName = printName
    self.geom = geom
    self.geomGroup = geomGroup
    self.oplst = oplst
    self.translation = trans
    self.rotation = rot
    self.orientation = orient
    self.center = center
    self.hidden = hidden
    self.addToMenu = addToMenu




class ChannelDescriptor(LogStatus):
  ''' New Internal Channel descriptor '''
  def __init__(self, no, actorName, chanTypeName=None, chanName=None, printName=None, initValue=None, minValue=-10000.0, maxValue=10000.0, \
               trackingScale = 0.1, lstAltFiles=None, lstOps=None, isHidden=False, groupName=None, altGeomNo=0 ):
    super(ChannelDescriptor, self).__init__() 
    
    self.no = no # Either a column or a line number    
    self.isSet = False
    self.act = None
    self.gt = None
    self.chanName = chanName
    self.printName = printName if printName else chanName
    
    ct = LowerChanTypes.get(chanTypeName.lower()) if chanTypeName else None
    self.chanType = ct if ct else PoserToken.E_valueParm
      
    self.actorName = actorName
    self.initValue = initValue
    self.min = minValue
    self.max = maxValue
    self.trackingScale = trackingScale
    self.isHidden = isHidden
    self.lstAltFiles = lstAltFiles if lstAltFiles else []
    self.groupName = groupName # GeomGroup Name to fetch for morph creation
    self.altGeomNo = altGeomNo # Alternate geometry Index of morph desination. 0 ==> Default Geometry
    self.lstOps = lstOps if lstOps else [ ]
    

  def checkLink(self, fig, dirPathList=''):
    
    p = self.actorName.find(':')
    if p<0:
      self.actorName = self.actorName + ':' + str(fig.getBodyIndex())

    
    self.act = fig.findActor(self.actorName)
    if not self.act:
      return self.status(PoserConst.C_ACTOR_NOTFOUND, "Unknown actor[{:s}] at column {:d}", self.actorName, self.no)
      
    # Check Channel Name (if the actor exists)
    self.gt = self.act.getChannel(self.chanName)
    if self.gt:
      # The channel already exists
      self.chanType = self.gt.getPoserType()
      logging.info("Channel [%s:%s] exists for actor[%s] at %d", self.chanName, self.chanType.token, self.actorName, self.no)

    # Check channel type : valueParm, visibility, geomChan
#     if self.chanType not in (PoserToken.E_valueParm, PoserToken.E_geomChan, PoserToken.E_targetGeom, PoserToken.E_visibility):
      # Incorrect channel type  ... But will work for 'upgrade' Not a failure anymore
      # Keep existing channel data
#       if self.gt:
#         self.min = self.gt.getMin()
#         self.max = self.gt.getMax()
#         self.trackingScale = self.gt.getTrackingScale()
#       logging.info("Other Channel Type [%s] for actor[%s] at column %d", self.chanType.token, self.actorName, self.no)

    try:
      if self.chanType==PoserToken.E_geomChan:
        self.initValue = 0
        self.min = 0
        # cd.max = 1 : To be computed later
        self.trackingScale = 1

        # Check alternate presence
        if self.lstAltFiles:
          lstFic = []
          # Check geometries filenames
          for altgeomName in self.lstAltFiles:
            
            altGeomFile1 = File.finder(altgeomName, imgdirpath=dirPathList, throwFNF=False, fileExt=('.obj', '.obz'), retFile=True)
            
            if altGeomFile1:
              lstFic.append(altGeomFile1)
            else:
              self.status(C_FILE_NOT_FOUND, "AlternateGeom File[{:s}] does not exist at column {:d}", altgeomName, self.no)

          self.max = len(lstFic)
          self.lstAltFiles = lstFic
        else:
          logging.info("No alternate geometries exists for actor[%s] at column %d", self.actorName, self.no)
          self.max = 0

      elif self.chanType==PoserToken.E_visibility:
        self.min = 0
        self.max = 1
        self.trackingScale = 1

      elif self.chanType==PoserToken.E_targetGeom: # Nothing to do with other channel types
        # Check morph file presence
        if self.lstAltFiles:
          # Check geometry filename
          altgeomName = self.lstAltFiles[0]
          altGeomFile1 = File.finder(altgeomName, imgdirpath=dirPathList, throwFNF=False, fileExt=('.obj', '.obz'), retFile=True)
          if altGeomFile1:
            self.lstAltFiles = [ altGeomFile1, ] # We keep the Alternate Geom List structure
            
            if not self.groupName:
              logging.info("No GroupName for morph creation in %s at %d", self.chanName, self.no)
          else:
            self.status(C_FILE_NOT_FOUND, "Morph Geometry File[{:s}] does not exist at column {:d}", altgeomName, self.no)
        else:
          self.max = 0
          self.status(C_FILE_NOT_FOUND, "No morph geometry exists for actor[{:s}] at column {:d}", self.actorName, self.no)
          
      elif self.chanType==PoserToken.E_shaderNodeParm: # check NodeInput Qualified name
        # Check syntax : MaterialName.NodeName.NodeInputName
        try:
          MaterialName, NodeName, NodeInputName = self.groupName.split('.')
          
          self.mat = fig.getMaterial(MaterialName)          
          if not self.mat:
            return self.status(PoserConst.C_MATERIAL_NOTFOUND, "Unknown material[{:s}] at column {:d}", MaterialName, self.no)
          
          self.node = self.mat.getShaderTree().getNodeByInternalName(NodeName)
          if not self.node:
            return self.status(PoserConst.C_NODE_NOTFOUND, "Unknown node[{:s}] in Material[{:s}] at column {:d}", NodeName, MaterialName, self.no)
          
          self.ni = self.node.getInputByInternalName(NodeInputName)
          if not self.ni:
            return self.status(PoserConst.C_NODE_NOTFOUND, "Unknown node input[{:s}] in Node[{:s}] of Material[{:s}] at column {:d}", \
                               NodeInputName, NodeName, MaterialName, self.no)
          
        except ValueError as ve:
          self.status(PoserConst.C_BAD_QUALNAME, "Incorrect NodeInput Qualified Name [{:s}] at column {:d}", self.groupName, self.no)
 
      #else: self.chanType  is PoserToken.E_valueParm or else

      self.analyseOps(fig)

    except ValueError as ve:
      self.status(C_ERROR, "Numeric Conversion error at column {:d} Avoid calculated cells:{:s}", self.no, str(ve))
      
    return self.ret
  
  

  def analyseOps(self, fig):    
    ''' Check operations descriptions and replace string list by
    a list of ValueOp 
    '''
    ret = C_OK
    if not self.lstOps:
      return ret
    
    ops, op = [], None
    figName, actName, gtName = None, None, None
    
    for opsstr in [ s for s in self.lstOps if s ]:
      
      if opsstr[0]=='?': # Optkeys are identifed by a question mark at the beginning of the cell
        # Current string contains an OptKey definition
        # We suppose that key / val are well organised
        qualifiedName, suitestr = nextWord(opsstr[1:])

        if not qualifiedName or not suitestr:
          self.worstStatus(C_FAIL, 'Syntax error in optkeys definition for {:s}:{:s} ==> (Missing Qualified Name or opt keys)', self.chanName, suitestr)
          continue

        ptind = qualifiedName.find('.')
        if ptind < 0:
          figName = "Figure " + str(fig.getBodyIndex())
          actName = self.act.getName()
          gtName = qualifiedName
        else:
          actName = qualifiedName[0:ptind]

          ptdp = qualifiedName.find(':')
          if (ptdp < 0):
            actName = actName + ':' + str(fig.getBodyIndex())

          figName = "Figure " + str(index(actName))
          gtName = qualifiedName[ptind + 1:]

        #op = ValueOpDelta(PoserToken.E_valueOpKey, figName, actName, gtName, 0.0)
        try:
          keys = eval(suitestr)
          op = ValueOpDelta(PoserToken.E_valueOpKey, figName, actName, gtName, keys=keys)
          
        except (SyntaxError, NameError) as e:
          ret = self.worstStatus(C_FAIL, 'Syntax error in optkeys definition for {:s}:{:s} ==> {:s}', self.chanName, suitestr, \
                                 e.text if isinstance(e, SyntaxError) else str(e))
          
      else: # Current tabChan[nolgn][nocol] is a simple expression
        try:
          op = ValueOpDelta(pfigure=fig, pactor=self.act, channelExpr=opsstr)
        except ParsingErrorException as e:
          ret = self.worstStatus(C_FAIL, 'Syntax error in operation definition for {:s}:{:s} ==> {:s}', self.chanName, opsstr, str(e))

      ops.append(op)
    #End For opsstr
      
    self.lstOps = ops
    return ret

class ChannelImportAnalysis: # implements PoserConst
  ''' Result of a XLS/XLSX/ODS file import for channel creation
   
   When using alternateGeom on Victoria4, Victoria4.2 with Poser7 :
   - The alternateGeom channel starts at 1!!! (even if it should not)
   - It's probably a Poser7 bug
  '''
  # Operation keywords : Op, OpKey.Dep, valueKey.key, valueKey.val
  C_CMD_OP = "Op"
  C_CMD_OPKEY_DEP = "OpKey.Dep"
  C_CMD_OPKEY_KEY = "valueKey.key"
  C_CMD_OPKEY_VAL = "valueKey.val"

  # public ChannelImportAnalysis(Figure f, String baseDir, String tabChannel[][])
  def __init__(self, f, baseDir, tabChannel):
    self.fig = f
    self.tabChan = tabChannel
    self.nblgn = len(self.tabChan)
    self.nbcol = len(self.tabChan[0])
    self.ts = [ [0]*self.nbcol for _ in range(0, self.nblgn) ]
    self.lstChan = [ ]
    self.baseDir = baseDir
  

  def checkVocab(self):
    ret = C_OK

    # Check col #0 key words
    self.ts[0][0] = C_OK if self.tabChan[0][0].lower()==LowerLangName[PoserToken.E_actor] else C_FAIL
    self.ts[1][0] = C_OK if self.tabChan[1][0].lower()=="channel" else C_FAIL
    self.ts[2][0] = C_OK if self.tabChan[2][0].lower()=="type" else C_FAIL
    self.ts[3][0] = C_OK if self.tabChan[3][0].lower()==LowerLangName[PoserToken.E_initValue] else C_FAIL
    self.ts[4][0] = C_OK if self.tabChan[4][0].lower()==LowerLangName[PoserToken.E_min] else C_FAIL
    self.ts[5][0] = C_OK if self.tabChan[5][0].lower()==LowerLangName[PoserToken.E_max] else C_FAIL
    self.ts[6][0] = C_OK if self.tabChan[6][0].lower()==LowerLangName[PoserToken.E_trackingScale] else C_FAIL
    self.ts[7][0] = C_OK if self.tabChan[7][0].lower()==LowerLangName[PoserToken.E_alternateGeom] else C_FAIL

    # Operation keywords : Op, OpKey.Dep, valueKey.key, valueKey.val
    for nolgn in range( 8, self.nblgn):
      val = self.tabChan[nolgn][0]

      if val:
        if (val.lower()==self.C_CMD_OP.lower()) and (val.lower()==self.C_CMD_OPKEY_DEP.lower()) \
            and (val.lower()==self.C_CMD_OPKEY_KEY.lower()) and (val.lower()==self.C_CMD_OPKEY_VAL.lower()):
          logging.info("Unknown key word[" + self.tabChan[nolgn][0] + "] at line :" + nolgn)
          self.ts[nolgn][0] = C_FAIL
      else:
        logging.info("Missing Ligne Title[] at line :%d", nolgn)
        self.ts[nolgn][0] = C_FAIL

    return ret

  def checkColumns(self):
    cd = None
    ret = C_OK

    for nocol in range(1, self.nbcol):
      # Check actor presence
      if self.tabChan[0][nocol].endswith(".*"):
        actorBaseName = self.tabChan[0][nocol][0:len(self.tabChan[0][nocol]) - 2]

        # Search for actorBaseName descendant
        lstDescName = self.fig.getDescendant(actorBaseName)

        for i in range(0,  len(lstDescName)): # Avoid first name!!
          cd = self.create(lstDescName[i], nocol)
          cd.isSet = True
          self.lstChan.append(cd)
      else:
        actorName = self.tabChan[0][nocol] + ":" + str(self.fig.getBodyIndex())
        cd = self.create(actorName, nocol)
        self.lstChan.append(cd)

    return ret

  def create(self, actorName, nocol):
    # Convert the 'column' of operations into the new list format
    lstOps, nolgn = [], 8
    while nolgn < self.nblgn:
      if (self.ts[nolgn][0] == C_OK) and self.tabChan[nolgn][0] and self.tabChan[nolgn][nocol]:
        if self.tabChan[nolgn][0].lower()==self.C_CMD_OP.lower():
          # Current tabChan[nolgn][nocol] is a simple expression
          lstOps.append(self.tabChan[nolgn][nocol])
        else:
          # Current tabChan identifies the beginning of en OptKey definition
          # We suppose that key / val are well organised
          qualifiedName = self.tabChan[nolgn][nocol]
          nolgn+=1

          strkey = ''

          while (nolgn < self.nblgn - 1) and self.tabChan[nolgn][0].lower()==self.C_CMD_OPKEY_KEY.lower():
            if self.tabChan[nolgn][nocol]:
              strkey = strkey + '(' + self.tabChan[nolgn][nocol] + ',' + self.tabChan[nolgn + 1][nocol] + '),'
            nolgn += 2

          lstOps.append('? {:s} ({:s})'.format(qualifiedName, strkey))
          nolgn-=1 # Push Back one line, because the optkeys may be followed by others operations

      nolgn+=1
      #End While

    #  ChannelDescriptor(no, actorName, chanTypeName, chanName,    printName,  initValue, minValue, maxValue. trackingScale, lstAltFiles, lstOps, groupName, altGeom
    cd = ChannelDescriptor(nocol, actorName, chanTypeName=self.tabChan[2][nocol], chanName=self.tabChan[1][nocol], \
          initValue = parseOrNull(self.tabChan[3][nocol]), \
          minValue = parseOrNull(self.tabChan[4][nocol]), \
          maxValue = parseOrNull(self.tabChan[5][nocol]), \
          trackingScale = parseOrNull(self.tabChan[6][nocol]), \
          lstAltFiles = self.tabChan[7][nocol].split("\n") if self.tabChan[7][nocol] else None, \
          lstOps = lstOps)

    return cd


  def getWorstStatus(self, ligne=None):
    return min(self.ts[ligne]) if ligne else min( v for lgn in self.ts for v in lgn)

