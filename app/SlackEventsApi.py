'''
File: SlackEventsApi.py
Description: Main Adapter use to interface with Slack's Event API adapter
Info: List of Events can be found https://api.slack.com/events. Make 
      sure to Add Bot User Event in the Slack Event Subscriptions
'''

import json
from slackeventsapi import SlackEventAdapter
from flask import Flask, jsonify, Response, request

config = {}
with open('config/creds.json') as json_data:
    config = json.load(json_data)

slackBot = None
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(config.get("slack_signing_secret"), "/slack/events", app)

# Start listening on configuration port for Slackbot
def start(bot, debug) :
    global slackBot
    slackBot = bot
    app.run(port=config['port'])

''' Custom API Endpoints '''
# Handles all slash commands. You must configure slash commands within your app at www.api.slack.com
@app.route("/slash", methods=['POST'])
def handleSlashCommand():
    message = request.values.to_dict()
    slackBot.handle(message)

    return Response(), 200

''' Slack API Endpoints via https://api.slack.com/events '''
# A message was sent to a channel
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data.get("event")

    if message.get("subtype") is None :
        # Handles direct messages
        if message.get('channel_type') == "im" :
            slackBot.handle(message)

        # Handles messages in channels
        if message.get('channel_type') == "channel":
            slackBot.handle(message)

# Subscribe to only the message events that mention your app or bot
@slack_events_adapter.on("app_mention")
def handle_direct_message(event_data) :
    
    message = event_data.get("event")
    slackBot.handle(message)