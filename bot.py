from pyrogram import Client, filters

API_ID=2345556
API_HASH="de82747f73f93def6b37"
BOT_TOKEN="7458000387:AAFy6vucKRBLHNwdDUzs"

bot = Client("mybot",api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(Client,message):
    message.reply_text("hello! I AM YOUR TESTING BOT")

bot.run()    