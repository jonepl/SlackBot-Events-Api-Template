<h1 align="center">
  <br>
  <a href="#"><img src="https://venturebeat.com/wp-content/uploads/2015/07/slackbot.png" alt="Markdownify" width="200"></a>
  <br>
  Slackbot Events Api Example
</h1>

## Setting up SlackBot Events Api Template
In order for this your Slackbot to work it will need to retrieve a couple of tokens from Slack. 

1. slack_bot_token: This is the token of the bot user configured in slack
2. slack_signing_secret: This is the signing secret that the bot will use to authenticate to the channel sent by the events subscription.

### config/creds.json
```json
{
    "slack_bot_token" : "Your SlackBot Token",
    "slack_signing_secret" : "Signing Secret",
    "port" : 8080,
    "mongoDB" : {
        "dbName" : "DB Name",
        "uri" : "DB uri",
        "collectionName" : "Collection Name"
    }
}
```

### Ngrok
In order to run this bot locally you are first going to need a tunneling software set up and configured. When you post a message in slack, the slack event handler will send a message to your server. As you will be running this locally you will need a way to forward that request to your local host. For this example I have used ngrok.

### Creating your Slack Application

1. Create an application in slack via https://api.slack.com/
2. Add a bot user to the slack application
3. Navigate OAuth & Permissions and enable bot user. Don't for get to grab the Bot User *OAuth Access Token* and save it as your **slack_bot_token** and save it to your creds.json file
4. Grant the bot user chat:write:bot scope
5. Navigate to *Event subscriptions* and to on events for your app
6. Grant the subscribe to bot events the message.channels scope
7. Navigate to the *Basic Information* tab and grab your **slack_signing_secret** and save it to your creds.json file 
8. In terminal session a, launch ngrok 
    ```bash
    ./ngrok http 3000
    ```
9. In terminal session b, launch the slack bot
    ```bash
    pip3 install -r requirements.txt
    python3 main.py

### DB Setup

Currently this application use MongoDB to store service data. You can get a 0.5 GB space at https://mlab.com or you may use any MongoDB Database as you wish. Setup your DB environment and add your **dbName**, **uri** and **collectionName** to you **creds.json** file


## References

Helpful Video: https://www.youtube.com/watch?v=EYxAhK_eDx0&t=168s

Special Thanks: https://github.com/CoffeeCodeAndCreatine
