class AllPawns: 
  def __init__(self,Start,End,Board):
    self.Start=Start
    self.End=End
    self.Board=Board
    
  def PawnsWhiteMovement(self):

    #Attack
    if (self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]+1 and (self.Board[(self.End)] in Pawns['Black'])) or (self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]-1 and (self.Board[(self.End)] in Pawns['Black'])):
      if self.End[0]==0:
        Change=input('What piece to you want to change this pawn to.\n Type q to change the pawn into a Queen \n b to change the pawn into a Bishop \n e to change the pawn into a Elephant \n h to change the pawn into a Horse\n')
        if Change in 'qbeh':
          return Change.upper()
      else:
        return True

    #Starting Movement
    elif self.Start[0]==6:
      if self.End[0]>3 and self.End[0]<6:
        if self.End[1]==self.Start[1]:
          return True   

    #Movement
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]:
      if self.End[0]==0:
        Change=input('What piece to you want to change this pawn to.\n Type q to change the pawn into a Queen \n b to change the pawn into a Bishop \n e to change the pawn into a Elephant \n h to change the pawn into a Horse\n')
        if Change in 'qbeh':
          return Change.upper()
      elif self.Board[(self.End)]=='   ':
        return True
    else:
      return False

  def PawnsBlackMovement(self):

    #Attack
    if (self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]-1 and (self.Board[(self.End)] in Pawns['White'])) or (self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]+1 and (self.Board[(self.End)] in Pawns['White'])):
      if self.End[0]==7:
        Change=input('What piece to you want to change this pawn to.\n Type q to change the pawn into a Queen \n b to change the pawn into a Bishop \n e to change the pawn into a Elephant \n h to change the pawn into a Horse\n')
        if Change=='q' or Change=='b' or Change=='e' or Change=='h':
          return Change.upper()
      else:
        return True

    #Starting Movement
    elif self.Start[0]==1:
      if self.End[0]>1 and self.End[0]<4:
        if self.End[1]==self.Start[1]:
          return True   

    #Movement 
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]:
      if self.End[0]==7:
        Change=input('What piece to you want to change this pawn to.\n Type q to change the pawn into a Queen \n b to change the pawn into a Bishop \n e to change the pawn into a Elephant \n h to change the pawn into a Horse\n')
        if Change=='q' or Change=='b' or Change=='e' or Change=='h':
          return Change.upper()
      elif self.Board[(self.End)]=='   ':
        return True
    else:
      return False

   
  def EleBlackMovement(self):
    #Right
    if self.Start[0]==self.End[0] and self.Start[1]-self.End[1]<0:
      for x in range(self.Start[1]+1,self.End[1]):
        if (self.Board[(self.Start[0],x)]) in Pawns['White'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]+1)]) in Pawns['White'] or self.Board[(self.Start[0],self.Start[1]+1)]=='   ':
        return True
      else:
        return False

    #Left
    elif self.Start[0]==self.End[0] and self.Start[1]-self.End[1]>0:
      for x in range(self.Start[1]-1,self.End[1],-1):
        if (self.Board[(self.Start[0],x)]) in Pawns['White'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]-1)]) in Pawns['White'] or self.Board[(self.Start[0],self.Start[1]-1)]=='   ':
        return True
      else:
        return False 

    #Down  
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]<0:
      for x in range(self.Start[0]+1,self.End[0]):
        if (self.Board[(x,self.Start[1])]) in Pawns['White'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1])]) in Pawns['White'] or self.Board[(self.Start[0]+1,self.Start[1])]=='   ':
        return True
      else:
        return False
    
    #Up
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(self.Start[0]-1,self.End[0],-1):
        if (self.Board[(x,self.Start[1])]) in Pawns['White'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1])]) in Pawns['White'] or self.Board[(self.Start[0]-1,self.Start[1])]=='   ':
        return True
      else:
        return False
    else:
      return False  


  def EleWhiteMovement(self):
    #Right
    if self.Start[0]==self.End[0] and self.Start[1]-self.End[1]<0:
      for x in range(self.Start[1]+1,self.End[1]):
        if (self.Board[(self.Start[0],x)]) in Pawns['Black'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]+1)]) in Pawns['Black'] or self.Board[(self.Start[0],self.Start[1]+1)]=='   ':
        return True
      else:
        return False

    #Left
    elif self.Start[0]==self.End[0] and self.Start[1]-self.End[1]>0:
      for x in range(self.Start[1]-1,self.End[1],-1):
        if (self.Board[(self.Start[0],x)]) in Pawns['Black'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]-1)]) in Pawns['Black'] or self.Board[(self.Start[0],self.Start[1]-1)]=='   ':
        return True
      else:
        return False 

    #Down  
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]<0:
      for x in range(self.Start[0]+1,self.End[0]):
        if (self.Board[(x,self.Start[1])]) in Pawns['Black'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1])]) in Pawns['Black'] or self.Board[(self.Start[0]+1,self.Start[1])]=='   ':
        return True
      else:
        return False
    
    #Up
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(self.Start[0]-1,self.End[0],-1):
        if (self.Board[(x,self.Start[1])]) in Pawns['Black'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1])]) in Pawns['Black'] or self.Board[(self.Start[0]-1,self.Start[1])]=='   ':
        return True
      else:
        return False
    else:
      return False  

  def BishWhiteMovement(self):
    #NorthEast Movement
    if self.Start[0]-self.End[0]==self.End[1]-self.Start[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]+x)]) in Pawns['Black'] or self.Board[(self.Start[0]-x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1]+1)]) in Pawns['Black'] or self.Board[(self.Start[0]-1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
    
    #NorthWest Movement
    elif self.Start[0]-self.End[0]==self.Start[1]-self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]-x)]) in Pawns['Black'] or self.Board[(self.Start[0]-x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1]-1)]) in Pawns['Black'] or self.Board[(self.Start[0]-1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthWest Movement
    elif self.End[0]-self.Start[0]==self.Start[1]-self.End[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]-x)]) in Pawns['Black'] or self.Board[(self.Start[0]+x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]-1)]) in Pawns['Black'] or self.Board[(self.Start[0]+1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthEast Movement
    elif self.End[0]-self.Start[0]==self.End[1]-self.Start[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]+x)]) in Pawns['Black'] or self.Board[(self.Start[0]+x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]+1)]) in Pawns['Black'] or self.Board[(self.Start[0]+1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
    else:
      return False  
  
  def BishBlackMovement(self):
    #NorthEast Movement
    if self.Start[0]-self.End[0]==self.End[1]-self.Start[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]+x)]) in Pawns['White'] or self.Board[(self.Start[0]-x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if self.Board[(self.Start[0]-1,self.Start[1]+1)] in Pawns['White'] or self.Board[(self.Start[0]-1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
      
    
    #NorthWest Movement  
    elif self.Start[0]-self.End[0]==self.Start[1]-self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]-x)]) in Pawns['White'] or self.Board[(self.Start[0]-x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1]-1)]) in Pawns['White'] or self.Board[(self.Start[0]-1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthWest Movement 
    elif self.End[0]-self.Start[0]==self.Start[1]-self.End[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]-x)]) in Pawns['White'] or self.Board[(self.Start[0]+x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]-1)]) in Pawns['White'] or self.Board[(self.Start[0]+1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthEast Movement 
    elif self.End[0]-self.Start[0]==self.End[1]-self.Start[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]+x)]) in Pawns['White'] or self.Board[(self.Start[0]+x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]+1)]) in Pawns['White'] or self.Board[(self.Start[0]+1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
    else:
      return False  

  def QuBlackMovement(self):
    #NorthEast Movement
    if self.Start[0]-self.End[0]==self.End[1]-self.Start[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]+x)]) in Pawns['White'] or self.Board[(self.Start[0]-x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if self.Board[(self.Start[0]-1,self.Start[1]+1)] in Pawns['White'] or self.Board[(self.Start[0]-1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
      
    
    #NorthWest Movement  
    elif self.Start[0]-self.End[0]==self.Start[1]-self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]-x)]) in Pawns['White'] or self.Board[(self.Start[0]-x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1]-1)]) in Pawns['White'] or self.Board[(self.Start[0]-1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthWest Movement 
    elif self.End[0]-self.Start[0]==self.Start[1]-self.End[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]-x)]) in Pawns['White'] or self.Board[(self.Start[0]+x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]-1)]) in Pawns['White'] or self.Board[(self.Start[0]+1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthEast Movement 
    elif self.End[0]-self.Start[0]==self.End[1]-self.Start[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]+x)]) in Pawns['White'] or self.Board[(self.Start[0]+x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]+1)]) in Pawns['White'] or self.Board[(self.Start[0]+1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
    
    #Right
    if self.Start[0]==self.End[0] and self.Start[1]-self.End[1]<0:
      for x in range(self.Start[1]+1,self.End[1]):
        if (self.Board[(self.Start[0],x)]) in Pawns['White'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]+1)]) in Pawns['White'] or self.Board[(self.Start[0],self.Start[1]+1)]=='   ':
        return True
      else:
        return False

    #Left
    elif self.Start[0]==self.End[0] and self.Start[1]-self.End[1]>0:
      for x in range(self.Start[1]-1,self.End[1],-1):
        if (self.Board[(self.Start[0],x)]) in Pawns['White'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]-1)]) in Pawns['White'] or self.Board[(self.Start[0],self.Start[1]-1)]=='   ':
        return True
      else:
        return False 

    #Down  
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]<0:
      for x in range(self.Start[0]+1,self.End[0]):
        if (self.Board[(x,self.Start[1])]) in Pawns['White'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1])]) in Pawns['White'] or self.Board[(self.Start[0]+1,self.Start[1])]=='   ':
        return True
      else:
        return False
    
    #Up
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(self.Start[0]-1,self.End[0],-1):
        if (self.Board[(x,self.Start[1])]) in Pawns['White'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1])]) in Pawns['White'] or self.Board[(self.Start[0]-1,self.Start[1])]=='   ':
        return True
      else:
        return False
    else:
      return False 

  def QuWhiteMovement(self):
    #NorthEast Movement
    if self.Start[0]-self.End[0]==self.End[1]-self.Start[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]+x)]) in Pawns['Black'] or self.Board[(self.Start[0]-x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1]+1)]) in Pawns['Black'] or self.Board[(self.Start[0]-1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
    
    #NorthWest Movement
    elif self.Start[0]-self.End[0]==self.Start[1]-self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(1,self.Start[0]-self.End[0]):
        if (self.Board[(self.Start[0]-x,self.Start[1]-x)]) in Pawns['Black'] or self.Board[(self.Start[0]-x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1]-1)]) in Pawns['Black'] or self.Board[(self.Start[0]-1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthWest Movement
    elif self.End[0]-self.Start[0]==self.Start[1]-self.End[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]-x)]) in Pawns['Black'] or self.Board[(self.Start[0]+x,self.Start[1]-x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]-1)]) in Pawns['Black'] or self.Board[(self.Start[0]+1,self.Start[1]-1)]=='   ':
        return True
      else:
        return False

    #SouthEast Movement
    elif self.End[0]-self.Start[0]==self.End[1]-self.Start[1] and self.End[0]-self.Start[0]>0:
      for x in range(1,self.End[0]-self.Start[0]):
        if (self.Board[(self.Start[0]+x,self.Start[1]+x)]) in Pawns['Black'] or self.Board[(self.Start[0]+x,self.Start[1]+x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1]+1)]) in Pawns['Black'] or self.Board[(self.Start[0]+1,self.Start[1]+1)]=='   ':
        return True
      else:
        return False
    
    #Right
    if self.Start[0]==self.End[0] and self.Start[1]-self.End[1]<0:
      for x in range(self.Start[1]+1,self.End[1]):
        if (self.Board[(self.Start[0],x)]) in Pawns['Black'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]+1)]) in Pawns['Black'] or self.Board[(self.Start[0],self.Start[1]+1)]=='   ':
        return True
      else:
        return False

    #Left
    elif self.Start[0]==self.End[0] and self.Start[1]-self.End[1]>0:
      for x in range(self.Start[1]-1,self.End[1],-1):
        if (self.Board[(self.Start[0],x)]) in Pawns['Black'] or self.Board[(self.Start[0],x)]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0],self.Start[1]-1)]) in Pawns['Black'] or self.Board[(self.Start[0],self.Start[1]-1)]=='   ':
        return True
      else:
        return False 

    #Down  
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]<0:
      for x in range(self.Start[0]+1,self.End[0]):
        if (self.Board[(x,self.Start[1])]) in Pawns['Black'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]+1,self.Start[1])]) in Pawns['Black'] or self.Board[(self.Start[0]+1,self.Start[1])]=='   ':
        return True
      else:
        return False
    
    #Up
    elif self.Start[1]==self.End[1] and self.Start[0]-self.End[0]>0:
      for x in range(self.Start[0]-1,self.End[0],-1):
        if (self.Board[(x,self.Start[1])]) in Pawns['Black'] or self.Board[(x,self.Start[1])]=='   ':
          return True
        else:
          return False
      if (self.Board[(self.Start[0]-1,self.Start[1])]) in Pawns['Black'] or self.Board[(self.Start[0]-1,self.Start[1])]=='   ':
        return True
      else:
        return False
    else:
      return False 

  def KingWhiteMovement(self):
    #NorthEast
    if self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #NorthWest
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False

    #SouthEast
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #SouthWest
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Up
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Down
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Right
    elif self.End[0]==self.Start[0] and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Left
    elif self.End[0]==self.Start[0] and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    else:
      return False
  
  def KingBlackMovement(self):
    #NorthEast
    if self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #NorthWest
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False

    #SouthEast
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #SouthWest
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Up
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Down
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Right
    elif self.End[0]==self.Start[0] and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    #Left
    elif self.End[0]==self.Start[0] and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      else:
        return False
    
    else:
      return False

  def HorseWhiteMovement(self):
    #
    if self.End[0]==self.Start[0]+2 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'  
    
    #
    elif self.End[0]==self.Start[0]+2 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-2 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-2 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]+2:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]+2:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]-2:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]-2:
      if self.Board[self.End] in Pawns['Black'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['White']:
        return False
      else:
          return 'the logic for this code is wrong'
    
    else:
      return False

  def HorseBlackMovement(self):
    #
    if self.End[0]==self.Start[0]+2 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]+2 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-2 and self.End[1]==self.Start[1]+1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-2 and self.End[1]==self.Start[1]-1:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]+2:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]+2:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]-1 and self.End[1]==self.Start[1]-2:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    #
    elif self.End[0]==self.Start[0]+1 and self.End[1]==self.Start[1]-2:
      if self.Board[self.End] in Pawns['White'] or self.Board[self.End]=='   ':
        return True
      elif self.Board[self.End] in Pawns['Black']:
        return False
      else:
        return 'the logic for this code is wrong'
    
    else:
      return False

def ChessBoard():
  #Printing the game board
  SubBoard={(0,0):'   ',(0,1):'   ',(0,2):'   ',(0,3):'   ',(0,4):'   ',(0,5):'   ',(0,6):'   ',(0,7):'   ',
            (1,0):'   ',(1,1):'   ',(1,2):'   ',(1,3):'   ',(1,4):'   ',(1,5):'   ',(1,6):'   ',(1,7):'   ',
            (2,0):'   ',(2,1):'   ',(2,2):'   ',(2,3):'   ',(2,4):'   ',(2,5):'   ',(2,6):'   ',(2,7):'   ',
            (3,0):'   ',(3,1):'   ',(3,2):'   ',(3,3):'   ',(3,4):'   ',(3,5):'   ',(3,6):'   ',(3,7):'   ',
            (4,0):'   ',(4,1):'   ',(4,2):'   ',(4,3):'   ',(4,4):'   ',(4,5):'   ',(4,6):'   ',(4,7):'   ',
            (5,0):'   ',(5,1):'   ',(5,2):'   ',(5,3):'   ',(5,4):'   ',(5,5):'   ',(5,6):'   ',(5,7):'   ',
            (6,0):'   ',(6,1):'   ',(6,2):'   ',(6,3):'   ',(6,4):'   ',(6,5):'   ',(6,6):'   ',(6,7):'   ',
            (7,0):'   ',(7,1):'   ',(7,2):'   ',(7,3):'   ',(7,4):'   ',(7,5):'   ',(7,6):'   ',(7,7):'   '}
  def printBoard(board):
    print(' '+'|'+' 0 '+'|'+' 1 '+'|'+' 2 '+'|'+' 3 '+'|'+' 4 '+'|'+' 5 '+'|'+' 6 '+'|'+' 7 '+'|'),
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|'),
    print('0'+'|'+board[(0,0)]+'|'+board[(0,1)]+'|'+board[(0,2)]+'|'+board[(0,3)]+'|'+board[(0,4)]+'|'+board[(0,5)]+'|'+board[(0,6)]+'|'+board[(0,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('1'+'|'+board[(1,0)]+'|'+board[(1,1)]+'|'+board[(1,2)]+'|'+board[(1,3)]+'|'+board[(1,4)]+'|'+board[(1,5)]+'|'+board[(1,6)]+'|'+board[(1,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('2'+'|'+board[(2,0)]+'|'+board[(2,1)]+'|'+board[(2,2)]+'|'+board[(2,3)]+'|'+board[(2,4)]+'|'+board[(2,5)]+'|'+board[(2,6)]+'|'+board[(2,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('3'+'|'+board[(3,0)]+'|'+board[(3,1)]+'|'+board[(3,2)]+'|'+board[(3,3)]+'|'+board[(3,4)]+'|'+board[(3,5)]+'|'+board[(3,6)]+'|'+board[(3,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('4'+'|'+board[(4,0)]+'|'+board[(4,1)]+'|'+board[(4,2)]+'|'+board[(4,3)]+'|'+board[(4,4)]+'|'+board[(4,5)]+'|'+board[(4,6)]+'|'+board[(4,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('5'+'|'+board[(5,0)]+'|'+board[(5,1)]+'|'+board[(5,2)]+'|'+board[(5,3)]+'|'+board[(5,4)]+'|'+board[(5,5)]+'|'+board[(5,6)]+'|'+board[(5,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('6'+'|'+board[(6,0)]+'|'+board[(6,1)]+'|'+board[(6,2)]+'|'+board[(6,3)]+'|'+board[(6,4)]+'|'+board[(6,5)]+'|'+board[(6,6)]+'|'+board[(6,7)]+'|')
    print(' '+'|'+'---+---+---+---+---+---+---+---'+'|')
    print('7'+'|'+board[(7,0)]+'|'+board[(7,1)]+'|'+board[(7,2)]+'|'+board[(7,3)]+'|'+board[(7,4)]+'|'+board[(7,5)]+'|'+board[(7,6)]+'|'+board[(7,7)]+'|')

  #Extra helpful functions
  Pawns={'Black':{'BE0':'BE0','BH0':'BH0','BB0':'BB0','BQ0':'BQ0','BK0':'BK0','BB1':'BB1','BH1':'BH1','BE1':'BE1','BP2':'BP2','BP3':'BP3','BP4':'BP4','BP5':'BP5',
        'BP6':'BP6','BP7':'BP7','BP8':'BP8','BP9':'BP9','BE2':'BE2','BE3':'BE3','BE4':'BE4','BE5':'BE5','BE6':'BE6','BE7':'BE7','BE8':'BE8','BE9':'BE9',
        'BH2':'BH2','BH3':'BH3','BH4':'BH4','BH5':'BH5','BH6':'BH6','BH7':'BH7','BH8':'BH8','BH9':'BH9','BB2':'BB2','BB3':'BB3','BB4':'BB4','BB5':'BB5',
        'BB6':'BB6','BB7':'BB7','BB8':'BB8','BB9':'BB9'},
        'White':{'WE0':'WE0','WH0':'WH0','WB0':'WB0','WQ0':'WQ0','WK0':'WK0','WB1':'WB1','WH1':'WH1','WE1':'WE1','WP2':'WP2','WP3':'WP3','WP4':'WP4','WP5':'WP5',
        'WP6':'WP6','WP7':'WP7','WP8':'WP8','WP9':'WP9','WE2':'WE2','WE3':'WE3','WE4':'WE4','WE5':'WE5','WE6':'WE6','WE7':'WE7','WE8':'WE8','WE9':'WE9',
        'WH2':'WH2','WH3':'WH3','WH4':'WH4','WH5':'WH5','WH6':'WH6','WH7':'WH7','WH8':'WH8','WH9':'WH9','WB2':'WB2','WB3':'WB3','WB4':'WB4','WB5':'WB5',
        'WB6':'WB6','WB7':'WB7','WB8':'WB8','WB9':'WB9'}}


  def SetBoard():
    SubBoard[(0,0)]='BE0' 
    SubBoard[(0,1)]='BH0'
    SubBoard[(0,2)]='BB0'
    SubBoard[(0,3)]='BQ0'
    SubBoard[(0,4)]='BK0'
    SubBoard[(0,5)]='BB1'
    SubBoard[(0,6)]='BH1' 
    SubBoard[(0,7)]='BE1' 
    SubBoard[(1,0)]='BP2' 
    SubBoard[(1,1)]='BP3' 
    SubBoard[(1,2)]='BP4' 
    SubBoard[(1,3)]='BP5' 
    SubBoard[(1,4)]='BP6' 
    SubBoard[(1,5)]='BP7' 
    SubBoard[(1,6)]='BP8'
    SubBoard[(1,7)]='BP9'
    SubBoard[(6,0)]='WP2'
    SubBoard[(6,1)]='WP3'
    SubBoard[(6,2)]='WP4'
    SubBoard[(6,3)]='WP5' 
    SubBoard[(6,4)]='WP6'
    SubBoard[(6,5)]='WP7'
    SubBoard[(6,6)]='WP8'
    SubBoard[(6,7)]='WP9'
    SubBoard[(7,0)]='WE0'
    SubBoard[(7,1)]='WH0'
    SubBoard[(7,2)]='WB0'
    SubBoard[(7,3)]='WQ0'
    SubBoard[(7,4)]='WK0'
    SubBoard[(7,5)]='WB1'
    SubBoard[(7,6)]='WH1'
    SubBoard[(7,7)]='WE1'

  def ClearBoard():
    for r in range(8):
      for c in range(8):
        SubBoard[(r,c)]='   '
    
  #Starting the game
  game=input('Do you want to start the game Type Y or N')
  if game.lower() =='y':
    ClearBoard()
    SetBoard()
    printBoard(SubBoard)

  #Continuing the game
  turn='Black'
  while Pawns['White']['WK0'] in SubBoard.values() and Pawns['Black']['BK0'] in SubBoard.values():
    if turn=='Black':
      turn='White'
    else:
      turn='Black'
    Check=False
    while Check==False or Check==None:
      Start=input('Its your turn '+turn+',What is your starting position')
      Start=tuple([int(x) for x in Start.split(',')]) #To convert multiple items in a list to certain thing at once
      
      End=input('What is your end position')
      End=tuple([int(x) for x in End.split(',')])
      
      a=AllPawns((Start),(End),SubBoard)
      
      if turn=='White' and SubBoard[Start] in Pawns['White'] and (SubBoard[Start])[1]=='E':
        Check=a.EleWhiteMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='Black' and SubBoard[Start] in Pawns['Black'] and (SubBoard[Start])[1]=='E':
        Check=a.EleBlackMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='White' and SubBoard[Start] in Pawns['White'] and (SubBoard[Start])[1]=='B':
        Check=a.BishWhiteMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='Black' and SubBoard[Start] in Pawns['Black'] and (SubBoard[Start])[1]=='B':
        Check=a.BishBlackMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='White' and SubBoard[Start] in Pawns['White'] and (SubBoard[Start])[1]=='Q':
        Check=a.QuWhiteMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='Black' and SubBoard[Start] in Pawns['Black'] and (SubBoard[Start])[1]=='Q':
        Check=a.QuBlackMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='White' and SubBoard[Start] in Pawns['White'] and (SubBoard[Start])[1]=='K':
        Check=a.KingWhiteMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='Black' and SubBoard[Start] in Pawns['Black'] and (SubBoard[Start])[1]=='K':
        Check=a.KingBlackMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='White' and SubBoard[Start] in Pawns['White'] and (SubBoard[Start])[1]=='H':
        Check=a.HorseWhiteMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='Black' and SubBoard[Start] in Pawns['Black'] and (SubBoard[Start])[1]=='H':
        Check=a.HorseBlackMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        else:
          print(Check)
      elif turn=='White' and SubBoard[Start] in Pawns['White'] and (SubBoard[Start])[1]=='P':
        Check=a.PawnsWhiteMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        elif Check=='Q' or Check=='B' or Check=='E' or Check=='H':
          Pawns['White'][SubBoard[Start]]=Pawns['White'][SubBoard[Start]][0]+Check+Pawns['White'][SubBoard[Start]][2]
          SubBoard[End]=Pawns['White'][SubBoard[Start]]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        else:
          print(Check)
      elif turn=='Black' and SubBoard[Start] in Pawns['Black'] and (SubBoard[Start])[1]=='P':
        Check=a.PawnsBlackMovement()
        if Check==True:
          SubBoard[End]=SubBoard[Start]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        elif Check==False:
          print('You there is a piece block your path or this piece cannot move in this direction try again')
          pass
        elif Check=='Q' or Check=='B' or Check=='E' or Check=='H':
          Pawns['Black'][SubBoard[Start]]=Pawns['Black'][SubBoard[Start]][0]+Check+Pawns['Black'][SubBoard[Start]][2]
          SubBoard[End]=Pawns['Black'][SubBoard[Start]]
          SubBoard[Start]='   '
          printBoard(SubBoard)
        else:
          print(Check)
      else:
        print('You have written starting co-ordinates that have no piece in them, please put another set of co-ordinates')
    if Pawns['White']['WK0'] not in SubBoard.values():
      print('The Black Pieces Have Won This Game Of Chess \n Yaaaaaaaaaaaaaaaaa Good Job Black Player')
    elif Pawns['Black']['BK0'] not in SubBoard.values():
      print('The White Pieces Have Won This Game Of Chess \n Yaaaaaaaaaaaaaaaaa Good Job White Player')

