from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!
I am 𝙻𝚄𝙽𝙰 VC Music Player, play music in your Telegram groups.
 ❤
pleas add 𝙻𝚄𝙽𝙰 assistant bot @Luna_assistant_bot
and give permission to manage voice chat to 
add Admin.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "COMMAND", url="https://telegra.ph/𝙰ₚₐᵣᵢₕᵢₜₕₐ𝙽𖧷-04-13",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👩‍🦯 OWNER", url="https://t.me/stranger_of_telegram"
                    ),
                    InlineKeyboardButton(
                        "🎵 SONG BOT", url="https://t.me/Nora_song_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✨JOIN CHANNEL", url="https://t.me/Love_Birds_Official"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
