import random
question = input('Ask me anything:')
responses = ["Outlook is hazy, try again later.",
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
"Don't hold your breath."]

print (question)
for i in range(3):
    print('*thinking*')
print(responses[random.randint(0,19)])