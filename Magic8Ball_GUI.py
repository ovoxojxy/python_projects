import PySimpleGUI as sg
import random


sg.theme('DarkAmber')

layout = [[sg.Text("Ask anything (preferably Yes or No)")],
          [sg.InputText()],
          [sg.Submit('Ask'), sg.Cancel('Quit')]
          ]

window = sg.Window('Magic 8 Ball', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Ask':
        responses = [
            "Outlook is hazy, try again later.",
            "Signs point to yes.",
            "Don't count on it.",
            "Ask again after lunch.",
            "Very doubtful.",
            "You may rely on it.",
            "My sources say no.",
            "All signs are pointing to a positive outcome.",
            "Better not tell you now.",
            "Yes, definitely.",
            "Cannot predict now.",
            "Reply hazy, try again.",
            "Yes, but proceed with caution.",
            "Outlook is good.",
            "My answer is no.",
            "Ask someone else.",
            "Absolutely.",
            "Not in the cards for you.",
            "Ask again when the stars align.",
            "Don't hold your breath."
        ]

        sg.popup('Magic 8 ball says:', random.choice(responses))

window.close()