import os
import lorem
import requests
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import CallbackContext

load_dotenv()

server_url = os.getenv('SERVER_URL')


async def start_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hi. I\'m {context.bot.first_name}. How may I help you today?')


async def api_command(update: Update, context: CallbackContext) -> None:
    try:
        response = requests.get(server_url)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text('No such endpoint exists!')


async def insert_command(update: Update, context: CallbackContext) -> None:
    try:
        random_sentence = lorem.sentence()
        response = requests.post(f'{server_url}telegram-bot/string/?string={random_sentence.replace(' ', '%20')}')
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text('No such endpoint exists!')


async def test_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('This is a test response')


async def help_command(update: Update, context: CallbackContext) -> None:
    help_commands = (
        '/start - Start the bot\n'
        '/api - Make a request to the API\n'
        '/insert - Insert a new string to database\n'
        '/test - Show the test response\n'
        '/help - Show the available commands'
    )

    await update.message.reply_text(help_commands)
