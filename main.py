import gui.gui as gui
from note_taking_API import *

db_create_db(connection)
db_create_table(connection)

window = gui.Window()

window.mainloop()
