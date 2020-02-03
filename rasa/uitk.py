# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/core/actions/#custom-actions/


# # This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# #
class ActionSpecialPaneerBiriyani(Action):

    def name(self) -> Text:
        print(Text)
        return "action_Special_Paneer_Biryani"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("i want paneer!")
        return []
    
class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("hi")
        # dispatcher.utter_message(tracker.get_slot("matches"))
        # dispatcher.utter_message("is it ok for you? "
        #                          "hint: I'm not going to "
        #                          "find anything else :)")
        return []
# #
########################################################################
from tkinter import Tk, BOTH, Canvas,Button,messagebox
from tkinter.ttk import Frame, Label, Style,Entry
from tkinter import *
from tkinter import ttk
import numpy
##########################################################################
class ActionHelloWorld(Action):
    window = Tk()
    window.title("Welcome to minichat")
    window.geometry('250x100')
    window.configure(background = "grey")
    
    
    def hello():
        user_input =  str(a1.get())
        print(user_input)
        # name(user_input)
        # name = Text
        
        return user_input        
        
    btn = ttk.Button(window ,text="ask",command = hello).grid(row=2,column=1)
    a = Label(window ,text = "customer input ").grid(row = 0,column = 0) #,command = 
    b = Label(window ,text = "answer").grid(row = 3,column = 0)
    a1 = Entry(window)
    a1.grid(row = 0,column = 1)
    b1 = Entry(window)
    b1.grid(row = 3,column = 1)
    window.mainloop()
    
    
    # def name(self) -> Text:
    #     return "utter_Special_Paneer_Biryani"

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    #     dispatcher.utter_Special_Paneer_Biryani(hello)

        return []


#ui

# from uipluslogic import resz
# import uipluslogic 
# window = Tk()
# window.title("Welcome to minichat")
# window.geometry('250x100')
# window.configure(background = "grey")
# # img = cv2.imread("010.jpg")
# def hello():
# #    messagebox.showinfo("info", "Compressed successfully")
#    user_input =  str(a1.get())
#    print(user_input)
# #    height = int(b1.get())

# #    resz(user_input)

# btn = ttk.Button(window ,text="ask",command = hello).grid(row=2,column=1)
# a = Label(window ,text = "customer input ").grid(row = 0,column = 0) #,command = 
# b = Label(window ,text = "answer").grid(row = 3,column = 0)
# a1 = Entry(window)
# a1.grid(row = 0,column = 1)
# b1 = Entry(window)
# b1.grid(row = 3,column = 1)
# window.mainloop()

# # class resizeee():
# #     def __int__(self):
# #         print("_")
# def medec(func):
# 	def indec(*args, **kwargs):
# 		print("replying ON PROGRESS")
# 		print ("customer---> {}".format(h,w))
# 		# print(*args, **kwargs)
# 		func(*args, **kwargs)
# 		print ("bot  --->{}".format(h,w))
# 		print ("SUCCESSFULLY replied")
# 		# print(result)
# 		# return result
# 	return indec
# @medec
# def resz(text):
# 	print(text)