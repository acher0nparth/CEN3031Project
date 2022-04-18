import gui.gui as gui
from database_API import *
from note_taking_API import *

db_create_db()
db_create_table()

window = gui.Window()

window.mainloop()
