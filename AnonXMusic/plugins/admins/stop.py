from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from strings.filters import command
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import set_loop
from AnonXMusic.utils.decorators import AdminRightsCheck
from pyrogram.enums import ChatType
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    command(["/stop","كافي","ايقاف","انهاء"]) & filters.group & ~BANNED_USERS
)
@app.on_message(
    command(["/stop","كافي","ايقاف","انهاء"]) & filters.channel & ~BANNED_USERS
)# تعديل فلتر القناة @V_V_G
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Anony.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    if message.chat.type == ChatType.CHANNEL:
       await message.reply_text(
        _["admin_36"]
       )
    else:
         await message.reply_text(
         _["admin_9"].format(message.from_user.mention)
         )
