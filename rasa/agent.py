
# #Starting the Bot

# from rasa.core.agent import Agent
# agent = Agent.load('models/20191024-130152.tar', interpreter=model_directory)



# print("Your bot is ready to talk! Type your messages here or send 'stop'")
# while True:
#     a = input("User: ")
#     if a == 'stop':
#         break
#     responses = agent.handle_message(a)
#     for response in responses:
#         print("Robo: ",response["text"])

from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
agent = Agent.load("models/20191024-130152.tar")
# await agent.handle_text("hello")
# [u'how can I help you?']
print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    a = input("User: ")
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        print("Robo: ",response["text"])