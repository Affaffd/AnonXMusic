import asyncio
from pyrogram import Client, filters
from strings.filters import command
from typing import Union
#تعديل مبرمج سورس ايثون
from pyrogram.types import Message, VideoChatEnded
from AnonXMusic import app
#تعديل مبرمج سورس ايثون
@app.on_message(filters.video_chat_started)
async def babloo(client: Client, message: Message): 
      Startt = "بدأت المحادثة الصوتية 👤"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def bablo(client: Client, message: Message): 
      Enddd = "- تم انهاء المحادثه الصوتية 🙁"
      await message.reply_text(Enddd)
    
@app.on_message(command("لمار"))
async def throw_dice(client, message: Message): 
    await message.reply_text("عيونها")
@app.on_message(command("هلا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هلا فيك/ي عمري .")


#@app.on_message(command(["عتكططجنهعة"])
 #   & filters.group
  #  & ~filters.edited
#)
#async def ahmad(client: Client, message: Message):
   # await message.reply_video(
  #      video="https://te.legra.ph/file/dbcf6af7538952498c41c.mp4",
 #       caption=f"""- فرررررررطت ضحك قمنقلععع 😂""",
 #       reply_markup=InlineKeyboardMarkup(
       # [
     #       [
       #         InlineKeyboardButton("‹ ضيفني لكروبك ›", url=f"https://t.me/MAE_Rbot?startgroup=true",
    #            ),
      #      ],
       #     [
     #           InlineKeyboardButton("‹ دخول البوت ›", url=f"https://t.me/MAE_Rbot"),
     #       ],
     #       ]
       # ),
#    )
