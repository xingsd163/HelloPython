
# https://www.simplifiedpython.net/python-chatbot/
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MyChatBot')
# bot.set_trainer(ListTrainer)
trainer=ListTrainer(bot)

conversation = open('/home/nathan/chats.txt', 'r').readlines()

trainer.train(conversation)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
    print('ChatBot:', reply)
    if message.strip() == 'Bye':
        print('ChatBot:Bye')
        break