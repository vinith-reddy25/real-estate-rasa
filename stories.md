## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## survey buy happy path
* greet
  - utter_greet
* affirm
  - buy_form
  - form{"name":"buy_form"}
  - form{"name":"null"}
  - utter_slots_values
* thankyou
  - utter_goodbye

## survey buy stop
* greet
  - utter_greet
* affirm
  - buy_form
  - form{"name":"buy_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":null}
  - utter_goodbye

## survey buy continue
* greet
  - utter_greet
* affirm
  - buy_form
  - form{"name":"buy_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - buy_form
  - form{"name":null}
  - utter_slots_values

## no survey
* greet
  - utter_greet
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
