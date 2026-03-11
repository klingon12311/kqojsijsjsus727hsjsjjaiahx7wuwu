from PyroUbot import *

__MODULE__ = "asupan"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}asupan</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cewek</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴇᴡᴇᴋ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cowok</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴏᴡᴏᴋ ʀᴀɴᴅᴏᴍ
  
"""

@PY.UBOT("asupan")
async def video_asupan(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ...</b>")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@jejudjdisjsiejsisjjs", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("cewek")
async def photo_cewek(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("jmx")
async def photo_cowok(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ member jmx...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@uwuwhhshs", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
