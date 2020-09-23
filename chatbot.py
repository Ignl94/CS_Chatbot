# This is my chatbot app

from random import choice


# Create bot response function


def get_bot_response(user_response):
    bot_response_good = ["Zoltar welcomes you!", "Yes, I am Zoltar.",
                         "Fortune for quarters, I love quarters!", "You have awoken Zoltar from his nap."]
    bot_response_bad = ["How rude you are to Zoltar.",
                        "Sorry, Zoltar only tells fortunes for friends.", "Did you know Zoltar is also a black belt?"]

    if user_response == 'Hello' or user_response == 'hello' or user_response == 'Hello Zoltar' or user_response == 'hello Zoltar' or user_response == 'hello zoltar' or user_response == 'Hello zoltar' or user_response == 'Hi' or user_response == 'hi':
        return choice(bot_response_good)
    elif user_response == 'Hey stupid' or user_response == 'You suck' or user_response == 'I don\'t believe in fortunes' or user_response == 'poopy head':
        return choice(bot_response_bad)
    elif user_response.isnumeric():
        return "Zoltar is bad at math."
    else:
        return "Zoltar is late for back massage, how can I help you?"


def get_bot_fortune(user_response):
    bot_fortunes = ["The answer to that is relative", "Allow Zoltar to refer to his scrolls",
                    "To know that you know not, is the greatest form of wisdom", "It is best to look within yourself."]
    if user_response.isnumeric():
        return "Zoltar is bad at math."
    else:
        return choice(bot_fortunes)


print('Welcome to the Zoltar Chatbot!')
print('Speak to Zoltar and get your fortune!')
user_response = " "
fortune_counter = 0
while True and fortune_counter < 2:
    fortune_counter = 0
    user_response = input('Say hello to Zoltar. ')
    if user_response == 'done' or user_response == 'goodbye' or user_response == 'Bye Zoltar' or user_response == 'bye zoltar':
        print('Goodbyes from Zoltar')
        break
    zoltar_response = get_bot_response(user_response)
    print(zoltar_response)
    # ---------------------------------------- Fortune Portion ------------------------------------------------------
    user_response = input('Would you like Zoltar to read your fortune? ')
    if user_response == 'done' or user_response == 'goodbye' or user_response == 'Bye Zoltar' or user_response == 'bye zoltar' or user_response == 'no' or user_response == 'No' or user_response == 'No thanks':
        print('Goodbyes from Zoltar')
        break
    elif user_response == 'yes' or user_response == 'Yes' or user_response == 'ok' or user_response == 'Ok' or user_response == 'sure' or user_response == 'Sure':
        user_response = input("Ask Zoltar a question. ")
        zoltar_fortune = get_bot_fortune(user_response)
        print(zoltar_fortune)
        fortune_counter += 1
        user_response = input(
            'Would you like to ask Zoltar one more question? ')
        if user_response == 'yes' or user_response == 'Yes' or user_response == 'ok' or user_response == 'Ok' or user_response == 'sure' or user_response == 'Sure':
            user_response = input("Ask Zoltar a question. ")
            zoltar_fortune = get_bot_fortune(user_response)
            print(zoltar_fortune)
            print('Zoltar thanks you for your visit, goodbyes from Zoltar!')
            fortune_counter += 1
        elif user_response == 'done' or user_response == 'goodbye' or user_response == 'Bye Zoltar' or user_response == 'bye zoltar' or user_response == 'no' or user_response == 'No' or user_response == 'No thanks':
            print('Goodbyes from Zoltar')
            break
        elif user_response.isnumeric():
            print('Zoltar is bad at math.')
        else:
            print('Zoltar does not understand')
    elif user_response.isnumeric():
        print('Zoltar is bad at math.')
    else:
        print('Zoltar does not understand.')

