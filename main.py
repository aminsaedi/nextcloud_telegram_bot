from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from webdav3.client import Client
from os import getenv, remove

server_option = {
    'webdav_hostname': getenv("WEBDAV_HOSTNAME"),
    'webdav_login': getenv("WEBDAV_LOGIN"),
    'webdav_password': getenv("WEBDAV_PASSWORD"),
    'webdav_timeout': 120
}


async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    try:
        file_id = getattr(update.message, "document", None) or getattr(
            update.message, "audio", None) or getattr(update.message, "video", None)
        file_id = file_id.file_id
        file = await context.bot.get_file(file_id=file_id)

        result = await file.download_to_drive(write_timeout=120, read_timeout=120)
        result = str(result)
        extension = result.split(".")[-1]

        client = Client(server_option)
        check_result = client.check("Telegram")
        if not check_result:
            client.mkdir("Telegram")

        client.upload_sync(
            remote_path=f"Telegram/{file_id}.{extension}", local_path=f"{result}")
        await update.message.reply_text(
            f"File uploaded to  Telegram/{file_id}.{extension}")
        remove(result)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


app = ApplicationBuilder().token(getenv("TELEGRAM_BOT_TOKEN")).build()

app.add_handler(MessageHandler(
    filters=filters.Document.ALL | filters.AUDIO | filters.VIDEO, callback=upload))

app.run_polling()
