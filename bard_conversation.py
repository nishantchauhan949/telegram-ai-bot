#!/usr/bin/env python

from requests import Session
from bardapi.core import Bard

from settings import BARD_API_KEY, logger

session = Session()
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}
session.cookies.set("__Secure-1PSID", BARD_API_KEY)
bard = Bard(session=session, timeout=30, token=BARD_API_KEY)


def get_response_from_bard(input_text, func_name='') -> str:
    """
    The get_response_from_bard function takes in a string of text and returns the response from the BARD API.
        Args:
            func_name:
            input_text (str): The user's question to be sent to the BARD API.

    Args:

    Returns:
        Response from BARD

    Doc Author:
        Trelent
    """
    func_name = func_name + '.get_response_from_bard()' if func_name else 'get_response_from_bard()'
    prepend = f'{func_name} :: '
    try:
        input_text += '\nPlease keep it under 4096 characters.'
        # Send an API request and get a response.
        response = bard.get_answer(input_text)
        # logger.info(f'{prepend} type(response) :: {type(response)}')
        # logger.info(f'response :: {response}')
        return response['content']
    except Exception as e:
        logger.error(f'{prepend} Some unexpected error occurred: {e}')


if __name__ == '__main__':
    get_response_from_bard('What is google?')
