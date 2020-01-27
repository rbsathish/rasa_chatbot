from rasa.core.channels.slack import SlackInput
# from rasa_core.agent import Agent
# # from rasa_core.interpreter import RegexInterpreter
# # from rasa_core.interpreter import RasaNLUInterpreter
# # nlu_interpreter = RasaNLUInterpreter('C:\\Users\\Dell\\Desktop\\rasa\\models')
# # agent = Agent.load('C:\\Users\\Dell\\Desktop\\rasa\\models', interpreter = nlu_interpreter)

# from rasa.model import get_model_subdirectories, get_model

# async def run(serve_forever=True):
#     model_path = get_model('./models/nlu')
#     _, nlu_model = get_model_subdirectories(model_path)
#     interpreter = RasaNLUInterpreter(nlu_model)
#     agent = Agent.load('./models/core', interpreter=interpreter)
# input_channel = SlackInput(
#         slack_token="xoxb-226167828518-917903335220-JgysfOc3fjSAqgmRcrkVSHB6"
#         # this is the `bot_user_o_auth_access_token`
#         #slack_channel="YOUR_SLACK_CHANNEL"
#             # the name of your channel to which the bot posts (optional)
#     )
# # set serve_forever=True if you want to keep the server running
# s = agent.handle_channels([input_channel], 5004, serve_forever=True)


from rasa.model import get_model_subdirectories, get_model

async def run(serve_forever=True):
    model_path = get_model('./models/nlu')
    _, nlu_model = get_model_subdirectories(model_path)
    interpreter = RasaNLUInterpreter(nlu_model)
    agent = Agent.load('./models/core', interpreter=interpreter)
    input_channel = SlackInput(
        slack_token="xoxb-226167828518-920643594710-QwGV9EjjOuFiATFjUGU1Kfn1"
        # this is the `bot_user_o_auth_access_token`
        #slack_channel="YOUR_SLACK_CHANNEL"
            # the name of your channel to which the bot posts (optional)
    )

    # if serve_forever:
        
    #     agent.handle_channel(CmdlineInput())
    # return agent
    s = agent.handle_channels([input_channel], 5055, serve_forever=True)
    
    # https://hooks.slack.com/services/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