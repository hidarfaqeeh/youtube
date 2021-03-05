from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f""مرحبا بك عزيزي كل كما عليك فعله هو ارسال رابط الفديو يوتيوب فقط وانا ساقوم بتحميله لك"
    await message.reply_text(helptxt)
