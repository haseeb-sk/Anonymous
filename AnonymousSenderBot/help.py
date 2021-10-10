import random
from pyrogram import Client, filters


STICKERS = ["CAACAgUAAxkBAAEGPnNgPcbx75_XWKMwgMtZIJlvpUa9gAACsQIAAkzoiVdQPozmP6_Gjx4E", "CAACAgEAAxkBAAJnA2FiQlc2S-2PlBVKdgcxiYAVURxWAAIqAQACwl0RRx0DdhnThgv8HgQ"]


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def _help(_, msg):
	STICKER = random.choice(STICKERS)
	await msg.reply_sticker(STICKER)
