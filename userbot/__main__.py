import os
import re
import sys
from pathlib import Path

import telethon.utils
from telethon import Button, TelegramClient, custom, events
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import LOGS, LEGENDversion, bot
from userbot.Config import Config
from userbot.utils import (
    load_abuse,
    load_addons,
    load_module,
    start_assistant,
    start_spam,
)
from var import Var

l2 = Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"
l1 = Config.COMMAND_HAND_LER


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"LEGEND_STRING - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting LegendBot ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 LegendBot Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")


async def module():
    import glob

    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


assistant = os.environ.get("ASSISTANT", None)


async def assistants():
    if assistant == "ON":
        import glob

        path = "userbot/plugins/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))
    else:
        print("⚠️Assistant Not Loaded⚠️")


addon = os.environ.get("EXTRA_PLUGIN", None)


async def addons():
    if addon == "ON":
        import glob

        path = "userbot/plugins/Xtra_Plugin/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        print("⚠️Addons Not Loading⚠️")


abuse = os.environ.get("ABUSE", None)


async def abuses():
    if abuse == "ON":
        import glob

        path = "userbot/plugins/Abuse/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                load_abuse(shortname.replace(".py", ""))
    else:
        print("⚠️Abuse Not Loading⚠️")


spam = os.environ.get("SPAM", None)


async def spams():
    if spam == "ON":
        import glob

        path = "userbot/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")


tgbot = bot.tgbot


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="Hello sir/miss,\nHow can i help u",
            buttons=[
                [
                    custom.Button.inline("🙇 Usᴇʀs Lɪsᴛ 🙇", data="users"),
                    custom.Button.inline("👾 Cᴏᴍᴍᴀɴᴅs ✘👾", data="gibcmd"),
                ],
                [
                    Button.url(" Support ", "https://t.me/Legend_Userbot"),
                    Button.url(" Updates ", "https://t.me/Official_LegendBot"),
                ],
                [custom.Button.inline("⚙ Sᴇᴛᴛɪɴɢs ⚙", data="osg")],
                [custom.Button.inline("⚜ Hack ⚜", data="hack")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                [
                    custom.Button.inline(
                        "🚫 Cʟᴏsᴇ 🚫",
                        data="close_vcc",
                    )
                ],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close_vcc")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "⚜List Of Total Users In Bot.⚜ \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏ Eᴅɪᴛ Iɴ Aʟɪᴠᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ Nᴀᴍᴇ ✘", data="name"),
                    Button.inline("✘ Aʟɪᴠᴇ Pɪᴄ ✘", data="img"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"img")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜɪᴄʜ Aʟɪᴠᴇ Pɪᴄ Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cʜᴀɴɢᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Lêɠêɳ̃dẞø†](https://t.me/Official_LegendBot)**",
            buttons=[
                [Button.inline("✘ Dᴇғᴀᴜʟᴛ Aʟɪᴠᴇ ✘", data="aimg")],
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="alive")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"name")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Yᴏᴜ Cᴀɴ Cʜᴀɴɢᴇ Aʟɪᴠᴇ Nᴀᴍᴇ..!!\nJᴜsᴛ Fᴏʟʟᴏᴡ Tʜᴇ Sᴛᴇᴘs.! \n\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Pʀᴏʙʟᴇᴍ Oʀ Dᴏᴜʙᴛ Dᴏ Jᴏɪɴ [Lêɠêɳ̃dẞø†](http://t.me/Official_LegendBot)\n\nJᴜsᴛ Tʏᴘᴇ\n\n`.set var ALIVE_NAME <Name>`\n\nRᴇᴍᴏᴠᴇ `<>` Tʜɪs.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="alive")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dalive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dalive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"permit")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**What do you want to edit in Pm Permit?\nFor Any kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Tᴇxᴛ ✘", data="text"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Mᴇᴅɪᴀ ✘", data="media"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"media")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit Pic..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot) type\n\n`.set var PM_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="permit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"text")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit message..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var PM_MSG <Text>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="permit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can change anything from these..!!\nAny kind for help do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ ✘", data="alive"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ ✘", data="permit"),
                ],
                [
                    Button.inline("✘ Chat Bot ✘", data="chat"),
                    Button.inline("✘ Vc Bot ✘", data="Vc_Bot"),
                ],
                [Button.inline("✘ Cʟᴏsᴇ ✘", data="close")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "🇮🇳Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def users(event):
    await event.delete()
    grabon = "I am Giving U Full Power To Hack Anyone Through String session\nClick Here 👉/hack."
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"v_hack")))
async def users(event):
    await event.delete()
    grabon = "Sorry, Only My Owner Can Acess This Button. If U Want To Use Then Deploy Ur Own Lêɠêɳ̃dẞø†"
    await tgbot.send_message(event.chat_id, grabon)


print(
    f"""
╔════❰LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - {Config.ALIVE_NAME}
║┣⪼ Group - @Legend_Userbot
║┣⪼ CREATOR - @The_LegendBoy
║┣⪼ LEGENDBOT - {LEGENDversion}
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱"""
)
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")


async def legends():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    YESS = f"""
    Hello Sir/Miss Something Happened 
    Ding Dong Ting Tong Ping Pong
    Successfully LegendBot Has Been Deployed 
    My Master ~ 『{legd_mention}』 
    Version ~ {LEGENDversion}
    Click Below To Know More About Me👇🏾👇👇🏼
    """
    try:
        TRY = [[Button.inline("⭐ Start ⭐", data="start")]]
        await lnbot.send_message(bot.me.id, LEGEND_PIC, YESS, buttons=TRY)
    except Exception as e:
        print(str(e))


async def hekp():
    try:
        os.environ[
            "LEGEND_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By LegendBot"
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LEGEND_PIC,
                f"Deployed Lêɠêɳ̃dẞø† Successfully\n\nLêɠêɳ̃dẞø† ~ {LEGENDversion}\n\nType `{l1}help` or `{l1}ping` to check!\nFor Assistant Type `.on` \n\nJoin [LegendBot Channel](t.me/Official_LegendBot) for Updates & [LegendBot Chat](t.me/Legend_Userbot) for any query regarding LegendBot",
            )
    except Exception as e:
        print(str(e))

    try:
        await bot(JoinChannelRequest("@Official_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Legend_Userbot"))
    except BaseException:
        pass


bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.create_task(hekp())
bot.loop.run_until_complete(assistants())
bot.loop.run_until_complete(spams())
bot.loop.run_until_complete(legends())


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
