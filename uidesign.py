# import the libraries
import PySimpleGUI as sg

# calculator function definition
def todoList():
  # set the background color
  sg.theme('Dark Blue 2')
  
  # set layout row and column-wise
  layout = [
    [sg.Text("Tasks to be done")],
    [
      # create text area and buttons
      sg.Multiline("1. UI Design Completion \n2. Add event handlers", size=(50, 10))
    ],
    # create buttons for numbers and operators with corresponding backgrounds and text colors
    [
      sg.Button('Add Task', size=(8, 2), button_color=('white', 'blue')),
      sg.Button('Set Reminders', size=(10, 2), button_color=('white', 'blue')),
      sg.Button('View History', size=(8, 2), button_color=('white', 'blue')),
      sg.Button('Close Window', size=(8, 2), button_color=('white', 'blue')),
        
    ],
  ]
  # assign the title and layout to a variable
  window = sg.Window('  To-Do List', layout)

  # iterate the event and values using a loop
  while True:
    event, values = window.read()
    
  # close the application window
  window.close()
todoList()
