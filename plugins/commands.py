# By @Kalam_Company
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💬 Feedback 💬", url="https://t.me/kalam_feedback_bot"),
                        InlineKeyboardButton("↗️ Share Me ↗️", url="tg://msg?text=Hai%20Friend%20%E2%9D%A4%EF%B8%8F%2C%0AToday%20I%20just%20found%20out%20an%20Simple%20and%20Powerful%20%2A%2AYouTube%20URL%20Uploader%20Bot%2A%2A%20for%20Free%F0%9F%A5%B0.%20%0A%2A%2ABot%20Link%20%3A%2A%2A%20%40Kalam_YT_Bot%20%F0%9F%94%A5"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🔥 Developer 🔥",
                             url="https://t.me/kalam_company",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True
            reply_to_message_id=update.message_id
       )


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True
            reply_to_message_id=update.message_id
       )

