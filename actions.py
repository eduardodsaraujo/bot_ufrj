from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		
		loc = tracker.get_slot('location')
		response = "It is currently in  at the moment. The "
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionDefaultCallback(Action):
	def name(self):
		return 'action_default_fallback'
