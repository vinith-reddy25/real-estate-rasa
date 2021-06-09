# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import uuid
#

class TicketForm(FormAction):
    
    def name(self):
        return "ticket_form"


    @staticmethod
    def required_slots(tracker):
        return ["explainproblem", "time"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "explainproblem": [
               self.from_text(), 
            ],
            "time": [
                self.from_text(),
            ],

        }
    

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
         id = uuid.uuid4()
         idd = str(id)
         dispatcher.utter_message(text="We have raised a ticket for you. Ticket number is " + idd + " Use the ticket number to track the progress.")
         dispatcher.utter_message(template="utter_submt")
         return []


class TicketemerForm(FormAction):
    
    def name(self):
        return "ticket_emer_form"


    @staticmethod
    def required_slots(tracker):
        return ["aboutenvironment","explainproblem", "time"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "aboutenvironment": [
               self.from_text(), 
            ],
            "explainproblem": [
               self.from_text(), 
            ],
            "time": [
                self.from_text(),
            ],

        }
    

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
         id = uuid.uuid4()
         idd = str(id)
         dispatcher.utter_message(text="We have raised a ticket for you. Ticket number is " + idd + " Use the ticket number to track the progress. Do you want to continue?")
         dispatcher.utter_message(template="utter_submt")
         return []



class BuyPlanForm(FormAction):
    
    def name(self):
        return "buy_plan_form"


    @staticmethod
    def required_slots(tracker):
        return ["orgsize","emailid","plan"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "orgsize": [
               self.from_text(), 
            ],
            "emailid": [
                self.from_text(),
            ],
            "plan": [
                self.from_text(),
            ],

        }
    

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
         dispatcher.utter_message(template="utter_submt")
         return []




# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
