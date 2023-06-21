#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from telegram_ai_bot.config.settings import BOT_TOKEN, logger
from telegram_ai_bot.src.bard_conversation import get_response_from_bard
from telegram_ai_bot.src.chatgpt_apis import get_response_from_chatgpt

BARD_QUERY, BARD_QUERY_RECURSION, CHATGPT_QUERY, CHATGPT_QUERY_RECURSION, BARD_OR_CHATGPT = range(5)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, func_name='') -> int:
    """
    The start function is the first function that will be called when a user interacts with the bot.
    Its purpose is to send a message to the user, and then return an integer value representing which
    state we want our conversation handler to move into next. In this case, we are returning BARD_QUERY,
    which means that after sending this message, our conversation handler will call bard_query_handler().

    Args:
        func_name:
        update: Update: Get the update object
        context: ContextTypes.DEFAULT_TYPE: Pass the context of the message

    Returns:
        bard_query_handler()

    Doc Author:
        Trelent
    """
    func_name = func_name + '.get_response_from_bard()' if func_name else 'get_response_from_bard()'
    try:
        user = update.message.from_user.first_name
        prepend = f'{user} :: {func_name},'
        logger.info(f'{prepend} Start prompt received from user')
        text = """Please choose either /bard or /chatgpt, based on your preference.
        
Some things to note:
1. Bard can crawl the web to get latest information available but it can hallucinate.

2. ChatGPT cannot crawl the web and it's data cut off was Sept 2021, but responses from ChatGPT are generally better.

3. Hallucination rate: Bard > ChatGPT

4. You can use /stop and /cancel at any time to end the conversation."""
        await update.message.reply_text(
            text=text,
        )

        return BARD_OR_CHATGPT
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return ConversationHandler.END


async def bard_or_chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    func_name = 'bard_or_chatgpt()'
    try:
        user = update.message.from_user.first_name
        prepend = f'{user} :: {func_name},'
        user_query = update.message.text
        if user_query == '/bard':
            logger.info(f'{prepend} User wants to chat with Bard')
            await update.message.reply_text(
                text="Bard will take your prompts now.\n\nMake sure to use /stop after your conversation ends."
            )
            return BARD_QUERY
        elif user_query == '/chatgpt':
            logger.info(f'{prepend} User wants to chat with ChatGPT')
            await update.message.reply_text(
                text="ChatGPT will take your prompts now.\n\nMake sure to use /stop after your conversation ends."
            )
            return CHATGPT_QUERY
        else:
            logger.info(f'{prepend} User ended the conversation')
            return ConversationHandler.END
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return ConversationHandler.END


async def bard_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    The bard_query_handler function is a conversation handler that takes in user input
    and returns the response from BARD.
        The function will continue to take in user input until the user types '/stop' or '/cancel'.


    Args:
        update: Update: Access the update object, which contains information about the incoming message
        context: ContextTypes.DEFAULT_TYPE: Pass the context of the conversation

    Returns:
        ConversationHandler

    Doc Author:
        Trelent
    """
    func_name = 'bard_query_handler()'
    try:
        user = update.message.from_user.first_name
        prepend = f'{user} :: {func_name},'
        user_query = update.message.text
        if user_query in ['/stop', '/cancel']:
            logger.info(f'{prepend} User ended the conversation')
            return ConversationHandler.END
        logger.info(f'{prepend} User Query :: {user_query}')
        bard_response = await get_response_from_bard(input_text=user_query, func_name=func_name)
        logger.info(f'{prepend} Response :: {bard_response}')
        await update.message.reply_text(text="Here's your response!")
        await update.message.reply_text(text=bard_response)
        return BARD_QUERY_RECURSION
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return ConversationHandler.END


async def chatgpt_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    The chatgpt_query_handler function is a conversation handler that takes in user input
    and returns the response from BARD.
        The function will continue to take in user input until the user types '/stop' or '/cancel'.


    Args:
        update: Update: Access the update object, which contains information about the incoming message
        context: ContextTypes.DEFAULT_TYPE: Pass the context of the conversation

    Returns:
        ConversationHandler

    Doc Author:
        Trelent
    """
    func_name = 'chatgpt_query_handler()'
    try:
        user = update.message.from_user.first_name
        prepend = f'{user} :: {func_name},'
        user_query = update.message.text
        if user_query in ['/stop', '/cancel']:
            logger.info(f'{prepend} User ended the conversation')
            return ConversationHandler.END
        logger.info(f'{prepend} User Query :: {user_query}')
        chatgpt_response = await get_response_from_chatgpt(input_text=user_query, func_name=func_name)
        logger.info(f'{prepend} Response :: {chatgpt_response}')
        await update.message.reply_text(text="Here's your response!")
        await update.message.reply_text(text=chatgpt_response)
        return CHATGPT_QUERY_RECURSION
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return ConversationHandler.END


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    The cancel_handler function is a callback function that ends the conversation.
        It is called when the user sends /cancel or presses the Cancel button in an inline keyboard.
        The cancel_handler function takes two arguments: update and context, which are passed by Python-Telegram-Bot.

    Args:
        update: Update: Pass the update object to the function
        context: ContextTypes.DEFAULT_TYPE: Pass the context of the conversation

    Returns:
        ConversationHandler

    Doc Author:
        Trelent
    """
    func_name = 'cancel_handler()'
    try:
        user = update.message.from_user.first_name
        prepend = f'{user} :: {func_name},'
        logger.info(f'{prepend} conversation ended.')
        await update.message.reply_text("Bye! I hope we can talk again.")
        return ConversationHandler.END
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return ConversationHandler.END


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    The unknown function is a fallback function that will be called when the bot receives an unknown command.
    It simply sends a message to the user saying &quot;Sorry, I didn't understand that command.&quot;


    Args:
        update: Update: Pass the update object to the handler
        context: ContextTypes.DEFAULT_TYPE: Tell the bot what type of context to expect

    Returns:
        A message to the user that the bot did not understand their command

    Doc Author:
        Trelent
    """
    func_name = 'unknown()'
    try:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Sorry, I didn't understand that command.")
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return ConversationHandler.END


def main() -> None:
    """
    The main function of the bot.

    Args:

    Returns:
        None

    Doc Author:
        Trelent
    """
    func_name = 'main()'
    try:
        prepend = f'{func_name},'
        # Create the Application and pass it your bot's token.
        application = Application.builder().token(BOT_TOKEN).build()

        # Add conversation handler
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler(command=['start', 'ask'], callback=start)],
            states={
                BARD_OR_CHATGPT: [CommandHandler(command=['bard', 'chatgpt'], callback=bard_or_chatgpt)],
                BARD_QUERY: [MessageHandler(filters=filters.ALL,
                                            callback=bard_query_handler)],
                BARD_QUERY_RECURSION: [MessageHandler(filters=filters.TEXT & ~filters.COMMAND,
                                                      callback=bard_query_handler)],
                CHATGPT_QUERY: [MessageHandler(filters=filters.ALL,
                                               callback=chatgpt_query_handler)],
                CHATGPT_QUERY_RECURSION: [MessageHandler(filters=filters.TEXT & ~filters.COMMAND,
                                                         callback=chatgpt_query_handler)],
            },
            fallbacks=[CommandHandler(command=['stop', 'cancel'], callback=cancel_handler),
                       MessageHandler(filters=filters.COMMAND, callback=unknown)],
        )

        unknown_handler = MessageHandler(filters=filters.COMMAND, callback=unknown)

        application.add_handler(conv_handler)
        application.add_handler(unknown_handler)

        logger.info(f'{prepend} Starting the bot.')
        # Run the bot until the user presses Ctrl-C
        application.run_polling()
    except Exception as e:
        logger.error(f'{func_name} :: Some unexpected error occurred: {e}')
        return


if __name__ == "__main__":
    main()
