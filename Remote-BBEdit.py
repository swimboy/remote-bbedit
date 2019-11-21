#!/usr/bin/env python3

import asyncio
import iterm2
import os

async def main(connection):
    app = await iterm2.async_get_app(connection)
    async def watch(session_id):
        session = app.get_session_by_id(session_id)
        async with iterm2.CustomControlSequenceMonitor(connection, "remote-bbedit", r'.*', session_id) as mon:
            while True:
                match = await mon.async_get()
                os.system("/usr/local/bin/bbedit --wait --resume -- " + match.string)
                await session.async_send_text("Y")
    await iterm2.EachSessionOnceMonitor.async_foreach_session_create_task(app, watch)

iterm2.run_forever(main)
