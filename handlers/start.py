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
I am π»ππ½π° VC Music Player, play music in your Telegram groups.
 β€
pleas add π»ππ½π° assistant bot @Luna_assistant_bot
and give permission to manage voice chat to 
add Admin.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "COMMAND", url="https://telegra.ph/π°ββα΅£α΅’βα΅’βββπ½π§·-04-13",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π©βπ¦― OWNER", url="https://t.me/stranger_of_telegram"
                    ),
                    InlineKeyboardButton(
                        "π΅ SONG BOT", url="https://t.me/Nora_song_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β¨JOIN CHANNEL", url="https://t.me/Love_Birds_Official"
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
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
