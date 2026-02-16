from pyrogram import Client, filters

API_ID = 12345
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("miniapp_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    web_app = {
        "text": "Open Mini App",
        "web_app": {"url": "https://your-domain.com"}
    }

    await message.reply(
        "Click below to open Mini App",
        reply_markup={"inline_keyboard": [[web_app]]}
    )

@app.on_message(filters.web_app_data)
async def webdata(client, message):
    await message.reply(f"Received: {message.web_app_data.data}")

app.run()
