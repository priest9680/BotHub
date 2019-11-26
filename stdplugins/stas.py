# (c) @UniBorg
""" command: .stas """
from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.stas", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("sTaS"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
