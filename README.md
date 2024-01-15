# Basic, AWS Lambda + Telegram Bot

A basic serverless solution for making a telegram bot, without command line.

**Requirements:**
- An AWS account.
- A Telegram account.

## 1. Create a Telegram bot

**Step 1 - Meet "BotFather"**: Search for the bot **@BotFather** $\rightarrow$ Type **/start**.

**Step 2 - Create a bot**: Follow the instructions to create a bot.

**Step 3 - Say hi to your bot**: Search for your bot and message it, to create a conversation.

**Step 4 - Get the bot's Token**: Message **@BotFather** $\rightarrow$ Type **/mybots** $\rightarrow$ Choose the bot $\rightarrow$ **API Token**.

**Step 5 - Get the conversation id**:
- Access the URL: [https://api.telegram.org/bot`TOKEN`/getUpdates]()
- Find the value of **chat.id** property

Now you have 2 important secrets: `TOKEN` and `CHAT_ID`.

## 2. Create a AWS Lambda function
**Step 1 - Create a function**
- Go to `AWS Lambda` $\rightarrow$ `Functions` $\rightarrow$ `Create function`
- In the *Create function* page:
  - Choose `Author from scratch`.
  - **Function name**:  Give the function a name.
  - **Runtime**: `Python 3.10`
  - **Architecture**: `x86_64`
  
**Step 3 - Give your function some code**
- In the *Your-Function* page: Code source section, paste the source code from file `lambda_function.py` in the repo.

**Step 4 - Create a runtime layer** (Give your python function additional packages)
- In *Your-Function* page: Layers section, **Add a layer**.
- In *Add a layer* page: Layer source, **create a new layer** (The small text).
- In *Create layer* page: 
  - Upload the file `python3.10_packages.zip` in the repo. (This zip file contains some PIP packages: requests, pytz, pandas, numpy).
  - **Compatible architectures**: `x86_64`.
  - **Compatible runtimes**: `Python 3.10`.
- Return to your *Your-Function* page: **Add a layer**.
- In *Add a layer* page: Layer source, **Custom layers** $\rightarrow$ Choose your layer in the following dropdown.

**Step 5 - Set environment variables** (Your 2 secrets)
- In the *Your-Function* page $\rightarrow$ Configuration tab $\rightarrow$ Environment variables $\rightarrow$ Edit.
  - CHATID: ...
  - TOKEN: ...

## 3. Hook your Telegram bot to your AWS Lambda function
**Step 1 - Get your function URL**
- In the *Your-Function* page $\rightarrow$ Configuration tab $\rightarrow$ Function URL $\rightarrow$ Create function URL:
  - Auth type: NONE

**Step 2 - Set webhook**
- Access the URL: [https://api.telegram.org/bot`TOKEN`/setWebhook?url=`FUNCTION_URL`]()

<hr/>

Start chatting! ...
