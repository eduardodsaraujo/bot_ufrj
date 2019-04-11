from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.telegram import TelegramInput
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/bot_ufrj')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)
input_channel = TelegramInput(
        # you get this when setting up a bot
        access_token="877815343:AAGFaRsOcxSO583k6c_XA9_RqKPcjTqoMQU",
        # this is your bots username
        verify="testufrj_bot",
        # the url your bot should listen for messages
        webhook_url="https://9c5428b7.ngrok.io/webhooks/telegram/webhook"
    )

agent.handle_channels([input_channel], 5004, serve_forever=True)