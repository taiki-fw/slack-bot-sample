from ...lib.logger import logger
from .index import client


def post_dm(user_slack_id: str, text="", blocks={}):
    """
    Scopes
    - chat:write
    - im:write
    """
    dm_open_res = client.conversations_open(users=user_slack_id)
    dm_channel_ids = dm_open_res["channel"]["id"]

    res = client.chat_postMessage(channel=dm_channel_ids, text=text, blocks=blocks)

    return res
