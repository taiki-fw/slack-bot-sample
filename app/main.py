from fastapi import FastAPI, Request

from .Slack.signature import slack_signature

app = FastAPI()


@app.post("/slack/commands")
async def slack_commands(req: Request):

    if not await slack_signature(req):
        return {"message": "Bad Request!"}

    return {"Hello": "World"}
