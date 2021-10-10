from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nSend me anything and I'll send it back after removing the forwarded tag. \n\nBy @Royalbotz"

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @Royalbotz

Server : [paid vps ](https://my.racknerd.com/aff.php?aff=2985)
Channel : [Royalbotz](https://t.me/Royalbotz/84/)
Support : [tgBotsChat](t.me/tgBotsChat)
Language : [Python](www.python.org)
Developer : [Haseeb](t.me/haseeb_TG)
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("🥄Remove Caption ", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🍄 ABOUT ME", callback_data="about")
        ],
        [InlineKeyboardButton("🔍 CHANNEL", url="https://t.me/Royalbotz")],
        [InlineKeyboardButton("👥 SUPPORT", url="https://t.me/tgBotsChat")],
    ]
