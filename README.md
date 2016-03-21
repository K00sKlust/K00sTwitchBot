# K00sTwitchBot
An irc-bot written in Python 2.7. It's very easy to create functions for it.

## Configure your bot
Rename SettingsTemplate.py to Settings.py!

### Twitch API
This key is required. Probably you want to create a new Twitch account for your bot first.
Then, while logged in with your bot's account, go to https://twitchapps.com/tmi/ and get your twitch-oauth.
Copy it (Including 'oauth:') to you Settings.py file. (Instead of "oauth:##############################")

### WOT_API
It is possible to check links via WebOfTrust (myWOT.com). 
If you want the links to be checked, you have to create an account at myWOT.com and get an API key (http://www.mywot.com/profile/api).
Then, paste your fresh key between the brackets after 'WOT_KEY = ' in the settings file.
Also, do not forget to set CHECK_LINKS to True.

## Create commands
All commands are in the folder './commands/src'.
If you want to create a new one, all you have to do is to copy the template, rename the file and edit it. That's all!
It's save to just remove a command file.
