from rasa_sdk import Tracker,FormValidationAction
from typing import Text,Dict,Any
import requests
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

url = "https://vast-reaches-86350.herokuapp.com/webhook"
class GetAccountNumber(FormValidationAction):
    def name(self) -> Text:
        return "validate_balance_check_form"
    def validate_account_number(self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker:Tracker,
            domain: DomainDict):
            acctNum=slot_value
            r = requests.post(url=url,data={'account':acctNum})
            balance = r.json()
            dispatcher.utter_message(text=f'Your account balance is:{balance}')
            return {'account_number':slot_value}
