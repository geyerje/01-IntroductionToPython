"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and James (Bo) Geyer
"""
###############################################################################
# Done
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

bo = rg.SimpleTurtle()
bo.pen = rg.Pen('red',10)
bo.speed = 100


rob = rg.SimpleTurtle()
rob.pen = rg.Pen('blue',10)
rob.speed = 100


for k in range(35):
    bo.forward(30)
    bo.left(150)
    bo.forward(50)
    bo.left(110)
    bo.forward(50)
    bo.left(90)
    bo.forward(30)

for k in range(35):
    rob.backward(30)
    rob.right(150)
    rob.backward(50)
    rob.right(110)
    rob.backward(50)
    rob.right(90)
    rob.backward(30)

window.close_on_mouse_click()
