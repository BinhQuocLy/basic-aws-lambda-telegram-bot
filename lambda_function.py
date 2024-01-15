import json
import os
import requests

BOT_TOKEN = os.environ.get('TOKEN')
BOT_CHAT_ID = os.environ.get('CHATID')
BASE_URL = 'https://api.telegram.org/bot' + BOT_TOKEN

# ============================================================
# TELEGRAM API
# ============================================================
def sendMessage(text, mode=""):
    requests.post(BASE_URL + '/sendMessage', data={
        "chat_id": BOT_CHAT_ID,
        "text": text,
    })


def sendPhoto(photo):
    requests.post(BASE_URL + '/sendPhoto', data={
        "chat_id": BOT_CHAT_ID,
        "photo": photo,
    })

# ============================================================
# COMMAND HANDLERS
# ============================================================
def handle_command1(args):
    sendMessage(args)


def handle_command2(args):
    sendMessage(args)


def handle_command3(args):
    sendMessage(args)

# ============================================================
# MAIN
# ============================================================
def lambda_handler(event, context):
    try:
        messageContent = json.loads(event["body"])["message"]["text"]
        commandMap = {
            "/command1": lambda x: handle_command1(x),
            "/command2": lambda x: handle_command2(x),
            "/command3": lambda x: handle_command3(x),
        }

        tokens = messageContent.split(' ')
        command = tokens[0]
        args = []
        if len(tokens) > 1:
            args = tokens[1:]

        if command in commandMap.keys():
            commandMap[command](args)
        else:
            sendMessage(f'Command {messageContent} not found!')
    except Exception as ex:
        sendMessage(str(ex))

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
