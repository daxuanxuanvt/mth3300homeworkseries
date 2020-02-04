"""****************************************************************************
Program: BaseTenToBinary.py
*******************************************************************************
Your names: Shannon & Shakeem
    
*******************************************************************************
Collaborators/outside sources used (IMPORTANT! Write "NONE" if none were used):

None

Reminder: you are to jointly write your own code.
****************************************************************************"""
# Your code starts here:
import random
import numpy as np
import math

x = np.random.randint(1, 1024)
print(x)

a = []
while x != 0:
    a.append(x % 2)
    x = x // 2
a.reverse()    
print(a)






# And ends here.
"""****************************************************************************
Overall notes (these notes do not replace in-code comments):


    
****************************************************************************"""


