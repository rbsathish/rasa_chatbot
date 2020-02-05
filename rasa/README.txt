Rasa_bot_by_RB

First you need to install requirements.txt

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

normal shell chat:
	rasa shell r for debug---> rasa shell --debug

For interactive chat:
	rasa interactive --skip-visualization -m models --endpoints endpoints.yml

Voice interaction:
	* You can run this bot through agent.py 

Web based interaction:
	* Run this cmt first:
		   rasa run -m models --enable-api --cors "*" --debug
	* After open Rasa_CustomUI-v_2.0-master ---> open Index.html

Custom actions:
	rasa run actions

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


