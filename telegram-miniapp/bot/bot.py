from pyrogram import Client, filters

API_ID = 27806628
API_HASH = "25d88301e886b82826a525b7cf52e090"
BOT_TOKEN = "8314360850:AAFGX0fzrTVHXQ7A5jgXqGcjMk6DceTzILA"

app = Client("miniapp_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    web_app = {
        "text": "Open Mini App",
        "web_app": {"url": "https://trading-vs-trading-mini-app-dnke.onrender.com"}
    }

    await message.reply(
        "Click below to open Mini App",
        reply_markup={"inline_keyboard": [[web_app]]}
    )

@app.on_message(filters.web_app_data)
async def webdata(client, message):
    await message.reply(f"Received: {message.web_app_data.data}")

app.run()
