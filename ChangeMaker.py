"""****************************************************************************
Program: ChangeMaker.py
*******************************************************************************
Your names: Shannon & Shakeem
    
*******************************************************************************
Collaborators/outside sources used (IMPORTANT! Write "NONE" if none were used):

None

Reminder: you are to jointly write your own code.
****************************************************************************"""
# Your code starts here:
import random
import numpy
import math

x = np.random.randint(1,100)
a = x % 5 # = 3
b = (x - a) % 10 # =5, needs to be /5
c = (x - a - b) // 25
d = (x - a - b - c * 25) // 10
b = b / 5
print(x, "cents is equal to", c, "quarters", d, "dimes", b, "nickles", a, "cents")






# And ends here.
"""****************************************************************************
Overall notes (these notes do not replace in-code comments):


    
****************************************************************************"""


