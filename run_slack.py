from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-599023632341-599992337350-KjGgdg7Ft8iCvZW0nyFloNQY' #your bot user authentication token
                           )

agent.handle_channels([input_channel], 5004, serve_forever=True)
# -*- coding: utf-8 -*-

