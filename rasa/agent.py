
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

    # from rasa.core.agent import Agent
    # from rasa.core.interpreter import RasaNLUInterpreter
    # agent = Agent.load("models/20191024-130152.tar")
    # # await agent.handle_text("hello")
    # # [u'how can I help you?']
    # print("Your bot is ready to talk! Type your messages here or send 'stop'")
    # while True:
    #     a = input("User: ")
    #     if a == 'stop':
    #         break
    #     responses = agent.handle_message(a)
    #     for response in responses:
    #         print("Robo: ",response["text"])
        

# from rasa.core.agent import Agent
# from rasa.core.interpreter import RasaNLUInterpreter
# agent = Agent.load("models/20200203-115808.tar.gz")
# # agent = Agent.load_data("models/20200203-115808.tar.gz")
# # reply = await agent.handle_text("hello")

# import asyncio

# # ...
# loop = asyncio.get_event_loop()
# reply = loop.run_until_complete(agent.handle_text("hi"))


import asyncio
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
############################ text to text ######################################
# async def parse(msg):
#     response = await agent.handle_text(msg)
#     print(response)
#     return response

# if __name__ == "__main__":
#     agent = Agent.load("models/20200203-115808.tar.gz")

#     loop = asyncio.get_event_loop()
#     user_input = input(str()) #[List[Dict[str, Any]]]
#     response = loop.run_until_complete(parse(user_input))   
#################################################################################
####################### speech to text+ text to speech ##########################
async def parse(msg):
    responses = await agent.handle_text(msg)
    for response in responses:
        # print("bot_response: ",response["text"])
        text = response["text"]
        print("bot_response",text)
        from st_ts.text_to_speach import tts
        text_to_speech = tts(text)
    return responses

if __name__ == "__main__":
    agent = Agent.load("models/20200204-143750.tar.gz")
    loop = asyncio.get_event_loop()
    from st_ts.speach_to_text import stt
    response = loop.run_until_complete(parse(stt()))   
