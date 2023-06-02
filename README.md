## Telegram-AI-bot

Some of the things being assumed here
1. You have installed python3.7 or above.
2. You have created a virtual environment (recommended but not mandatory).
3. You have used pip to install from the requirements.txt file.

<br>

## Getting Bot token
> **Warning** Do not expose the `BOT_TOKEN`    

**Link for generating BOT_TOKEN**: https://medium.com/geekculture/generate-telegram-token-for-bot-api-d26faf9bf064

<br>

## Getting Google Bard API KEY
> **Warning** Do not expose the `__Secure-1PSID` 
 
Since Google Bard is being used as the AI backend, you need to fetch the **BARD_API_KEY** from Bard.
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

Note that while I referred to `__Secure-1PSID` value as an API KEY for convenience, it is not an officially provided API KEY. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

<br>

## Create .env file
Creating .env file at the base directory from which the **BOT_TOKEN** and **BARD_API_KEY** will be fetched.
```env
BOT_TOKEN=xxxxxxxxxx
BARD_API_KEY=xxxxxxxxxx
```

<br>

## Usage 
From the base directory run:
```bash
python3 -m src.ai_telegram_bot_async
```

<br>