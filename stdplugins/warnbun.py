"""Commands:
.warn0
.warn1
.warn2
.warn3
.gbun
.fw
.ocb"""
import asyncio
import html
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import MessageEntityMentionName
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="warn1 ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    first_name = html.escape(replied_user.user.first_name)
    reason=event.pattern_match.group(1)
    mentions = "{first_name} has been warned!\nReason: {reason}\nWarnings: 1/3"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="warn2 ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    first_name = html.escape(replied_user.user.first_name)
    reason=event.pattern_match.group(1)
    mentions = "{first_name} has been warned!\nReason: {reason}\nWarnings: 2/3\n Be careful!"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="warn3 ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    first_name = html.escape(replied_user.user.first_name)
    reason=event.pattern_match.group(1)
    mentions = "{first_name} has been warned!\nReason: {reason}\nWarnings: 3/3\n Be carefull"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="warn0"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    first_name = html.escape(replied_user.user.first_name)
    reason=event.pattern_match.group(1)
    mentions = "Warnings resetted.\nWarnings: 0/3"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="gbun ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    first_name = html.escape(replied_user.user.first_name)
    reason=event.pattern_match.group(1)
    mentions = "{first_name} has been gbanned!\nReason: {reason}\n"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("ocb"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Warning..\n\nBattery Below 10%, Please Charge Your Phone**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("fw"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`U Got A FloodWait:\nReason:telethon.errors.rpcerrorlist.FloodWaitError: A wait of 546578265716823 seconds is required (caused by EditMessageRequest)`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
