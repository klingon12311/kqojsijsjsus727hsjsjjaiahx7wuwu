from PyroUbot import *

__MODULE__ = "ᴛᴏᴜʀʟ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Tourl

perintah : <code>{0}tourl</code> [ replay media ]
    mengupload media ke link</blockquote></b>

"""

@PY.UBOT("tourl|tg")
async def _(client, message):
    reply_message = message.reply_to_message
    if not reply_message:
        return await message.reply("Please reply to a media message to upload.")
    try:
        url = await upload_media(message)
    except Exception as e:
        return await message.reply(str(e))
    return await message.reply(f"-- succes upload : <a href='{url}'>link potonya --</a>", disable_web_page_preview=True)
        
