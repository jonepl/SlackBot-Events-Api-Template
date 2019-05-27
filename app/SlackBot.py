'''
File: Slackbot.py
Description: Core class of the SlackBot application. All handlers and Scheduler class
             communicate to the Slack Servers using this class
'''

import random, re
from app.SlackWebApi import SlackWebApi

GREETINGS = ["hello", "hey", "howdy", "sup", "greetings Human", "what bruh"]

class Slackbot() :
    def __init__(self, config, debug) :

        self.slackWebApi = SlackWebApi(config.get("slack_bot_token"))

    def handle(self, message) :
        text = self.stripTag(message.get("text"))
        if(text.lower() in GREETINGS) :
            text = random.choice(GREETINGS).capitalize()
            self.slackWebApi.chatPostMessage(message.get("channel"), text)
        else :
            text = "Sorry I don't know what to do here. Write some code to make some magic :wink:."
            self.slackWebApi.chatPostMessage(message.get("channel"), text)

    def stripTag(self, text) :
        return re.sub("<@[A-Z0-9]{9}>", "", text).strip()

if __name__ == "__main__":
    pass