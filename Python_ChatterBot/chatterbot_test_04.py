# https://github.com/gunthercox/ChatterBot/blob/master/examples/default_response_example.py
# ChatterBot Examples

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create a new instance of a ChatBot
bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.99
        }
    ]
)

trainer = ListTrainer(bot)

# Train the chat bot with a few responses
trainer.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html',
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼",
    "白日依山尽",
    "春晓",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "春江花月夜",
    "张若虚",
    "春江潮水连海平\n，海上明月共潮生\n。 滟滟随波千万里，何处春江无月明！ 江流宛转绕芳甸，月照花林皆似霰； 空里流霜不觉飞，汀上白沙看不见。 江天一色无纤尘，皎皎空中孤月轮。 江畔何人初见月？江月何年初照人？ 人生代代无穷已，江月年年只相似。",
    "十里平湖霜满天",
    "size",
    "bigger"
])

# # Get a response for some unexpected input
# response = bot.get_response('How can I help you?')
# print(response)


while True:
    message = input('You:')
    if message.strip() == 'Bye' or message.strip() == 'bye':
        print('ChatBot:Bye')
        break
    elif message.strip() != 'Bye':
        reply = bot.get_response(message)
    print('ChatBot:', reply)


