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

## Third-Party Package: Bard-API

Bard-API is a powerful Python library that provides functionality for using Bard's webserver for getting your answers.

The Bard-API library is released under the MIT License. Please refer to the Bard-API's license file for detailed terms and conditions.

For more information about Bard-API, please visit the [Bard-API GitHub repository](https://github.com/dsdanielpark/Bard-API).

<br>

## Shifting Service Policies: Bard and Google's Dynamics 
Bard's service status and Google's API interfaces are in constant flux. *The number of replies is currently limited, but certain users,* such as those utilizing VPNs or proxy servers, have reported slightly higher message caps. Adaptability is crucial in navigating these dynamic service policies. Please note that the cookie values used in this package are not official API values.

<br>

### Important Notice
  The user assumes all legal responsibilities associated with using the BardAPI package and Telegram-AI-bot project. This Python project merely facilitates easy access to Google Bard Telegram Bot for developers. Users are solely responsible for managing data and using the package appropriately. For further information, please consult the Google Bard Official Documentation.
    
### Caution
This Python project is not an official Google package or API service. It is not affiliated with Google and uses Google account cookies, which means that excessive or commercial usage may result in restrictions on your Google account. The project was created to support developers in testing functionalities due to delays in the official Google package. However, it should not be misused or abused. Please be cautious and refer to the Readme for more information.
  

## License

This project is licensed under the GNU General Public License (GPL) version 3.0. By using, contributing, or redistributing this project, you agree to abide by the terms and conditions of the GPL. You can find a copy of the license in the [LICENSE](LICENSE) file.
