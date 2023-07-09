# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 20:59:50 2023

@author: finnj
"""

X = "X"
O = "O"

class Board:
    def __init__(self, a1, a2, a3, b1, b2, b3, c1, c2, c3):
        
        # top row
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        
        # middle row
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        
        # bottom row
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        
    # Check win condition by row        

    def checkTopRow(self):
        if self.a1 == self.a2 == self.a3:
            return self.a1

    def checkMiddleRow(self):
        if self.b1 == self.b2 == self.b3:
            return self.b1
        
    def checkBottomRow(self):
        if self.c1 == self.c2 == self.c3:
            return self.c1
        
    # Check by column
    
    def checkLeftColumn(self):
        if self.a1 == self.b1 == self.c1:
            return self.a1
        
    def checkMiddleColumn(self):
        if self.a2 == self.b2 == self.c2:
            return self.a2
        
    def checkRightColumn(self):
        if self.a3 == self.b3 == self.c3:
            return self.a3
      
    # Check by diagonal  
      
    def checkMainDiagonal(self):
        if self.a1 == self.b2 == self.c3:
            return self.a1
        
    def checkCounterDiagonal(self):
        if self.a3 == self.b2 == self.c1:
            return self.a3
        
    
        
firstBoard = Board(X,X,X,O,O,O,X,X,X)

"""def showGame():
    print("        1     2     3")
    print("")
    print("     -------------------")
    print("A    I     I     I     I")
    print("     -------------------")
    print("B    I     I     I     I")
    print("     -------------------")
    print("C    I     I     I     I")
    print("     -------------------")
    

showGame()"""
