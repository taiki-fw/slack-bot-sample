import os
import json
import requests

from ...lib.logger import logger
from .index import client

SLACK_BOT_USER_OAUTH_TOKEN = os.environ.get("BOT_USER_OAUTH_TOKEN")
SLACK_HEADERS = {
    "Content-Type": "application/json; charset=UTF-8",
    "Authorization": "Bearer {0}".format(SLACK_BOT_USER_OAUTH_TOKEN),
}


def post_dm(user_slack_id: str, text="", blocks={}):
    """
    Scopes
    - chat:write
    - im:write
    """
    # dm_open_res = client.conversations_open(users=user_slack_id)
    dm_open_res = requests.post(
        "https://slack.com/api/conversations.open",
        data=json.dumps({"token": SLACK_BOT_USER_OAUTH_TOKEN, "users": user_slack_id}),
        headers=SLACK_HEADERS,
    )
    dm_open_res = dm_open_res.json()

    dm_channel_ids = dm_open_res["channel"]["id"]

    # res = client.chat_postMessage(channel=dm_channel_ids, text=text, blocks=blocks)
    res = requests.post(
        "https://slack.com/api/chat.postMessage",
        data=json.dumps(
            {
                "token": SLACK_BOT_USER_OAUTH_TOKEN,
                "channel": dm_channel_ids,
                "text": text,
                "blocks": blocks,
            }
        ),
        headers=SLACK_HEADERS,
    )
    logger.warn(res.json())

    return res.json()
