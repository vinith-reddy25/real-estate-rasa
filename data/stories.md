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

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot



## survey support bnp
* greet
  - utter_greet
* buy_new_plan
  - buy_plan_form
  - form{"name":"buy_plan_form"}
  - form{"name":null}
  - utter_confirmemail
* affirm
  - utter_greet

## survey support bnpone
* greet
  - utter_greet
* buy_new_plan
  - buy_plan_form
  - form{"name":"buy_plan_form"}
  - form{"name":null}
  - utter_confirmemail
* deny
  - utter_goodbye
  



## survey support tic
* greet
  - utter_greet
* support_ticket
  - utter_severity
* emer
  - ticket_emer_form
  - form{"name":"ticket_emer_form"}
  - form{"name":null}
* affirm
  - utter_greet

## survey support ticone
* greet
  - utter_greet
* support_ticket
  - utter_severity
* emer
  - ticket_emer_form
  - form{"name":"ticket_emer_form"}
  - form{"name":null}
* deny
  - utter_goodbye


## survey support tick
* greet
  - utter_greet
* support_ticket
  - utter_severity
* notemer
  - ticket_form
  - form{"name":"ticket_form"}
  - form{"name":null}
* affirm
  - slot{"explainproblem":null}
  - slot{"time":null}
  - utter_greet

## survey support tickone
* greet
  - utter_greet
* support_ticket
  - utter_severity
* notemer
  - ticket_form
  - form{"name":"ticket_form"}
  - form{"name":null}
* deny
  - utter_goodbye


## no survey
* greet
  - utter_greet
* deny
  - utter_goodbye
