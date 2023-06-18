import asyncio
import openai
from dotenv import load_dotenv

from telegram_ai_bot.config.settings import OPENAI_API_KEY, logger

load_dotenv('../.env')

openai.api_key = OPENAI_API_KEY


# models = openai.Model.list()


async def get_response_from_chatgpt(input_text, func_name='') -> str:
    """
    The get_response_from_chatgpt function takes in a string of text and returns the response from the ChatGPT API.
        Args:
            func_name:
            input_text (str): The user's question to be sent to the BARD API.
    get_bard_object
    Args:

    Returns:
        Response from C

    Doc Author:
        Trelent
    """
    func_name = func_name + '.get_response_from_chatgpt()' if func_name else 'get_response_from_chatgpt()'
    prepend = f'{func_name} :: '
    try:
        # Send an API request and get a response.
        completion = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{input_text}"}
            ]
        )
        return completion.choices[0].message['content']
    except Exception as e:
        logger.error(f'{prepend} Some unexpected error occurred: {e}')


if __name__ == '__main__':
    asyncio.run(get_response_from_chatgpt('Who is Wolverine?'))
