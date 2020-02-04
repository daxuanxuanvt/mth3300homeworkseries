"""****************************************************************************
Program: BinaryToTen.py
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

x = np.random.randint(0,2,10)
y = [2^9, 2^8,2^7,2^6, 2^5, 2^4, 2^3, 2^2, 2^1, 2^0]
z = np.dot(x, np.transpose(y))
print(x)
print(y)
print(z)
print("x", "base 2 equals", "z", "base 10")





# And ends here.
"""****************************************************************************
Overall notes (these notes do not replace in-code comments):


    
****************************************************************************"""


