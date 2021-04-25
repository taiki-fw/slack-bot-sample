import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

BOT_USER_OAUTH_TOKEN = os.environ["BOT_USER_OAUTH_TOKEN"]

client = WebClient(token=BOT_USER_OAUTH_TOKEN)