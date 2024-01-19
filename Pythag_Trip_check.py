# sides = []
# sides.append(int(input('List first side:')))
# sides.append(int(input('List second side:')))
# sides.append(int(input('List third side:')))
# hypotenuse = sides.pop(sides.index(max(sides)))

# if (sides[0] **2) + (sides[1] **2) == (hypotenuse ** 2):
#     print("This is a triple")
# else:
#     print("This is not a triple")

import PySimpleGUI as sg
import random


sg.theme('DarkAmber')

layout = [[sg.Text("Enter triangle sides")],
          [sg.Text("Enter side one"), sg.InputText(key='-first-')],
          [sg.Text("Enter side two"), sg.InputText(key='-second-')],
          [sg.Text("Enter side three"), sg.InputText(key='-third-')],
          [sg.Submit('Calculate'), sg.Cancel('Quit')]
          ]

window = sg.Window('Pythagorean Triples Checker', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Calculate':
        try:
            sides = [int(values['-first-']), int(values['-second-']), int(values['-third-'])]
            hypotenuse = sides.pop(sides.index(max(sides)))

            if (sides[0] ** 2) + (sides[1] ** 2) == (hypotenuse ** 2):
                sg.popup('This is a triple')
            else:
                sg.popup('This is not a triple')
        except ValueError:
            sg.popup('Please enter valid integers for all sides')

window.close()