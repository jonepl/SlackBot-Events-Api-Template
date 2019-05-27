'''
File: SlackWebApi.py
Description: Single class used to interface with the Slack Server via api calls
'''

from slackclient import SlackClient

class SlackWebApi(object) :

    _instance = None

    def __new__(self, token) :
        if(not self._instance) :
            self._instance = super(SlackWebApi, self).__new__(self)
            self.slack_client = SlackClient(token)
        
        return self._instance

    # Writes the message to specified slack channel
    def chatPostMessage(self, channel, text, attachments=[], blocks=[]):
        return self.slack_client.api_call('chat.postMessage', channel=channel, text=text, attachments=attachments, blocks=blocks)

    # This method updates a message in a channel.
    def chatUpdateMessage(self, channel, ts, text="", attachments=[], blocks=[]) :
        return self.slack_client.api_call("chat.update", channel=channel, text=text, ts=ts, attachments=attachments, blocks=blocks)

    # Opens a form to start a interactive message dialog with a slack user
    def dialogOpen(self, dialog, trigger) :
        return self.slack_client.api_call("dialog.open", trigger_id=trigger, dialog=dialog)

    # Attaches a file or a code snippet to slack channel
    def filesUpload(self, channel, filePath, filename=None, title=None) :
        return self.slack_client.api_call("files.upload", channels=channel, file=open(filePath, 'rb'))

    # Retrieves a detailed list of all members in slack group
    def usersList(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            return api_call.get('members')
        else :
            if(self.debug) : logger.error("Issue occurred when getting member list")

    # Retrieves a portion of message events from the specified public channel.
    def imHistory(self, channel, count=100, inclusive=True, unreads=True) :
        api_call = self.slack_client.api_call("im.history", channel=channel, count=count, inclusive=inclusive, unreads=unreads)
        if api_call.get('ok'):
            return api_call
        else :
            print("Get History failed.")

    # Retrieves a detailed list of all channels in slack
    def channelsList(self) :
        api_call = self.slack_client.api_call("channels.list")
        if api_call.get('ok'):
            return api_call
        else :
            if(self.debug) : logger.error("Issue occurred when getting channel list")

    # Retrieves channel information
    def channelInfo(self, channel) :
        return self.slack_client.api_call("channels.info", channel=channel)

    # Retrieves group information
    def groupInfo(self, channel) :
        return self.slack_client.api_call("groups.info", channel=channel)