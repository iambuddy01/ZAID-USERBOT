import asyncio
import importlib
from pyrogram import idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids, init_aiosession, close_aiosession


async def start_bot():
    await init_aiosession()  # Start aiohttp session
    await app.start()
    print("LOG: Found Bot token. Booting...")

    # Import all modules dynamically
    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")

    # Start all clients
    for cli in clients:
        try:
            await cli.start()
            me = await cli.get_me()
            await join(cli)
            print(f"Started {me.first_name} 🔥")
            ids.append(me.id)
        except Exception as e:
            print(f"Error starting client: {e}")

    print("All clients started successfully ✅")
    await idle()  # Keep bot running
    await close_aiosession()  # Close aiohttp session


if __name__ == "__main__":
    asyncio.run(start_bot())
