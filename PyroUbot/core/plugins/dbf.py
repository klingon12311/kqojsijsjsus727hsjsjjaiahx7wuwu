from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if message.from_user.id not in await get_seles():
        return await Tm.edit(
            "ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ"
        )
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if get_id in premium:
        return await Tm.edit("ᴅɪᴀ sᴜᴅᴀʜ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ")
    added = await add_prem(get_id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(get_id, expired)
        await Tm.edit(
            f"✅ {get_id} ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ sᴇʟᴀᴍᴀ {get_bulan} ʙᴜʟᴀɴ\n\nsɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅɪ @{bot.me.username}"
        )
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {get_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "👤 ᴘʀᴏғɪʟ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "ᴘʀᴏғɪʟ 👤", callback_data=f"profil {get_id}"
                        ),
                    ],
                ]
            ),
        )
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await Tm.edit("<b>ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    removed = await remove_prem(user.id)
    if removed:
        await Tm.edit(f"<b> ✅ {user.mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"<blockquote><b>• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code></blockquote></b>"
        except Exception:
            continue
        text += f"<b><blockquote>{userlist}\n</blockquote></b>"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blaclist(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        chat_id = message.chat.id
        blacklist = await get_chat(client.me.id)
        if chat_id in blacklist:
            return await Tm.edit("ɢʀᴏᴜᴘ ɪɴɪ sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʙʟᴀᴄᴋʟɪsᴛ")
        add_blacklist = await add_chat(client.me.id, chat_id)
        if add_blacklist:
            return await Tm.edit(
                f"<b>{message.chat.title} ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ᴊᴇᴍʙᴏᴛ</b>\n\n<b>USERBOT 10K/BULAN BY @USERBOTDIN</b>"
            )
        else:
            return await Tm.edit("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
    else:
        return await Tm.edit("ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ʙᴇʀғᴜɴɢsɪ ᴅɪ ɢʀᴏᴜᴘ sᴀJᴀ")


async def del_blacklist(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        try:
            if not get_arg(message):
                chat_id = message.chat.id
            else:
                chat_id = int(message.command[1])
            blacklist = await get_chat(client.me.id)
            if chat_id not in blacklist:
                return await Tm.edit(
                    f"{message.chat.title} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴊᴇᴍʙᴏᴛ"
                )
            del_blacklist = await remove_chat(client.me.id, chat_id)
            if del_blacklist:
                return await Tm.edit(f"<b>{chat_id} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴊᴇᴍʙᴏᴛ</b>\n\n<b>USERBOT 10K/BULAN BY @USERBOTDIN</b>")
            else:
                return await Tm.edit("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
        except Exception as error:
            return await Tm.edit(error)
    else:
        return await Tm.edit("ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ʙᴇʀғᴜɴɢsɪ ᴅɪ ɢʀᴏᴜᴘ sᴀJᴀ")


async def get_blacklist(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    msg = f"<b>• ᴛᴏᴛᴀʟ ʙʟᴀᴄᴋʟɪsᴛ {len(await get_chat(client.me.id))}</b>\n\n"
    for X in await get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await Tm.delete()
    await message.reply(msg)


async def rem_all_blacklist(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs....</b>", quote=True)
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit("<b>ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ ᴀɴᴅᴀ ᴋᴏsᴏɴɢ</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await msg.edit("<b>sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ᴊᴇᴍʙᴏᴛ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("sᴜᴅᴀʜ ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(f"<b>✅ {user.mention} ᴛᴇʟᴇʜ ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ</b>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</n>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit("ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"{user.mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def get_seles_user(cliebt, message):
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{user}\n"
    if not text:
        await message.reply_text("Tᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʜᴀʀɪ</b>")
    elif user_id not in ubot._get_my_id:
        return await Tm.edit(f"<b>{user_id} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sʏsᴛᴇᴍ</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"{get_id} ᴛᴇʟᴀʜ ᴅɪᴀᴋᴛɪғᴋᴀɴ sᴇʟᴀᴍᴀ {get_day} ʜᴀʀɪ.")


async def expired_cek(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ")
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"{user_id} ʙᴇʟᴜᴍ ᴅɪᴀᴋᴛɪғᴋᴀɴ.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(
            f"{user_id} ᴀᴋᴛɪғ ʜɪɴɢɢᴀ {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. sɪsᴀ ᴡᴀᴋᴛᴜ ᴀᴋᴛɪғ {remaining_days} ʜᴀʀɪ."
        )


async def un_expired(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    await rem_expired_date(user.id)
    return await Tm.edit(f"<b>✅ {user.id} ᴇxᴘɪʀᴇᴅ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs</b>")
