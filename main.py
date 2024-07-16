from bot_commands import *
from telegram.ext import ApplicationBuilder, CommandHandler


bot_token = os.getenv('BOT_TOKEN')


def main():
    if bot_token is None:
        print('Bot token not found. Please save your bot token in .env file under the name BOT_TOKEN')
        return

    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('api', api_command))
    application.add_handler(CommandHandler('insert', insert_command))
    application.add_handler(CommandHandler('test', test_command))
    application.add_handler(CommandHandler('help', help_command))

    application.run_polling()


if __name__ == '__main__':
    main()
