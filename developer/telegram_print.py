from fastapi import HTTPException, status
from telegram import Bot

# Create a Telegram Bot:
# Open Telegram and search for the "BotFather" bot.
# Start a chat with BotFather and use the /newbot command to create a new bot.

# Get Chat ID:
# Send the /my_id to telegram bot @get_id_bot.
# To get group chat ID, first add the bot to the group, then send /my_id in the group.


async def telegram_print(text):
    try:
        # Check if the text is empty or None
        if not text:
            return

        # Your bot token here
        token = ""
        # Your chat ID here
        chat_id = ""

        # Create a new instance of the Telegram Bot
        bot = Bot(token)
        # Send a message to the specified chat ID
        await bot.send_message(chat_id, text)

    except Exception as e:
        # Handle any exceptions that occur during execution
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
