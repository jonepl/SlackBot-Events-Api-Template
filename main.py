'''
File: main.py
Description: Entry point for Events API Slack application
'''

import app.SlackEventsApi as SlackEventsApi
from app.SlackBot import Slackbot
import json, argparse, sys, os

config = {}
with open('config/creds.json') as json_data:
    config = json.load(json_data)

def main():

    args = prepCmdArgs()
    try:
        slackbot = Slackbot(config, args.debug)
        SlackEventsApi.start(slackbot, args.debug)

    except Exception as e:
        print("Exception: " + str(e))
        sys.exit(1)

def prepCmdArgs() :
    
    parser = argparse.ArgumentParser(description='Kicks off an instance of of a Slackbot')
    parser.add_argument('-d', '--debug', action='store_true')
    return parser.parse_args()

if __name__ == '__main__':
    main()