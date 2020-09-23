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
