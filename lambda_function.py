def lambda_handler(event, context):
    try:
        messageContent = json.loads(event["body"])["message"]["text"]
        commandMap = {
            "/full": lambda _: handle_full(event["body"]),
            "/time": lambda _: handle_time(),
            "/random_image": lambda x: handle_random_image(x),
            "/random_video": lambda x: handle_random_video(x),
        }

        tokens = messageContent.split(' ')
        command = tokens[0]
        args = []
        if len(tokens) > 1:
            args = tokens[1:]

        if command in commandMap.keys():
            commandMap[command](args)
        else:
            telegram.sendMessage(f'Command {messageContent} not found!')
    except Exception as ex:
        telegram.sendMessage(str(ex))

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }