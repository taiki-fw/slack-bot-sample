from fastapi import FastAPI, Request

from .Slack.util.lib import post_dm
from .Slack.signature import slack_signature
from .Slack.blocks.notification import create_thread_by_reacted

app = FastAPI()

my_account = {"name": "たいき", "id": "UNLKCAJUC"}
users = [my_account, {"name": "Gmail1", "id": "U020NEYCYNL"}]


@app.post("/slack/commands")
async def slack_commands(req: Request):

    if not await slack_signature(req):
        return {"message": "Bad Request!"}

    res = [create_thread_by_reacted("野菜を育てたい", users[1]["name"])]

    for user in users:
        post_dm(user["id"], "chat bot test message", res)

    return None
