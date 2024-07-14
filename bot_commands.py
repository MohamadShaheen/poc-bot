from telegram import Update
from telegram.ext import CallbackContext


async def start_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hi. I\'m {context.bot.first_name}. How may I help you today?')


async def test_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('This is a test response')


async def help_command(update: Update, context: CallbackContext) -> None:
    help_commands = (
        "/start - Start the bot\n"
        "/help - Show the available commands\n"
        "/test - Show the test response\n"
    )

    await update.message.reply_text(help_commands)
