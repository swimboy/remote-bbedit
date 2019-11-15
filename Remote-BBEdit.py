#!/usr/bin/env python3.7

import asyncio
import iterm2
import os

async def main(connection):
    app = await iterm2.async_get_app(connection)
    async with iterm2.CustomControlSequenceMonitor(connection, "remote-bbedit", r'.*') as mon:
        while True:
            match = await mon.async_get()
            session = app.current_terminal_window.current_tab.current_session
            os.system("/usr/local/bin/bbedit --wait --resume -- " + match.string)
            await session.async_send_text("Y")
iterm2.run_forever(main)
