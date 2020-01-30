## welcome
* greet
 - utter_ask_howcanhelp
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

## urname
*ur_name
  - utter_name

<!-- ## biriyani
* chicken_biriyani
  - utter_chicken_biriyani
* chicken_dum_biriyani
  - utter_chicken_dum_biriyani -->
<!-- * egg_biriyani
  - utter_egg_biriyani
* Chicken_Bone_Less_Pulao
  - utter_Chicken_Bone_Less_Pulao -->
## available_biriyani
* biriyani
  - utter_available_biriyani
## egg_biriyani
* egg_biriyani
  - utter_egg_biriyani

## Chicken_Bone_Less_Pulao
* Chicken_Bone_Less_Pulao
  - utter_Chicken_Bone_Less_Pulao

## Keema_Biryani
* Keema_Biryani
  - utter_Keema_Biryani

## Special_Paneer_Biryani
* Special_Paneer_Biryani
  - utter_Special_Paneer_Biryani
## interactive_story_2
* biriyani{"biriyani": "biriyani"}
    - slot{"biriyani": "biriyani"}
    - utter_available_biriyani
    - utter_choose_which_biriyani_you_want

* carrot_halwa
  - utter_carrot_halwa
* Double_Ka_Meeta
  - utter_Double_Ka_Meeta
* Gulab_Jamun
    - utter_Gulab_Jamun
* Ras_Malai
  - utter_Ras_Malai
<!-- ## price_querry
* price_querry
  - utter_price_querry -->
## available_deserts
* deserts
  -utter_available_deserts
## carrot_halwa
* carrot_halwa
  - utter_carrot_halwa
## Double_Ka_Meeta
* Double_Ka_Meeta
  - utter_Double_Ka_Meeta
## Gulab_Jamun
* Gulab_Jamun
  - utter_Gulab_Jamun
## Ras_Malai
* Ras_Malai
  - utter_Ras_Malai
<!-- ## interactive_story_1
* deserts{"deserts": "deserts"}
    - slot{"deserts": "deserts"}
    - utter_available_deserts
    - utter_choose_any_deserts -->
    <!-- - utter_happy -->

## interactive_story_1
* deserts{"deserts": "deserts"}
    - slot{"deserts": "deserts"}
    - utter_available_deserts
    - utter_choose_any_deserts
* carrot_halwa
  - utter_carrot_halwa
* Double_Ka_Meeta
  - utter_Double_Ka_Meeta
* Gulab_Jamun
    - utter_Gulab_Jamun
* Ras_Malai
  - utter_Ras_Malai
