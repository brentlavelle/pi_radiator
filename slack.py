from slackclient import SlackClient
import os

# slack_token = os.environ["SLACK_API_TOKEN"] or "xoxb-96210617732-EXWyhNpTXvwJ4Baf3wEF6KH8"
slack_token = "xoxb-96210617732-EXWyhNpTXvwJ4Baf3wEF6KH8"
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#brents-bot",
  text="Hello from Python! :tada:"
)
