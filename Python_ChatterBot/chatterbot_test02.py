from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Create a new chat bot

from chatterbot import ChatBot
chatbot = ChatBot("Nathan")

# Training your ChatBot
# Training is a good way to ensure that the bot starts off with knowledge about specific responses. The current training method takes a list of statements that represent a conversation

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

conversation1 = [
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼",
    "白日依山尽"
]

conversation2 = [
    "Hello",
    "Hi man",
    "How are you doing?",
    "I am feeling great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

conversation3 = [
    "十里平湖霜满天",
    "寸寸青丝愁华年",
    "对月形单望相护",
    "只羡鸳鸯不羡仙",
    "十里平湖霜满天"
]

conversation4 = [
    "春晓",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "春江花月夜",
    "春江潮水连海平\n，海上明月共潮生\n。 滟滟随波千万里，何处春江无月明！ 江流宛转绕芳甸，月照花林皆似霰； 空里流霜不觉飞，汀上白沙看不见。 江天一色无纤尘，皎皎空中孤月轮。 江畔何人初见月？江月何年初照人？ 人生代代无穷已，江月年年只相似。",
    "十里平湖霜满天"
]

conversation5 = [
    "春晓",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "春江花月夜",
    "张若虚",
    "春江潮水连海平\n，海上明月共潮生\n。 滟滟随波千万里，何处春江无月明！ 江流宛转绕芳甸，月照花林皆似霰； 空里流霜不觉飞，汀上白沙看不见。 江天一色无纤尘，皎皎空中孤月轮。 江畔何人初见月？江月何年初照人？ 人生代代无穷已，江月年年只相似。",
    "十里平湖霜满天"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
trainer.train(conversation1)
trainer.train(conversation2)
trainer.train(conversation3)
trainer.train(conversation4)
trainer.train(conversation5)
# Get a response
response = chatbot.get_response("春江花月夜")
response_text = str(response)
print(response_text)

# next_needed = input("是否需要提示下一句？")
# if next_needed == "yes":
#     response2 = chatbot.get_response(response_text)
#     print(response2)

