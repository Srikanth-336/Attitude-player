# https://t.me/Srikanth_36

from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(command(["start", f"start@Sriki_Music_Player_Bot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1f3bb73d56a201431783.jpg",
        caption=f"""
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂ᴊᴏɪɴ ᴏᴜʀ ꜱᴜᴩᴩᴏʀᴛ🥂🔥", url=f"https://t.me/Kings_World_36")
                ]
            ]
        ),
    )


@Client.on_message(command(["help", f"help@Attitude_Player_Bot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1f3bb73d56a201431783.jpg",
        caption=f"""
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂ᴄʟɪᴄᴋ ʜᴇʀᴇ ꜰᴏʀ ʜᴇʟᴩ🥂🔥", url=f"https://t.me/Kings_World_36")
                ]
            ]
        ),
    )
