import pytest
from unittest.mock import AsyncMock, MagicMock
from bot_commands import *


@pytest.mark.asyncio
async def test_start_command():
    update = MagicMock()
    context = MagicMock()
    context.bot.first_name = 'Mohamad Shaheen'
    update.message.reply_text = AsyncMock()

    await start_command(update, context)
    update.message.reply_text.assert_called_once_with("Hi. I'm Mohamad Shaheen. How may I help you today?")


@pytest.mark.asyncio
async def test_api_command():
    update = MagicMock()
    context = MagicMock()
    update.message.reply_text = AsyncMock()

    await api_command(update, context)
    update.message.reply_text.assert_called_once_with('Hello! I am the FastAPI server, we successfully connected!')


@pytest.mark.asyncio
async def test_insert_command():
    update = MagicMock()
    context = MagicMock()
    update.message.reply_text = AsyncMock()

    await insert_command(update, context)
    assert update.message.reply_text.call_args[0][0].startswith('String inserted: ')


@pytest.mark.asyncio
async def test_test_command():
    update = MagicMock()
    context = MagicMock()
    update.message.reply_text = AsyncMock()

    await test_command(update, context)
    update.message.reply_text.assert_called_once_with('This is a test response')


@pytest.mark.asyncio
async def test_help_command():
    update = MagicMock()
    context = MagicMock()
    update.message.reply_text = AsyncMock()

    await help_command(update, context)
    update.message.reply_text.assert_called_once_with((
        '/start - Start the bot\n'
        '/api - Make a request to the API\n'
        '/insert - Insert a new string to database\n'
        '/test - Show the test response\n'
        '/help - Show the available commands'
    ))
