def create_thread_by_reacted(posted_title, person):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "こんばんは！\nあなたの投稿「"
            + posted_title
            + " 」に"
            + person
            + "さんからリアクションが届きました。",
        },
    }