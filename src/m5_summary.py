"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and James (BO) Geyer.
"""
########################################################################
# Done
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)

bo = rg.SimpleTurtle()
bo.pen = rg.Pen('red',15)
bo.speed = 20

bo.left(45)
bo.forward(50)
bo.right(120)
bo.backward(80)
bo.left(60)
bo.forward(70)

window.close_on_mouse_click()