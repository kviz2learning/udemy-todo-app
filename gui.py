import PySimpleGUI as sg

# Create a text label
label = sg.Text("Type in a to-do")

# Create an input textbox
input_box = sg.InputText(tooltip="Enter todo")

# Create a button
add_button = sg.Button("Add")

# Create a window object (instance); `layout` is a list containing the UI elements meant for the window
window = sg.Window("Title of the window", layout=[[label], [input_box, add_button]])
window.read()     # Display the window object
print("Hello")
window.close()