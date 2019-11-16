#!/usr/bin/env python3

import asyncio
import iterm2
import os

async def main(connection):
    app = await iterm2.async_get_app(connection)
    async def bbeditWrapper():
        async with iterm2.CustomControlSequenceMonitor(connection, "remote-bbedit", r'.*') as mon:
            while True:
                match = await mon.async_get()
                session = app.current_terminal_window.current_tab.current_session
                os.system("/usr/local/bin/bbedit --wait --resume -- " + match.string)
                await session.async_send_text("Y")
    asyncio.create_task(bbeditWrapper())
iterm2.run_forever(main)
